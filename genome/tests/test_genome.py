import os

from genome import load


def test_genome(snp):
    test_dir = os.path.dirname(os.path.realpath(__file__))
    genome = load(os.path.join(str(test_dir), 'test.txt'))
    assert len(genome) == 10
    assert repr(genome) == '<Genome: SNPs=10, name=\'test.txt\'>'
    assert 'rs75333668' in genome
    assert genome['rs75333668'] == snp
    keys = genome.keys()
    values = genome.values()
    for key, val in zip(keys, values):
        assert genome[key] == val
    for key, val in genome.items():
        assert genome[key] == val
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
