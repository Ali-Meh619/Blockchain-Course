import hashlib
import numpy as np
import math as ma


class MerkleTreeCalculator:

    def sha256sum(self, filename):
        h = hashlib.sha256()
        with open(filename, 'rb', buffering=0) as f:
            for b in iter(lambda: f.read(128 * 1024), b''):
                h.update(b)
        return h.hexdigest()

    def h(self, x):
        sha = hashlib.sha256(str.encode(x)).hexdigest()
        return sha

    def calculate_merkle_root(self, n):

        t = [];

        for i in range(1, n + 1):
            t.append(self.sha256sum("../blockchain/resource/file" + str(i) + ".txt"))

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
                w.append(self.h(t[2 * j] + t[2 * j + 1]));

            mer.append(w);
            t = w;

        print(t[0])

        return mer


r = MerkleTreeCalculator()
tree = r.calculate_merkle_root()