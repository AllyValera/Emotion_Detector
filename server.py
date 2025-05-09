from flask import Flask, request, jsonify, render_template
from Emotion_Detector.emotion_detection import emotion_detector

# NOTE: MOVE THIS OUTSIDE OF THE Emotion_Detector DIR TO START THE SERVER

app = Flask(
    __name__,
    template_folder='Emotion_Detector/templates',  
    static_folder='Emotion_Detector/static'     
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    data = request.get_json()

    # Handle missing input
    if "text_to_analyze" not in data:
        return jsonify({"error": "Missing 'text_to_analyze' in request"}), 400

    text = data["text_to_analyze"]
    result = emotion_detector(text)

    # Format the result string for display
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_output, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)