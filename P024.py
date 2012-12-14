#! /usr/bin/python

from itertools import permutations,imap

perms = list(imap(lambda x : ''.join(str(i) for i in x),list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))))
perms = sorted(perms)
print perms[999999]