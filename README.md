# YouTube Transcript Summarizer

This project uses the Hugging Face API and YouTube Transcript API to fetch, summarize, and display a summary of YouTube video transcripts. It’s a web-based application built using **Flask** for the backend, and it allows users to input a YouTube video URL and get a summarized version of the video transcript.

## Features
- Fetches YouTube video transcripts in multiple languages (default: English).
- Summarizes the transcript using the Hugging Face **BART** model.
- Displays the summarized text in a user-friendly web interface.

## Technologies Used
- **Flask**: A lightweight web framework for Python to handle the web server and routing.
- **YouTube Transcript API**: To fetch transcripts of YouTube videos.
- **Hugging Face Inference API**: To summarize the transcript using the **BART** model.
- **HTML/CSS**: For building the user interface.

## Requirements
- Python 3.x
- Flask
- youtube-transcript-api
- requests
- Hugging Face API key

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/YouTube-Transcript-Summarizer.git
cd YouTube-Transcript-Summarizer
```

### 2. Set up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up Hugging Face API Key
You’ll need a Hugging Face API key to access the **BART** model for summarization.

- Sign up on [Hugging Face](https://huggingface.co) if you don’t have an account.
- Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens) and generate a new API key.
- Add the key to the `HUGGING_FACE_API_KEY` variable in the code.

### 5. Run the Flask App
```bash
python app.py
```
The application will be running at [http://localhost:5000](http://localhost:5000).

## Usage

1. Open the app in your browser.
2. Enter a YouTube video URL in the input field.
3. Click on the "Summarize" button.
4. View the summarized text of the video transcript.

## Example

### Input:
YouTube video URL: [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

### Output:
A summarized version of the video transcript will be shown below the input form.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README file provides a clear understanding of what the project does, how to set it up, and how to use it. You can customize the URL in the **clone** command and provide your actual repository URL when pushing to GitHub.
