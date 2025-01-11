from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io
import imghdr

app = Flask(__name__)
CORS(app)

# Constants
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# Load BLIP model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/generate-caption', methods=['POST'])
def generate_caption():
    # Check if file exists in request
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    # Check if filename is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Validate file type
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Allowed types: PNG, JPG, JPEG, GIF"}), 400

    # Check file size
    file_content = file.read()
    if len(file_content) > MAX_FILE_SIZE:
        return jsonify({"error": "File size exceeds 10MB limit"}), 400

    try:
        # Open and validate image
        image = Image.open(io.BytesIO(file_content)).convert("RGB")
        
        # Process image and generate caption
        inputs = processor(images=image, return_tensors="pt")
        output = caption_model.generate(
            **inputs,
            max_length=50,
            num_beams=5,
            early_stopping=True,
            temperature=1.0,  # Add some randomness to generations
            top_k=50,        # Limit to top 50 tokens
            top_p=0.95       # Nucleus sampling
        )
        caption = processor.decode(output[0], skip_special_tokens=True)

        # Clean and format caption
        caption = caption.strip().capitalize()
        if not caption.endswith('.'):
            caption += '.'

        return jsonify({
            "caption": caption,
            "status": "success",
            "image_size": f"{image.size[0]}x{image.size[1]}"
        })

    except Exception as e:
        app.logger.error(f"Error processing image: {str(e)}")
        return jsonify({
            "error": "Failed to process image. Please try again with a different image.",
            "details": str(e)
        }), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Load models before starting server
    try:
        # Warm up the model with a small test image
        test_image = Image.new('RGB', (100, 100))
        inputs = processor(images=test_image, return_tensors="pt")
        caption_model.generate(**inputs, max_length=20)
        print("Models loaded successfully!")
    except Exception as e:
        print(f"Error loading models: {str(e)}")
        exit(1)

    app.run(host='0.0.0.0', port=5000, debug=True)