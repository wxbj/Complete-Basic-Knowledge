class tuple(object):
    def __init__(self, seq=()):
        """
        内置的不可变序列。

        如果没有给出参数，构造函数将返回一个空元组。
        如果指定了iterable，则元组将从iterable的项初始化。
        如果参数是元组，则返回值是同一个对象。

        >>> tuple()
        ()
        >>> tuple([1, 2, 3])
        (1, 2, 3)
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

    def __iter__(self, *args, **kwargs):
        """
        迭代器协议。iter(self)
        """
        pass

    def __hash__(self, *args, **kwargs):
        """
        哈希值。hash(self)
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

    def __class_getitem__(self, *args, **kwargs):
        """
        //TODO 干什么用的？
         See PEP 585
        """
        pass

    def count(self, *args, **kwargs):
        """
        返回值的出现次数。

        >>> a = (1, 2, 3, 4, 5, 6)
        >>> a.count(1)
        1
        """
        pass

    def index(self, *args, **kwargs):
        """
        返回值的第一个索引。
        如果值不存在，则引发ValueError。

        >>> (1, 2, 3, 4, 5, 6).index(6)
        5
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

    def __mul__(self, *args, **kwargs):
        """
        乘法。self*value.

        >>> (1, 2).__mul__(2)
        (1, 2, 1, 2)
        """
        pass

    def __rmul__(self, *args, **kwargs):
        """
        乘法。value*self.

        >>> (1, 2).__rmul__(2)
        (1, 2, 1, 2)
        """
        pass

    def __add__(self, *args, **kwargs):
        """
        加法。self+value.

        >>> (1, 2).__add__((3, 4))
        (1, 2, 3, 4)
        """
        pass

    def __contains__(self, *args, **kwargs):
        """
        包含

        >>> (1, 2).__contains__((1,))
        True
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        元组长度。len(self).

        >>> (1, 2).__len__()
        2
        """
        pass

    def __getitem__(self, *args, **kwargs):
        """
        返回键值对应的值。self[key].

        >>> (1, 2).__getitem__(1)
        2
        """
        pass
