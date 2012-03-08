from hashes import murmur

HASHES_MAX = 50

class Bloom(object):
    
    def __init__(self, capacity, num_hashes):
        self.filter = 0L
        self.capacity = capacity
        self.num_hashes = num_hashes
    
    def add(self, value):
        # print self._hash(value)
        for v in self._hash(value):
            self.filter |= (2 ** v)
    
    def has(self, value):
        ret = True
        for v in self._hash(value):
            ret = ret and bool(self.filter & (2 ** v))
        return ret
    
    def _hash(self, value):
        hash1 = murmur(value, 0)
        hash2 = murmur(value, hash1)
        return [abs((hash1 + i * hash2) % self.capacity) for i in range(self.num_hashes)]
    
    def __contains__(self, value):
        return self.has(value)