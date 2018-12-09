# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 14:29
# @Author  : MengnanChen
# @FileName: synthesis_mel.py
# @Software: PyCharm

from datasets.audio import *
import os
from hparams import hparams
import time


def mel_synthesis(out_dir='wav_griffi_syn',in_dir='mel'):
    os.makedirs(out_dir, exist_ok=True)

    #mel_file = os.path.join(mel_folder, mel_file)
    mel_filenames=[x.split('.')[0] for x in os.listdir(in_dir)]
    start_time=time.time()
    for mel_file in mel_filenames:
        try:
            print('process {}'.format(mel_file))
            mel_file_path = os.path.join('training_data/mels', 'mel-{}.wav.npy'.format(mel_file))
            mel_spectro = np.load(mel_file_path)
            wav = inv_mel_spectrogram(mel_spectro.T, hparams)
            # save the wav under test_<folder>_<file>
            save_wav(wav, os.path.join(out_dir, 'test_mel_{}.wav'.format(
                mel_file.replace('/', '_').replace('\\', '_').replace('.npy', ''))),
                     sr=hparams.sample_rate)
        except:
            print('{} error'.format(mel_file))

    print('griffin-lim :{}'.format(time.time()-start_time))


if __name__ == '__main__':
    mel_synthesis()