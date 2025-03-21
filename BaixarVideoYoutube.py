import yt_dlp
import os

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
video_filename = "video.webm"

ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'merge_output_format': 'webm',
    'outtmpl': video_filename,
    'quiet': False
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if not os.path.exists(video_filename):
        raise FileNotFoundError("O vídeo não foi baixado corretamente.")

    print(f"Vídeo baixado com sucesso: {video_filename}")

except Exception as e:
    print("Erro ao baixar o vídeo do YouTube:", e)
    exit()

