'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''

import os
import glob

AUTO_DETECT_SYMBOLS = True

train_text_files = glob.glob(os.path.join('../../training_data', 'train.txt'))
if train_text_files and AUTO_DETECT_SYMBOLS:
    _characters = set()
    for file in train_text_files:
        with open(file, 'rb') as fin:
            for line in fin:
                line = line.decode('utf-8').strip('\r\n ').split('|')[5]
                _characters = _characters.union(line)
else:
    _characters = 'abcdefghijklmnopqrstuvwxyz12345，。？，！- '

_pad = '_'
_eos = '~'

# Export all symbols:
symbols = [_pad, _eos] + list(_characters)

print('all symbols is: {}'.format(symbols))

# from . import cmudict

# _pad        = '_'
# _eos        = '~'
# _characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'\"(),-.:;? '
#
# # Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# #_arpabet = ['@' + s for s in cmudict.valid_symbols]
#
# # Export all symbols:
# symbols = [_pad, _eos] + list(_characters) #+ _arpabet
