# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 17:02
# @Author  : MengnanChen
# @FileName: check_slience_trim.py
# @Software: PyCharm

import os,shutil,glob,random

from datasets.audio import *
import os
from hparams import hparams

def get_some_inversed_samples(training_data_path='training_data',output_inversed_path='tmp_inverse_wav_out',n_samples=5):
    mel_files=glob.glob(os.path.join(training_data_path,'mels','*.npy'))
    assert len(mel_files)>=n_samples,'no enough .npy to inverse...'
    if os.path.exists(output_inversed_path):
        shutil.rmtree(output_inversed_path)
    os.makedirs(output_inversed_path,exist_ok=False)
    random.seed(2018)
    mel_files=random.sample(mel_files,n_samples)
    for mel_file in mel_files:
        mel_file_basename=os.path.basename(mel_file)
        mel_spectro=np.load(mel_file)
        wav=inv_mel_spectrogram(mel_spectro.T, hparams)
        save_wav(wav,os.path.join(output_inversed_path,'{}.wav'.format(mel_file_basename))
                 ,sr=hparams.sample_rate)

if __name__ == '__main__':
    get_some_inversed_samples()