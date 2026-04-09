import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.p.cloud.ibm.com/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=5)
        
        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            emotions['dominant_emotion'] = dominant_emotion
            return emotions
            
        if response.status_code == 400:
            return {key: None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}

    except Exception:
        # This catches the NameResolutionError/ConnectionError
        # Returning None for dominant_emotion will trigger your "Invalid text" message in server.py
        return {key: None for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']}
    
    return None