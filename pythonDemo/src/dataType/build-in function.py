def delattr(x, y):
    """
    从给定对象中删除命名属性。
    delattr(x,'y')等同于"del x.y"
    """
    pass


def setattr(x, y, v):
    """
    将给定对象上的命名属性设置为指定值。
    setattr(x,'y',v)等同于"x.y=v"
    """
    pass


def getattr(object, name, default=None):
    """
    getattr(object, name[, default]) -> value
    getattr(x,'y')等同于x.y。
    从对象中获取命名属性;
    给定默认参数时:当属性不存在时返回该参数;
    没有给定默认参数时:当属性不存在时引发异常;
    """
    pass


def hasattr(*args, **kwargs):
    """
    返回对象是否具有具有给定名称的属性。
    通过调用getattr(obj, name)并捕获AttributeError完成。
    """
    pass


def isinstance(x, A_tuple):
    """
    返回对象是类的实例还是其子类的实例。

    元组,如"isinstance(x, (A, B, ...))"中的元组,可以作为对照。
    这相当于"isinstance(x, A)或isinstance(x, B)或者..." 等等。
    """
    pass


def issubclass(x, A_tuple):
    """
    返回"cls"是从另一个类派生的还是同一个类。

    元组,如"issubclass(x, (A, B, ...))",可以作为检查的目标。
    这相当于"issubclass(x, A)或issubclass(x, B)或..."等。
    """
    pass


def callable(i_e_, some_kind_of_function):
    """
    返回对象是否可调用(i.e.,某种函数)。
    注意:类是可调用的,带有__call__()方法的类的实例也是可调用的。
    """
    pass


def hash(*args, **kwargs):
    """
    返回给定对象的哈希值。
    相等的两个对象具有相同的哈希值,反过来不一定对。

    >>> hash(1)
    1
    >>> hash(1.1)
    230584300921369601
    >>> hash('1')
    4193414619064226038
    """
    pass


def exit(*args, **kwargs):
    """
    退出程序
    """
    pass


def quit(*args, **kwargs):
    """
    退出程序
    """
    pass


def help():
    """
    定义内置的"help"。
        这是一个围绕pydoc.help的包装器,当在Python交互提示符下键入"help"时,它会提供一条有用的消息。
        在Python提示符处调用help()将启动交互式帮助会话。
        调用help(thing)打印python对象"thing"的帮助。
    """
    pass


def compile(*args, **kwargs):
    """
    将源代码编译成可由exec()或eval()执行的代码对象。

    源代码可以是Python模块、语句或表达式。
    文件名将用于运行时错误消息。
    mode参数必须为'exec'才能编译模块,为'single'才能编译单个(交互式)语句,为'eval'才能编译表达式。
    flags参数(如果存在)控制将来哪些语句会影响代码的编译。
    dont_inherit参数(如果为true)将停止编译,该编译将继承调用compile的代码中任何未来有效语句的效
    果;如果不存在或错误,除了明确指定的任何特性外,这些语句也会影响编译。
    """
    pass


def eval(*args, **kwargs):
    """
    在全局和局部上下文中评估给定源。

    源可以是表示Python表达式的字符串,也可以是compile()返回的代码对象。
    全局变量必须是字典,局部变量可以是任何映射,默认为当前全局变量和局部变量。
    如果只提供全局变量,则局部变量默认为全局变量。
    """
    pass


def exec(*args, **kwargs):
    """
    在全局和局部上下文中执行给定的源。

    源可以是表示一个或多个Python语句的字符串,也可以是compile()返回的代码对象。
    全局变量必须是字典,局部变量可以是任何映射,默认为当前全局变量和局部变量。
    如果只提供全局变量,则局部变量默认为全局变量。
    """
    pass


def all(*args, **kwargs):
    """
    如果bool(x)对于iterable中的所有值x都为真,则返回真。
    如果iterable为空,则返回True。

    >>> all([0, 1])
    False
    >>> all([1, 2])
    True
    """
    pass


def any(*args, **kwargs):
    """
    如果bool(x)对于iterable中的x,存在为真,则返回真。
    如果iterable为空,则返回False。

    >>> any([0, 1])
    True
    >>> any([0])
    False
    """
    pass


def copyright(*args, **kwargs):
    """
    用于打印许可证文本、贡献者列表和版权声明的交互式提示对象。
    """
    pass


def credits(*args, **kwargs):
    """
    用于打印许可证文本、贡献者列表和版权声明的交互式提示对象。
    """
    pass


def license(*args, **kwargs):
    """
    用于打印许可证文本、贡献者列表和版权声明的交互式提示对象。
    """
    pass


