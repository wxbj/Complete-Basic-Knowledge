class str(object):

    def __init__(self, value='', encoding=None, errors='strict'):
        """
        str(object='') -> str
        str(bytes_or_buffer[, encoding[, errors]]) -> str

        从给定对象创建新字符串对象。
        如果指定了编码或错误级别，则对象必须暴露一个数据缓冲区,该缓冲区将使用给定的编码和错误处理程序进行解码。
        否则，返回object.__str__()(如果已定义)或repr(object)。
        编码默认为sys.getdefaultencoding()。
        错误默认为“strict”。

        >>> str('a')
        a
        """
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        """
        创建并返回实例化对象
        """
        pass

    def __str__(self, *args, **kwargs):
        """
        返回字符串。str(self)
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

    def __format__(self, *args, **kwargs):
        """
         返回字符串的格式化版本，如format_spec所述。
         由于format_spec内容较多,所以这里不展开。
        """
        pass

    def __getattribute__(self, *args, **kwargs):
        """
        获取对象方法名。getattr(self, name).
        """
        pass

    def __getnewargs__(self, *args, **kwargs):
        """
        序列化为元组
        """
        pass

    def __hash__(self, *args, **kwargs):
        """
         哈希值。hash(self)
        """
        pass

    def __sizeof__(self, *args, **kwargs):
        """
        返回对象在内存中的大小（以字节为单位）

        >>> 'a'.__sizeof__()
        50
        >>> 'hello'.__sizeof__()
        54
        """
        pass

    def isalnum(self, *args, **kwargs):
        """
        如果字符串是字母数字字符串，则返回True，否则返回False。
        如果字符串中的所有字符都是字母数字，且字符串中至少有一个字符，则该字符串为字母数字。

        >>> str.isalnum('hello')
        True
        >>> str.isalnum('12345')
        True
        >>> str.isalnum('hello12345')
        True
        """
        pass

    def isalpha(self, *args, **kwargs):
        """
        如果字符串是字母字符串,则返回True,否则返回False。
        如果字符串中的所有字符都是字母,且字符串中至少有一个字符,则该字符串为字母。

        >>> str.isalpha('hello')
        True
        >>> str.isalpha('hello12345')
        False
        """
        pass

    def isascii(self, *args, **kwargs):
        """
        如果字符串中的所有字符都是ASCII,则返回True,否则返回False。
        ASCII字符的代码点范围为U+0000-U+007F。
        空字符串也是ASCII码。

        >>> str.isascii('Hello')
        True
        >>> str.isascii('侯茜')
        False
        """
        pass

    def isdecimal(self, *args, **kwargs):
        """
        如果字符串是十进制字符串，则返回True，否则返回False。
        如果字符串中的所有字符都是十进制的，并且字符串中至少有一个字符，则该字符串为十进制字符串。

        >>> str.isdecimal('0123456789')
        True
        >>> str.isdecimal('Hello')
        False
        """
        pass

    def isdigit(self, *args, **kwargs):
        """
        如果字符串是数字字符串，则返回True，否则返回False。
        如果字符串中的所有字符都是数字，且字符串中至少有一个字符，则该字符串为数字字符串。

        >>> str.isdigit('Hello')
        False
        >>> str.isdigit('0123456789')
        True
        """
        pass

    def isidentifier(self, *args, **kwargs):
        """
        如果字符串是有效的Python标识符，则返回True，否则返回False。
        调用keyword.iskeyword(s)测试字符串s是否是保留标识符，例如“def”或“class”。

        >>> str.isidentifier('1Hello')
        False
        >>> str.isidentifier('Hello')
        True
        """
        pass

    def isnumeric(self, *args, **kwargs):
        """
        如果字符串是数字字符串，则返回True，否则返回False。
        如果字符串中的所有字符都是数字且字符串中至少有一个字符，则该字符串为数字字符串。

        >>> str.isnumeric('123')
        True
        >>> str.isnumeric('Hello')
        Flase
        """
        pass

    def isprintable(self, *args, **kwargs):
        """
        如果字符串可打印，则返回True，否则返回False。
        如果字符串的所有字符在repr()中都被认为是可打印的,或者字符串为空,则该字符串是可打印的。

        >>> str.isprintable('')
        True
        >>> str.isprintable(' ')
        True
        >>> str.isprintable('\t')
        False
        >>> str.isprintable('Hello')
        True
        """
        pass

    def isspace(self, *args, **kwargs):
        """
        如果字符串是空白字符串,则返回True,否则返回False。
        如果字符串中的所有字符都是空白，并且字符串中至少有一个字符，则该字符串为空白。

        >>> str.isspace('')
        False
        >>> str.isspace(' ')
        True
        """
        pass

    def upper(self, *args, **kwargs):
        """
        返回转换为大写的字符串的副本。

        >>> str.upper('hello')
        HELLO
        """
        pass

    def isupper(self, *args, **kwargs):
        """
        如果字符串为大写字符串，则返回True，否则返回False。
        如果字符串中的所有大小写字符均为大写,且字符串中至少有一个大小写字符,则该字符串为大写。

        >>> str.isupper('Hello')
        False
        >>> str.isupper('HELLO')
        True
        """
        pass

    def lower(self, *args, **kwargs):
        """
         返回转换为小写的字符串的副本。

         >>> str.lower('HELLO')
         hello
        """
        pass

    def islower(self, *args, **kwargs):
        """
        如果字符串是小写字符串，则返回True，否则返回False。
        如果字符串中的所有大小写字符都是小写，并且字符串中至少有一个大小写字符，则该字符串为小写。

        >>> str.islower('str')
        True
        >>> str.islower('Str')
        False
        >>> str.islower('')
        False
        >>> str.islower('123')
        False
        """
        pass

    def title(self, *args, **kwargs):
        """
        返回每个单词都有标题的字符串版本。
        更具体地说，单词以大写字母开头，所有剩余的大小写字符都以小写字母开头。

        >>> str.title('HELLO WORLD')
        Hello World
        """
        pass

    def istitle(self, *args, **kwargs):
        """
        如果字符串是以标题为大小写的字符串,则返回True,否则返回False。
        在按标题大小写的字符串中,大写和小写字符只能跟在未按大小写的字符后面,而小写字符只能跟在按大小写的字符后面。

        >>> str.istitle('hello world')
        False
        >>> str.istitle('Hello World')
        True
        """
        pass

    def capitalize(self, *args, **kwargs):
        """
        返回字符串的首字母大写版本。
        更具体地说,使第一个字符具有大写字母,其余字符具有小写字母。

        >>> str.capitalize("hello world")
        Hello world
        """
        pass

    def casefold(self, *args, **kwargs):
        """
        返回适合无大小写比较的字符串版本。

        >>> str.casefold("HELLO")
        hello
        >>> str.casefold("hello")
        hello
        """
        pass

    def swapcase(self, *args, **kwargs):
        """
         将大写字符转换为小写，将小写字符转换为大写。

        >>> str.swapcase('HELLO')
        hello
        >>> str.swapcase('hello')
        HELLO
        """
        pass

    def endswith(self, suffix, start=None, end=None):
        """
        S.endswith(suffix[, start[, end]]) -> bool

        如果S以指定的后缀结尾，则返回True，否则返回False。
        使用可选开始，测试从该位置开始。
        使用可选结束，停止在该位置比较S。
        后缀也可以是要尝试的字符串元组。

        >>> 'Hello'.endswith('lo')
        True
        >>> 'Hello'.endswith('lo', 3)
        True
        >>> 'Hello'.endswith('lo', 3, 5)
        True
        >>> 'Hello'.endswith(('l','o',), 3, 5)
        True
        """
        return False

    def startswith(self, prefix, start=None, end=None):
        """
        S.startswith(prefix[, start[, end]]) -> bool

        如果S以指定的前缀开头，则返回True，否则返回False。
        使用可选开始，测试从该位置开始。
        使用可选结束，停止在该位置比较S。
        前缀也可以是要尝试的字符串元组。

        >>> 'Hello'.endswith('lo')
        True
        >>> 'Hello'.endswith('lo', 3)
        True
        >>> 'Hello'.endswith('lo', 3, 5)
        True
        >>> 'Hello'.endswith(('l', 'o',), 3, 5)
        True
        """
        return False

    def ljust(self, *args, **kwargs):
        """
        返回长度和宽度为左对齐的字符串。
        填充使用指定的填充字符完成（默认为空格）。

        >>> str.ljust('hello', 20, '*')
        hello***************
        """
        pass

    def rjust(self, *args, **kwargs):
        """
        返回一个长度和宽度右对齐的字符串。
        填充使用指定的填充字符完成（默认为空格）。

        >>> str.rjust('hello', 20, '*')
        str.rjust('hello', 20, '*')
        >>> str.rjust('hello', 20)
                       hello
        """
        pass

    def zfill(self, *args, **kwargs):
        """
        在左边用零填充数字字符串,以填充给定宽度的字段。
        字符串永远不会被截断。

        >>> str.zfill('hello', 20)
        000000000000000hello
        """
        pass

    def center(self, *args, **kwargs):
        """
        返回一个长宽居中的字符串。
        填充使用指定的填充字符完成（默认为空格）。

        >>> str.center('Hello', 20)
               Hello
        >>> str.center('Hello', 20, '*')
        *******Hello********

        """
        pass

    def expandtabs(self, *args, **kwargs):
        """
        返回使用空格展开所有制表符的副本。
        如果未指定选项卡大小，则假定为8个字符。

        >>> 'Hel\tlo'.expandtabs(8)
        Hel     lo
        """
        pass

    def rsplit(self, *args, **kwargs):
        """
        使用sep作为分隔符字符串，返回字符串中的单词列表。

          sep
            用于拆分字符串的分隔符。
            None (默认值) 表示根据任何空格进行拆分,并从结果中丢弃空字符串。
          maxsplit
            要执行的最大拆分数。
            -1 (默认值) 意味着没有限制。

        拆分从字符串的末尾开始，一直到前面。

        >>> str.rsplit('hello world hello world')
        ['hello', 'world', 'hello', 'world']
        >>> str.rsplit('hello world hello world', ' ')
        ['hello', 'world', 'hello', 'world']
        >>> str.rsplit('hello world hello world', ' ', 2)
        ['hello world', 'hello', 'world']
        """
        pass

    def split(self, *args, **kwargs):
        """
        使用sep作为分隔符字符串，返回字符串中的单词列表。

          sep
            用于拆分字符串的分隔符。
            None (默认值) 表示根据任何空格进行拆分,并从结果中丢弃空字符串。
          maxsplit
            要执行的最大拆分数。
            -1 (默认值) 意味着没有限制。

        >>> str.split('hello world hello world')
        ['hello', 'world', 'hello', 'world']
        >>> str.split('hello world hello world', ' ')
        ['hello', 'world', 'hello', 'world']
        >>> str.split('hello world hello world', ' ', 2)
        ['hello', 'world', 'hello world']
        """
        pass

    def splitlines(self, *args, **kwargs):
        """
        返回字符串中的行列表，在行边界处断开。
        除非给定了keepends且为true，否则换行符不包括在结果列表中。

        >>> str.splitlines('hello world\\nhello world')
        ['hello', 'world', 'hello', 'world']
        >>> str.splitlines('hello world\\nhello world',keepends=True)
        ['hello world\n', 'hello world']
        """
        pass

    def rpartition(self, *args, **kwargs):
        """
        使用给定的分隔符将字符串分成三部分。
        这将在字符串中搜索分隔符，从末尾开始。
        如果找到分隔符，则返回一个3元组，其中包含分隔符前的部分、分隔符本身以及分隔符后的部分。
        如果未找到分隔符，则返回包含两个空字符串和原始字符串的3元组。

        >>> str.rpartition('hello world', ' ')
        ('hello', ' ', 'world')
        >>> str.rpartition('hello world', '*')
        ('', '', 'hello world')
        """
        pass

    def partition(self, *args, **kwargs):
        """
        使用给定的分隔符将字符串分成三部分。
        这将在字符串中搜索分隔符。
        如果找到分隔符，则返回一个3元组，其中包含分隔符前的部分、分隔符本身以及分隔符后的部分。
        如果未找到分隔符，则返回一个包含原始字符串和两个空字符串的3元组。

        >>> str.partition('hello world', ' ')
        ('hello', ' ', 'world')
        >>> str.partition('hello world', '*')
        ('hello world', '', '')
        """
        pass

    def maketrans(self, *args, **kwargs):
        """
        返回可用于str.translate（）的转换表。

        如果只有一个参数,则必须是将Unicode序号（整数）或字符,映射到Unicode序号、字符串或无的字典。
        然后，字符键将转换为序数。
        如果有两个参数,它们必须是长度相等的字符串,并且在生成的字典中,x中的每个字符都将映射到y中相同位置的字符。
        如果有第三个参数,则必须是字符串,其字符将在结果中映射为“无”。

        >>> str.maketrans({1: 2})
        {1: 2}
        >>> str.maketrans('1', '2')
        {49: 50}
        >>> str.maketrans('1', '2', '3')
        {49: 50, 51: None}
        """
        pass

    def translate(self, *args, **kwargs):
        """
        使用给定的翻译表替换字符串中的每个字符。

          table
            转换表，它必须是Unicode序数到Unicode序数、字符串或无的映射。

        该表必须通过_getitem __实现查找/索引，例如字典或列表。
        如果此操作引发LookupError，则该字符保持不变。
        将删除映射到“无”的字符。

        >>> str.translate('hello', str.maketrans({'h': 'hq'}))
        hqello
        """
        pass

    def removeprefix(self, *args, **kwargs):
        """
        返回一个删除了给定前缀字符串（如果存在）的str。
        如果字符串以前缀字符串开头，则返回字符串[len（前缀）：]。
        否则，返回原始字符串的副本。

        >>> str.removeprefix('hello world', 'ld')
        hello world
        >>> str.removeprefix('hello world', 'he')
        llo world
        """
        pass

    def removesuffix(self, *args, **kwargs):
        """
        返回一个删除了给定后缀字符串（如果存在）的str。
        如果字符串以后缀字符串结尾且该后缀不是空的，则返回字符串[：-len（后缀）]。
        否则，返回原始字符串的副本。

        >>> str.removesuffix('hello world', 'ld')
        hello wor
        >>> str.removesuffix('hello world', 'he')
        hello world
        """
        pass

    def replace(self, *args, **kwargs):
        """
        传入三个参数,返回一个其中所有出现的子字符串old均替换为new的副本。
        传入四个参数,返回一个替换指定次数的子串的副本。-1 (默认值) 表示替换所有。

        >>> str.replace('hello hello hello', 'll', 'jj')
        hejjo hejjo hejjo
        >>> str.replace('hello hello hello', 'll', 'jj', 2)
        hejjo hejjo hello
        """
        pass

    def format(self, *args, **kwargs):
        """
        S.format(*args, **kwargs) -> str

        使用args和kwargs中的替换返回S的格式化版本。
        替换由大括号（“{”和“}”）标识。

        >>> 'H{}e{}llo'.format('hq', 'zy')
        Hhqezyllo
        """
        pass

    def format_map(self, mapping):
        """
        S.format_map(mapping) -> str

        使用映射(mapping)中的代换(substitutions)返回S的格式化版本。
        代换substitutions)由大括号（“{”和“}”）标识。

        >>> '{H}ello'.format_map({'H': 'hq'})
        hqello
        """
        return ""

    def lstrip(self, *args, **kwargs):
        """
        返回删除前导空格的字符串副本
        如果给定了字符而不是无，则删除字符中的字符。

        >>> str.lstrip('      HELLO')
        HELLO
        """
        pass

    def rstrip(self, *args, **kwargs):
        """
        返回已删除尾随空格的字符串副本。
        如果给定了字符而不是无,则删除字符中的字符。

        >>> str.rstrip('hello ')
        hello
        """
        pass

    def strip(self, *args, **kwargs):
        """
        返回删除前导和尾随空格的字符串副本。
        如果给定了字符而不是无，则删除字符中的字符。

        >>> str.strip('  hello  ')
        hello
        """
        pass

    def find(self, sub, start=None, end=None):
        """
        S.find(sub[, start[, end]]) -> int

        返回在S中找到子字符串sub的最低索引,以便sub包含在S[start:end]中。
        失败时返回-1。

        >>> 'Hello'.find('ll')
        2
        >>> 'Hello'.find('ll', 1)
        2
        >>> 'Hello'.find('ll', 1, 5)
        2
        """
        return 0

    def rfind(self, sub, start=None, end=None):
        """
        S.rfind(sub[, start[, end]]) -> int

        返回在S中找到子字符串sub的最高索引，以便sub包含在S[start:end]中。
        可选参数start和end解释为切片表示法。
        失败时返回-1。

        >>> str.rfind('hello hello hello', 'll')
        14
        >>> str.rfind('hello hello hello', 'll', 2)
        14
        >>>str.rfind('hello hello hello', 'll', 2, 8)
        2
        """
        return 0

    def index(self, sub, start=None, end=None):
        """
        S.index(sub[, start[, end]]) -> int

        返回在S中找到子字符串sub的最低索引，以便sub包含在S[start:end]中。
        可选参数start和end解释为切片表示法。
        未找到子字符串时引发ValueError。

        >>> 'HelloHello'.index('el')
        1
        >>> 'HelloHello'.index('el', 3)
        6
        >>> 'HelloHello'.index('el', 5, 9)
        6
        """
        return 0

    def rindex(self, sub, start=None, end=None):
        """
        S.rindex(sub[, start[, end]]) -> int

        返回在S中找到子字符串sub的最高索引，以便sub包含在S[start:end]中。
        可选参数start和end解释为切片表示法。
        未找到子字符串时引发ValueError。
        >>> str.rindex('hello hello hello', 'll')
        14
        >>> str.rindex('hello hello hello', 'll', 2)
        14
        str.rindex('hello hello hello', 'll', 2, 8)
        2
        """
        return 0

    def count(self, sub, start=None, end=None):
        """
        S.count(sub[, start[, end]]) -> int

        返回子字符串sub在字符串S[start:end]中不重叠的出现次数。
        可选参数start和end解释为切片表示法。

        >>> 'HelloHelloHelloHelloHello'.count('Hello')
        5
        >>> 'HelloHelloHelloHelloHello'.count('Hello', 10)
        3
        >>> 'HelloHelloHelloHelloHello'.count('Hello', 10, 15)
        1
        """
        return 0

    def encode(self, *args, **kwargs):
        """
        使用注册用于编码的编解码器对字符串进行编码。

          encoding
            用于对字符串进行编码的编码。
          errors
            用于编码错误的错误处理方案。
            默认值为“strict”，这意味着编码错误会引发UnicodeEncodeError。
            其他可能的值包括“ignore”、“replace”和“xmlcharrefreplace”,
            以及在编解码器中注册的任何其他名称。
            可处理UnicodeErrors的寄存器错误。

        >>> 'Hello'.encode(encoding='utf-8', errors='strict')
        b'Hello'
        """
        pass

    def join(self, ab=None, pq=None, rs=None):
        """
        连接任意数量的字符串。
        调用其方法的字符串将插入到每个给定字符串之间。
        结果将作为新字符串返回。

        >>> str.join('-', ['hello', 'world'])
        hello-world
        """
        pass

    def __add__(self, *args, **kwargs):
        """
        加法。self+value.

        >>> 'hello '.__add__('world')
        hello world
        """
        pass

    def __mod__(self, *args, **kwargs):
        """
        //TODO 目前不知道怎么用
        除法。self%value.
        """
        pass

    def __rmod__(self, *args, **kwargs):
        """
        //TODO 目前不知道怎么用
         除法。value%self.
        """
        pass

    def __mul__(self, *args, **kwargs):
        """
        重复。self*value.

        >>> 'hello'.__mul__(2)
        hellohello
        """
        pass

    def __rmul__(self, *args, **kwargs):
        """
        重复。value*self.

        >>> str.__rmul__('hello', 2)
        hellohello
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

    def __contains__(self, *args, **kwargs):
        """
         包含

        >>> 'hello '.__contains__('ll')
        True
        """
        pass

    def __getitem__(self, *args, **kwargs):
        """
        根据位序获取值。self[key].

        >>> 'hello'.__getitem__(2)
        l
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        字符串长度。len(self)

        >>> 'hello'.__len__()
        5
        """
        pass
