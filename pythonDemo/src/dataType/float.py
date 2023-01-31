class float(object):
    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)
    """
    复数的虚部
    >>> (2.2).imag
    0.0
    >>> (2.2+2.3j).imag
    2.3
    """

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)
    """
    复数的实部
    >>> (2+2j).real
    2.0
    >>> 2.2.real
    2.2
    """

    def __init__(self, *args, **kwargs):
        """
        将一个字符串或者整数转换为浮点数

        >>> float('2')
        2.0
        >>> float(2)
        2.0
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

    def __pos__(self, *args, **kwargs):
        """
        //TODO 目前不知道有什么用
        在原数的基础上加上＋
        +self

        >>> -1.1.__pos__()
        -1.1
        >>> 1.1.__pos__()
        1.1
        """
        pass

    def __set_format__(self, *args, **kwargs):
        """
        //TODO 目前尚不明白怎么用
        您可能不想使用此功能。

        typestr/字符串类型
          必须为“double”或“float”。
        fmt
          必须是“unknown”、“IEEE，big-endian”或“IEEE，little-endian”中的一个，
          此外，如果它看起来与底层C现实相匹配，则只能是后两个中的一个。

        它主要用于Python的测试套件中。

        重写C级浮点类型的自动确定。
        这会影响浮动与二进制字符串之间的转换方式。
        """
        pass

    def __getformat__(self, *args, **kwargs):
        """
        //TODO 目前尚不知道不知道怎么用
        您可能不想使用此功能。

          typestr
          必须为“double”或“float”。

        它主要用于Python的测试套件中。

        此函数返回“unknown”、“IEEE,big-endian”或“IEEE,little-endian”中
        最能描述由typestr命名的C类型使用的浮点数格式的一个。
        """
        pass

    def as_integer_ratio(self):
        """
        最小整数比
        若传入整数,返回格式为(self,1)
        若传入浮点数,格式为(分子,分母)
        注意由于计算机中以2进制存储,所以不是所有的小数都可以精确表达
        2的次数  -1      -2        -3          -4       -5         -6       -7          -8         -9          -10
        值      0.5     0.25     0.125       0.0625   0.03125   0.015625 0.0078125  0.00390625 0.001953125 0.0009765625
        由上面的部分表格可以看出来,0.1不能精确表达,所以当想返回0.1的整数比时,会返回奇奇怪怪的值
        最有由上面表格中的任意组合的小数才能精确表达
        当为无穷大时引发 OverflowError错误
        当为NaN时引发 ValueError。

        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        >>> 0.5009765625.as_integer_ratio()
        (513, 1024)
        >>> 0.1.as_integer_ratio()
        (3602879701896397, 36028797018963968)
        """
        pass

    def conjugate(self, *args, **kwargs):
        """
        复共轭

        >>> 3.1-9.1j.conjugate()
        (3.1+9.1j)
        """
        pass

    @staticmethod
    def fromhex(*args, **kwargs):
        """
        从十六进制字符串创建一个浮点数。

        p10:表示乘以2的10次幂
        p-1074：表示乘以2的-1074次幂
        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -5e-324
        """
        pass

    def hex(self):
        """
        返回浮点数的十六进制表示。

        注意：由于大多数小数并不能精确表示,所以会得出很奇怪的数
        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        >>> (0.5).hex()
        0x1.0000000000000p-1
        """
        pass

    def is_integer(self, *args, **kwargs):
        """
         如果浮点数是整数，则返回 True。

        >>> 5.1.is_integer()
        False
        >>> 5.0.is_integer()
        True
        """
        pass

    def __add__(self, *args, **kwargs):
        """
        求两数和。self+value

        >>> 8.2.__add__(9.3)
        17.5
        """
        pass

    def __radd__(self, *args, **kwargs):
        """
        两数和。value+self

         >>> 2.2.__radd__(3.3)
         5.5
        """
        pass

    def __sub__(self, *args, **kwargs):
        """
        减法。self-value.

        >>> 2.3.__sub__(2.1)
        0.19999999999999973
        """
        pass

    def __rsub__(self, *args, **kwargs):
        """
        减法。value-self.

        >>> 1.1.__rsub__(2)
        0.8999999999999999
        """
        pass

    def __mul__(self, *args, **kwargs):
        """
        两数相乘。self*value

        >>> 2.1.__mul__(3.1)
        6.510000000000001
        """
        pass

    def __rmul__(self, *args, **kwargs):
        """
        两数相乘。value*self

        >>> 2.1.__mul__(5.1)
        10.709999999999999
        """
        pass

    def __divmod__(self, *args, **kwargs):
        """
         两数相除,返回(商,余数)。divmod(self, value)

         >>> 5.2.__divmod__(3.1)
         (1.0, 2.1)
        """
        pass

    def __rdivmod__(self, *args, **kwargs):
        """
        两数相除,返回(商,余数)。divmod(value,self)

         >>> 5.2.__rdivmod__(3.3)
         (0.0, 3.3)
        """
        pass

    def __mod__(self, *args, **kwargs):
        """
        取余。self%value

        >>> 2.1.__mod__(4.2)
        2.1
        """
        pass

    def __rmod__(self, *args, **kwargs):
        """
        取余。value%self.

        >>> 2.1.__rmod__(5.3)
        1.0999999999999996
        """
        pass

    def __floordiv__(self, *args, **kwargs):
        """
         取商。self//value

        >>> 100.1.__floordiv__(9.2)
        10.0
        """
        pass

    def __rfloordiv__(self, *args, **kwargs):
        """
        取商。value//self

        >>> 3.1.__rfloordiv__(9.2)
        2.0
        """
        pass

    def __truediv__(self, *args, **kwargs):
        """
        真除，返回的数据类型为float。self/value.

        >>> 2.33.__truediv__(2.2)
        1.059090909090909
        """
        pass

    def __rtruediv__(self, *args, **kwargs):
        """
        真除，返回的数据类型为float。value/self.

        >>> 2.5.__rtruediv__(4.2)
        1.6800000000000002
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
        注意：只有三个参数都是整数是才可以使用三个参数的调用

        >>> pow(2.2, 3.3)
        13.489468760533386
        >>> pow(2, 3, 6)
        2
        """
        pass

    def __rpow__(self, *args, **kwargs):
        """
        运算。pow(value, self, mod)
        当传入前两个参数时,返回幂值
        当传入三个参数时,返回前两个数对第三个参数的余数
        注意：只有三个参数都是整数是才可以使用三个参数的调用

        >>> 2.2.__rpow__(3.3)
        13.827086118044146
        >>> (2).__rpow__(3,8)
        1
        """
        pass

    def __abs__(self, *args, **kwargs):
        """
         绝对值。abs(self)

        >>> 8.2.__abs__()
        8.2
        >>> -8.2.__abs__()
        8.2
        >>> 0.0.__abs__()
        0.0
        """
        pass

    def __bool__(self, *args, **kwargs):
        """
        bool值
        0.0的bool值为False
        正值bool值为True
        负值bool值为-1

        >>> -1.1.__bool__()
        -1
        >>> 1.1.__bool__()
        True
        >>> 0.0.__bool__()
        False
        """
        pass

    def __neg__(self, *args, **kwargs):
        """
        相反数。-self

        >>> 2.2.__neg__()
        -2.2
        >>> -2.2.__neg__()
        2.2
        """
        pass

    def __ceil__(self, *args, **kwargs):
        """
         向上取整

         >>> 0.0.__ceil__()
         0
         >>> -1.1.__ceil__()
         -1
         >>> 1.1.__ceil__()
         2
         """
        pass

    def __floor__(self, *args, **kwargs):
        """
         向下取整

         >>> (0).__floor__()
         0
         >>> -1.1.__floor__()
         -2
         >>> 1.1.__floor__()
         1
        """
        pass

    def __round__(self, *args, **kwargs):
        """
        四舍五入。round(self, ndigits)
        传入一个参数时,默认向整数转换
        传入两个参数时,第二个参数为保留的小数位数
        ndigits 参数可以是负数,此时,该运算会作用在十位、百位、千位等上面
        当一个值刚好在两个边界的中间的时候,返回离它最近的偶数

        >>> 2.3.__round__()
        2
        >>> 2.3.__round__(1)
        2.3
        >>> 2.5.__round__()
        2
        >>> 3.5.__round__()
        4
        >>> (222).__round__(-1)
        220
        """
        pass

    def __trunc__(self, *args, **kwargs):
        """
         截断

        >>> 1.1.__trunc__()
        1
        """
        pass

    def __float__(self, *args, **kwargs):
        """
         转换为浮点数。float(self)

        >>> 3.3.__float__()
        3.3
        """
        pass

    def __int__(self, *args, **kwargs):
        """
        转换为整数。int(self)

         >>> 1.1.__int__()
         1
        """
        pass