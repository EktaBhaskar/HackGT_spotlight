import os
# from wsgiref.util import request_uri, 
from werkzeug.utils import secure_filename
from setup import setup, allowed_file
from video_to_audio import video_to_audio
from audio_to_text import audio_to_text
from text_summarizer import generate_summary

from flask import Flask, request, render_template, flash, request, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    print("home")
    return "home"

@app.route('/upload/', methods=['GET', 'POST'])
def upload_function():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "File not found"
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        if file.filename == '':
            return "Empty filename"

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            setup()
            if filename.endswith('.mp4'):
                file.save(os.path.join(app.config['VIDEO_DIR'],
                      filename))
                audio_name = video_to_audio(filename)
                text_file = audio_to_text(audio_name)
                summary = generate_summary(text_file, 2)
            elif filename.endswith('.wav'):
                file.save(os.path.join(app.config['AUDIO_DIR'],
                      filename))
                text_file = audio_to_text(filename)
                summary = generate_summary(text_file, 2)
            else:
                file.save(os.path.join(app.config['TEXT_DIR'],
                      filename))
                summary = generate_summary(filename, 2)
            return send_from_directory(directory='pdf', filename=summary)
    return ''






if __name__=="__main__":
    # file.save(os.path.join(app.config['VIDEO_DIR'],
    #                   filename))
    audio_name = video_to_audio('videoplayback.mp4')
    # text_file = audio_to_text(audio_name)
    generate_summary(text_file, 2)
	# app.run(host='0.0.0.0', port = 81)
