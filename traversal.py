# -*- coding: utf-8 -*-
'''
from collections import Iterable
def flat(items, L=None):
	if L is None:
		L = []
	for item in items:
		if isinstance(item, Iterable):
			return flat(item, L)
		else:
			L.append(item)

	return L
			
if __name__ == "__main__":
	items = [1, 2, [3, 4, [5, 6, 7], 8, 9]]
	new_items = flat(items)
	print(new_items)
'''
from collections import Iterable
def flat(items, ignore_types=(str, bytes)):
	'''
	http://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p14_flattening_nested_sequence.html
	'''
	for item in items:
		if isinstance(item, Iterable) and not isinstance(item, ignore_types):
			yield from flat(item)
		else:
			yield item

if __name__ == "__main__":
	items = [1, 2, [3, 4, [5, 6, 7], 8], 9]
	for i in flat(items):
		print(i)
