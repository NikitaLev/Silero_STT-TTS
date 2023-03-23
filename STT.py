import torch
import zipfile
import torchaudio
from glob import glob

from silero.utils import *

device = torch.device('cpu')
local_file = 'en_v6.jit'

model = torch.jit.load(local_file, map_location=device)
model.eval()
decoder = Decoder(model.labels)

def silero_stt_test(name):

    test_files = glob(name)
    batches = split_into_batches(test_files, batch_size=10)

    input = prepare_model_input(read_batch(batches[0]),
                                device=device)

    output = model(input)
    for example in output:
        return decoder(example.cpu())
