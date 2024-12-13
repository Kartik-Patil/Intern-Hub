# Intern Hub

## Project Overview
This repository contains three projects demonstrating advanced concepts in chatbot development, movie recommendation systems, and real-time object detection using YOLO:

1. **Advanced Chatbot**: A Python-based chatbot that interacts with users, provides time and date, and assists with casual inquiries.
2. **Movie Recommendation System**: A hybrid recommendation system combining genre-based and collaborative filtering techniques using the MovieLens dataset.
3. **Real-Time Object Detection**: A real-time object detection system implemented with YOLO (You Only Look Once) using OpenCV.

## Requirements

Before running the projects, ensure you have the following dependencies installed:

### Common Requirements
- Python 3.7+
- `pip`

### Advanced Chatbot
- `re`
- `datetime`

### Movie Recommendation System
- Flask
- pandas
- scikit-learn

### Real-Time Object Detection
- OpenCV (cv2)
- NumPy

### YOLO Files (required for Real-Time Object Detection)
- `yolov3.weights` (download from [YOLO website](https://pjreddie.com/darknet/yolo/))
- `yolov3.cfg` (download from [YOLO website](https://pjreddie.com/darknet/yolo/))
- `coco.names` (list of class labels, available from the YOLO website)

## Installation

1. Clone the repository:
    ```bash
    git clone (https://github.com/Kartik-Patil/Intern-Hub.git)
    cd Intern-Hub
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Place YOLO files (`yolov3.weights`, `yolov3.cfg`, `coco.names`) in the project directory.

## Running the Projects

### Advanced Chatbot

Run the chatbot using the following command:
```bash
python chatbot.py
```

### Movie Recommendation System

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`.

3. Enter your favorite genres to get movie recommendations.

### Real-Time Object Detection

Run the object detection script:
```bash
python realtime_detection.py
```
Press `q` to exit the real-time detection window.

## Large Files

Due to repository size constraints, the following files were deleted:

- `yolov3.weights`
- `movies.csv`
- `rating.csv`

These files can be downloaded and placed in the respective directories:

- `yolov3.weights`: [Download here](https://pjreddie.com/media/files/yolov3.weights)
- `movies.csv` and `rating.csv`: Part of the MovieLens dataset, available [here](https://grouplens.org/datasets/movielens/).

## Contributing

Feel free to fork this repository and submit pull requests. If you encounter any issues, please open an issue on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
