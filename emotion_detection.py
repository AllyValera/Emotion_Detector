import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        # manage blank entries
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400 
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    body = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        return None

    # turns the response into a dictionary
    result = json.loads(response.text)

    # extracts the emotion scores from the rest of the response
    emotions = result['emotionPredictions'][0]['emotion']

    # get emotion with highest score
    dominant_emotion = max(emotions, key=emotions.get)

    # formatting for result
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }