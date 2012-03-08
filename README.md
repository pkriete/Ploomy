# Ploomy

Ploomy implements a very simple python bloom filter.

## What is a bloom filter?
A bloom filter is a fast and memory efficient way to check if an element has
_not_ been added to it (the reverse is _not_ true). This makes it a good
choice as a front to data store or when you need unique random data.

It works by hashing your input multiple times using a hashing algorithm
that returns a number between 0 and _n_. These numbers represent indexes in
a bit array. When an element is added to the filter, its hash indexes are
set to 1. When you query for an element it is once again hashed and the bloom
filter will return false iff any of the buckets are not 1.

[More info ...](http://en.wikipedia.org/wiki/Bloom_filter)

## Usage

Any hash function has collisions, so correctly sizing your bloom filter is
important to get the best possible performance from it. You must specify
both the number of buckets and the amount of hashing that should be done.

    buckets = 500
    hashes = 5
    bfilter = Bloom(buckets, hashes)

With that in place, you can add data and check if it exists:

    bfilter.add('pony')
    'pony' in bfilter # true
    'frog' in bfilter # false