import re
from collections import Counter, defaultdict, namedtuple, deque
from itertools import chain, cycle, product, islice, count as count_from, groupby, takewhile, permutations, dropwhile

from cmath import phase, pi

from functools import lru_cache, total_ordering, partial

from copy import deepcopy

from operator import itemgetter

from itertools import islice

from math import gcd, factorial
from functools import reduce
from textwrap import wrap

infinity = float('inf')
bignum = 10 ** 100

up, down, left, right = -1j, 1j, -1, 1


def Input(day, line_parser=str.strip, file_template='data/advent2015/input{}.txt'):
    """For this day's input file, return a tuple of each line parsed by `line_parser`."""
    return mapt(line_parser, open(file_template.format(day)))


def integers(text):
    """A tuple of all integers in a string (ignore other characters)."""
    return mapt(int, re.findall(r'-?\d+', text))


def comma_integers(text):
    """A list of comma separated integers in a string."""
    return list(map(int, map(text, str.split(','))))


def mapt(fn, *args):
    """Do a map, and make the results into a tuple."""
    return tuple(map(fn, *args))


def first(iterable, default=None):
    """Return first item in iterable, or default."""
    return next(iter(iterable), default)


def nth(iterable, n):
    return next(islice(iter(iterable), n, n + 1))


cat = ''.join
fs = frozenset


def rangei(start, end, step=1):
    """Inclusive, range from start to end: rangei(a, b) = range(a, b+1)."""
    return range(start, end + 1, step)


def quantify(iterable, pred=bool):
    """Count how many items in iterable have pred(item) true."""
    return sum(map(pred, iterable))


def multimap(items):
    """Given (key, val) pairs, return {key: [val, ....], ...}."""
    result = defaultdict(list)
    for key, val in items:
        result[key].append(val)
    return result


def repeat(func, n, x):
    """Call function func n-times with initial argument x"""
    for _ in range(n):
        x = func(x)
    return x


def chunks(iterable, n):
    it = iter(iterable)
    while True:
        chunk_it = islice(it, n)
        try:
            first_el = next(chunk_it)
        except StopIteration:
            return
        yield chain((first_el,), chunk_it)


def manhattan(z, w):
    return quantify((z.real, z.imag, w.real, w.imag), abs)

