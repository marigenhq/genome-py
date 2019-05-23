# coding=utf-8
"""Genome"""
import os

from .genome import Genome
from .snp import SNP
from .genotype import Genotype


def load(filename, provider='23andme'):
    """

    Parameters
    ----------
    filename : str
        filepath to data source
    provider : str
        the data provider

    Returns
    -------
    genome : Genome
        Genome data
    """
    filepath = os.path.expanduser(filename)
    genome = Genome(name=filepath)
    if provider.lower() == '23andme':
        reader = ttandme_reader
    elif provider.lower() == 'ancestry':
        reader = ancestry_reader
    else:
        raise TypeError('We don\'t support provider: {}'.format(provider))

    with open(filepath, 'r') as fin:
        while True:
            line = fin.readline()
            if not line.startswith('#'):
                break
        if provider.lower() == 'ancestry':
            line = fin.readline()
        while line:
            rsid, snp = reader(line)
            genome[rsid] = snp
            line = fin.readline()
    return genome


def ttandme_reader(line):
    rsid, chromosome, position, genotype = line.strip().split('\t')
    snp = SNP(chromosome=chromosome,
              position=position,
              genotype=Genotype(genotype))
    return rsid, snp


def ancestry_reader(line):
    rsid, chromosome, position, allele1, allele2 = line.strip().split('\t')
    genotype = allele1 + allele2
    snp = SNP(chromosome=chromosome,
              position=position,
              genotype=Genotype(genotype))
    return rsid, snp
