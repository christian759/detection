# Object Detection Website [link](https://objects-detection.streamlit.app/)

## Overview

This Streamlit-based website allows users to upload images and perform object detection on them. It utilizes pre-trained object detection models to identify and label objects within the images. The application is designed to be user-friendly and provides immediate feedback on the objects detected in the uploaded images.

## Features

- **Image Upload**: Easily upload images from your local device.
- **Object Detection**: Automatically detect and label objects in the uploaded images.
- **Results Display**: View the detected objects directly on the image with bounding boxes and labels.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/christian759/detection.git
    cd detection
    ```

2. **Set Up a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**

    ```bash
    streamlit run main.py
    ```

5. **Open the Application**

    After running the application, open your web browser and go to `http://localhost:8501` to use the website.

## Usage

1. On the homepage, click the "Upload Image" button to select an image from your device.
2. The image will be displayed on the screen, and object detection will automatically be performed.
3. Detected objects will be highlighted with bounding boxes and labels on the image.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Pre-trained Object Detection Model**: (e.g., YOLO) for performing object detection.
- **Python Libraries**: Including `PIL`, `OpenCV`, and any other dependencies specified in `requirements.txt`.

## Contributing

If you want to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Name**: Eighemhenrio Christian
- **Email**: christian4onos@gmail.com
- **GitHub**: [christian759](https://github.com/christian759)
- **Whatsapp**: +2347018029291

