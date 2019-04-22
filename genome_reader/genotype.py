# coding=utf-8
"""Genotype"""


class Genotype:
    """
    Genotype

    Parameters
    ----------
    genotype : str
        genotype
    """
    def __init__(self, genotype):
        self._genotype = genotype

    def __repr__(self):
        return '<Genotype: {!r}>'.format(str(self))

    def __str__(self):
        return self._genotype

    def __eq__(self, other):
        return self._genotype == other
