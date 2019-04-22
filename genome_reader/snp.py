# coding=utf-8
"""SNP"""


class SNP:
    """
    SNP
    
    Parameters
    ----------
    chromosome : str or int
        chromosome
    position : str or int
        position
    genotype : Genotype
        genotype
    """
    def __init__(self, chromosome, position, genotype):
        self.chromosome = str(chromosome)
        self.position = int(position)
        self.genotype = genotype

    def __repr__(self):
        return '<SNP: chromosome={!r} position={!r} genotype={!r}>'.format(
            self.chromosome,
            self.position,
            self.genotype)

    def __eq__(self, other):
        return self.genotype == other.genotype and \
               self.position == other.position and \
               self.genotype == other.genotype
