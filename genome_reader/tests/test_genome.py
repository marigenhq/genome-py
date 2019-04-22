import os

from genome_reader import load


def test_load(snp):
    test_dir = os.path.dirname(os.path.realpath(__file__))
    genome = load(os.path.join(str(test_dir), 'test.txt'))
    assert len(genome) == 10
    assert repr(genome) == '<Genome: SNPs=10, name=\'test.txt\'>'
    assert 'rs75333668' in genome
    assert genome['rs75333668'] == snp
    assert [i for i in genome]
    assert len(genome.chromosome(1)) == 10
    assert len(genome.chromosome(2)) == 0


def test_snp(snp):
    assert repr(snp) == '<SNP: chromosome=\'1\' position=762320 genotype=<Genotype: \'CC\'>>'
    assert snp.chromosome == "1"
    assert snp.position == 762320


def test_genotype(genotype):
    assert genotype == "CC"
    assert repr(genotype) == '<Genotype: \'CC\'>'
    assert str(genotype) == 'CC'
