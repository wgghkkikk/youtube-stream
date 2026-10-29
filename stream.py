import subprocess
import time
import sys

# مفتاح البث الخاص بك
STREAM_KEY = "8uus-v85g-xe8g-w65d-b1ca"
RTMP_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

def start_stream():
    # أمر FFmpeg لتوليد شاشة سوداء خفيفة ومستقرة مع ضغط يمنع استهلاك السيرفر
    cmd = [
        "ffmpeg",
        "-re",
        "-f", "lavfi",
        "-i", "color=c=black:s=1280x720:r=30",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-tune", "zerolatency",
        "-b:v", "400k",
        "-maxrate", "400k",
        "-bufsize", "800k",
        "-pix_fmt", "yuv420p",
        "-g", "60",
        "-f", "flv",
        RTMP_URL
    ]
    
    print("جاري بدء تشغيل البث الثابت...", flush=True)
    
    # تشغيل العملية ومراقبتها
    process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return process

def main():
    while True:
        proc = start_stream()
        
        # مراقبة عملية البث؛ إذا توقف FFmpeg لأي سبب، الكود ينتظر ثواني ويحاول الاتصال من جديد
        while proc.poll() is None:
            time.sleep(5)
            
        print("حدث انقطاع مؤقت، جاري إعادة الاتصال خلال 3 ثوانٍ...", flush=True)
        time.sleep(3)

if __name__ == "__main__":
    main()
