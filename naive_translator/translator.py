from .dictionary import DictionaryTree
from typing import Dict

__all__ = ('Translator',)


class Translator:

    def __init__(self, trees: Dict[str, DictionaryTree], use: str = None):
        assert len(trees) > 0

        self.trees = trees
        self.all_uses = list(trees.keys())
        if not use or use not in self.all_uses:
            self._use = self.all_uses[0]
        else:
            self._use = use

    @property
    def use(self):
        return self._use

    @use.setter
    def use(self, val):
        assert val in self.all_uses
        self._use = val

    def translate(self, sentence: str, use: str = None):
        tree = self.trees[use or self.use]
        translation = []
        idx = 0
        while idx < len(sentence):
            trans_part = tree.max_match(sentence[idx:])
            idx += len(trans_part)
            translation.append(trans_part)

        return ''.join(translation)

    __call__ = translate

