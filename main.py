# This is a sample Python script.
import threading
from fuzzywuzzy import fuzz
from datetime import datetime

import STT
import TTS
import psutil
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

str_ex = 'the birch canoe slid on the smooth planks glue the sheet to the dark blue background it\'s easy to tell the ' \
         'depth of a well four hours of steady work faced us'
timer = 0


def recognize_cmd(cmd: str, name):
    rc = {'name': '', 'percent': 0}
    # print('rc', rc)
    vrt = fuzz.ratio(cmd, str_ex)
    rc['name'] = name
    rc['percent'] = vrt
    # print(x + ' x = '+str(vrt))
    return vrt


def silero_test(count, filename):
    start_time = datetime.now()
    res = STT.silero_stt_test(filename)
    """pr = recognize_cmd(res, 'silero')
        print('threading ------- ', count)
    print('silero = ', res)
    print('orig   = ', str_ex)
    print('% = ', pr)
    print()"""
    print('thread read -', count, 'time -', datetime.now() - start_time)

    start_time = datetime.now()
    TTS.test_en(example_text=res)
    print('thread write -', count, 'time -', datetime.now() - start_time)

    return


def test_cpu():
    pid = psutil.Process()
    time_end = time.time() + 15  # + 20 seconds
    cpu_count = psutil.cpu_count(logical=True)
    print('pid = ', pid)
    print('cpu_count = ', cpu_count)
    while time.time() < time_end:
        print('cpu =', pid.cpu_percent(interval=1.0) / cpu_count, '%')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name_file1 = 'en_sample_1_16k.wav'
    params1 = {"count": 1, "filename": name_file1}
    task = threading.Thread(name="test_cpu", target=test_cpu)
    task.start()
    task_silero_test = []
    count = 0
    while count < 1:
        count += 1
        task_silero_test.append(threading.Thread(name="listen_silero_" + str(count), target=silero_test,
                                                 kwargs={"count": count, "filename": name_file1}))
        task_silero_test[-1].start()

"""    task_file1 = threading.Thread(name="listen_silero_1", target=silero_test, kwargs=params1)
    task_file1.start()"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
