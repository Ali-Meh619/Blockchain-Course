import numpy as np
import hashlib


class CollisionFinder:
    def __init__(self):
        pass

    def Hash_bits(message, x):

        a = hashlib.sha256(message.encode())

        return a.hexdigest()[64 - x:64]

    def floyd(x, initial):

        x0 = initial
        m0 = None
        m1 = None

        q0 = Hash_bits(x0, x)
        q1 = Hash_bits(q0, x)

        while q0 != q1:
            q0 = Hash_bits(q0, x)
            q1 = Hash_bits(Hash_bits(q1, x), x)

        CL = 0
        q0 = x0

        while q0 != q1:
            m0 = q0

            q0 = Hash_bits(q0, x)
            q1 = Hash_bits(q1, x)

            CL += 1

        CL = 1
        q1 = Hash_bits(q0, x)

        while q0 != q1:
            m1 = q1
            q1 = Hash_bits(q1, x)

            CL += 1

        return m0, m1

    def findCollision(self):

        username1, username2 = floyd(6, 0);

        password1, password2 = floyd(6, 1);

        return [username1, username2, password1, password2]



