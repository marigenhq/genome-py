# coding=utf-8
"""conftest"""


import pytest

from genome import Genotype, SNP


@pytest.fixture()
def genotype():
    return Genotype('CC')


@pytest.fixture
def snp(genotype):
    return SNP(1, 762320, genotype)

