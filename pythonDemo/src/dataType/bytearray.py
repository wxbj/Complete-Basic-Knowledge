class bytearray(object):
    def __init__(self, source=None, encoding=None, errors='strict'):
        """
        bytearray(iterable_of_ints) -> bytearray
        bytearray(string, encoding[, errors]) -> bytearray
        bytearray(bytes_or_buffer) -> bytes_or_buffer的不可变副本
        bytearray(int) -> bytes对象,其大小由初始化为空字节的参数给定
        bytearray() -> 空字节对象

        从以下内容构造不可变的字节数组:
          -一个可生成range(256)内整数的迭代器
          -使用指定编码进行编码的文本字符串
          -实现缓冲区API的任何对象.
          -整数
        """
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """
        创建并返回实例化对象
        """
        pass

    def __sizeof__(self, *args, **kwargs):
        """
        返回对象在内存中的大小（以字节为单位）
        """
        pass

    def __str__(self, *args, **kwargs):
        """
        返回字符串。str(self)
        """
        pass

    __hash__ = None

    def __reduce_ex__(self, *args, **kwargs):
        """
         返回pickling的状态信息。
        """
        pass

    def __reduce__(self, *args, **kwargs):
        """
         返回pickling的状态信息。
        """
        pass

    def __repr__(self, *args, **kwargs):
        """
        返回字符串。repr(self)
        """
        pass

    def __getattribute__(self, *args, **kwargs):
        """
        获取对象方法名。getattr(self, name).
        """
        pass

    def __iter__(self, *args, **kwargs):
        """
        迭代器协议。iter(self)
        """
        pass

    def append(self, *args, **kwargs):
        """
        Append a single item to the end of the bytearray.

          item
            The item to be appended.
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

    def clear(self, *args, **kwargs):
        """ Remove all items from the bytearray. """
        pass

    def copy(self, *args, **kwargs):
        """ Return a copy of B. """
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
        Decode the bytearray using the codec registered for encoding.

          encoding
            The encoding with which to decode the bytearray.
          errors
            The error handling scheme to use for the handling of decoding errors.
            The default is 'strict' meaning that decoding errors raise a
            UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
            as well as any other name registered with codecs.register_error that
            can handle UnicodeDecodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None):
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

    def extend(self, *args, **kwargs):
        """
        Append all the items from the iterator or sequence to the end of the bytearray.

          iterable_of_ints
            The iterable of items to append.
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
        Create a bytearray object from a string of hexadecimal numbers.

        Spaces between two numbers are accepted.
        Example: bytearray.fromhex('B9 01EF') -> bytearray(b'\\xb9\\x01\\xef')
        """
        pass

    def hex(self):
        """
        Create a str of hexadecimal numbers from a bytearray object.

          sep
            An optional single character or byte to separate hex bytes.
          bytes_per_sep
            How many bytes between separators.  Positive values count from the
            right, negative values count from the left.

        Example:
        >>> value = bytearray([0xb9, 0x01, 0xef])
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

    def index(self, sub, start=None, end=None):
        """
        B.index(sub[, start[, end]]) -> int

        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the subsection is not found.
        """
        return 0

    def insert(self, *args, **kwargs):
        """
        Insert a single item into the bytearray before the given index.

          index
            The index where the value is to be inserted.
          item
            The item to be inserted.
        """
        pass

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

    def join(self, *args, **kwargs):
        """
        Concatenate any number of bytes/bytearray objects.

        The bytearray whose method is called is inserted in between each pair.

        The result is returned as a new bytearray object.
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

        If the argument is omitted or None, strip leading ASCII whitespace.
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
        Partition the bytearray into three parts using the given separator.

        This will search for the separator sep in the bytearray. If the separator is
        found, returns a 3-tuple containing the part before the separator, the
        separator itself, and the part after it as new bytearray objects.

        If the separator is not found, returns a 3-tuple containing the copy of the
        original bytearray object and two empty bytearray objects.
        """
        pass

    def pop(self, *args, **kwargs):
        """
        Remove and return a single item from B.

          index
            The index from where to remove the item.
            -1 (the default value) means remove the last item.

        If no index argument is given, will pop the last item.
        """
        pass

    def remove(self, *args, **kwargs):
        """
        Remove the first occurrence of a value in the bytearray.

          value
            The value to remove.
        """
        pass

    def removeprefix(self, *args, **kwargs):
        """
        Return a bytearray with the given prefix string removed if present.

        If the bytearray starts with the prefix string, return
        bytearray[len(prefix):].  Otherwise, return a copy of the original
        bytearray.
        """
        pass

    def removesuffix(self, *args, **kwargs):
        """
        Return a bytearray with the given suffix string removed if present.

        If the bytearray ends with the suffix string and that suffix is not
        empty, return bytearray[:-len(suffix)].  Otherwise, return a copy of
        the original bytearray.
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

    def reverse(self, *args, **kwargs):
        """ Reverse the order of the values in B in place. """
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
        Partition the bytearray into three parts using the given separator.

        This will search for the separator sep in the bytearray, starting at the end.
        If the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it as new bytearray
        objects.

        If the separator is not found, returns a 3-tuple containing two empty bytearray
        objects and the copy of the original bytearray object.
        """
        pass

    def rsplit(self, *args, **kwargs):
        """
        Return a list of the sections in the bytearray, using sep as the delimiter.

          sep
            The delimiter according which to split the bytearray.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.

        Splitting is done starting at the end of the bytearray and working to the front.
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
        Return a list of the sections in the bytearray, using sep as the delimiter.

          sep
            The delimiter according which to split the bytearray.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs):
        """
        Return a list of the lines in the bytearray, breaking at line boundaries.

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

    def __alloc__(self):
        """
        B.__alloc__() -> int

        Return the number of bytes actually allocated.
        """
        return 0

    def __delitem__(self, *args, **kwargs):
        """ Delete self[key]. """
        pass

    def __setitem__(self, *args, **kwargs):
        """ Set self[key] to value. """
        pass

    def __getitem__(self, *args, **kwargs):
        """
        返回键值对应的值。self[key].
        """
        pass

    def __contains__(self, *args, **kwargs):
        """ Return key in self. """
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

    def __len__(self, *args, **kwargs):
        """
        列表的长度。len(self).

        >>> list.__len__([1, 2])
        2
        """
        pass

    def __iadd__(self, *args, **kwargs):
        """ Implement self+=value. """
        pass

    def __add__(self, *args, **kwargs):
        """ Return self+value. """
        pass

    def __mod__(self, *args, **kwargs):
        """ Return self%value. """
        pass

    def __rmod__(self, *args, **kwargs):
        """ Return value%self. """
        pass

    def __imul__(self, *args, **kwargs):
        """ Implement self*=value. """
        pass

    def __mul__(self, *args, **kwargs):
        """ Return self*value. """
        pass

    def __rmul__(self, *args, **kwargs):
        """
         Return value*self.
        """
        pass
