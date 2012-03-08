# Murmur Hash
# Based on the java implementation found here:
# https://github.com/jbellis/cassandra-dev/blob/e284df7536ef32869b87d903a5f92f6a96c84801/src/com/facebook/infrastructure/utils/MurmurHash.java

import ctypes

# unsigned shift
def _ushift_right(num, offset):
    # performance ifs
    if offset == 0:
        return num
    elif offset < 0 or num == 0:
        return 0
    elif num < 0:
        # this is the case we're really looking for here:
        # shift as unsigned, but return as signed. Thank
        # the cookie monster for ctypes - pk
        num = ctypes.c_uint(num).value >> offset
        return ctypes.c_int(num).value
    return num >> offset;

def _cint_mul(num1, num2):
    return ctypes.c_int(num1 * num2).value    

def murmur(data, seed):
    length = len(data) # reasonable enough
    m = 0x5bd1e995
    r = 24
    
    h = seed ^ length
    len_4 = length >> 2
    
    for i in range(0, len_4):
        i_4 = i << 2
        k = ord(data[i_4 + 3])
        k = k << 8
        k = k | (ord(data[i_4 + 2]) & 0xff)
        k = k << 8
        k = k | (ord(data[i_4 + 1]) & 0xff)
        k = k << 8
        k = k | (ord(data[i_4 + 0]) & 0xff)        

        k = _cint_mul(k, m)
        k = k ^ _ushift_right(k, r)

        k = _cint_mul(k, m)
        h = _cint_mul(h, m)
        h = h ^ k
        
    len_m = len_4 << 2
    left = length - len_m
    
    if left != 0:
        if left >= 3:
            h = h ^ (ord(data[length - 3]) << 16)
        if left >= 2:
            h = h ^ (ord(data[length - 2]) << 8)
        if left >= 1:
            h = h ^ ord(data[length - 1])
        h = _cint_mul(h, m)
    
    h = h ^ _ushift_right(h, 13)
    h = _cint_mul(h, m)
    h = h ^ _ushift_right(h, 15)
    
    return h;