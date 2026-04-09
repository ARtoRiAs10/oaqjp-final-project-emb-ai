import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Custom headers required by the service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Dictionary to be sent as the JSON payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request to the API
    response = requests.post(url, json=myobj, headers=header)
    
    # Return the text attribute of the response
    return response.text
    