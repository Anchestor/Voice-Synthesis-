from flask import Flask, request, jsonify
from utils.downloader import download_audio_from_url
from utils.audio_utils import convert_to_wav
from utils.speaker_encoder import extract_voice_embedding
import os

app = Flask(__name__)

@app.route("/clone", methods=["GET"])
def clone_voice():
    audio_url = request.args.get("audio_url")

    if not audio_url:
        return jsonify({"error": "Missing audio_url parameter"}), 400

    try:
        print(f"[INFO] Downloading from: {audio_url}")
        local_path = download_audio_from_url(audio_url)

        print("[INFO] Converting to WAV...")
        wav_path = convert_to_wav(local_path)

        print("[INFO] Extracting voice embedding...")
        result = extract_voice_embedding(wav_path)

        # Clean up
        os.remove(local_path)
        os.remove(wav_path)

        return jsonify({
            "status": "success",
            "embedding_dim": len(result['embedding']),
            "mel_shape": result['mel_shape'],
            "duration_sec": result['duration'],
            "embedding": result['embedding']
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
  
