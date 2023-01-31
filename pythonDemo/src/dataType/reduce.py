def reduce(function, sequence, initial='_initial_missing'):
    """
    reduce(function, sequence[, initial]) -> value

    将两个参数的函数从左到右累加地应用于序列项,以便将序列减少为单个值。
    例如,reduce（lambda x,y:x+y,[1,2,3,4,5]）计算（（（1+2）+3）+4）+5）。
    如果存在initial,则在计算中将其放置在序列项之前,并在序列为空时用作默认值。

    >>> reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    15
    >>> reduce(lambda x, y: x + y, (1, 2, 3, 4, 5), 10)
    25
    """

    it = iter(sequence)

    if initial is '_initial_missing':
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value") from None
    else:
        value = initial

    for element in it:
        value = function(value, element)

    return value
