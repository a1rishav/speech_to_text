import wave
import deepspeech
import numpy as np
import os
from src.utils import init_logger
logger = init_logger("SpeechtoText")
from application_properties import ApplicationProperties as props

class SpeechtoText:

    def __init__(self, model_file_path, lm_file_path=None, trie_file_path=None,
                 lm_alpha=0.75, lm_beta = 1.85, beam_width = 500):
        self.model = deepspeech.Model(model_file_path, beam_width)
        if lm_file_path and trie_file_path and lm_alpha and lm_beta:
            self.model.enableDecoderWithLM(lm_file_path, trie_file_path, lm_alpha, lm_beta)
        logger.info("Model sample rate : {}".format(self.model.sampleRate()))

    def get_text_from_speech(self, audio_file_path):
        w = wave.open(audio_file_path, 'r')
        audio_file_rate = w.getframerate()
        audio_file_frames = w.getnframes()
        audio_file_buffer = w.readframes(audio_file_frames)

        if audio_file_rate != self.model.sampleRate():
            raise "Model sample rate {} != audio file's sample rate : {} "\
                .format(self.model.sampleRate(), audio_file_rate)

        data16 = np.frombuffer(audio_file_buffer, dtype=np.int16)
        return self.model.stt(data16)

if __name__ == '__main__':
    model_file_path = os.path.join(props.model_dir, "output_graph.pbmm")
    speech_to_text = SpeechtoText(model_file_path=model_file_path)
    sample_audio_file = os.path.join(props.sample_audio_dir, 'test.wav')
    print(speech_to_text.get_text_from_speech(sample_audio_file))

