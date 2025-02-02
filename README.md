# Image Caption Generator - Hugging Face and LangChain

This project is a full-stack web application for generating captions for images using a Hugging Face model and LangChain. The backend is built using Flask and the Hugging Face API, while the frontend is a React-based web application where users can upload images and receive captions generated by the model.

## Project Overview

The application allows users to upload an image, which is then processed by a deep learning model hosted on the backend to generate an accurate caption describing the image. The model used is a pre-trained vision-to-text model from Hugging Face, specifically designed to generate captions for images.

## Key Technologies Used:

- **Frontend**: React.js for building the user interface.
- **Backend**: Flask for the API, utilizing Hugging Face models for image caption generation.
- **Hugging Face**: The application uses a state-of-the-art vision-to-text model available in the Hugging Face model hub to generate captions.
- **LangChain**: Integration for processing the generated captions (if required for enhancing the text generation pipeline).
- **Image Upload**: The frontend allows users to upload images, which are sent to the backend for caption generation.

## Features

- **Image Upload**: Users can upload an image from their local device to generate a caption.
- **Image Captioning**: The backend uses a Hugging Face model to generate accurate captions based on the content of the image.
- **Real-Time Feedback**: Users get immediate feedback with the generated caption or error messages.
- **Easy-to-Use Interface**: The frontend is built with React, ensuring a responsive and user-friendly interface.

## Hugging Face Model

- The backend uses the BLIP (Bootstrapping Language-Image Pretraining) model available on Hugging Face, which is fine-tuned for generating captions from images.
- BLIP is capable of generating detailed and context-aware descriptions of the images, making it ideal for this application.

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
