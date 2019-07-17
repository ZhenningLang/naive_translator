"""
Based on a naive dictionary tree
"""

from typing import Tuple, Iterable
from weakref import proxy


class Node:

    def __init__(self, character: str, translation: str = '', parent: 'Node' = None):
        """Node of dictionary tree

        :param character: this node's character
        :param translation: the translation of the word from the root to this node in dictionary tree
        """
        self.character = character
        self.children = {}  # character, Node
        if parent is None:
            self._parent = None
        else:
            self._parent = proxy(parent)
        self.translation = translation

    def __str__(self):
        return f'Node(character={self.character}, translation={self.translation}, children#{len(self.children)})'

    __repr__ = __str__

    def add_child(self, character: str, translation: str = '') -> 'Node':
        child = Node(character, translation, self)
        self.children[character] = child
        return child

    def has_child(self, character: str) -> (bool, 'Node'):
        if character in self.children:
            return True, self.children[character]
        else:
            return False, None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent: 'Node'):
        self._parent = proxy(parent)

    def translate(self, sentence) -> str:
        assert sentence[0] == self.character

        searching_node = self
        for character in sentence[1:]:
            has_child, node = searching_node.has_child(character)
            if has_child:
                searching_node = node
            else:
                break

        while not searching_node.translation:  # in case node.translation is empty, search its parent
            if searching_node.parent is None:
                return searching_node.character
            searching_node = searching_node.parent
        return searching_node.translation


def build_single_tree(root: Node, word: str, translation: str):
    assert root.character == word[0]

    if len(word) == 1:
        root.translation = translation
        return

    node = root
    for character in word[1:]:
        has_child, child_node = node.has_child(character)
        if not has_child:
            child_node = node.add_child(character)
        node = child_node
    node.translation = translation


class DictionaryTree:

    def __init__(self, pair: Iterable[Tuple]):
        """

        :param pair: List(origin, translation)
        """
        self.roots = {}
        self._build_tree(pair)

    def _build_tree(self, pair: Iterable[Tuple]):
        for origin, translation in pair:
            if origin == translation:
                continue
            first_character = origin[0]
            if first_character not in self.roots:
                self.roots[first_character] = Node(character=first_character)
            build_single_tree(self.roots[first_character], origin, translation)

    def max_match(self, sentence: str) -> str:
        """返回字典中的最大匹配词组

        :param sentence:
        :return:
        """
        if not sentence:
            return ''
        first_character = sentence[0]
        if first_character not in self.roots:
            return first_character

        return self.roots[first_character].translate(sentence)
