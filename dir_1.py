#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 2:
    sys.exit('Usage: %s PATTERN' % sys.argv[0])

str_pattern = sys.argv[1]
folders = ['.']
results = []

for folder in folders:
    folders += [os.path.join(folder, x) for x in os.listdir(folder) if os.path.isdir(os.path.join(folder, x))]
    results += [os.path.join(folder, y) for y in os.listdir(folder) if os.path.isfile(os.path.join(folder, y)) and str_pattern in y]

for result in results:
    print(result)

print('找到%s个满足条件的文件。' % len(results))
