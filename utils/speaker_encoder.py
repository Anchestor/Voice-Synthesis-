import librosa
import numpy as np

def extract_voice_embedding(wav_path):
    y, sr = librosa.load(wav_path, sr=16000)
    duration = librosa.get_duration(y=y, sr=sr)

    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=1024,
                                         hop_length=256, n_mels=80)
    mel_db = librosa.power_to_db(mel, ref=np.max)

    # Mock embedding = mean of mel across time
    embedding = np.mean(mel_db, axis=1)

    return {
        "embedding": embedding.tolist(),
        "mel_shape": mel_db.shape,
        "duration": round(duration, 2)
    }
  