def bin(*args, **kwargs):
    """
    返回整数的二进制表示形式。

    >>> bin(10)
    0b1010
    """
    pass


def oct(*args, **kwargs):
    """
    返回整数的八进制表示形式。

       >>> oct(123)
       0o173
    """
    pass


def hex(*args, **kwargs):
    """
    返回整数的十六进制表示形式。

       >>> hex(123)
       0x7b
    """
    pass


def abs(*args, **kwargs):
    """
    返回参数的绝对值。
    """
    pass


def divmod(x, y):
    """
    返回元组(x//y,x%y)。
    不变量:div*y+mod==x。
    (商,余数)

    >>> divmod(5.1, 1.2)
    (4.0, 0.2999999999999998)
    >>> divmod(5, 2)
    (2, 1)
    """
    return (0, 0)


def max(*args, key=None):
    """
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value

    使用单个iterable参数,返回其最大项。
    如果提供的iterable为空,则默认的keyword-only参数指定要返回的对象。
    对于两个或多个参数,返回最大的参数。

    >>> max(list(), default=1)
    1
    """
    pass


def min(*args, key=None):
    """
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    使用单个iterable参数,返回其最小项。
    如果提供的iterable为空,则默认的keyword-only参数指定要返回的对象。
    对于两个或多个参数,返回最小的参数。

    >>> min(list(), default=1)
    1
    """
    pass


def sum(*args, **kwargs):
    """
    返回一个"start"值(默认值:0)加上一组数字的总和
    当iterable为空时,返回"start"值。
    此函数专门用于数值,可能会拒绝非数值类型。

    >>> sum([])
    0
    """
    pass


def round(*args, **kwargs):
    """
    将数字四舍五入到小数位数的给定精度。
    传入一个参数时,默认向整数转换
    传入两个参数时,第二个参数为保留的小数位数
    ndigits 参数可以是负数,此时,该运算会作用在十位、百位、千位等上面
    当一个值刚好在两个边界的中间的时候,返回离它最近的偶数

    >>> round(222, -1)
    220
    >>> round(2.333, 1)
    2.3
    >>> round(2.5)
    2
    >>> round(3.5)
    4
    """
    pass


def pow(*args, **kwargs):
    """
    等效于带2个参数的base**exp或带3个参数的base**exp%mod
    某些类型(如int)在使用三参数形式调用时能够使用更高效的算法。

    >>> pow(2, 3)
    8
    >>> pow(2, 3, 7)
    1
    >>> pow(2.1, 3.1)
    9.97423999265871
    """
    pass


def sorted(*args, **kwargs):
    """
    按升序返回一个包含iterable中所有项的新列表。
    可以提供自定义键函数来自定义排序顺序,并且可以设置反向标志以按降序请求结果。

    >>> sorted([5, 2, 6, 4], reverse=True)
    [2, 4, 5, 6]
    """
    pass


def len(*args, **kwargs):
    """
     返回容器中的项目数。

     >>> len([5, 2, 6, 4])
     4
    """
    pass


def chr(*args, **kwargs):
    """
    返回序数i的,一个字符的Unicode字符串;0 <= i <= 0x10ffff.

    >>> chr(123)
    {
    >>> chr(321)
    Ł
    """
    pass


def ord(*args, **kwargs):
    """
    返回单字符字符串,的Unicode代码点。

    >>> ord('a')
    97
    """
    pass


def locals(*args, **kwargs):
    """
    返回包含当前作用域的局部变量的字典。
    注意:此词典的更新是否会影响本地范围内的名称查找,取决于*implementation
    dependent*并且不受任何向后兼容性保证的影响,反之亦然。
    """
    pass


def globals(*args, **kwargs):
    """
    返回包含当前作用域全局变量的字典。
    注意:此词典的更新将影响当前全局范围内的名称查找,反之亦然。
    """
    pass


def vars(p_object=None):
    """
    vars([object]) -> dictionary

    不带参数,相当于locals()。
    带有一个参数,相当于object.__dict__.
    """
    return {}


def dir(p_object=None):
    """
    dir([object]) -> 字符串列表

    如果在没有参数的情况下调用,则返回当前作用域中的名称。
    否则,返回一个按字母顺序排列的名称列表,其中包含给定对象的(部分)属性以及可从该对象访问的属性。
    如果对象提供了一个名为_dir__的方法,则将使用该方法;
    否则,将使用默认的dir()逻辑并返回:
      对于模块对象:模块的属性。
      对于类对象:它的属性,并递归地返回其基类的属性。
      对于任何其他对象:它的属性、它的类的属性,以及它的类的基类的递归属性。

    """
    return []


