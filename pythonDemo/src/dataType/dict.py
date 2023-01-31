class dict(object):
    def __init__(self, seq=None, **kwargs):
        """
        dict() -> 新空字典
        dict(mapping) -> 从映射对象的(key, value)初始化新字典
        dict(iterable) -> 新字典初始化为 via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> 使用关键字参数列表中的name=value初始化新字典。
                          For example:  dict(one=1, two=2)

        >>> dict()
        {}
        >>> dict({'a': 1, 'b': 2})
        {'a': 1, 'b': 2}
        >>> dict(a=1, b=2)
        {'a': 1, 'b': 2}
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

    def __repr__(self, *args, **kwargs):
        """
        返回字符串。repr(self)
        """
        pass

    def __class_getitem__(self, *args, **kwargs):
        """
        //TODO 干什么用的？
         See PEP 585
        """
        pass

    def __getattribute__(self, *args, **kwargs):
        """
        获取对象方法名。getattr(self, name).
        """
        pass

    def __sizeof__(self):
        """
        返回对象在内存中的大小（以字节为单位）

        >>> {}.__sizeof__()
        48
        >>> {'a': 1}.__sizeof__()
        216
        >>> {'a': 1, 'b': 2}.__sizeof__()
        216
        """
        pass

    def __reversed__(self, *args, **kwargs):
        """
         返回dict键上的反向迭代器。
        """
        pass

    __hash__ = None

    @staticmethod
    def fromkeys(*args, **kwargs):
        """
        使用iterable中的键和设置为value的值创建一个新字典。

        >>> dict.fromkeys([1, 2, 3], 'a')
        {1: 'a', 2: 'a', 3: 'a'}
        """
        pass

    def items(self):
        """
        D.items() -> 提供D项视图的集合状对象

        >>> {'a': 1, 'b': 2}.items()
        dict_items([('a', 1), ('b', 2)])
        """
        pass

    def keys(self):
        """
         D.keys() -> 在D键上提供视图的类似集合的对象

         >>> {'a': 1, 'b': 2}.keys()
         dict_keys(['a', 'b'])
        """
        pass

    def values(self):
        """
         D.values() -> 提供D值视图的对象

         >>> {'a': 1, 'b': 2}.values()
         dict_values([1, 2])
        """
        pass

    def clear(self):
        """
        清空

        >>> d = {'a': 1, 'b': 2}
        >>> d.clear()
        {}
        """
        pass

    def copy(self):
        """
        浅复制

        >>> {'a': 1, 'b': 2}.copy()
        {'a': 1, 'b': 2}
        """
        pass

    def get(self, *args, **kwargs):
        """
        如果键在字典中，则返回键的值，否则为默认值。

        >>> {'a': 1, 'b': 2}.get('a')
        1
        """
        pass

    def pop(self, k, d=None):
        """
        D.pop(k[,d]) -> v,删除指定的键并返回相应的值。
        若找不到键，则返回默认值（若给定），否则将引发KeyError

        >>> {'a': 1, 'b': 2}.pop('a')
        1
        >>> {'a': 1, 'b': 2}.pop('c', 3)
        3
        """
        pass

    def popitem(self, *args, **kwargs):
        """
        移除(key, value)对并将其作为2元组返回。
        按后进先出的顺序返回。
        如果dict为空，则引发KeyError。

        >>> {'a': 1, 'b': 2}.popitem()
        ('b', 2)
        """
        pass

    def setdefault(self, *args, **kwargs):
        """
        如果关键字不在字典中，则插入默认值为的关键字。
        如果键在字典中，则返回键的值，否则为默认值。

        >>> {'a': 1, 'b': 2}.setdefault('a', 3)
        1
        >>> {'a': 1, 'b': 2}.setdefault('c', 3)
        {'a': 1, 'b': 2, 'c': 3}
        """
        pass

    def update(self, E=None, **F):
        """
        D.update([E, ]**F) -> None.  从dict/iterable E和F更新D。
        如果E存在并且有一个.keys（）方法，则对E中的k执行：D[k]=E[k]
        如果E存在并且缺少.keys（）方法，则会：对于k，E中的v:D[k]=v
        在这两种情况下，后面都是：对于F中的k:D[k]=F[k]

        >>> d = {'a': 1, 'b': 2}
        >>> d.update({'a': 3, 'b': 4})
        {'a': 3, 'b': 4}
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

    def __ror__(self, *args, **kwargs):
        """
        或运算。value|self.
        要将键提取出来进行运算

        >>> {'a': 1, 'b': 2}.keys().__ror__(set('ac'))
        {'a', 'b', 'c'}
        """
        pass

    def __or__(self, *args, **kwargs):
        """
        或运算。value|self.
        要将键提取出来进行运算

        >>> {'a': 1, 'b': 2}.keys().__or__(set('ac'))
        {'a', 'b', 'c'}
        """
        pass

    def __ior__(self, *args, **kwargs):
        """
        //TODO 目前不知道怎么用
        或运算。value|self.
        """
        pass

    def __setitem__(self, *args, **kwargs):
        """
        通过建设定值

        >>> d = {'a': 1, 'b': 2}
        >>> d.__setitem__('a', 2)
        {'a': 2, 'b': 2}
        >>> d = {'a': 1, 'b': 2}
        >>> d.__setitem__('c', 2)
        {'a': 1, 'b': 2, 'c': 2}
        """
        pass

    def __delitem__(self, *args, **kwargs):
        """
        通过键删除

        >>> d = {'a': 1, 'b': 2}
        >>> d.__delitem__('a')
        {'b': 2}
        """
        pass

    def __getitem__(self, y):
        """
        通过键获取值

        >>> {'a': 1, 'b': 2}.__getitem__('a')
        1
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        字典长度。len(self).

        >>> {'a': 1, 'b': 2}.__len__()
        2
        """
        pass

    def __contains__(self, *args, **kwargs):
        """
        如果字典具有指定的键，则为True，否则为False。

        >>> {'a': 1, 'b': 2}.__contains__('a')
        True
        """
        pass
