import os
from application_properties import ApplicationProperties as props
import wave
import deepspeech
import numpy as np

# load model
model_file_path = os.path.join(props.model_dir, "output_graph.pbmm")
beam_width = 500
model = deepspeech.Model(model_file_path, beam_width)
lm_file_path = os.path.join(props.model_dir, 'lm.binary')
trie_file_path = os.path.join(props.model_dir, 'trie')
lm_alpha = 0.75
lm_beta = 1.85
model.enableDecoderWithLM(lm_file_path, trie_file_path, lm_alpha, lm_beta)
print("Model sample rate : {}".format(model.sampleRate()))

# prepare sample file
sample_file = os.path.join(props.sample_audio_dir, 'test.wav')
# sample_file = os.path.join(props.sample_audio_dir, '8455-210777-0068.wav')
w = wave.open(sample_file, 'r')
rate = w.getframerate()
frames = w.getnframes()
buffer = w.readframes(frames)
print("Sample audio file sample rate : {}".format(rate))
print("frames : {} ".format(frames))
print("rate : {} ".format(rate))
data16 = np.frombuffer(buffer, dtype=np.int16)

# Run STT
text = model.stt(data16)
print(text)