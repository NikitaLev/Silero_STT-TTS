import torch
import sounddevice as sd
import time

import os
import torch

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model_en.pt'
if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/en/v3_en.pt',
                                   local_file)
model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

sample_rate = 48000
speaker = 'en_0'


def test_en(example_text=''):
    audio_paths = model.save_wav(text=example_text,
                                 speaker=speaker,
                                 sample_rate=sample_rate
                                 )
    # print(audio_paths)
