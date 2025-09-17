#!/usr/bin/env python3
import subprocess
import sys
import os

# Path to the voice model (make sure you have run your fetch script to download .onnx + .json)
MODEL = os.path.abspath(os.path.join("voices", "en_US-lessac-medium.onnx"))
WAV   = "tmp.wav"

def speak(text: str):
    """Generate speech with Piper and play it back."""
    # Generate speech
    subprocess.run(
        [
            "piper",
            "--model", MODEL,
            "--output_file", WAV,
            "--output_file_format", "wav",
        ],
        input=text.encode("utf-8"),
        check=True,
    )

    # Play audio (macOS: afplay, Linux: ffplay/aplay fallback)
    try:
        subprocess.run(["afplay", WAV], check=True)
    except FileNotFoundError:
        try:
            subprocess.run(["ffplay", "-nodisp", "-autoexit", WAV], check=True)
        except FileNotFoundError:
            subprocess.run(["aplay", WAV], check=True)

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or "Hi aqib, Piper is working on your pc!"
    speak(text)
