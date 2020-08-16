# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:55:52 2020

@author: Ali Mehrabian
"""

import hashlib
import math as ma
import numpy as np


def h(x):
    sha = hashlib.sha256(str.encode(x)).hexdigest()
    return sha


def calculate_merkle_root(t):
    mer = [];
    mer.append(t);
    n = 20;
    k = ma.floor(ma.log(n) / ma.log(2));
    a = n;

    for i in range(k + 1):

        s = a / 2;
        a = ma.ceil(a / 2);
        w = [];

        if s != a:
            t.append(t[-1]);

        for j in range(a):
            w.append(h(t[2 * j] + t[2 * j + 1]));

        mer.append(w);
        t = w;

    return mer


def ind_find(n, m):
    k = ma.floor(ma.log(n) / ma.log(2));

    p = []

    for i in range(k + 1):

        if m % 2 == 0:

            p.append(m - 1)

        else:

            p.append(m + 1)

        m = ma.ceil(m / 2)

    return p


t = [];
n = 20;

for i in range(0, 21):

    if i != 20:

        t.append(input());
    else:
        m = int(input());

tree = calculate_merkle_root(t);
p = ind_find(n, m);
k = ma.floor(ma.log(n) / ma.log(2));
s = tree[k + 1]
print(s[0]);
for i in range(k + 1):
    a = tree[i];

    print(a[p[i] - 1])