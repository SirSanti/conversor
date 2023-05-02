from flask import Flask, render_template, request
from pytube import YouTube
from moviepy.editor import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    url = request.form['url']
    if url:
        try:
            # Faz o download do vídeo em formato MP4
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            video.download(output_path='downloads', filename='audio')

            # Extrai o áudio do arquivo MP4 e salva como um arquivo MP3
            clip = AudioFileClip("downloads/audio.mp4")
            clip.write_audiofile("downloads/audio.mp3")
            clip.close()

            return render_template('index.html', success=True)
        except Exception as e:
            return render_template('index.html', error=True)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
