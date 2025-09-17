# audio
Piper Voice Model
	Architecture:
Piper voices are trained using a FastSpeech2-like acoustic model + HiFi-GAN vocoder, exported to ONNX for CPU/GPU inference.
	•	Sample rate: 22,050 Hz, mono, 16-bit PCM output (which is what you played via afplay).
	•	Size: ~60 MB (your ls -lh showed 60.2M for .onnx).
	•	This is compact enough to run on laptops, Raspberry Pi 4/5, Jetson, etc.
	•	Phoneme backend: Uses espeak-ng to convert English text → phonemes → neural model.
Low-latency → generates speech in real time or faster-than-real-time on MacBook Pro ARM.
	•	Lightweight → can deploy on edge devices without GPU.
	•	Quality → intelligible, pleasant, not robotic (though not as natural as “high”).
	Hosted on Hugging Face by Rhasspy / Piper project:
https://huggingface.co/rhasspy/piper-voices
	•	License depends on the specific voice dataset (most are under CC BY 4.0). \
