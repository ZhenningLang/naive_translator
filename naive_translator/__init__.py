from typing import Iterable, Tuple, Dict

from .config import DICT_PATH
from .dictionary import DictionaryTree
from .translator import Translator

__all__ = ('load_dictionary', 'translator')


def load_dictionary(dict_path: Dict[str, str] = DICT_PATH) -> Dict[str, Iterable[Tuple]]:
    pairs = {}
    for name, path in dict_path.items():
        pair = []
        with open(path, 'r') as f:
            while True:
                line = f.readline()
                if not line or not line.strip():
                    break
                line = line.strip()
                pair.append(tuple(line.split(',')))
        pairs[name] = pair
    return pairs


trees = {}
for name_, pair_ in load_dictionary().items():
    trees[name_] = DictionaryTree(pair_)
translator = Translator(trees)
