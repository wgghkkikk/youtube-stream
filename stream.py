import subprocess
import time

# مفتاح البث الخاص بك
STREAM_KEY = "8uus-v85g-xe8g-w65d-b1ca"
RTMP_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

def start_stream():
    command = [
        "ffmpeg",
        "-re",
        "-f", "lavfi",
        "-i", "color=c=black:s=1280x720:r=30",
        "-f", "lavfi",
        "-i", "anullsrc=r=44100:cl=stereo",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-b:v", "800k",
        "-maxrate", "800k",
        "-bufsize", "1600k",
        "-pix_fmt", "yuv420p",
        "-g", "60",
        "-c:a", "aac",
        "-b:a", "128k",
        "-ar", "44100",
        "-f", "flv",
        RTMP_URL
    ]
    
    while True:
        print("جاري بدء تشغيل البث المباشر...")
        process = subprocess.Popen(command)
        process.wait()
        print("توقف البث، سيتم إعادة التشغيل خلال 5 ثواني...")
        time.sleep(5)

if __name__ == "__main__":
    start_stream()