def iter(source, sentinel=None):
    """
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    从对象获取迭代器。
    在第一种形式中,参数必须提供自己的迭代器,或者是一个序列。
    在第二种形式中,调用callable直到它返回sentinel。

    >>> iter(list([1, 2, 3]))
    <list_iterator object at 0x000001EB12368460>
    """
    pass


def next(iterator, default=None):
    """
    next(iterator[, default])

    从迭代器返回下一项。
    如果给定了默认值并且迭代器已用尽,则返回该迭代器,而不是引发StopIteration。

    >>> next(iter(list([1, 2, 3])))
    1
    """
    pass


def repr(obj):
    """
    返回对象的规范字符串表示形式。
    对于许多对象类型,包括大多数内置对象,eval(repr(obj)) == obj。

    >>> repr(list([1, 2, 3]))
    [1, 2, 3]
    """
    pass


def ascii(*args, **kwargs):
    """
    返回对象的ASCII-only表示形式。

    作为repr(),返回包含对象的可打印表示形式的字符串,但使用\\x,
    \\u或\\U转义来转义repr()返回的字符串中的非ASCII字符。这将
    生成一个类似于Python 2中repr()返回的字符串。

    >>> ascii('好')
    '\u597d'
    """
    pass


def breakpoint(*args, **kws):
    """
    调用sys.breakpointhook(*args, **kws)。
    sys.breakpointhook()必须接受传递的任何参数。
    默认情况下,将您放入调用站点的调试器中
    """
    pass


def format(*args, **kwargs):
    """
    返回value.__format__(format_spec)

    format_spec默认为空字符串。
    有关详细信息,可参阅help('FORMATTING')的格式规范迷你语言部分。
    由于内容较多,这里就不展开了
    """
    pass


def id(*args, **kwargs):
    """
    返回对象的标识。
    这保证同时存在的对象,是唯一的。
    (CPython使用对象的内存地址。)

    >>> id(float)
    140725487146448
    """
    pass


def input(*args, **kwargs):
    """
    从标准输入读取字符串。后面的换行符被剥离。
    提示字符串(如果给定)将在读取输入之前打印到标准输出,不带尾随换行符。
    如果用户点击EOF(*nix: Ctrl-D, Windows: Ctrl-Z+Return),则提高EOF。
    在*nix系统上,如果可用,则使用readline。
    """
    pass


def __build_class__(func, name, *args, **kwargs):
    """
    创建类
    __build_class__(func, name, /, *bases, [metaclass], **kwds) -> class
    类语句使用的内部帮助函数。
    """
    pass


def __import__(name, globals=None, locals=None, fromlist=(), level=0):
    """
    __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module

    导入模块。由于此函数是供Python解释器使用的,而不是一般用途,因此
    最好使用importlib.import_module()以编程方式导入模块。

    globals参数仅用于确定上下文;
    它们没有被修改。locals参数未使用。
    fromlist应该是要模拟"from name import ..."的名称列表,或者
    是要模拟"import name"的空列表。
    从包中导入模块时,注意:当fromlist为空时,__import__('A.B', ...)
    返回包a,但当fromlist不为空时返回其子模块B。
    level参数用于确定是执行绝对导入还是相对导入:0是绝对导入,而正数是
    相对于当前模块要搜索的父目录数。
    """
    pass


