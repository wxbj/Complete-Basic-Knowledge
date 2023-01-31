class list(object):
    def __init__(self, seq=()):
        """
        内置可变序列。
        如果没有给出参数，构造函数将创建一个新的空列表。
        如果指定，则参数必须是iterable。

        >>> list()
        []
        >>> list((1, 2, 3))
        [1, 2, 3]
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

    def __getattribute__(self, *args, **kwargs):
        """
        获取对象方法名
        """
        pass

    def __class_getitem__(self, *args, **kwargs):
        """
        //TODO 干什么用的？
         See PEP 585
        """
        pass

    def __sizeof__(self, *args, **kwargs):
        """
         返回内存中列表的大小（以字节为单位）。

         >>> [].__sizeof__()
         40
         >>> [1].__sizeof__()
         48
        """
        pass

    def __reversed__(self, *args, **kwargs):
        """
        返回列表上的反向迭代器。
        """
        pass

    __hash__ = None

    def append(self, *args, **kwargs):
        """
         将对象追加到列表的末尾。

         >>> [1, 2].append(3)
         [1, 2, 3]
        """
        pass

    def clear(self, *args, **kwargs):
        """
        从列表中删除所有项目。

        >>> [1, 2].clear()
        []
        """
        pass

    def copy(self, *args, **kwargs):
        """
        返回列表的浅表副本。

        >>> [1, 2].copy()
        [1, 2]
        """
        pass

    def count(self, *args, **kwargs):
        """
        返回值的出现次数。

        >>> [1, 2].count(1)
        1
        """
        pass

    def extend(self, *args, **kwargs):
        """
        通过从iterable中添加元素来扩展列表。

        >>> [1, 2].extend([3, 4])
        [1, 2, 3, 4]
        """
        pass

    def index(self, *args, **kwargs):
        """
        返回值的第一个索引。
        使用可选开始，测试从该位置开始。
        使用可选结束，停止在该位置比较S。
        如果值不存在，则引发ValueError。

        >>> [1,2].index(2)
        1
        >>> [1,2].index(1,0,1)
        0
        """
        pass

    def insert(self, *args, **kwargs):
        """
         在索引之前插入对象。

         >>> [1, 2].insert(1, 'a')
         [1, 'a', 2]
        """
        pass

    def pop(self, *args, **kwargs):
        """
        删除并返回索引处的项目（默认为最后一个）。
        如果列表为空或索引超出范围，则引发索引器错误。

        >>> [1, 2].pop()
        2
        >>> [1, 2].pop(0)
        1
        """
        pass

    def remove(self, *args, **kwargs):
        """
        删除第一次出现的值。
        如果值不存在，则引发ValueError。

        >>> [1, 2].remove(1)
        [2]
        """
        pass

    def reverse(self, *args, **kwargs):
        """
        反转

        >>> [1, 2].reverse()
        [2, 1]
        """
        pass

    def sort(self, *args, **kwargs):
        """
        按升序对列表进行排序并返回None。
        排序且稳定（即保持两个相等元素的顺序）。
        如果给定了键函数，请将其应用于每个列表项一次，并根据它们的函数值对它们进行升序或降序排序。
        反向标志可以设置为按降序排序。

        >>> [1, 2].sort(reverse=True)
        [2, 1]
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

    def __delitem__(self, *args, **kwargs):
        """
        按给定键删除。self[key]

        >>> a = [1,2]
        >>> a.__delitem__(0)
        [2]
        """
        pass

    def __getitem__(self, y):
        """
        根据键取值。x[y]

        >>> [1, 2].__getitem__(0)
        1
        """
        pass

    def __setitem__(self, *args, **kwargs):
        """
        通过键设置值。self[key]=value

        >>> a = [1, 2]
        >>> a.__setitem__(0, 3)
        [3, 2]
        """
        pass

    def __add__(self, *args, **kwargs):
        """
        加法。self+value.

        >>> [1, 2].__add__([3, 4])
        [1, 2, 3, 4]
        """
        pass

    def __iadd__(self, *args, **kwargs):
        """
        加法。self+=value.

        >>> a = [1, 2]
        >>> a.__iadd__([3])
        [1, 2, 3]
        """
        pass

    def __contains__(self, *args, **kwargs):
        """
        包含

        >>> [1, 2].__contains__(1)
        True
        """
        pass

    def __imul__(self, *args, **kwargs):
        """
        乘法。self*=value.

        >>> [1, 2].__imul__(2)
        [1, 2, 1, 2]
        """
        pass

    def __mul__(self, *args, **kwargs):
        """
        乘法。self*value.

        >>> [1, 2].__mul__(2)
        [1, 2, 1, 2]
        """
        pass

    def __rmul__(self, *args, **kwargs):
        """
        乘法。value*self.

        >>> [1, 2].__rmul__(2)
        [1, 2, 1, 2]
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        列表的长度。len(self).

        >>> list.__len__([1, 2])
        2
        """
        pass
