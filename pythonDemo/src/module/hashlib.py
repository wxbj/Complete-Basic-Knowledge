"""
NAME
    hashlib - hashlib module - A common interface to many hash functions.

MODULE REFERENCE
    https://docs.python.org/3.9/library/hashlib

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    new(name, data=b'', **kwargs) - returns a new hash object implementing the
                                    given hash function; initializing the hash
                                    using the given binary data.

    Named constructor functions are also available, these are faster
    than using new(name):

    md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
    sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.

    More algorithms may be available on your platform but the above are guaranteed
    to exist.  See the algorithms_guaranteed and algorithms_available attributes
    to find out what algorithm names can be passed to new().

    NOTE: If you want the adler32 or crc32 hash functions they are available in
    the zlib module.

    Choose your hash function wisely.  Some have known collision weaknesses.
    sha384 and sha512 will be slow on 32 bit platforms.

    Hash objects have these methods:
     - update(data): Update the hash object with the bytes in data. Repeated calls
                     are equivalent to a single call with the concatenation of all
                     the arguments.
     - digest():     Return the digest of the bytes passed to the update() method
                     so far as a bytes object.
     - hexdigest():  Like digest() except the digest is returned as a string
                     of double length, containing only hexadecimal digits.
     - copy():       Return a copy (clone) of the hash object. This can be used to
                     efficiently compute the digests of datas that share a common
                     initial substring.

    For example, to obtain the digest of the byte string 'Nobody inspects the
    spammish repetition':

        >>> import hashlib
        >>> m = hashlib.md5()
        >>> m.update(b"Nobody inspects")
        >>> m.update(b" the spammish repetition")
        >>> m.digest()
        b'\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'

    More condensed:

        >>> hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
        'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'

CLASSES
    builtins.object
        _blake2.blake2b
        _blake2.blake2s

    class blake2b(builtins.object)
     |  blake2b(data=b'', /, *, digest_size=64, key=b'', salt=b'', person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False, usedforsecurity=True)
     |
     |  Return a new BLAKE2b hash object.
     |
     |  Methods defined here:
     |
     |  copy(self, /)
     |      Return a copy of the hash object.
     |
     |  digest(self, /)
     |      Return the digest value as a bytes object.
     |
     |  hexdigest(self, /)
     |      Return the digest value as a string of hexadecimal digits.
     |
     |  update(self, data, /)
     |      Update this hash object's state with the provided bytes-like object.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  block_size
     |
     |  digest_size
     |
     |  name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  MAX_DIGEST_SIZE = 64
     |
     |  MAX_KEY_SIZE = 64
     |
     |  PERSON_SIZE = 16
     |
     |  SALT_SIZE = 16

    class blake2s(builtins.object)
     |  blake2s(data=b'', /, *, digest_size=32, key=b'', salt=b'', person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False, usedforsecurity=True)
     |
     |  Return a new BLAKE2s hash object.
     |
     |  Methods defined here:
     |
     |  copy(self, /)
     |      Return a copy of the hash object.
     |
     |  digest(self, /)
     |      Return the digest value as a bytes object.
     |
     |  hexdigest(self, /)
     |      Return the digest value as a string of hexadecimal digits.
     |
     |  update(self, data, /)
     |      Update this hash object's state with the provided bytes-like object.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  block_size
     |
     |  digest_size
     |
     |  name
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  MAX_DIGEST_SIZE = 32
     |
     |  MAX_KEY_SIZE = 32
     |
     |  PERSON_SIZE = 8
     |
     |  SALT_SIZE = 8

FUNCTIONS
    md5 = openssl_md5(string=b'', *, usedforsecurity=True)
        Returns a md5 hash object; optionally initialized with a string

    new = __hash_new(name, data=b'', **kwargs)
        new(name, data=b'') - Return a new hashing object using the named algorithm;
        optionally initialized with data (which must be a bytes-like object).

    pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None)
        Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function.

    sha1 = openssl_sha1(string=b'', *, usedforsecurity=True)
        Returns a sha1 hash object; optionally initialized with a string

    sha224 = openssl_sha224(string=b'', *, usedforsecurity=True)
        Returns a sha224 hash object; optionally initialized with a string

    sha256 = openssl_sha256(string=b'', *, usedforsecurity=True)
        Returns a sha256 hash object; optionally initialized with a string

    sha384 = openssl_sha384(string=b'', *, usedforsecurity=True)
        Returns a sha384 hash object; optionally initialized with a string

    sha3_224 = openssl_sha3_224(string=b'', *, usedforsecurity=True)
        Returns a sha3-224 hash object; optionally initialized with a string

    sha3_256 = openssl_sha3_256(string=b'', *, usedforsecurity=True)
        Returns a sha3-256 hash object; optionally initialized with a string

    sha3_384 = openssl_sha3_384(string=b'', *, usedforsecurity=True)
        Returns a sha3-384 hash object; optionally initialized with a string

    sha3_512 = openssl_sha3_512(string=b'', *, usedforsecurity=True)
        Returns a sha3-512 hash object; optionally initialized with a string

    sha512 = openssl_sha512(string=b'', *, usedforsecurity=True)
        Returns a sha512 hash object; optionally initialized with a string

    shake_128 = openssl_shake_128(string=b'', *, usedforsecurity=True)
        Returns a shake-128 variable hash object; optionally initialized with a string

    shake_256 = openssl_shake_256(string=b'', *, usedforsecurity=True)
        Returns a shake-256 variable hash object; optionally initialized with a string

DATA
    __all__ = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'bla...
    algorithms_available = {'blake2b', 'blake2s', 'md4', 'md5', 'md5-sha1'...
    algorithms_guaranteed = {'blake2b', 'blake2s', 'md5', 'sha1', 'sha224'...

FILE
    d:\software\python\python39\lib\hashlib.py
"""