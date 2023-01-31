class set(object):
    def __init__(self, seq=()):
        """
        set() -> 新的空集对象
        set(iterable) -> 新集合对象
        构建独特元素的无序集合。

        >>> set()
        set()
        >>> set([1, 2, 3])
        {1, 2, 3}
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
        获取对象方法名。getattr(self, name).
        """
        pass

    def __class_getitem__(self, *args, **kwargs):
        """
        //TODO 干什么用的？
         See PEP 585
        """
        pass

    def __reduce__(self, *args, **kwargs):
        """
        返回pickle的状态信息。
        """
        pass

    def __sizeof__(self):
        """
        返回对象在内存中的大小（以字节为单位）

        >>> {1}.__sizeof__()
        200
        >>> {1, 2, 3, 4, 5}.__sizeof__()
        456
        """
        pass

    __hash__ = None

    def difference(self, *args, **kwargs):
        """
        将两个或多个集合的差值作为新集合返回。
        (i.e.此集合中的所有元素，但不包括其他元素。)

        >>> {1, 2, 3, 4}.difference({1, 2, 5, 6})
        {3, 4}
        """
        pass

    def difference_update(self, *args, **kwargs):
        """
        从此集合中删除另一集合的所有元素。

        >>> a = {1, 2, 3, 4}
        >>> a.difference_update({1, 2, 5, 6})
        {3, 4}
        """
        pass

    def intersection(self, *args, **kwargs):
        """
        将两个集合的交集作为新集合返回。
        (i.e. 两个集合中的所有元素。)

        >>> {1, 2, 3, 4}.intersection({1, 2, 5, 6})
        {1, 2}
        """
        pass

    def intersection_update(self, *args, **kwargs):
        """
        使用集合自身和另一集合的交点更新集合。

        >>> a = {1, 2, 3, 4}
        >>> a.intersection_update({1, 2, 5, 6})
        {1, 2}
        """
        pass

    def symmetric_difference(self, *args, **kwargs):
        """
        将两个集合的对称差作为新集合返回。
        (i.e. 恰好位于其中一个集合中的所有元素。)

        >>> {1, 2, 3, 4}.symmetric_difference({1, 5, 6})
        {2, 3, 4, 5, 6}
        """
        pass

    def symmetric_difference_update(self, *args, **kwargs):
        """
        使用自身和另一个集合的对称差异更新集合。

        >>> a = {1, 2, 3, 4}
        >>> a.symmetric_difference_update({1, 5, 6})
        {2, 3, 4, 5, 6}
        """
        pass

    def union(self, *args, **kwargs):
        """
        将集合的并集作为新集合返回。
        (i.e. 任一集合中的所有元素。)

        >>> {1, 2, 3, 4}.union({5, 6})
        {1, 2, 3, 4, 5, 6}
        """
        pass

    def update(self, *args, **kwargs):
        """
        使用集合自身和其他集合的并集更新集合。

        >>> a = {1, 2, 3, 4}
        >>> a.update({5, 6})
        {1, 2, 3, 4, 5, 6}
        """
        pass

    def issubset(self, *args, **kwargs):
        """
        报告另一个集合是否包含此集合。

        >>> {1, 2, 3, 4}.issubset({1, 2, 3, 4, 5})
        True
        """
        pass

    def issuperset(self, *args, **kwargs):
        """
        报告此集合是否包含其他集合。

        >>> {1, 2, 3, 4}.issuperset({1, 2})
        True
        """
        pass

    def isdisjoint(self, *args, **kwargs):
        """
        如果两个集合有空交集，则返回True。

        >>> {1, 2, 3, 4}.isdisjoint({5, 6}
        True
        """
        pass

    def add(self, *args, **kwargs):
        """
        向集合中添加元素。
        如果元素已存在，则此操作无效。

        >>> a = set()
        >>> a.add(1)
        {1}
        """
        pass

    def clear(self, *args, **kwargs):
        """
        从该集中删除所有元素。

        >>> b = {1, 2, 3, 4}
        >>> b.clear()
        set()
        """
        pass

    def discard(self, *args, **kwargs):
        """
        如果元素是成员，则从集合中删除该元素。
        如果元素不是成员，则不执行任何操作。

        >>> a = {1, 2, 3, 4}
        >>> a.discard(1)
        {2, 3, 4}
        """
        pass

    def pop(self, *args, **kwargs):
        """
        删除并返回任意集合元素。
        如果集合为空，则引发KeyError。

        >>> {1, 2, 3, 4}.pop()
        1
        """
        pass

    def remove(self, *args, **kwargs):
        """
        从集合中删除一个元素；它必须是一个成员。
        如果元素不是成员，则引发KeyError。

        >>> {1, 2, 3, 4}.remove(1)
        {2, 3, 4}
        """
        pass

    def copy(self, *args, **kwargs):
        """
        返回集合的浅副本。

        >>> {1, 2, 3, 4}.copy()
        {1, 2, 3, 4}
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

    def __and__(self, *args, **kwargs):
        """
         与--交。self&value.

         >>> {1, 2, 4}.__and__({1, 2, 3})
         {1, 2}
        """
        pass

    def __iand__(self, *args, **kwargs):
        """
        与--交。self&=value.

        >>> {1, 2, 4}.__iand__({1, 2, 3})
        {1, 2}
        """
        pass

    def __rand__(self, *args, **kwargs):
        """
         与--交。value&self.

         >>> {1, 2, 4}.__rand__({1, 2, 3})
         {1, 2}
        """
        pass

    def __sub__(self, *args, **kwargs):
        """
        差。self-value.

        >>> {1, 2, 4}.__sub__({1, 2, 3})
        {4}
        """
        pass

    def __isub__(self, *args, **kwargs):
        """
        差。self-=value.

        >>> {1, 2, 4}.__isub__({1, 2, 3})
        {4}
        """
        pass

    def __rsub__(self, *args, **kwargs):
        """
         差。value-self.

         >>> {1, 2, 4}.__rsub__({1, 2, 3})
         {3}
        """
        pass

    def __or__(self, *args, **kwargs):
        """
        或--并。self|value.

        >>> {1, 2, 4}.__or__({1, 2, 3})
        {1, 2, 3, 4}
        """
        pass

    def __ior__(self, *args, **kwargs):
        """
        或--并。self|=value.

        >>> {1, 2, 4}.__ior__({1, 2, 3})
        {1, 2, 3, 4}
        """
        pass

    def __ror__(self, *args, **kwargs):
        """
        或--并。value|self.

        >>> {1, 2, 4}.__ror__({1, 2, 3})
        {1, 2, 3, 4}
        """
        pass

    def __ixor__(self, *args, **kwargs):
        """
        异或--对称差。self^=value.

        >>> {1, 2, 4}.__ixor__({1, 2, 3})
        {3, 4}
        """
        pass

    def __rxor__(self, *args, **kwargs):
        """
        异或--对称差。value^self.

        >>> {1, 2, 4}.__rxor__({1, 2, 3})
        {3, 4}
        """
        pass

    def __xor__(self, *args, **kwargs):
        """
        异或--对称差。self^value.

        >>> {1, 2, 4}.__xor__({1, 2, 3})
        {3, 4}
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        集合的长度。len(self).

        >>> {1, 2, 3, 4, 1}.__len__()
        4
        """
        pass

    def __contains__(self, y):
        """
        包含。y in x.

        >>> {1, 2, 3, 4}.__contains__(1)
        True
        """
        pass
