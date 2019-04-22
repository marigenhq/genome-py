import os


class Genome(object):
    def __init__(self, name):
        self.name = name
        self.dict = dict()

    def __setitem__(self, key, item):
        self.dict[key] = item

    def __getitem__(self, key):
        return self.dict[key]

    def __repr__(self):
        return "<Genome: SNPs={:d}, name={!r}>".format(self.__len__(),
                                                       os.path.os.path.basename(self.name))

    def __len__(self):
        return len(self.dict)

    def __contains__(self, item):
        return item in self.dict

    def __iter__(self):
        return iter(self.dict)

    def chromosome(self, key):
        def search(snp, key):
            if snp.chromosome == key:
                return snp
        return list(filter(lambda snp: search(snp, str(key)), self.dict.values()))


class Genotype(object):
    def __init__(self, genotype):
        self._genotype = genotype

    def __repr__(self):
        return "<Genotype: {!r}>".format(str(self))

    def __str__(self):
        return self._genotype

    def __eq__(self, other):
        return self._genotype == other

