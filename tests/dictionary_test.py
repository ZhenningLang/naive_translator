import os
import sys

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from naive_translator.dictionary import DictionaryTree  # noqa

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
    ('abc', '333'),
    ('def', '666'),
    ('efg', '999'),
)


tree = DictionaryTree(pair)
print(tree.max_match('abcdefg'))
