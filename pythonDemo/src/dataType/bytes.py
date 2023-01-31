class bytes(object):

    def __init__(self, value=b'', encoding=None, errors='strict'):
        """
        bytes(iterable_of_ints) -> bytes
        bytes(string, encoding[, errors]) -> bytes
        bytes(bytes_or_buffer) -> bytes_or_buffer的不可变副本
        bytes(int) -> bytes对象,其大小由初始化为空字节的参数给定
        bytes() -> 空字节对象

        从以下内容构造不可变的字节数组:
          -一个可生成range(256)内整数的迭代器
          -使用指定编码进行编码的文本字符串
          -实现缓冲区API的任何对象.
          -整数

        >>> bytes(range(1))
        b'\x00'
        >>> bytes("魏振", encoding="utf8")
        b'\xe9\xad\x8f\xe6\x8c\xaf'
        >>> bytes(2)
        b'\x00\x00'
        >>> bytes()
        b''
        """
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """
        创建并返回实例化对象
        """
        pass

    def __repr__(self, *args, **kwargs):
        """
        返回字符串。repr(self)
        """
        pass

    def __str__(self, *args, **kwargs):
        """
        返回字符串。str(self)
        """
        pass

    def __hash__(self, *args, **kwargs):
        """
         哈希值。hash(self)
        """
        pass

    def __iter__(self, *args, **kwargs):
        """
        迭代器协议。iter(self)
        """
        pass

    def __getnewargs__(self, *args, **kwargs):
        """
        序列化为元组
        """
        pass

    def __getattribute__(self, *args, **kwargs):
        """
        获取对象方法名。getattr(self, name).
        """
        pass

    def capitalize(self):
        """
        B.capitalize() -> copy of B

        Return a copy of B with only its first character capitalized (ASCII)
        and the rest lower-cased.
        """
        pass

    def center(self, *args, **kwargs):
        """
        Return a centered string of length width.

        Padding is done using the specified fill character.
        """
        pass

    def count(self, sub, start=None,
              end=None):
        """
        B.count(sub[, start[, end]]) -> int

        Return the number of non-overlapping occurrences of subsection sub in
        bytes B[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, *args, **kwargs):
        """
        Decode the bytes using the codec registered for encoding.

          encoding
            The encoding with which to decode the bytes.
          errors
            The error handling scheme to use for the handling of decoding errors.
            The default is 'strict' meaning that decoding errors raise a
            UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
            as well as any other name registered with codecs.register_error that
            can handle UnicodeDecodeErrors.
        """
        pass

    def endswith(self, suffix, start=None,
                 end=None):
        """
        B.endswith(suffix[, start[, end]]) -> bool

        Return True if B ends with the specified suffix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        suffix can also be a tuple of bytes to try.
        """
        return False

    def expandtabs(self, *args, **kwargs):
        """
        Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None,
             end=None):
        """
        B.find(sub[, start[, end]]) -> int

        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return 0

    @classmethod
    def fromhex(cls, *args,
                **kwargs):
        """
        Create a bytes object from a string of hexadecimal numbers.

        Spaces between two numbers are accepted.
        Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
        """
        pass

    def hex(self):
        """
        Create a str of hexadecimal numbers from a bytes object.

          sep
            An optional single character or byte to separate hex bytes.
          bytes_per_sep
            How many bytes between separators.  Positive values count from the
            right, negative values count from the left.

        Example:
        >>> value = b'\xb9\x01\xef'
        >>> value.hex()
        'b901ef'
        >>> value.hex(':')
        'b9:01:ef'
        >>> value.hex(':', 2)
        'b9:01ef'
        >>> value.hex(':', -2)
        'b901:ef'
        """
        pass

    def index(self, sub, start=None,
              end=None):
        """
        B.index(sub[, start[, end]]) -> int

        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the subsection is not found.
        """
        return 0

    def isalnum(self):
        """
        B.isalnum() -> bool

        Return True if all characters in B are alphanumeric
        and there is at least one character in B, False otherwise.
        """
        return False

    def isalpha(self):
        """
        B.isalpha() -> bool

        Return True if all characters in B are alphabetic
        and there is at least one character in B, False otherwise.
        """
        return False

    def isascii(self):
        """
        B.isascii() -> bool

        Return True if B is empty or all characters in B are ASCII,
        False otherwise.
        """
        return False

    def isdigit(self):
        """
        B.isdigit() -> bool

        Return True if all characters in B are digits
        and there is at least one character in B, False otherwise.
        """
        return False

    def islower(self):
        """
        B.islower() -> bool

        Return True if all cased characters in B are lowercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def isspace(self):
        """
        B.isspace() -> bool

        Return True if all characters in B are whitespace
        and there is at least one character in B, False otherwise.
        """
        return False

    def istitle(self):
        """
        B.istitle() -> bool

        Return True if B is a titlecased string and there is at least one
        character in B, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self):
        """
        B.isupper() -> bool

        Return True if all cased characters in B are uppercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def join(self, *args,
             **kwargs):
        """
        Concatenate any number of bytes objects.

        The bytes whose method is called is inserted in between each pair.

        The result is returned as a new bytes object.

        Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
        """
        pass

    def ljust(self, *args, **kwargs):
        """
        Return a left-justified string of length width.

        Padding is done using the specified fill character.
        """
        pass

    def lower(self):
        """
        B.lower() -> copy of B

        Return a copy of B with all ASCII characters converted to lowercase.
        """
        pass

    def lstrip(self, *args, **kwargs):
        """
        Strip leading bytes contained in the argument.

        If the argument is omitted or None, strip leading  ASCII whitespace.
        """
        pass

    @staticmethod
    def maketrans(*args, **kwargs):
        """
        Return a translation table useable for the bytes or bytearray translate method.

        The returned table will be one where each byte in frm is mapped to the byte at
        the same position in to.

        The bytes objects frm and to must be of the same length.
        """
        pass

    def partition(self, *args, **kwargs):
        """
        Partition the bytes into three parts using the given separator.

        This will search for the separator sep in the bytes. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing the original bytes
        object and two empty bytes objects.
        """
        pass

    def removeprefix(self, *args, **kwargs):
        """
        Return a bytes object with the given prefix string removed if present.

        If the bytes starts with the prefix string, return bytes[len(prefix):].
        Otherwise, return a copy of the original bytes.
        """
        pass

    def removesuffix(self, *args, **kwargs):
        """
        Return a bytes object with the given suffix string removed if present.

        If the bytes ends with the suffix string and that suffix is not empty,
        return bytes[:-len(prefix)].  Otherwise, return a copy of the original
        bytes.
        """
        pass

    def replace(self, *args, **kwargs):
        """
        Return a copy with all occurrences of substring old replaced by new.

          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None,
              end=None):
        """
        B.rfind(sub[, start[, end]]) -> int

        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None,
               end=None):
        """
        B.rindex(sub[, start[, end]]) -> int

        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raise ValueError when the subsection is not found.
        """
        return 0

    def rjust(self, *args, **kwargs):
        """
        Return a right-justified string of length width.

        Padding is done using the specified fill character.
        """
        pass

    def rpartition(self, *args, **kwargs):
        """
        Partition the bytes into three parts using the given separator.

        This will search for the separator sep in the bytes, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing two empty bytes
        objects and the original bytes object.
        """
        pass

    def rsplit(self, *args, **kwargs):
        """
        Return a list of the sections in the bytes, using sep as the delimiter.

          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.

        Splitting is done starting at the end of the bytes and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs):
        """
        Strip trailing bytes contained in the argument.

        If the argument is omitted or None, strip trailing ASCII whitespace.
        """
        pass

    def split(self, *args, **kwargs):
        """
        Return a list of the sections in the bytes, using sep as the delimiter.

          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs):
        """
        Return a list of the lines in the bytes, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None,
                   end=None):
        """
        B.startswith(prefix[, start[, end]]) -> bool

        Return True if B starts with the specified prefix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        prefix can also be a tuple of bytes to try.
        """
        return False

    def strip(self, *args, **kwargs):
        """
        Strip leading and trailing bytes contained in the argument.

        If the argument is omitted or None, strip leading and trailing ASCII whitespace.
        """
        pass

    def swapcase(self):
        """
        B.swapcase() -> copy of B

        Return a copy of B with uppercase ASCII characters converted
        to lowercase ASCII and vice versa.
        """
        pass

    def title(self):
        """
        B.title() -> copy of B

        Return a titlecased version of B, i.e. ASCII words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        pass

    def translate(self, *args, **kwargs):
        """
        Return a copy with each character mapped by the given translation table.

          table
            Translation table, which must be a bytes object of length 256.

        All characters occurring in the optional argument delete are removed.
        The remaining characters are mapped through the given translation table.
        """
        pass

    def upper(self):
        """
        B.upper() -> copy of B

        Return a copy of B with all ASCII characters converted to uppercase.
        """
        pass

    def zfill(self, *args, **kwargs):
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.

        The original string is never truncated.
        """
        pass

    def __contains__(self, *args, **kwargs):
        """
        包含:Return key in self.

        """
        pass

    def __getitem__(self, *args, **kwargs):
        """
        返回键值对应的值。self[key].
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        bytes的长度。len(self).
        """
        pass

    def __eq__(self, *args, **kwargs):
        """
        相等运算。self==value.
        整形比较真实大小,其他的按照ASCII表比较
        """
        pass

    def __ne__(self, *args, **kwargs):
        """
        不相等。self!=value
        整形比较真实大小,其他的按照ASCII表比较
        """
        pass

    def __ge__(self, *args, **kwargs):
        """
        大于等于。self>=value.
        整形比较真实大小,其他的按照ASCII表比较
        """
        pass

    def __gt__(self, *args, **kwargs):
        """
         大于。self>value.
        整形比较真实大小,其他的按照ASCII表比较
        """
        pass

    def __le__(self, *args, **kwargs):
        """
         小于等于。self<=value.
        整形比较真实大小,其他的按照ASCII表比较
        """
        pass

    def __lt__(self, *args, **kwargs):
        """
         小于。self<value.
        整形比较真实大小,其他的按照ASCII表比较
        """
        pass

    def __mod__(self, *args, **kwargs):
        """ Return self%value. """
        pass

    def __rmod__(self, *args, **kwargs):
        """ Return value%self. """
        pass

    def __mul__(self, *args, **kwargs):
        """ Return self*value. """
        pass

    def __rmul__(self, *args, **kwargs):
        """ Return value*self. """
        pass

    def __add__(self, *args, **kwargs):
        """ Return self+value. """
        pass
