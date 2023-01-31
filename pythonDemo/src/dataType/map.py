class map(object):
    def __init__(self, func, *iterables):
        """
        map(func, *iterables) --> map object

        制作一个迭代器,使用每个Iterable的参数计算函数。
        当最短iterable耗尽时停止。

        >>> tuple(map(lambda x: x ** 2, [1, 2]))
        (1, 4)
        """
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """
        创建并返回实例化对象
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

    def __reduce__(self, *args, **kwargs):
        """
         返回pickling的状态信息。
        """
        pass

    def __next__(self, *args, **kwargs):
        """
         下一个值.next(self).
        """
        pass