def print(self, *args, sep=' ', end='\n', file=None):
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    默认情况下,将值输出到流或sys.stdout。
    可选关键字参数:
    file:  类似于文件,object (stream);默认为当前sys.stdout。
    sep:   在值之间插入字符串,默认为空格。
    end:   附加在最后一个值之后的字符串,默认为换行符。
    flush: 是否强制刷新流。

    >>> print(1, 2, 3, sep='*', end='')
    1*2*3
    """
    pass


def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
    """
    打开文件并返回一个流。失败时引发操作错误。

    file是一个文本或字节字符串,提供要打开的文件的名称(如果文件不在当前工作目
    录中,则提供路径),或者是要包装的文件的整数文件描述符。(如果给定了文件描
    述符,则在关闭返回的I/O对象时关闭该描述符,除非closefd设置为False。)

    mode是一个可选字符串,用于指定打开文件的模式。它默认为"r",表示以文本模式打开
    阅读。其他常用值包括"w"用于写入(如果文件已经存在,则截断该文件),"x"用于创建
    和写入新文件,以及"a"用于追加(在某些Unix系统上,这意味着所有写入操作都追加到
    文件的末尾,而不管当前查找位置如何)。在文本模式下,如果未指定编码,则使用的
    编码依赖于平台:locale.getpreferredencoding(False)将被调用以获取当前的
    locale编码。(对于读取和写入原始字节,请使用二进制模式,不指定编码。)
    可用模式有:

    ========= ===============================================================
    字符      含义
    --------- ---------------------------------------------------------------
    'r'       只读(默认)
    'w'       写,首先清空文件
    'x'       创建,写文件
    'a'       写,如果文件存在,则追加到文件末尾
    'b'       二进制模式
    't'       文本模式(默认)
    '+'       更新(读写)
    'U'       通用换行符模式(已弃用)
    ========= ===============================================================

    默认模式为"rt"(打开以读取文本)。对于二进制随机访问,模式"w+b"打开并将文件截
    断为0字节,而"r+b"打开文件时不截断。"x"模式表示"w",如果文件已经存在,则会引
    发"FileExistError"。

    Python区分以二进制和文本模式打开的文件,即使底层操作系统不这样做。以二进制模
    式打开的文件(在模式参数后添加"b")将内容作为字节对象返回,而不进行任何解码。
    在文本模式下(默认情况下,或在模式参数后附加"t"时),文件内容以字符串形式返回,
    字节首先使用平台相关编码或指定编码(如果给定)进行解码。

    "U"模式已被弃用,并将在Python的未来版本中引发异常。它在Python3中没有效果。
    使用换行符控制通用换行符模式。

    buffering是用于设置缓冲策略的可选整数。传递0可关闭缓冲(仅在二进制模式下允许),传递1可
    选择行缓冲(仅在文本模式下可用),传递大于1的整数可指示固定大小区块缓冲区的大小。
    当未给出缓冲参数时,默认缓冲策略的工作方式如下:

      *二进制文件缓冲在固定大小的块中;缓冲区的大小是通过尝试确定底层设备的"块大小"
      并返回'io.DEFAULT_BUFFER_SIZE'来选择的。在许多系统上,缓冲区的长度通常
      为4096或8192字节。

      *"交互式"文本文件(isatty()返回True的文件)使用行缓冲。其他文本文件对二
      进制文件使用上述策略。

    encoding是用于解码或编码文件的编码的名称。这只能在文本模式下使用。默认编
    码依赖于平台,但是可以传递Python支持的任何编码。有关支持的编码列表,请参
    见编解码器模块。

    errors是一个可选字符串,指定如何处理编码错误——此参数不应在二进制模式下使用。如
    果存在编码错误,则传递"strict"以引发ValueError异常(默认值None具有相同的效果),
    或者传递"ignore"以忽略错误。(请注意,忽略编码错误可能会导致数据丢失。)有关允许
    的编码错误字符串的列表,请参阅codecs.register文档或运行"help(codecs.Codec)"。

    newline控制通用换行符的工作方式(它仅适用于文本模式)。它可以是None、''、'\n'、
    '\r'和'\r\n'。其工作原理如下:

      *输入时,如果换行符为"None",则启用通用换行符模式。输入中的行可以以'\n'、'\r'
      或'\r\n'结尾,这些行在返回给调用方之前会被转换为'\n'。如果为'',则启用通用换行
      符模式,但行尾将返回给调用方,而不进行翻译。如果它具有任何其他合法值,则输入行仅
      由给定的字符串终止,并且行尾无需翻译就可返回给调用方。

      *在输出时,如果换行符为None,则写入的任何'\n'字符都将转换为系统默认的行分隔符,
      os.linesep。如果换行符为''或'\n',则不会进行转换。如果换行符是任何其他合法值,
      则写入的任何'\n'字符都将转换为给定字符串。

    如果closefd为False,则在关闭文件时,基础文件描述符将保持打开状态。当给定文件名时,
    此选项不起作用,在这种情况下必须为True。

    通过将可调用函数传递为*opener*,可以使用自定义的opener。然后通过使用(*file*,
    *flags*)调用*opener*获得文件对象的底层文件描述符。*opener*必须返回一个打开
    的文件描述符(将os.open作为*opener*传递会产生与不传递类似的功能)。

    open()返回一个file对象,该对象的类型取决于模式,并通过该对象执行标准文件操作,
    如读取和写入。当open()用于以文本模式('w','r', 'wt', 'rt',等)打开文件时,它
    将返回TextIOWrapper。当用于在二进制模式下打开文件时,返回的类会有所不同:在
    读取二进制模式下,它返回一个BufferedReader;在写二进制和附加二进制模式下,它
    返回一个BufferedWriter,在读/写模式下,它返回一个BufferedRandom。

    也可以使用字符串或bytearray作为文件进行读写。对于字符串,StringIO可以像在文
    本模式下打开的文件一样使用,对于字节,BytesIO可以像在二进制模式下打开的文件一
    样使用。
    """
    pass
