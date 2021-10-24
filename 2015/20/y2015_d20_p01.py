import fileinput as fi

import re
import itertools as it
import functools as ft

import more_itertools as mit

import math

import collections

import z3

import numpy as np

import string

# findall
# search
# parse
from parse import *

import regex

from tqdm import tqdm
INPUT = "".join(fi.input()).rstrip()

groups = INPUT.split("\n\n")
# print(groups[-1])
lines = list(INPUT.splitlines())

LIMIT = 36000000
UL = LIMIT//10

data = [0 for _ in range(UL)]

for x in tqdm(range(1, UL+1)):
    for y in range(x, UL+1, x):
        data[y-1] += x

for i, x in enumerate(data):
    if x >= LIMIT//10:
        print(i+1)
        break
