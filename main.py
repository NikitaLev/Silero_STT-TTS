# This is a sample Python script.
import threading
from fuzzywuzzy import fuzz

import STT
import TTS

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

str_ex = 'the birch canoe slid on the smooth planks glue the sheet to the dark blue background it\'s easy to tell the ' \
         'depth of a well four hours of steady work faced us'


def recognize_cmd(cmd: str, name):
    rc = {'name': '', 'percent': 0}
    # print('rc', rc)
    vrt = fuzz.ratio(cmd, str_ex)
    rc['name'] = name
    rc['percent'] = vrt
    # print(x + ' x = '+str(vrt))
    return vrt


def silero_test(filename):
    res = STT.silero_stt_test(filename)
    pr = recognize_cmd(res, 'silero')
    print(filename)
    print('silero = ', res)
    print('orig   = ', str_ex)
    print('% = ', pr)
    print()
    TTS.test_en(example_text=res)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name_file1 = 'en_sample_1_16k.wav'
    params1 = {"filename": name_file1}
    task_file1 = threading.Thread(name="listen_silero_1", target=silero_test, kwargs=params1)
    task_file1.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
