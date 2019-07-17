import os
import sys

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from naive_translator import translator  # noqa

print(translator('天好蓝要和你一起看，起风时由你来温暖。'))
print(translator("【GioGio的奇妙冒險 Ep.01】法拉利的收購者-Fiat GioGio的美國行|GioGio's Bizarre Adventure"))
print(translator('【豐田的遊戲 Ep.01】豐田的上門女婿和女人|Game of Toyota Ep.01'))
