#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import io
import pandas as pd

lines = io.open("tokens.txt", encoding="utf-8").readlines()
tokens = [l.strip() for l in lines]

# generate all permutations up to length 6
permutations_per_length = [list(itertools.permutations(tokens, i)) for i in range(2, 6)]
permutations = [e for sublist in permutations_per_length for e in sublist]
codes = [u"".join(p) for p in permutations]

# valid codes are always 8-char long!
codes = [c for c in codes if len(c) == 8]

s = u"FORTY40£"
assert s in codes

print len(codes)
print codes[:5]

df = pd.DataFrame({ "code": codes, "tested": False, "valid": False })
df.to_csv("codes.csv", index = False, encoding='utf-8')
