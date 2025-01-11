from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import requests

app = Flask(__name__)

# Hugging Face API Key
HUGGING_FACE_API_KEY = "API_Key" 

def get_transcript(video_id):
    """Fetch the transcript of the YouTube video."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    except Exception as e:
        print(f"English transcript error: {e}")
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en-IN', 'hi'])
        except Exception as inner_e:
            print(f"Alternate language transcript error: {inner_e}")
            return f"Error: No transcript available in supported languages."
    
    formatter = TextFormatter()
    return formatter.format_transcript(transcript)

def summarize_text_with_api(text):
    """Summarize the text using the Hugging Face Inference API."""
    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

    if not text or text.startswith("Error:"):
        return "Could not summarize the video as no valid transcript was found."

    max_chunk_words = 500
    words = text.split()

    # Split the text into chunks if it's too long
    chunks = [" ".join(words[i:i + max_chunk_words]) for i in range(0, len(words), max_chunk_words)]
    summaries = []

    for chunk in chunks:
        payload = {"inputs": chunk}
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            summaries.append(response.json()[0]['summary_text'])
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "Error: Unable to summarize the text using the API."

    # Combine all summaries
    return " ".join(summaries)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    video_url = request.form['video_url']
    if "youtube.com/watch" not in video_url:
        return render_template('result.html', summary="Invalid YouTube URL. Please try again.")

    video_id = video_url.split("v=")[-1].split("&")[0]
    transcript = get_transcript(video_id)
    summary = summarize_text_with_api(transcript)
    return render_template('result.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
