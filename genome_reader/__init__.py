import os

from genome_reader.genome import Genotype, Genome
from genome_reader.snp import SNP


def load(filename):
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