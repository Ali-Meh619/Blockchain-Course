# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:54:31 2020

@author: Ali Mehrabian
"""

import hashlib
import numpy as np
import math as m


def dis_log(p, g, y):
    k = (m.floor(m.log(p) / m.log(2)));

    result = 0
    power2 = 1

    for i in range(k):

        if int(pow(y, int((p - 1) / (power2 * 2)), p)) != 1:
            result = result + int(power2)

            y = y * int(pow(g, int(power2) * (p - 2), p))

        power2 = power2 * 2

    if result == 0:
        result = p - 1

    return result


q = int(input());
for k in range(0, q):
    p = int(input())
    g = int(input())
    y = int(input())
    print(dis_log(p, g, y))