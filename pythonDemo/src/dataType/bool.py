class bool(int):
    def __init__(self, x):
        """
        bool(x) -> bool

        当参数x为True时返回True，否则返回False。
        内置的True和False是bool类的仅有两个实例。
        类bool是int类的子类，不能被子类化。

        >>> bool(True)
        True
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

    def __and__(self, *args, **kwargs):
        """
        按位与。self&value.

        >>> True.__and__(True)
        True
        >>> True.__and__(False)
        False
        """
        pass

    def __rand__(self, *args, **kwargs):
        """
        按位与。value&self

        >>> True.__rand__(False)
        False
        >>> True.__rand__(True)
        True
        """
        pass

    def __or__(self, *args, **kwargs):
        """
        按位或。self|value.

        >>> True.__or__(False)
        True
        >>> False.__or__(False)
        False
        """
        pass

    def __ror__(self, *args, **kwargs):
        """
        按位或。value|self.

        >>> True.__ror__(False)
        True
        """
        pass

    def __xor__(self, *args, **kwargs):
        """
        异或。self^value
        相同为True,不同为False

        >>> True.__xor__(False)
        True
        """
        pass

    def __rxor__(self, *args, **kwargs):
        """
        异或。value^self
        相同为True,不同为False

        >>> True.__rxor__(False)
        True
        """
        pass
