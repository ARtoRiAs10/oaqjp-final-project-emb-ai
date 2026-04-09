"""
This module initiates the Flask application for emotion detection.
It provides endpoints for analyzing text and rendering the web interface.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_detector # pylint: disable=import-error

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes input text and returns a formatted string of emotion scores.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Extract emotions and dominant_emotion from the response dictionary
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    # Error handling when the dominant_emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return the formatted response
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': "
        f"{sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)

