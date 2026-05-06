import os
import yt_dlp

def extract_high_fidelity_audio(youtube_url):
    print("\n[+] STARTING EXTRACTION PROTOCOL...")
    print("[+] Intercepting signal from: " + youtube_url)
    
    # Configure yt-dlp for high fidelity WAV extraction
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'intercepted_anomaly.%(ext)s',
        'quiet': False,
        'no_warnings': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("\n[!] EXTRACTION COMPLETE.")
        print("[!] File saved as: intercepted_anomaly.wav")
        print("[!] WARNING: Do not play at high volume. Use analizador_espectro.py")
    except Exception as e:
        print("\n[X] INTERCEPTION ERROR. The signal is too unstable.")
        print(f"Details: {e}")

if __name__ == "__main__":
    print("==================================================")
    print(" EXTRACTION TERMINAL - MURMANSK NODE (M-14) ")
    print("==================================================")
    
    link = input("\nEnter the URL of the contaminated file (YouTube): ")
    
    if link:
        extract_high_fidelity_audio(link)
