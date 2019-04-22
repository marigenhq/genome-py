# coding=utf-8
"""Genome"""

import os


class Genome:
    """
    Genome

    Parameters
    ----------
    name : str
        name of input file
    """
    def __init__(self, name):
        self.name = name
        self.dict = dict()

    def __setitem__(self, key, item):
        self.dict[key] = item

    def __getitem__(self, key):
        return self.dict[key]

    def __repr__(self):
        return '<Genome: SNPs={:d}, name={!r}>'.format(self.__len__(),
                                                       os.path.os.path.basename(self.name))

    def __len__(self):
        return len(self.dict)

    def __contains__(self, item):
        return item in self.dict

    def __iter__(self):
        return iter(self.dict)

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

    def chromosome(self, key):
        def search(snp, key):
            return snp if snp.chromosome == key else None
        return list(filter(lambda snp: search(snp, str(key)), self.dict.values()))
