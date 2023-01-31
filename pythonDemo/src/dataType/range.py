class range(object):

    start = property(lambda self: object(), lambda self, v: None,
                     lambda self: None)

    step = property(lambda self: object(), lambda self, v: None,
                    lambda self: None)

    stop = property(lambda self: object(), lambda self, v: None,
                    lambda self: None)

    def __init__(self, stop):
        """
        range(stop) -> range object
        range(start, stop[, step]) -> range object

        返回一个对象,该对象逐步生成从start(inclusive（包含))到stop(exclusive（不包含
        ))的整数序列.range(i, j)产生i, i+1, i+2, ..., j-1.
        开始默认为0,stop被忽略！ range(4)产生0, 1, 2, 3.这些正是4个元素的列表的有效索
        引.当给定step时,它指定增量(或减量).

        >>> list(range(0, 100, 10))
        [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        """
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """
        创建并返回实例化对象
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

    def __getattribute__(self, *args, **kwargs):
        """
        获取对象方法名。getattr(self, name).
        """
        pass

    def count(self, value):
        """
         rangeobject.count(value) -> integer -- 返回value的出现次数

        >>> range(0, 100, 10).count(10)
        1
        """
        return 0

    def index(self, value):
        """
        rangeobject.index(value) -> integer -- 返回value的索引.
        如果value不存在,则引发ValueError.

        >>> range(0, 100, 10).index(50)
        5
        """
        return 0

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
        range的长度。len(self).

        >>> range(0, 100, 10).__len__()
        10
        """
        pass

    def __bool__(self, *args, **kwargs):
        """
         bool值:self != 0

         >>> range(0, 100, 10).__bool__()
         True
         >>> range(0).__bool__()
         False
        """
        pass

    def __contains__(self, *args, **kwargs):
        """
        包含:Return key in self.

        >>> range(0, 100, 10).__contains__(10)
        True
        """
        pass

    def __getitem__(self, *args, **kwargs):
        """
        通过序号获取值:Return self[key].

        >>> range(0, 100, 10).__getitem__(2)
        20
        """
        pass

    def __reversed__(self, *args, **kwargs):
        """
        反转:Return a reverse iterator.

        >>> list(range(0, 100, 10).__reversed__())
        [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        """
        pass
