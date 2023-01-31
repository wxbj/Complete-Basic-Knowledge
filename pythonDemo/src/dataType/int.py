class int(object):
    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)
    """
    有理数的分母,约分之后的最小值
    >>> (2).denominator
    1
    """

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)
    """
    有理数的分子,约分之后的最小值
    >>> (2).numerator
    2
    """

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)
    """
    复数的实部
    >>> (2+2j).real
    2.0
    >>> (2).real
    2
    """

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)
    """
    复数的虚部
    >>> (2).imag
    0
    >>> (2+2j).imag
    2.0
    """

    def __init__(self, x, base=10):
        """
        int([x]) -> integer
        int(x, base=10) -> integer

        [x]表示可选值.
        base表示进制,默认为10进制.
        没有给定参数时返回0。
        x是一个数字时，返回x.__int__(),当x为浮点数时，向下取整。
        x不是数字时,必须是表示整数文本的字符串、字节或字节数组的实例
        x中允许包含'+'、'-'号，两边可出现空格。
        base取值范围为0和2-36。
        base=0表示将任意进制下的的字符串解释为整型文本。
        浮点数的字符串形式不能直接转换为整数
         >>> int()
         0
         >>> int(1.11)
         1
        >>> int('0b100',0)
        4
        >>> int(' +9 ')
        9
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

    def __format__(self, *args, **kwargs):
        """
         格式化输出,用空格填充
        """
        pass

    def __getattribute__(self, *args, **kwargs):
        """
         获取属性。getattr(self, name)
        """
        pass

    def __getnewargs__(self, *args, **kwargs):
        """
        序列化为元组
        """
        pass

    def __hash__(self, *args, **kwargs):
        """
        哈希值。hash(self)
        """
        pass

    def __index__(self, *args, **kwargs):
        """
        如果self适合用作列表的索引，则返回self转换为的整数。
        """
        pass

    def __sizeof__(self, *args, **kwargs):
        """
        返回对象在内存中的大小（以字节为单位）

        >>> (2).__sizeof__()
        28
        >>> (110000000000).__sizeof__()
        32
        >>> (1011111111).__sizeof__()
        28
        """
        pass

    def __pos__(self, *args, **kwargs):
        """
        //TODO 目前不知道有什么用
        在原数的基础上加上＋
        +self

        >>> (-1).__pos__()
        -1
        >>> (1).__pos__()
        1
        """
        pass

    @classmethod
    def from_bytes(cls, *args, **kwargs):
        """
        返回由给定字节数组表示的整数。

        bytes/字节数组
            存放要转换的字节数组。
            参数必须支持缓冲区协议，或者是生成字节的可迭代的对象。
            字节和字节数组是支持缓冲区协议的内置对象的示例。
        byteorder/字节序,取值为（'big'或'little'或'sys.byteorder')
            用于表示整数的字节顺序。
            如果字节顺序为“大端”，则最高有效字节位于字节数组的开头.
            如果字节顺序为“小端”，则最高有效字节位于字节数组的末尾.
            要请求主机系统的本机字节顺序，请使用'sys.byteorder'作为字节顺序值.
        signed/符号,取值为(True或False)
            指示是否使用2进制补码表示整数。
        >>> int.from_bytes(bytes=b'\xff', byteorder='big', signed=False)
        255
        """
        pass

    def to_bytes(self, *args, **kwargs):
        """
        返回表示整数的字节数组。

          length
            要使用的字节对象的长度。如果整数不能用给定的字节数表示，则会引发溢出错误。
          byteorder/字节序,取值为（'big'或'little'或'sys.byteorder')
            用于表示整数的字节顺序。
            如果字节顺序为“大端”，则最高有效字节位于字节数组的开头.
            如果字节顺序为“小端”，则最高有效字节位于字节数组的末尾.
            要请求主机系统的本机字节顺序，请使用'sys.byteorder'作为字节顺序值.
          signed/符号,取值为(True或False)
            确定是否使用2进制补码表示整数。
            如果signed值为False，并且给出了一个负整数，则会引发溢出错误。
        >>> (2).to_bytes(4, 'big', signed=True)
        b'\x00\x00\x00\x02'
        >>> (2).to_bytes(4, 'little', signed=True)
        b'\x02\x00\x00\x00'
        """
        pass

    def as_integer_ratio(self):
        """
        最小整数比

        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self):
        """
        用二进制表示所需的位数.

        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs):
        """
        复共轭

        >>> 3-9j.conjugate()
        (3+9j)
        """
        pass

    def __add__(self, *args, **kwargs):
        """
        求两数和。self+value

        >>> (8).__add__(9)
        17
        """
        pass

    def __radd__(self, *args, **kwargs):
        """
        两数和。value+self

         >>> (2).__radd__(3)
         5
        """
        pass

    def __sub__(self, *args, **kwargs):
        """
        减法。self-value.

        >>> (1).__sub__(2)
        -1
        """
        pass

    def __rsub__(self, *args, **kwargs):
        """
        减法。value-self.

        >>> (1).__rsub__(4)
        3
        """
        pass

    def __mul__(self, *args, **kwargs):
        """
        两数相乘。self*value

        >>> (2).__mul__(3)
        6
        """
        pass

    def __rmul__(self, *args, **kwargs):
        """
        两数相乘。value*self

        >>> (2).__mul__(5)
        10
        """
        pass

    def __divmod__(self, *args, **kwargs):
        """
         两数相除,返回(商,余数)。divmod(self, value)

         >>> (5).__divmod__(3)
         (1, 2)
        """
        pass

    def __rdivmod__(self, *args, **kwargs):
        """
        两数相除,返回(商,余数)。divmod(value,self)

         >>> (5).__rdivmod__(3)
         (0, 3)
        """
        pass

    def __mod__(self, *args, **kwargs):
        """
        取余。self%value

        >>> (2).__mod__(4)
        2
        """
        pass

    def __rmod__(self, *args, **kwargs):
        """
        取余。value%self.

        >>> (2).__rmod__(5)
        1
        """
        pass

    def __floordiv__(self, *args, **kwargs):
        """
         取商。self//value

        >>> (100).__floordiv__(9)
        11
        """
        pass

    def __rfloordiv__(self, *args, **kwargs):
        """
        取商。value//self

        >>> (3).__rfloordiv__(9)
        3
        """
        pass

    def __truediv__(self, *args, **kwargs):
        """
        真除，返回的数据类型为float。self/value.

        >>> (4).__truediv__(2)
        2.0
        """
        pass

    def __rtruediv__(self, *args, **kwargs):
        """
        真除，返回的数据类型为float。value/self.

        >>> (2).__rtruediv__(4)
        2.0
        """
        pass

    def __and__(self, *args, **kwargs):
        """
         按位与：同时为1才为1，其他为0。self&value

         8： 0 0 0 0 1 0 0 0
         7： 0 0 0 0 0 1 1 1
         0： 0 0 0 0 0 0 0 0
        >>> (8).__and__(7)
        0
        """
        pass

    def __rand__(self, *args, **kwargs):
        """
        按位与：同时为1才为1，其他为0。value&self

         7： 0 0 0 0 0 1 1 1
         8： 0 0 0 0 1 0 0 0
         0： 0 0 0 0 0 0 0 0
        >>> (8).__rand__(7)
        0
        """
        pass

    def __or__(self, *args, **kwargs):
        """
        按位或。self|value

        0000 0010  2
        0000 0011  3
        0000 0011  3
        >>> (2).__or__(3)
        3
        """
        pass

    def __ror__(self, *args, **kwargs):
        """
        按位或。value|self.

        0000 0010  2
        0000 0011  3
        0000 0011  3
        >>> (3).__ror__(2)
        3
        """
        pass

    def __xor__(self, *args, **kwargs):
        """
        按位异或操作,相同为0不同为1。self^value.

        2与4按位异或得6
        0000 0100
        0000 0010
        0000 0110
        >>> (2).__rxor__(2)
        0
        >>> (4).__rxor__(2)
        6
        """
        pass

    def __rxor__(self, *args, **kwargs):
        """
        按位异或操作,相同为0不同为1。value^self.

        2与4按位异或得6
        0000 0010
        0000 0100
        0000 0110
        >>> (2).__rxor__(2)
        0
        >>> (2).__rxor__(4)
        6
        """
        pass

    def __lshift__(self, *args, **kwargs):
        """
        按位左移。self<<value

        将2左移两位
        0000 0010   2
        0000 1000   8
         >>> (2).__lshift__(2)
         8
        """
        pass

    def __rlshift__(self, *args, **kwargs):
        """
        按位左移。value<<self

        将1左移两位
        0000 0001
        0000 0100
        >>> (2).__rlshift__(1)
        4
        """
        pass

    def __rshift__(self, *args, **kwargs):
        """
        右移。self>>value.

        将4右移1位
        0000 0100
        0000 0010
        >>> (4).__rshift__(1)
        2
        """
        pass

    def __rrshift__(self, *args, **kwargs):
        """
        右移。value>>self.

        将4右移1位
        0000 0100
        0000 0010
        >>> (1).__rrshift__(4)
        2
        """
        pass

    def __invert__(self, *args, **kwargs):
        """
         按位取反
         注意：计算机中整数以补码存放
         负数转原码简便计算：如10010110是补码，符号位与最后一个1之间的所有数字按位取反，得11101010

         0000 0011  3
         1111 1100  是负数,要转为原码 1000 0100  -4
         >>> (3).__invert__()
         -4
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

    def __pow__(self, *args, **kwargs):
        """
        幂运算。pow(self, value, mod)
        当传入前两个参数时,返回幂值
        当传入三个参数时,返回前两个数对第三个参数的余数

        >>> pow(2, 3)
        8
        >>> pow(2, 3, 6)
        2
        """
        pass

    def __rpow__(self, *args, **kwargs):
        """
        运算。pow(value, self, mod)
        当传入前两个参数时,返回幂值
        当传入三个参数时,返回前两个数对第三个参数的余数

        >>> (2).__rpow__(3)
        9
        >>> (2).__rpow__(3,8)
        1
        """
        pass

    def __abs__(self, *args, **kwargs):
        """
         绝对值。abs(self)

        >>> (8).__abs__()
        8
        >>> (-8).__abs__()
        8
        >>> (0).__abs__()
        0
        """
        pass

    def __bool__(self, *args, **kwargs):
        """
        bool值
        0的bool值为False
        其他bool值为True

        >>> (-1).__bool__()
        True
        >>> (1).__bool__()
        True
        >>> (0).__bool__()
        False
        """
        pass

    def __neg__(self, *args, **kwargs):
        """
        相反数。-self

        >>> (2).__neg__()
        -2
        >>> (-2).__neg__()
        2
        """
        pass

    def __ceil__(self, *args, **kwargs):
        """
         向上取整

         >>> (0).__ceil__()
         0
         >>> (-1).__ceil__()
         -1
         >>> (1).__ceil__()
         1
         """
        pass

    def __floor__(self, *args, **kwargs):
        """
         向下取整

         >>> (0).__floor__()
         0
         >>> (-1).__floor__()
         -1
         >>> (1).__floor__()
         1
        """
        pass

    def __round__(self, *args, **kwargs):
        """
        四舍五入。round(self, ndigits)
        传入一个参数时,默认向整数转换
        传入两个参数时,第二个参数为保留的位数
        ndigits 参数可以是负数,此时,该运算会作用在十位、百位、千位等上面

        >>> (2).__round__()
        2
        >>> (222).__round__(-1)
        220
        """
        pass

    def __trunc__(self, *args, **kwargs):
        """
         截断

        >>> (10).__trunc__()
        10
        """
        pass

    def __float__(self, *args, **kwargs):
        """
         转换为浮点数。float(self)

        >>> (3).__float__()
        3.0
        """
        pass

    def __int__(self, *args, **kwargs):
        """
        转换为整数。int(self)

         >>> (1).__int__()
         1
        """
        pass