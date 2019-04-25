# coding=utf-8
"""Genome"""
import os

from .genome import Genome
from .snp import SNP
from .genotype import Genotype


def load(filename):
    """

    Parameters
    ----------
    filename : str
        filepath to data source

    Returns
    -------
    genome : Genome
        Genome data
    """
    filepath = os.path.expanduser(filename)
    genome = Genome(name=filepath)
    with open(filepath, 'r') as fin:
        while True:
            line = fin.readline()
            if not line.startswith('#'):
                break
        while line:
            rsid, chromosome, position, genotype = line.strip().split('\t')
            snp = SNP(chromosome=chromosome,
                      position=position,
                      genotype=Genotype(genotype))
            genome[rsid] = snp
            line = fin.readline()
    return genome
