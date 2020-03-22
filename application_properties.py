import os

class ApplicationProperties:
    app_home = "/media/data/projects/ai/speech_to_text"
    model_dir = os.path.join(app_home, "deepspeech-0.6.1-models")
    sample_audio_dir = os.path.join(app_home, "sample_audio")
    logs_dir = os.path.join(app_home, "logs")