import os

from genome_reader import load


def test_load():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    genome = load(os.path.join(str(test_dir), 'test.txt'))
    assert len(genome) == 10
    snp = genome['rs75333668']
    assert snp.chromosome == "1"
    assert snp.position == 762320
    assert snp.genotype == "CC"