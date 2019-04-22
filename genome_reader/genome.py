class Genome(object):
    def __init__(self, name):
        self.name = name
        self.dict = dict()

    def __setitem__(self, key, item):
        self.dict[key] = item

    def __getitem__(self, key):
        return self.dict[key]

    def __repr__(self):
        return "<Genome: SNPs={:d}, name={!r}, >".format(self.__len__(), self.name)

    def __len__(self):
        return len(self.dict)

    def __delitem__(self, key):
        del self.dict[key]

    def clear(self):
        return self.dict.clear()

    def copy(self):
        return self.dict.copy()

    def has_key(self, k):
        return k in self.dict

    def update(self, *args, **kwargs):
        return self.dict.update(*args, **kwargs)

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

    def pop(self, *args):
        return self.dict.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.dict, dict_)

    def __contains__(self, item):
        return item in self.dict

    def __iter__(self):
        return iter(self.dict)


class Genotype(object):
    def __init__(self, genotype):
        self._genotype = genotype

    def __repr__(self):
        return "<Genotype %r>" % str(self)

    def __str__(self):
        return str(self._genotype)

    def __eq__(self, other):
        return self._genotype == other

