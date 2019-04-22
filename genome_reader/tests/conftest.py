import pytest

from genome_reader import Genotype, SNP


@pytest.fixture()
def genotype():
    return Genotype('CC')


@pytest.fixture
def snp(genotype):
    return SNP(1, 762320, genotype)

