import os
import sys

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from naive_translator.dictionary import DictionaryTree  # noqa
from naive_translator.translator import Translator  # noqa

pair = (
    ('a', '1'),
    ('b', '2'),
    ('c', '3'),
    ('d', '4'),
    ('e', '5'),
    ('f', '6'),
    ('g', '7'),
    ('ab', '21'),
    ('bc', '32'),
    ('cd', '43'),
    ('def', '666'),
    ('efg', '999'),
)


tree = DictionaryTree(pair)
trees = {'test': tree}
translator = Translator(trees)
print(translator('abcdefg'))
