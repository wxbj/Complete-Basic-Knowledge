class filter(object):

    def __init__(self, function_or_None, iterable):
        """
        filter(function or None, iterable) --> filter object

        返回一个迭代器,该迭代器生成那些函数（item）为true的iterable项。
        如果函数为None,则返回为true的项。
        
        >>> list(filter(lambda x: x.startswith('hq'), ['hqHello', 'hqWorld',
        ... 'wzHello', 'wzWorld']))
        ['hqHello', 'hqWorld']
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
