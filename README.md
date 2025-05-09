# Emotion Detector 🌟

A simple Natural Language Processing (NLP) web app that detects emotions in user input using a Flask backend. The app uses the `requests` library to interact with IBM Watson's sentiment analysis API and displays the results on a responsive HTML page.

---

⚠️ **Important Note:**  
For GitHub versioning, `server.py` and `test_emotion_detection.py` appear inside the `Emotion_Detector` folder.  
To run the application and/or run unit tests, ensure both files are placed **outside** the `Emotion_Detector` directory.

---

## 🧠 About Watson AI

This project uses **IBM Watson Natural Language Understanding** – a powerful AI tool for analyzing emotions in text. The `emotion_detection.py` module sends requests to Watson's API and extracts five primary emotions from the input:

- `anger`
- `disgust`
- `fear`
- `joy`
- `sadness`

The API also identifies the **dominant emotion**, which is highlighted in the results.

---

## 🛠️ Technologies Used

- **Flask** – lightweight web framework for Python (used to serve the app)
- **Requests** – for sending API calls to IBM Watson's emotion detection service
- **HTML/CSS/JavaScript** – for the frontend interface

---

## 🚀 How to Run

**Install dependencies**

- ```pip3 install flask requests``` 

**Move files**

- Ensure server.py and test_emotion_detection.py are outside of the Emotion_Detector directory.

**Start the server**

- ```python3 server.py```

**Open your browser**

- Go to: ```http://127.0.0.1:5000```

**Run tests**

- ```python3 test_emotion_detection.py```

## ✅ Features

Analyze any sentence and detect emotions

Displays the dominant emotion

Handles blank or invalid input gracefully
