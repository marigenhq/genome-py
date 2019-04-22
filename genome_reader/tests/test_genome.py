import os
from collections import Iterable

from genome_reader import load


def test_load():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    genome = load(os.path.join(str(test_dir), 'test.txt'))
    assert len(genome) == 10
    assert repr(genome) == '<Genome: SNPs=10, name=\'test.txt\'>'
    assert 'rs75333668' in genome
    assert isinstance(genome, Iterable)
    snp = genome['rs75333668']
    assert repr(snp) == '<SNP: chromosome=\'1\' position=762320 genotype=<Genotype: \'CC\'>>'
    assert snp.chromosome == "1"
    assert snp.position == 762320
    genotype = snp.genotype
    assert genotype == "CC"
    assert repr(genotype) == '<Genotype: \'CC\'>'
    assert str(genotype) == 'CC'
