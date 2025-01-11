from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load BLIP model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route('/generate-caption', methods=['POST'])
def generate_caption():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    try:
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")

        # Generate a descriptive caption
        output = caption_model.generate(
            **inputs,
            max_length=50,
            num_beams=5,
            early_stopping=True
        )
        caption = processor.decode(output[0], skip_special_tokens=True)

        return jsonify({"caption": caption})
    except Exception as e:
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
