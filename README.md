# Image Caption Generator

A web application that allows users to upload images and generate captions using a backend Flask service. The frontend is built using React.js and communicates with the Flask backend to generate captions for the uploaded images.

## Features

- Upload an image and receive a generated caption.
- Display a preview of the uploaded image.
- Handle loading state while generating the caption.
- Show error messages if the caption generation fails.
- Fully responsive UI built with Tailwind CSS for easy interaction.

## Tech Stack

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Flask (Python)
- **API Communication**: Fetch API
- **Image Processing**: Flask API endpoint that processes uploaded images and generates captions

## Prerequisites

- Node.js (for frontend React application)
- Python (for Flask backend)
- Flask (Backend framework)
- Flask-CORS (for enabling CORS in Flask)
- Tailwind CSS (for styling)

## Setup Instructions

### Backend (Flask)

1. Clone the repository and navigate to the backend folder.

   ```bash
   git clone https://github.com/sriharshan136/Image-Caption-Generator.git
   cd backend

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
  requirements.txt should contain the necessary libraries, including Flask, flask-cors, and any other dependencies you need.

3. Run the Flask application:

    ```bash
    python app.py
  The backend will run at http://localhost:5000 by default.

### Frontend (React.js)

1. Navigate to the frontend directory:

    ```bash
    cd frontend

2. Install the required Node.js packages:

    ```bash
    npm install
    
3. Start the React development server:

    ```bash
    npm start
  The frontend will be accessible at http://localhost:3000.

## Configuration

Ensure that the frontend is making requests to the correct backend URL. By default, it is set to http://localhost:5000, but if your backend is hosted elsewhere, update the URL in the handleUpload function inside App.js:

  ```bash
  const response = await fetch("http://127.0.0.1:5000/generate-caption", {
    method: 'POST',
    body: formData
  });
  ```

## Usage

1. **Upload Image**: Click the image upload area or drag and drop an image to upload.
2. **Generate Caption**: Once the image is uploaded, click the "Generate Caption" button to process the image and get a caption.
3. **Caption Display**: After the processing is complete, the generated caption will be displayed below the upload area.
4. **Error Handling**: If there's an error in uploading or generating the caption, an error message will be shown.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any suggestions or improvements are welcome!

## License

This project is open-source and available under the MIT License.
