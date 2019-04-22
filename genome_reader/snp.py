class SNP(object):
    def __init__(self, chromosome, position, genotype):
        self.chromosome = str(chromosome)
        self.position = int(position)
        self.genotype = genotype

    def __repr__(self):
        return "<SNP: chromosome={!r} position={!r} genotype={!r}>".format(
            self.chromosome,
            self.position,
            self.genotype)