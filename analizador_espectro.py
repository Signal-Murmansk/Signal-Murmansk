import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

def reveal_spectrum(audio_file, output_img="revealed_spectrum.png"):
    print(f"--- Starting Signal Analysis: {audio_file} ---")
    
    # Load audio with original sampling rate
    y, sr = librosa.load(audio_file, sr=None)
    
    # Compute Short-Time Fourier Transform (STFT)
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=4096)), ref=np.max)
    
    # Visualization setup
    plt.figure(figsize=(15, 8))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='hz', cmap='magma')
    
    plt.colorbar(format='%+2.0f dB')
    plt.title('Frequency Analyzer - Project Cathode (Verification Protocol)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency (Hz)')
    
    # Focus on the high-frequency resonance zone
    plt.ylim(0, 20000) 
    plt.axhline(y=14000, color='cyan', linestyle='--', alpha=0.3, label='Alpha Resonance Zone')
    
    plt.tight_layout()
    plt.savefig(output_img, dpi=300)
    plt.show()
    
    print(f"--- Analysis Complete. Spectrum saved as: {output_img} ---")

if __name__ == "__main__":
    file_path = "intercepted_anomaly.wav" 
    
    if os.path.exists(file_path):
        reveal_spectrum(file_path)
    else:
        print(f"Error: File '{file_path}' not found.")
