class zip(object):

    def __init__(self, *iterables):
        """
        zip(*iterables) --> 在输入耗尽之前产生元组的zip对象。

        zip对象生成n个长度的元组，其中n是作为位置参数传递给zip()
        的iterables数。每个元组中的第i个元素都来自zip()的第i个
        iterable参数。这将一直持续到最短的参数用尽为止。
        
        >>> list(zip('abcdefg', range(3), range(4)))
           [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
        """
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """
        创建并返回实例化对象
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
