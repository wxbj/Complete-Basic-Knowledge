"""
and,or,not,BOOLEAN(布尔值),SHIFTING(移位),BINARY(二进制),BITWISE(按位)
class,CLASSES(类),def,TYPES(类型),MODULES(模块)
FUNCTIONS(方法),lambda(匿名函数),SEQUENCEMETHODS(测序方法),ATTRIBUTEMETHODS(属性方法)
MAPPINGMETHODS(映射方法)
BASICMETHODS(基本方法),CALLS(调用),COMPARISON(比较)
codecs.Codec(编解码器),UNICODE
FORMATTING(格式化),SPECIALMETHODS(特殊方法)
if,while,for,break,continue,import
COMPLEX(复数),FLOAT(浮点值),NUMBERS(数字),LITERALS(字面常量),LISTLITERALS(列表字面常量)
INTEGER(整数),DICTIONARYLITERALS(字典字面常量),TUPLELITERALS(元组字面常量)
LISTS(列表),STRINGS(字符串),DICTIONARIES(字典),MAPPINGS(映射)
OPERATORS(操作符),EXPRESSIONS(表达式),UNARY(一元),NUMBERMETHODS(数字方法),STRINGMETHODS(字符串方法)
POWER(乘方),in,is,SLICINGS(切片),SUBSCRIPTS(订阅),SEQUENCES(序列),TUPLES(元组)
PRIVATENAMES(私有名称),ATTRIBUTES(属性),CALLABLEMETHODS(可调用方法)
TRUTHVALUE(真实值),AUGMENTEDASSIGNMENT(增广赋值)
"""
"""
# help()
如果这是您第一次使用Python,那么您一定要在以下位置查看Internet上的教程:
https://docs.python.org/zh-cn/3/tutorial/index.html

输入任何module、keyword或topic,以获取有关编写Python程序和使用Python模
块的帮助.要退出此帮助实用程序并返回解释器,只需键入“quit”.

要获取可用modules、keywords、symbols、topics的列表,请键入"modules"、
"keywords"、"symbols"、"topics".每个模块还附带一行内容摘要;要列出其名
称或摘要所包含的给定字符串(如"spam")的模块,请键入"modules spam".
# -----------------------------modules---------------------------------#
IPython             bisect              mmap                subprocess
__future__          bleach              mmapfile            sunau
_abc                builtins            mmsystem            symbol
_aix_support        bz2                 modulefinder        sympyprinting
_ast                cProfile            msilib              symtable
_asyncio            calendar            msvcrt              sys
_bisect             certifi             multiprocessing     sysconfig
_blake2             cffi                nbclient            tabnanny
_bootlocale         cgi                 nbconvert           tarfile
_bootsubprocess     cgitb               nbformat            telnetlib
_bz2                charset_normalizer  nest_asyncio        tempfile
_cffi_backend       chunk               netbios             terminado
_codecs             cmath               netrc               test
_codecs_cn          cmd                 nntplib             testpath
_codecs_hk          code                notebook            tests
_codecs_iso2022     codecs              nt                  textwrap
_codecs_jp          codeop              ntpath              this
_codecs_kr          collections         ntsecuritycon       threading
_codecs_tw          colorama            nturl2path          time
_collections        colorsys            numbers             timeit
_collections_abc    commctrl            numpy               timer
_compat_pickle      compileall          odbc                tkinter
_compression        concurrent          opcode              token
_contextvars        configparser        operator            tokenize
_csv                contextlib          optparse            tornado
_ctypes             contextvars         os                  trace
_ctypes_test        copy                packaging           traceback
_datetime           copyreg             pandas              tracemalloc
_decimal            crypt               pandocfilters       traitlets
_distutils_hack     csv                 parser              tty
_elementtree        ctypes              parso               turtle
_functools          curses              pathlib             turtledemo
_hashlib            cythonmagic         pdb                 types
_heapq              dataclasses         perfmon             typing
_imp                datalore            pickle              unicodedata
_io                 datetime            pickleshare         unittest
_json               dateutil            pickletools         urllib
_locale             dbi                 pip                 urllib3
_lsprof             dbm                 pipes               uu
_lzma               dde                 pkg_resources       uuid
_markupbase         debugpy             pkgutil             venv
_md5                decimal             platform            warnings
_msi                decorator           plistlib            wave
_multibytecodec     defusedxml          poplib              wcwidth
_multiprocessing    difflib             posixpath           weakref
_opcode             dis                 pprint              webbrowser
_operator           distutils           profile             webencodings
_osx_support        doctest             prometheus_client   widgetsnbextension
_overlapped         email               prompt_toolkit      win2kras
_peg_parser         encodings           pstats              win32api
_pickle             ensurepip           pty                 win32clipboard
_py_abc             entrypoints         pvectorc            win32com
_pydecimal          enum                py_compile          win32con
_pyio               errno               pyclbr              win32console
_pyrsistent_version faulthandler        pycparser           win32cred
_queue              filecmp             pydoc               win32crypt
_random             fileinput           pydoc_data          win32cryptcon
_sha1               fnmatch             pyexpat             win32event
_sha256             formatter           pygments            win32evtlog
_sha3               fractions           pyparsing           win32evtlogutil
_sha512             ftplib              pyrsistent          win32file
_signal             functools           pythoncom           win32gui
_sitebuiltins       gc                  pytz                win32gui_struct
_socket             genericpath         pywin               win32help
_sqlite3            getopt              pywin32_bootstrap   win32inet
_sre                getpass             pywin32_testutil    win32inetcon
_ssl                gettext             pywintypes          win32job
_stat               glob                qtconsole           win32lz
_statistics         graphlib            qtpy                win32net
_string             gzip                queue               win32netcon
_strptime           hashlib             quopri              win32pdh
_struct             heapq               random              win32pdhquery
_symtable           hmac                rasutil             win32pdhutil
_testbuffer         html                re                  win32pipe
_testcapi           http                regcheck            win32print
_testconsole        idlelib             regutil             win32process
_testimportmultiple idna                reprlib             win32profile
_testinternalcapi   imaplib             requests            win32ras
_testmultiphase     imghdr              rlcompleter         win32rcparser
_thread             imp                 rmagic              win32security
_threading_local    importlib           runpy               win32service
_tkinter            inspect             sched               win32serviceutil
_tracemalloc        io                  secrets             win32timezone
_uuid               ipaddress           select              win32trace
_warnings           ipykernel           selectors           win32traceutil
_weakref            ipykernel_launcher  send2trash          win32transaction
_weakrefset         ipython_genutils    servicemanager      win32ts
_win32sysloader     ipywidgets          setuptools          win32ui
_winapi             isapi               shelve              win32uiole
_winxptheme         itertools           shlex               win32verstamp
_xxsubinterpreters  jedi                shutil              win32wnet
_zoneinfo           jinja2              signal              winerror
abc                 json                site                winioctlcon
adodbapi            jsonschema          sitecustomize       winnt
afxres              jupyter             six                 winperf
aifc                jupyter_client      smtpd               winpty
antigravity         jupyter_console     smtplib             winreg
argon2              jupyter_core        sndhdr              winsound
argparse            jupyterlab_pygments socket              winxpgui
array               jupyterlab_widgets  socketserver        winxptheme
ast                 keyword             sqlite3             wsgiref
asynchat            lib2to3             src                 xdrlib
asyncio             linecache           sre_compile         xml
asyncore            locale              sre_constants       xmlrpc
atexit              logging             sre_parse           xxsubtype
attr                lzma                ssl                 zipapp
audioop             mailbox             sspi                zipfile
autoreload          mailcap             sspicon             zipimport
backcall            markupsafe          stat                zlib
backend_interagg    marshal             statistics          zmq
base64              math                storemagic          zoneinfo
bdb                 matplotlib_inline   string              ~ip
binascii            mimetypes           stringprep          
binhex              mistune             struct              
# -----------------------------keywords---------------------------------#
False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
# -----------------------------symbols---------------------------------#
!=                  +                   <=                  __

"                   +=                  <>                  `

\"""                ,                   ==                  b"

%                   -                   >                   b'

%=                  -=                  >=                  f"

&                   .                   >>                  f'

&=                  ...                 >>=                 j

'                   /                   @                   r"

'''                 //                  J                   r'

(                   //=                 [                   u"

)                   /=                  \                   u'

*                   :                   ]                   |

**                  <                   ^                   |=

**=                 <<                  ^=                  ~

*=                  <<=                 _                   
# -----------------------------topics---------------------------------#
ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES       
"""
"""
# and,or,not,BOOLEAN

布尔运算

   or_test  ::= and_test | or_test "or" and_test
   and_test ::= not_test | and_test "and" not_test
   not_test ::= comparison | "not" not_test

在布尔运算的上下文中,以及当控制流语句使用表达式时,以下值被解释为false:"false"、"None"、
所有类型的数字零以及空字符串和容器(包括字符串、元组、列表、字典、集合和冻结集).所有其他值
都被解释为true.用户定义的对象可以通过提供一个"__bool__()"方法自定义其真值.

如果其参数为false,则运算符"not"将生成"True",否则将生成"False".

表达式"x and y"首先计算*x*;如果*x*为false,则返回其值;否则,将计算*y*,并返回结果值.

表达式"x or y"首先计算*x*;如果*x*为真,则返回其值;否则,将计算*y*,并返回结果值.

请注意,"and"和"or"都不限制于它们返回给"False" 和 "True"的值和类型,而是返回最后计算的参
数.这有时很有用,例如,s是一个字符串,如果该字符串为空,则应将其替换为默认值,则表达式
"s or 'foo'"将生成所需的值.因为"not"必须创建一个新值,所以无论其参数的类型如何,它都会返
回一个布尔值(例如,not 'foo'产生"False"而不是'')
"""
"""
# SHIFTING

移位运算

移位运算的优先级低于算术运算：

   shift_expr ::= a_expr | shift_expr ("<<" | ">>") a_expr

这些运算符接受整数作为参数.它们将第一个参数向左或向右移动第二个参数给定的位数.

按*n*位的右移位被定义为按"pow(2,n)"的整除.
*n*位的左移位被定义为与"pow(2,n)"相乘.
"""
"""
# BINARY

二进制算术运算

二进制算术运算具有传统的优先级.请注意,其中一些操作也适用于某些非数字类型.除幂运算符外,只
有两个级别,一个用于乘法运算符,一个用于加法运算符:

   m_expr ::= u_expr | m_expr "*" u_expr | m_expr "@" m_expr |
              m_expr "//" u_expr | m_expr "/" u_expr |
              m_expr "%" u_expr
   a_expr ::= m_expr | a_expr "+" m_expr | a_expr "-" m_expr

"*"(multiplication(乘法))运算符产生其参数的乘积.参数必须都是数字,或者一个参数必须是整
数,另一个参数必须是序列.在前一种情况下,这些数字被转换为一种通用类型,然后相乘在一起.在后
一种情况下,执行序列重复;负重复因子产生空序列.

"@"(at)运算符用于矩阵乘法.没有内置Python类型实现此运算符.
3.5版中的新特性.

"/"(除法)和"//"(整除)运算符产生其参数的商.数值参数首先转换为通用类型.整数的除法产生浮点,
而整数的整除产生整数;结果是应用"floor"函数对结果进行数学除法.被零除会引发
"ZeroDivisionError"异常.

"%"(modulo(模))运算符从第一个参数除以第二个参数得到余数.数值参数首先转换为通用类型.零对
参数引发"ZeroDivisionError"异常.参数可以是浮点数,例如,"3.14%0.7"等于"0.34"(因为"3.14
"等于"4*0.7 + 0.34".)模运算符总是产生与第二个操作数具有相同符号的结果(或零);结果的绝对
值严格小于第二个操作数的绝对值.

整除运算符和模运算符通过以下标识连接:"x == (x//y)*y + (x%y)".整除和模还与内置函数
"divmod()":"divmod(x, y) == (x//y, x%y)"连接.

除了对数字执行模运算外,"%"运算符还被字符串对象重载,以执行旧式字符串格式
(也称为interpolation(插值)).

没有为复数定义整除运算符、模运算符和"divmod()"函数.如果合适,可以使用"abs()"函数将其转换
为浮点数.

"+"(addition(加法))运算符产生其参数之和.参数必须都是数字或都是相同类型的序列.在前一种情
况下,这些数字被转换成一种通用类型,然后加在一起.在后一种情况下,序列是串联的.

"-"(subtraction(减法))运算符产生其参数的差.数值参数首先转换为通用类型.
"""
"""
# BITWISE

二进制位运算

三个按位操作中的每一个都具有不同的优先级：

   and_expr ::= shift_expr | and_expr "&" shift_expr
   xor_expr ::= and_expr | xor_expr "^" and_expr
   or_expr  ::= xor_expr | or_expr "|" xor_expr

"&"运算符生成其参数的按位AND,该参数必须是整数.

"^"运算符生成其参数的按位异或(exclusive OR(异或)),该参数必须是整数.

"|"运算符产生按位或其参数,该参数必须是整数.
"""
"""
# class

类:定义类对象

   classdef    ::= [decorators] "class" classname [inheritance] ":" suite
   inheritance ::= "(" [argument_list] ")"
   classname   ::= identifier

    注释:
        decorators:装饰器
        inheritance:继承
        identifier:标识符

类定义是一个可执行语句.继承列表通常给出一个基类列表,列表中的每个项都应该为允许子
类化的类对象.默认情况下,没有继承列表的类从基类"object"继承;
例如:

   class Foo:
       pass

相当于

   class Foo(object):
       pass

然后,使用新创建的本地名称空间和原始全局名称空间,在新的执行框架中执行该类的套件.(通常,套件
主要包含函数定义.)当类的套件完成执行时,其执行框架将被丢弃,但其本地命名空间将被保存.然后使
用基类的继承列表和属性字典保存的本地名称空间创建类对象.类名绑定到原始本地命名空间中的该类
对象.

在类主体中定义属性的顺序保留在新类的"__dict__"中.请注意,这仅在创建类之后才可靠,并且仅适
用于使用定义语法定义的类.

可以使用元类大量定制类创建.


类也可以被修饰:就像修饰函数一样,

   @f1(arg)
   @f2
   class Foo: pass

大致相当于

   class Foo: pass
   Foo = f1(arg)(f2(Foo))

装饰器表达式的求值规则与函数装饰器的求值规则相同.然后将结果绑定到类名.

在版本3.9中更改:类可以用任何有效的"assignment_expression(赋值表达式)"修饰.以前,语法的
限制性要大得多;

**Programmer’s note:**类定义中定义的变量是类属性;它们由实例共享.实例属性可以在
"self.name = value"的方法中设置.类和实例属性都可以通过符号"self.name"来访问,并且实例
属性在以这种方式访问时隐藏具有相同名称的类属性.类属性可以用作实例属性的默认值,但在其中使用
可变值可能会导致意外结果.描述符可用于创建具有不同实现细节的实例变量.
"""
"""
# FUNCTIONS

函数

函数对象由函数定义创建.对函数对象的唯一操作是调用它:"func(argument-list)".

函数对象实际上有两种风格:内置函数和用户定义函数.两者都支持相同的操作(调用函数),但实现不同
,因此对象类型不同.
"""
"""
# lambda

匿名函数

   lambda_expr ::= "lambda" [parameter_list] ":" expression

Lambda表达式(有时称为Lambda表单)用于创建匿名函数.表达式
"lambda parameters: expression"生成一个函数对象.未命名对象的行为类似于使用以下项定义
的函数对象:

   def <lambda>(parameters):
       return expression

请注意,使用lambda表达式创建的函数不能包含语句或注释.
"""
"""
# CLASSES,TYPES

标准类型层次结构

下面是Python中内置的类型列表.扩展模块(使用C、Java或其他语言编写,具体取决于实现)可以定义
其他类型.Python的未来版本可能会将类型添加到类型层次结构中(例如,有理数、高效存储的整数数组
等),尽管这样的添加通常会通过标准库提供.

下面的一些类型描述包含一个列出"special attributes(特殊属性)"的段落.这些属性提供了对实现
(implementation)的访问,不适用于一般用途.他们的定义将来可能会改变.

None
    此类型只有一个值.只有一个对象具有此值.通过内置名称"None"访问此对象.它用于表示在许多
    情况下没有值,例如,它是从没有显式返回任何内容的函数返回的.它的真值是假.

NotImplemented(未实现)
    此类型只有一个值.只有一个对象具有此值.通过内置名称"NotImplemented"访问此对象. 如果
    数值方法和富比较方法未对提供的操作数执行操作,则它们应返回此值.(解释器随后将尝试反射操
    作,或其他一些回退,具体取决于运算符)不应在布尔上下文中对其求值.

   在版本3.9中更改:不推荐在布尔上下文中计算"NotImplemented".虽然它当前的计算结果为true
   ,但它将发出"DeprecationWarning(弃用警告)".它将在Python的未来版本中引发一个
   "TypeError(类型错误)".

Ellipsis(省略)
    此类型只有一个值.只有一个对象具有此值.通过文本"..."或内置名称"Ellipsis"访问此对象.
    它的真值是真.

"numbers.Number"
    它们由数字文本创建,并由算术运算符和算术内置函数作为结果返回.数字对象是不可变的;一经创
    建,它们的值就永远不会改变.Python数字当然与数学数字密切相关,但受计算机中数字表示的限
    制.

   由"__repr__()"和"__str__()"计算的数值类的字符串表示具有以下属性：

       *它们是有效的数值文本,当传递给类构造函数时,会生成一个具有原始数值的对象.
       *如果可能,表示形式以10为基数.
       *不显示前导零,小数点前的单个零可能除外.
       *不显示尾随零,小数点后的单个零可能除外.
       *只有当数字为负数时才会显示符号.

   Python区分整数、浮点数和复数：

        "numbers.Integral"
            这表示数学集合中的整数(正整数和负整数)元素.

            有两种类型的整数:

                Integers ("int")
                     这表示无限范围内的数字,仅受可用(虚拟)内存的限制.为了移位和掩码操作
                     的目的,假设采用二进制表示,负数表示为2的补码的变体,这使人产生无限符
                     号位向左延伸的错觉.

                Booleans ("bool")
                     这代表了真值False和True.表示值"False"和"True"的两个对象是唯一的
                     布尔对象.布尔类型是整数类型的子类型,在几乎所有上下文中,布尔值的行
                     为分别类似于值0和1,但当转换为字符串时,将分别返回字符串"False"或
                     "True".

            整数表示规则旨在对涉及负整数的移位和掩码操作给出最有意义的解释.

        "numbers.Real" ("float")
            它们表示机器级别的双精度浮点数.对于溢出的可接受范围和处理,您将受制于底层机器
            体系结构(以及C或Java实现).Python不支持单精度浮点数;处理器和内存使用方面的
            节省(通常是使用它们的原因)与在Python中使用对象的开销相比相形见绌,因此没有理
            由使用两种浮点数使语言复杂化.

        "numbers.Complex" ("complex")
            它们将复数表示为一对机器级双精度浮点数.同样的注意事项也适用于浮点数.复数"z"
            的实部和虚部可以通过只读属性"z.real"和"z.imag"检索.

Sequences(序列)
   这表示由非负数索引的有限有序集.内置函数"len()"返回序列的项数.当序列的长度为*n*时,索引
   集包含数字0,1,…,*n*-1.序列*a*的项目*i*由"a[i]"选择.

   序列还支持切片:"a[i:j]"选择索引为*k*的所有项目,以便*i* "<=" *k* "<" *j*.当用作表达
   式时,切片是相同类型的序列.这意味着索引集将重新编号,以便从0开始.

   一些序列还支持带有第三个"step(步长)"参数的"extended slicing(扩展切片)":"a[i:j:k]"
   选择索引为*x*的*a*的所有项目,其中"x = i + n*k"、*n* ">=" "0"和*i* "<=" *x* "<"
   *j*.

   序列根据其可变性进行区分:

       Immutable sequences(不变序列)
          不可变序列类型的对象在创建后不能更改.(如果对象包含对其他对象的引用,则这些其他
          对象可能是可变的,并且可以更改;但是,不可变对象直接引用的对象集合不能更改.)

          以下类型是不可变序列:

              Strings(字符串)
                 字符串是表示Unicode代码点的值序列."U+0000 - U+10FFFF"范围内的所有代
                 码点都可以用字符串表示.Python没有*char*类型;相反,字符串中的每个代码点
                 都表示为长度为"1"的字符串对象.内置函数"ord()"将代码点从字符串形式转换
                 为"0-10FFFF"范围内的整数;"chr()"将范围为"0-10FFFF"的整数转换为相应
                 长度的"1"字符串对象."str.encode()"可用于使用给定的文本编码将"str"转
                 换为"bytes",而"bytes.decode()"可用于实现相反的目的.

              Tuples(元组)
                 元组的项是任意Python对象.两个或多个项的元组由逗号分隔的表达式列表组成.
                 一个项的元组("单元组")可以通过在表达式上附加逗号形成(表达式本身不会创
                 建元组,因为括号必须可用于表达式分组).空元组可以由一对空括号组成.

              Bytes(字节)
                 字节对象是一个不可变数组.这些项是8位字节,由0 <= x < 256范围内的整数
                 表示.字节文本(如"b'abc")和内置的"bytes()"构造函数可用于创建bytes对
                 象.此外,字节对象可以通过"decode()"方法解码为字符串.

       Mutable sequences(可变序列)
          可变序列可以在创建后更改.订阅和切片符号可以用作赋值和"del"(delete)语句的目标.

          目前有两种内在可变序列类型:

              Lists(列表)
                 列表中的项目是任意Python对象.列表是通过将逗号分隔的表达式列表放在方括
                 号中形成的.(请注意,形成长度为0或1的列表不需要特殊需求.)

              Byte Arrays(字节数组)
                 bytearray对象是可变数组.它们由内置的"bytearray()"构造函数创建.字节
                 数组除了是可变的(因此是不可破坏的),还提供与不可变的"bytes"对象相同的
                 接口和功能.

Set types(设置类型)
   这表示无序的、有限的、唯一的、不可变的对象集.因此,它们不能被任何下标索引.但是,它们可以
   被迭代,内置函数"len()"返回集合中的项数.集合的常见用途是快速成员资格测试、从序列中删除
   重复项以及计算数学运算,如交集、并集、差分和对称差分.

   对于集合元素,适用与字典键相同的不变性规则.请注意,数字类型遵循数字比较的常规规则:如果两
   个数字比较相等(例如,"1"和"1.0"),则一个集合中只能包含其中一个数字.

   目前有两种内在集合类型:

       Sets(集合)
          这些表示一个可变集.它们是由内置的"set()"构造函数创建的,之后可以通过多种方法进
          行修改,例如"add()".

       Frozen sets(冻结集)
          它们代表一个不变的集合.它们由内置的"frozenset()"构造函数创建.由于冻结集是不可
          变的且*hashable(可散列)*,因此它可以再次用作另一个集合的元素,或者用作字典键.

Mappings(映射)
   这表示由任意索引集索引的有限对象集.下标符号"a[k]"从映射"a"中选择由"k"索引的项;这可以
   在表达式中使用,也可以作为赋值或"del"语句的目标.内置函数"len()"返回映射中的项数.

   当前只有一种内部映射类型:

   Dictionaries(字典)
      这表示由几乎任意值索引的有限对象集.唯一不能接受作为键的值类型是包含列表或字典的值,
      或者其他可变类型,这些值是按值而不是按对象标识进行比较的,原因是字典的有效实现要求键
      的哈希值保持不变.用于键的数字类型遵循数字比较的正常规则:如果两个数字比较相等(例如,
      "1"和"1.0"),则可以互换使用它们来索引相同的字典条目.

      字典保留插入顺序,这意味着键将按照它们在字典上顺序添加的相同顺序生成.替换现有密钥不
      会改变顺序,但是移除密钥并重新插入它会将其添加到末尾,而不是保留其原来的位置.

      字典是可变的;它们可以通过"{...}"符号创建.

      在版本3.7中更改:在3.6之前的Python版本中,字典没有保留插入顺序.在CPython 3.6中,插
      入顺序被保留,但在当时它被认为是一个实现细节,而不是语言保证.

Callable types(可调用类型)
   以下是可以应用函数调用操作的类型:

       User-defined functions(用户定义函数)
          用户定义的函数对象由函数定义创建.应该使用参数列表调用它,该参数列表包含与函数的
          形式参数列表相同数量的项.

          Special attributes(特殊属性):

               Attribute(属性)         Meaning(含义)
               ----------------------------------------------------------------
               "__doc__"            函数的文档字符串,如果不可用,则        Writable
                                    为"None";不是由子类继承的.
               ----------------------------------------------------------------
              "__name__"            函数的名称.                         Writable
               ----------------------------------------------------------------
               "__qualname__"       函数的*qualified name(限定名)*      Writable
                                    .3.3版中的新属性.
               ----------------------------------------------------------------
               "__module__"         在其中定义函数的模块的名称,如果        Writable
                                    不可用,则为"None".
               ----------------------------------------------------------------
               "__defaults__"       包含具有默认值的参数的默认参数值       Writable
                                    的元组,如果没有参数具有默认值,则
                                    为"None".
               ----------------------------------------------------------------
               "__code__"           表示已编译函数体的代码对象.           Writable
               ----------------------------------------------------------------
               "__globals__"        对保存函数全局变量的字典的引用—       Read-only
                                    定义函数的模块的全局命名空间.
               ----------------------------------------------------------------
               "__dict__"           支持任意函数属性的命名空间.           Writable
               ----------------------------------------------------------------
               "__closure__"        "None"或包含函数自由变量绑定的单     Read-only
                                    元格元组.
               ----------------------------------------------------------------
               "__annotations__"    包含参数注释的记录.dict的键是参数     Writable
                                    名,如果提供,返回注释的键是'return'.
               ----------------------------------------------------------------
               "__kwdefaults__"     包含仅关键字参数的默认值的dict.       Writable

          大多数标记为"Writable"的属性都会检查赋值的类型.

          函数对象还支持获取和设置任意属性,例如,可以使用这些属性将元数据附加到函数.常规
          属性点表示法用于获取和设置此类属性.*请注意,当前实现仅支持用户定义函数上的函数
          属性.将来可能支持内置函数上的函数属性*

          单元对象具有"cell_contents(单元内容)"属性.这可用于获取单元格的值,以及设置值.

          关于函数定义的附加信息可以从其代码对象中检索;可以在"types"模块中访问"cell"类
          型.

       Instance methods(实例方法)
          实例方法对象组合了类、类实例和任何可调用对象(通常是用户定义的函数).

          特殊只读属性:"__self__"是类实例对象,"__func__是函数对象";"__doc__"是该方法
          的文档(与"__func__.__doc__"相同);"_name__"是方法名称(与"_func__._name__"
          相同);"_module__"是在其中定义方法的模块的名称,如果不可用,则为"None".

          方法还支持访问(但不设置)基础函数对象上的任意函数属性.

          如果某个类的属性是用户定义的函数对象或类方法对象,则在获取该类的属性时(可能通过
          该类的实例),可以创建用户定义的方法对象.

          当通过一个实例从类中检索用户定义的函数对象来创建实例方法对象时,其"__self__"属
          性就是实例,方法对象被称为绑定.新方法的"__func__"属性是原始函数对象.

          当通过从类或实例检索类方法对象来创建实例方法对象时,其"__self__"属性是类本身,
          其"__func__"属性是类方法的函数对象.

          当调用实例方法对象时,将调用基础函数("__func__"),并在参数列表前面插入类实例(
          "__self__").例如,当"C"是包含函数"f()"定义的类,"x"是"C"的实例时,调用"x.f(1)
          "相当于调用"C.f(x,1)".

          当实例方法对象是从类方法对象派生的时,存储在"__self__"中的"类实例"实际上就是类
          本身,因此调用"x.f(1)"或"C.f(1)"相当于调用"f(C,1)",其中"f"是底层函数.

          请注意,每次从实例检索属性时,都会发生从函数对象到实例方法对象的转换.在某些情况
          下,有效的优化是将属性分配给局部变量并调用该局部变量.还请注意,这种转换只发生在
          用户定义的函数中;其他可调用对象(以及所有不可调用对象)在不进行转换的情况下被检
          索.还需要注意的是,作为类实例属性的用户定义函数不会转换为绑定方法;只有当函数是
          类的属性时,才会发生这种情况.

       Generator functions(生成函数)
          使用"yield"语句的函数或方法称为*generator function(生成器函数)*.这样的函数
          在被调用时总是返回一个迭代器对象,该对象可用于执行函数体:调用迭代器的
          "iterator.__next__()"方法将导致函数执行,直到它使用"yield"语句提供值为止.当
          函数执行"return"语句或结束时,将引发"StopIteration"异常,迭代器将到达要返回的
          值集的末尾.

       Coroutine functions(协程函数)
          使用"async def"定义的函数或方法称为*coroutine function(协程函数)*.这样的函
          数在调用时返回一个*coroutine(协同程序)*对象.它可能包含"await"表达式,以及"
          async with"和"async for"语句.

       Asynchronous generator functions(异步生成函数)
          使用"async def"定义并使用"yield"语句的函数或方法称为*asynchronous
          generator functions(异步生成函数)*.调用此函数时,将返回一个异步迭代器对象,
          该对象可在"async for"语句中用于执行函数体.

          调用异步迭代器的"aiterator.__anext__()"方法将返回一个*awaitable*,等待时将
          执行该*awaitable*,直到它使用"yield"表达式提供一个值为止.当函数执行空的
          "return"语句或结束时,将引发"StopAsyncIteration(停止异步迭代)"异常,异步迭代
          器将到达要生成的值集的末尾.

       Built-in functions(内置函数)
          内置函数对象是C函数的包装器.内置函数的示例有"len()"和"math.sin()"("math"是
          标准内置模块).参数的数量和类型由C函数决定.特殊只读属性:"__doc__"是函数的文档
          字符串,如果不可用,则为"None";"__name__"是函数的名称;"__self__"设置为"None"
          ;"__module__"是定义函数的模块的名称,如果不可用,则为"None".

       Built-in methods(内置方法)
          这实际上是对内置函数的另一种伪装,这次包含一个作为隐式额外参数传递给C函数的对象.
          内置方法的一个示例是"alist.append()",假设*alist(属性表)*是一个列表对象.在这
          种情况下,特殊的只读属性"__self__"被设置为由*alist*表示的对象.

       Classes(类)
          类是可调用的.这些对象通常充当其自身新实例的工厂,但重写"__new__()"的类类型可能
          会有变化.调用的参数传递给"__new__()",在典型情况下,传递给"__init__()"以初始
          化新实例.

       Class Instances(类实例)
          任意类的实例可以通过在其类中定义"__call__()"方法来调用.

Modules(模块)
   模块是Python代码的基本组织单元,由导入系统创建,可以通过"import"语句调用,也可以通过调
   用诸如"importlib.import_module()"和内置"__import__()"之类的函数来调用.模块对象有
   一个由字典对象实现的名称空间(这是由模块中定义的函数的"__globals__"属性引用的字典).属
   性引用被转换为在字典中的查找,例如,"m.x"相当于"m.__dict__["x"]".模块对象不包含用于初
   始化模块的代码对象(因为初始化完成后不需要它).

   属性赋值更新模块的名称空间字典,例如,"m.x = 1"等同于"m.__dict__["x"] = 1".

   预定义(可写)属性:"__name__"是模块的名称;"__doc__"是模块的文档字符串,如果不可用,则为
   "None";"__annotations__"(可选)是一个包含在模块体执行期间收集的*variable
   annotations(变量注释)*的字典;"__file__"是加载模块的文件的路径名,如果模块是从文件加
   载的.对于某些类型的模块,例如静态链接到解释器中的C模块,可能缺少"__file__"属性;对于从共
   享库动态加载的扩展模块,它是共享库文件的路径名.

   特殊的只读属性:"__dict__"是作为字典对象的模块名称空间.

   **CPython implementation detail(实现细节):**由于CPython清除模块字典的方式,当模块
   超出范围时,即使字典仍有活动引用,模块字典也将被清除.要避免这种情况,请复制字典或在直接使
   用其字典时保留模块.

Custom classes(自定义类)
   自定义类类型通常由类定义创建.类具有由字典对象实现的命名空间.类属性引用被转换为本字典中
   的查找,例如,"C.x"被转换为"C.__dict__["x"]"(尽管有许多hook允许使用其他方法定位属性).
   如果在那里找不到属性名称,则在基类中继续进行属性搜索.基类的搜索使用C3方法解析顺序,即使
   在存在"菱形"继承结构的情况下,如果有多个继承路径指向一个共同的祖先,该顺序也能正确运行.
   有关Python使用的C3 MRO的更多详细信息,请参见2.3版本附带的文档,网址为
   https://www.python.org/download/releases/2.3/mro/.

   当一个类属性引用(比如类"C")将产生一个类方法对象时,它将被转换成一个实例方法对象,其
   "__self__"属性为"C".当产生一个静态方法对象时,它将被转换为由静态方法对象包装的对象.

   类属性赋值更新类的字典,而不是基类的字典.

   可以调用类对象以生成类实例.

   特殊属性:"__name__"为类名;"__module__"是定义类的模块名称;"__dict__"是包含类名称空
   间的字典;"__bases__"是包含基类的元组,按它们在基类列表中的出现顺序排列;"__doc__"是类
   的文档字符串,如果未定义,则为"None";"__annotations__"(可选)是包含在类主体执行期间收
   集的*variable annotations(变量注释)*的字典.

Class instances(类实例)
   类实例是通过调用类对象创建的.类实例有一个实现为字典的命名空间,字典是搜索属性引用的第一
   个位置.如果在那里找不到属性,并且实例的类具有该名称的属性,则搜索将继续使用类属性.如果发
   现一个类属性是用户定义的函数对象,它将被转换为一个实例方法对象,其"__self__"属性就是实
   例.静态方法和类方法对象也被转换;

   属性赋值和删除更新实例的字典,而不是类的字典.如果类具有"__setattr__()"或
   "__delattr__()"方法,则会调用该方法,而不是直接更新实例字典.

   类实例可以假装是数字、序列或映射.

   特殊属性:"__dict__"是属性字典;"__class__"是实例的类.

I/O objects (也称为文件对象)
   *file object(文件对象)*表示打开的文件.可以使用各种快捷方式创建文件对象:"open()"内置
   函数,以及套接字对象的"os.popen()"、"os.fdopen()"和"makefile()"方法(可能还可以通过
   扩展模块提供的其他函数或方法).

   对象"sys.stdin"、"sys.stdout"和"sys.stderr"被初始化为对应于解释器标准输入、输出和
   错误流的文件对象;它们都以文本模式打开,因此遵循"io.TextIOBase"抽象类定义的接口.

Internal types(内部类型)
   解释器内部使用的一些类型向用户公开.它们的定义可能会随着解释器的未来版本而改变,但为了完
   整性,这里提到它们.

   Code objects(代码对象)
      代码对象表示*byte-compiled(字节编译)*可执行Python代码,或*bytecode(字节码)*.代
      码对象和函数对象之间的区别在于,函数对象包含对函数全局变量(定义它的模块)的显式引用,
      而代码对象不包含上下文;默认参数值也存储在函数对象中,而不是代码对象中(因为它们表示在
      运行时计算的值).与函数对象不同,代码对象是不可变的,不包含对可变对象的引用(直接或间接
      ).

      特殊只读属性:"co_name"给出函数名;"co_argcount"是位置参数的总数(包括仅位置参数和
      具有默认值的参数);"co_posonlyargcount"是仅位置参数的数量(包括具有默认值的参数);"
      co_kwonlyargcount"是仅关键字参数的数量(包括具有默认值的参数);"co_nlocals"是函数
      使用的局部变量数(包括参数);"co_varnames"是一个元组,包含局部变量的名称(从参数名称
      开始);"co_cellvars"是一个元组,包含嵌套函数引用的局部变量的名称;"co_freevars"是
      一个包含自由变量名称的元组;"co_代码"是表示字节码指令序列的字符串;"co_consts"是一
      个元组,包含字节码使用的文本;"co_names"是一个元组,包含字节码使用的名称;
      "co_filename"是编译代码的文件名;"co_firstlineno"是函数的第一行号;"co_lnotab"
      是一个字符串,用于编码从字节码偏移量到行号的映射;"co_stacksize"是所需的堆栈大小;
      "co_flags"是一个整数,为解释器编码多个标志.

      为"co_flags"定义了以下标志位:如果函数使用"*arguments(参数)"语法接受任意数量的位
      置参数,则设置位"0x04";如果函数使用"**keywords"语法接受任意关键字参数,则设置位
      "0x08";如果函数为生成器,则设置位"0x20".

      未来功能声明("from __future__ import division(启用未来分区)")也使用"co_flags"
      中的位来指示代码对象是否在启用特定功能的情况下编译:如果函数在启用未来分区的情况下编
      译,则设置位"0x2000";位"0x10"和"0x1000"在早期版本的Python中使用.

      "co_flags"中的其他位保留供内部使用.

      如果代码对象表示函数,"co_conts"中的第一项是函数的文档字符串,如果未定义,则为"None"
      .

   Frame objects(帧对象)
      帧对象表示执行帧.它们可能出现在回溯对象中,也会传递给已注册的跟踪函数.

      特殊的只读属性:"f_back"指向上一个堆栈帧(指向调用方),如果这是底部堆栈帧,则为"None"
      ;"f_code"是在此帧中执行的代码对象;"f_locals"是用来查找局部变量的字典;"f_globals
      "用于全局变量;"f_builtins"用于内置(固有)名称;"f_lasti"给出了精确的指令(这是代码
      对象字节码字符串的索引).

      访问"f_code"会引发一个带有参数"obj"和"f_code",审核事件"object.__getattr__".

      特殊的可写属性:"f_trace",如果不是"None",则是在代码执行期间为各种事件调用的函数(调
      试器使用).通常情况下,每个新的源行都会触发一个事件-可以通过将"f_trace_line"设置为
      "False"来禁用此功能.

      通过将"f_trace_opcode"设置为"True",实现*may*允许请求各操作码事件.请注意,如果跟
      踪函数引发的异常转义到被跟踪的函数,则这可能导致未定义的解释器行为.

      "f_lineno"是帧的当前行号-从跟踪函数中写入该行会跳到给定行(仅适用于最底部的帧).调
      试器可以通过写入f_lineno来实现跳转命令(也称为aka Set Next语句).

      帧对象支持一种方法:

          frame.clear()
             此方法清除对帧所持有的局部变量的所有引用.此外,如果框架属于生成器,则生成器
             将最终确定.这有助于打破涉及帧对象的引用循环(例如,捕获异常并存储其回溯以供
             以后使用时).

             如果帧当前正在执行,则引发"RuntimeError".
             3.4版中的新性质.

   Traceback objects(回溯对象)
      回溯对象表示异常的堆栈跟踪.当发生异常时,将隐式创建回溯对象,也可以通过调用
      "types.TracebackType"显式创建回溯对象.

      对于隐式创建的回溯,当搜索异常处理程序展开执行堆栈时,在每个展开级别,都会在当前回溯之
      前插入一个回溯对象.当输入异常处理程序时,堆栈跟踪对程序可用.它可以作为
      "sys.exc_info()"返回的元组的第三项以及捕获的异常的"__traceback__"属性进行访问.

      当程序不包含合适的处理程序时,堆栈跟踪被写入(格式良好)标准错误流;如果解释器是交互式
      的,它也可以作为"sys.last_traceback"提供给用户.

      对于显式创建的回溯,由回溯的创建者决定如何链接"tb_next"属性以形成完整的堆栈跟踪.

      特殊只读属性:"tb_frame"指向当前级别的执行帧;"tb_lineno"给出发生异常的行号;
      "tb_lasti"表示精确的指令.如果异常发生在没有匹配exception子句或finally子句的"try
      "语句中,则回溯中的行号和最后一条指令可能与其帧对象的行号不同.

      访问"tb_frame"会引发一个审核事件"object.__getattr__",参数为"obj"和"tb_frame".

      特殊的可写属性:"tb_next"是堆栈跟踪中的下一个级别(指向发生异常的帧),如果没有下一个
      级别,则为"None".

      在版本3.7中进行了更改:现在可以从Python代码显式实例化回溯对象,并且可以更新现有实例
      的"tb_next"属性.

   Slice objects(切片对象)
      切片对象用于表示"__getitem__()"方法的切片.它们也由内置的"slice()"函数创建.

      特殊只读属性:"start"为下限;"stop"是上限;"step"是步长值;如果省略,每个都是"None".
      这些属性可以有任何类型.

      切片对象支持一种方法:

          slice.indices(self,length)
             此方法接受单个整数参数*length*,并计算有关切片的信息,如果应用于*length*项
             序列,则切片对象将描述该切片.它返回三个整数的元组;它们分别是切片的*start*
             和*stop*索引以及*step*或步长.丢失或越界索引的处理方式与常规切片一致.

   Static method objects(静态方法对象)
      静态方法对象提供了一种方法,可以阻止函数对象向上述方法对象的转换.静态方法对象是任何
      其他对象(通常是用户定义的方法对象)的包装器.当从类或类实例检索静态方法对象时,实际返
      回的对象是包装对象,它不受任何进一步转换的约束.静态方法对象本身不可调用,尽管它们包装
      的对象通常是可调用的.静态方法对象由内置的"staticmethod()"构造函数创建.

   Class method objects(类方法对象)
      类方法对象与静态方法对象一样,是另一个对象周围的包装器,它改变了从类和类实例检索该对
      象的方式.上述"用户定义方法"下描述了类方法对象在此类检索时的行为.类方法对象由内置的
      "classmethod()"构造函数创建.
"""
"""
# codecs.Codec

codecs.Codec = class Codec(builtins.object)
    定义无状态编码器/解码器的接口.
    .encode()/.decode()方法可以通过提供errors参数(字符串值)来使用不同的错误处理方案.
    这些字符串值是预定义的:
        'strict'            - 引发ValueError错误(或子类)
        'ignore'            - 忽略该字符并继续下一个字符
        'replace'           - 替换为合适的替换字符
                              Python将在解码时使用内置Unicode编
                              码解码器的官方U+FFFD替换字符,在编码
                              时使用'？'
        'surrogateescape'   - 替换为专用代码点U+DCnn
        'xmlcharrefreplace' - 替换为适当的XML字符引用(仅用于编码)
        'backslashreplace'  - 替换为反斜杠转义序列.
        'namereplace'       - 替换为\N{…}转义序列(仅用于编码)
        允许值集可通过register_error进行扩展.
    此处定义方法:
        decode(self, input, errors='strict')

            解码对象输入并返回tuple (output object, length consumed)
            输入必须是提供bf_getreadbuf缓冲槽的对象
            Python字符串、缓冲区对象和内存映射文件就是提供此插槽的对象的示例

            错误定义要应用的错误处理.它默认为"strict"处理

            该方法不能在编解码器实例中存储状态
            对于必须保持状态以使解码有效的编解码器,请使用StreamReader

            在这种情况下,解码器必须能够处理零长度输入并返回输出对象类型的空对象

        encode(self, input, errors='strict')

            对对象输入进行编码并返回tuple (output object, length consumed)

            错误定义要应用的错误处理.它默认为"strict"处理

            该方法不能在编解码器实例中存储状态
            对于必须保持状态以提高编码效率的编解码器,请使用StreamWriter

            在这种情况下,解码器必须能够处理零长度输入并返回输出对象类型的空对象
    此处定义数据描述符：
    __dict__
        实例变量字典(如果已定义)
    __weakref__
        对象的弱引用列表(如果已定义)
"""
"""
# def

函数定义:定义用户定义的函数对象(请参见"标准类型层次结构"一节):

    funcdef                   ::= [decorators] "def" funcname 
                           "(" [parameter_list] ")" ["->" expression] ":" suite
    decorators                ::= decorator+
    decorator                 ::= "@" assignment_expression NEWLINE
    parameter_list            ::= defparameter ("," defparameter)* "," "/" 
                  ["," [parameter_list_no_posonly]] | parameter_list_no_posonly
    parameter_list_no_posonly ::= defparameter ("," defparameter)* 
                      ["," [parameter_list_starargs]] | parameter_list_starargs
    parameter_list_starargs   ::= "*" [parameter] ("," defparameter)* 
                            ["," ["**" parameter [","]]] | "**" parameter [","]
    parameter                 ::= identifier [":" expression]
    defparameter              ::= parameter ["=" expression]
    funcname                  ::= identifier

   注释:
       decorators:装饰器
       parameter_list:参数列表a,b:1,c=1  /   a,b:1,c=1,*args,**kwargs
       expression:表达方式
       decorator:装饰器表达式
       assignment_expression:赋值表达式
       NEWLINE:换行字符
       identifier:标识符
       parameter:参数
       parameter_list_no_posonly:没有限制的参数列表a,b:1,c = 1,*args,**kwargs
       parameter_list_starargs:起始参数的参数列表*args,**kwargs
       ("," x)*:表示x出现0次或多次
       ["," [x]] | x:表示x至少出现一次
       /:或者,二选一

函数定义是一个可执行语句.它的执行将当前本地命名空间中的函数名绑定到函数对象(围绕函数的可执
行代码的包装器).此函数对象包含对当前全局命名空间的引用,作为调用函数时要使用的全局命名空间.

函数定义不执行函数体;仅在调用函数时执行.

函数定义可以由一个或多个*decorator*表达式包装.定义函数时,将在包含函数定义的范围内计算装
饰器表达式.结果必须是一个可调用的,它是以函数对象作为唯一参数调用的.返回值绑定到函数名而不
是函数对象.多个装饰器以嵌套方式应用.例如,下面的代码

   @f1(arg)
   @f2
   def func(): pass

大致相当于

   def func(): pass
   func = f1(arg)(f2(func))

在版本3.9中更改:函数可以用任何有效的"assignment_expression(赋值表达式)"修饰.以前,语法
的限制性要大得多;

当一个或多个*parameters*的形式为*parameter* "="*expression*时,该函数被称为具有
"default parameter values.".对于具有默认值的参数,可以从调用中省略相应的*argument*,在
这种情况下,参数的默认值被替换.如果一个参数有一个默认值,则在"*"之前的所有后续参数都必须有
一个默认值-这是一个语法未表达的语法限制.

**在执行函数定义时,默认参数值从左到右求值.**这意味着在定义函数时表达式求值一次,并且每次调
用都使用相同的"precomputed(预计算)"值.当默认参数是可变对象(如列表或字典)时,了解这一点尤
为重要:如果函数修改对象(例如,通过向列表中添加项),则默认值实际上已修改.这通常不是我们的初
衷.解决此问题的一种方法是使用“None”作为默认值,并在函数体中显式测试它,例如:

   def whats_on_the_telly(penguin=None):
       if penguin is None:
           penguin = []
       penguin.append("property of the zoo")
       return penguin

函数调用语义在"section Calls"一节中有更详细的描述.函数调用始终为参数列表中提到的所有参数
赋值,可以是位置参数、关键字参数,也可以是默认值.如果存在格式"*identifier",则将其初始化为
接收任何多余位置参数的元组,默认为空元组.如果存在格式"**identifier",则会将其初始化为接收
任何多余关键字参数的新有序映射,默认为相同类型的新空映射."*"或"*identifier"后的参数是仅限
关键字的参数,只能通过关键字参数传递."/"之前的参数仅为位置参数,只能由位置参数传递.
在版本3.8中更改:"/"函数参数语法可用于指示仅位置参数.

参数名称后面可能有一个格式为": expression"的*annotation(注释)*.任何参数都可以有注释,即
使是形式为"*identifier"或"**identifier"的参数.函数在参数列表后可能有格式为
"-> expression"的"return"注释.这些注释可以是任何有效的Python表达式.注释的存在不会改变
函数的语义.注释值可作为字典值使用,字典值由函数对象的"__annotations__"属性中的参数名称键
入.如果使用从"__future__"导入的"annotation(注释)",则注释将在运行时保留为字符串,从而启
用延迟计算.否则,将在执行函数定义时对其求值.在这种情况下,注释的计算顺序可能与它们在源代码中
出现的顺序不同.

还可以创建匿名函数(未绑定到名称的函数),以便在表达式中立即使用.这使用Lambda表达式,如
Lambdas一节所述.请注意,Lambda表达式只是简化函数定义的简写;"def"语句中定义的函数可以传递
或分配给另一个名称,就像lambda表达式定义的函数一样."def"表单实际上更强大,因为它允许执行多
个语句和注释.

**程序员须知:**函数是一级对象.在函数定义内执行的"def"语句定义了可以返回或传递的本地函数.
嵌套函数中使用的自由变量可以访问包含def的函数的局部变量.
"""
"""
# FORMATTING

Format String Syntax
********************
"str.format()"方法和"Formatter"类共享格式字符串的相同语法(尽管在"Formatter"的情况下,
    子类可以定义自己的格式化字符串语法).语法与格式化字符串文字的语法相关,但不太复杂,特别
    是不支持任意表达式.

    格式字符串包含由大括号"{}"包围的"replacement fields(替换字段)".大括号中不包含的任
    何内容都被视为文字文本,它会原封不动地复制到输出中.如果需要在文本中包含大括号字符,可以
    通过"{{}}"来对其进行转义.

    replacement field(替换字段)的语法如下所示:

          replacement_field ::= "{" [field_name] ["!" conversion] 
                                                          [":" format_spec] "}"
          field_name        ::= arg_name ("." attribute_name|"
                                                         [" element_index "]")*
          arg_name          ::= [identifier|digit+]
          attribute_name    ::= identifier
          element_index     ::= digit+|index_string
          index_string      ::= <any source character except "]"> +
          conversion        ::= "r"|"s"|"a"
          format_spec       ::= <将在下面详细介绍>

    在不太正式的术语中,replacement field(替换字段)可以以*field_name*开头,该字段指定要
    格式化其值并插入到输出中的对象,而不是替换字段.*field_name*后面有一个可选的
    *conversion*字段,该字段前面有一个感叹号"!",还有一个*format_spec*,该字段前面有一个
    冒号":".这些值指定替换值的非默认格式.

    *field_name*本身以一个*arg_name*开头,它是一个数字或一个关键字.如果是数字,则表示位
    置参数;如果是关键字,则表示命名关键字参数.如果格式字符串中的数字arg_names按顺序为
    0、1、2,…,则它们都可以省略(而不仅仅是部分),并且数字0、1、2,…将按顺序自动插入.由于
    *arg_name*不以引号分隔,因此无法在格式字符串中指定任意字典键(例如字符串"'10'"或
    "':-]'").*arg_name*后面可以跟任意数量的索引或属性表达式.格式为"'.name'"的表达式使
    用"getattr()"选择命名属性,而格式为"[index]"的表达式使用"__getitem__()"执行索引查
    找.在版本3.1中更改:可以省略"str.format()"的位置参数说明符,因此"{}{}.format(a,b)"
    相当于"{0}{1}.format(a,b)".
    在版本3.4中更改:"Formatter"可以省略位置参数说明符.

    *conversion*字段在格式化之前导致类型强制.通常,格式化值的工作由值本身的
    "__format__()"方法完成.但是,在某些情况下,需要强制将类型格式化为字符串,从而覆盖其自
    身的格式化定义.通过在调用"__format__()"之前将值转换为字符串,可以绕过正常的格式化逻
    辑.

    当前支持三个转换标志:"!s'"调用值上的"str()"、"!r'"调用"repr()"和"!a'"调用
    "ascii()".

    *format_spec*字段包含如何显示值的规范,包括字段宽度、对齐方式、填充、小数精度等详细
    信息.每个值类型都可以定义自己的"formatting mini-language"或对*format_spec*的解释

    大多数内置类型都支持Format Specification Mini-Language,这将在下面详细介绍.

    *format_spec*字段也可以包含嵌套的替换字段.这些嵌套替换字段可能包含字段名、转换标志
    和格式规范,但不允许更深的嵌套.在解释*format_spec*字符串之前,将替换*format_spec*中
    的替换字段.这允许动态指定值的格式.

    有关一些示例,请参见"Format examples"部分.


    Format Specification Mini-Language
    ==================================

    "Format specifications"在格式字符串中包含的replacement field(替换字段)中使用,以
    定义各个值的表示方式(see Format String Syntax and Formatted string literals).
    它们也可以直接传递给内置的"format()"函数.每个formattable类型都可以定义如何解释格式
    规范.

    大多数内置类型为格式规范实现以下选项,尽管某些格式选项仅受数值类型支持.

    一般的约定是,空格式规范生成的结果与对值调用"str()"时的结果相同.非空格式规范通常会修
    改结果.

    *standard format specifier*的一般形式为:

       format_spec     ::= [[fill]align][sign][#][0][width][grouping_option]
                                                             [.precision][type]
       fill            ::= <any character>
       align           ::= "<"|">"|"="|"^"
       sign            ::= "+"|"-"|" "
       width           ::= digit+
       grouping_option ::= "_"|","
       precision       ::= digit+
       type            ::= "b"|"c"|"d"|"e"|"E"|"f"|"F"|"g"|"G"|"n"|"o"|"s"|"x"
                                                                       |"X"|"%"

    如果指定了有效的*align*值,则该值前面可以有一个*fill*字符,该字符可以是任何字符,如果
    省略,则默认为空格.在formatted string literal中或使用"str.format()"方法时,不可能
    使用文本大括号("{"或"}")作为*fill*字符.但是,可以插入带有嵌套替换字段的大括号.此限制
    不影响"format()"函数.

    各种路线选项的含义如下:

        选项           含义
      -------------------------------------------------------------------------
       "'<'"    强制字段在可用空间内左对齐(这是大多数对象的默认设置).
      -------------------------------------------------------------------------
       "'>'"    强制字段在可用空间内右对齐(这是数字的默认设置).
      -------------------------------------------------------------------------
       "'='"    强制将填充放置在符号(如果有)之后但数字之前.这用于打印格式为
                "+000000120"的字段.此对齐选项仅对数字类型有效.当'0'紧跟在字段宽度之前
                时,它将成为默认值.
      -------------------------------------------------------------------------
       "'^'"    强制字段在可用空间内居中.

    请注意,除非定义了最小字段宽度,否则字段宽度将始终与要填充的数据大小相同,因此在这种情况
    下,*align*选项没有任何意义.

    *sign*选项仅对数字类型有效,可以是以下类型之一:
           选项          含义
        -------------------------------------------------
          "'+'"    指示符号应同时用于正数和负数.
        -------------------------------------------------
          "'-'"    指示符号应仅用于负数(这是默认行为).
        -------------------------------------------------
          space    指示应在正数上使用前导空格,在负数上使用减号.

    "#"选项导致转换使用"alternate form".对于不同的类型,替代形式的定义是不同的.此选项仅
    对整数、浮点和复杂类型有效.对于整数,当使用二进制、八进制或十六进制输出时,此选项会将相
    应的前缀"'0b'", "'0o'",or "'0x'"添加到输出值中.对于浮点型和复杂类型,替代形式会导致
    转换结果始终包含小数点字符,即使后面没有数字.通常,只有在转换结果后面有数字时,才会在转
    换结果中显示小数点字符.此外,对于"'g'" and "'G'"转换,尾随零不会从结果中移除.

    "','"选项表示使用逗号作为分隔符.对于区域设置识别分隔符,请改用"'n'"整数表示类型.
    在版本3.1中更改:添加了"','"选项.

    "'_'"选项表示浮点表示类型和整数表示类型"'d'"使用下划线作为千位分隔符.对于整数表示类
    型"'b'"、"'o'"、"'x'", and "'X'",将每隔4位插入下划线.对于其他演示文稿类型,指定此
    选项是错误的.
    在版本3.6中进行了更改:添加了"'_'"选项.

    *width*是定义最小总字段宽度的十进制整数,包括任何前缀、分隔符和其他格式字符.如果未指
    定,则字段宽度将由内容决定.

    如果没有给出明确的对齐方式,则在*width*字段前面加一个零("'0'")字符可以为数字类型启用
    符号感知的零填充.这相当于"'0'"的*fill*字符和"'='"的*alignment*类型.

    *precision*是一个十进制数,表示对于使用"'f'" and "'F'"格式的浮点值,小数点后应显示
    多少位;对于使用"'g'" or "'G'"格式的浮点值,小数点后应显示多少位.对于非数字类型,字段
    指示最大字段大小——换句话说,字段内容将使用多少个字符.整数值不允许使用*precision*.

    最后,*type*决定了数据的显示方式.

        可用的字符串表示形式有:
            类型      含义
           "'s'"   字符串格式.这是字符串的默认类型,可以省略.

           None    与"s"相同.

        可用的整数表示类型有:

            类型      含义
          ---------------------------------------------------------------------
           "'b'"   二进制格式.输出基数为2的数字.
          ---------------------------------------------------------------------
           "'c'"   字母.打印前将整数转换为相应的unicode字符
          ---------------------------------------------------------------------
           "'d'"   十进制整数.输出以10为基数的数字.
          ---------------------------------------------------------------------
           "'o'"   八进制格式.输出以8为基数的数字.
          ---------------------------------------------------------------------
           "'x'"   十六进制格式.输出以16为基数的数字,使用小写字母表示9以上的数字.
          ---------------------------------------------------------------------
           "'X'"   十六进制格式.输出以16为基数的数字,使用大写字母表示9以上的数字.
          ---------------------------------------------------------------------
           "'n'"   数字.数字这与"'d'"相同,只是它使用当前区域设置插入适当的数字分隔符.
          ---------------------------------------------------------------------
           None    与"'d'"相同.

        除上述表示类型外,整数还可以使用下面列出的浮点表示类型进行格式化(除了"'n'"和
        "None").进行此操作时,"float()"用于在格式化之前将整数转换为浮点数.

        "float" and "Decimal"值的可用表示形式有:
            类型       含义
        -----------------------------------------------------------------------
           "'e'"    科学计数型.对于给定精度"p",用字母'e'将系数与指数分开,以科学记数法
                    对数字进行格式化.系数在小数点前有一位数字,小数点后有"p"位,总共有
                    "p+1"个有效数字.在没有给定精度的情况下,在"float"的小数点后使用"6"
                    位精度,并显示"Decimal"的所有系数位数.如果小数点后没有数字,小数点也
                    将被删除,除非使用"#"选项.
        -----------------------------------------------------------------------
           "'E'"    科学计数型.科学符号.与"'e'"相同,只是它使用大写字母'E'作为分隔符.
        -----------------------------------------------------------------------
           "'f'"    定点表示法.对于给定精度"p",将数字格式化为小数点后紧跟"p"位的十进制
                    数字.在没有给定精度的情况下,在"float"的小数点后使用"6"位精度,并使
                    用足够大的精度来显示"decimal"的所有系数位数.如果小数点后没有数字,
                    小数点也将被删除,除非使用"#"选项.
        -----------------------------------------------------------------------
           "'F'"    定点表示法.与"'f'"相同,但将"nan"转换为"NAN",将"inf"转换为"INF".
        -----------------------------------------------------------------------
           "'g'"    通用格式.对于给定精度"p >= 1",这会将数字舍入为"p"有效数字,然后根
                    据其大小将结果格式化为定点格式或科学记数法.精度"0"被视为等同于精度
                    "1".精确规则如下:假设使用表示类型"'e'"和精度"p-1"格式化的结果将具
                    有指数"exp".然后,如果"m <= exp < p",其中"m"表示浮点数为-4,
                    "Decimals"为-6",则数字的格式为表示类型"'f'",精度为"p-1-exp".否
                    则,数字的格式为表示类型"'e'"和精度"p-1".在这两种情况下,都会从有效
                    位中删除不重要的尾随零,如果后面没有剩余的数字,小数点也会被删除,除非
                    使用了"#"选项.在没有给定精度的情况下,使用"6"有效数字的精度表示
                    "float".对于"Decimal",结果的系数由值的系数位数构成;科学记数法用于
                    绝对值小于"1e-6"的值以及最低有效位的位置值大于1的值,否则使用定点记
                    数法.无论精度如何,正无穷大和负无穷大、正零和负零以及nan的格式分别为
                    "inf"、"-inf"、"0"、"-0"和"nan".
        -----------------------------------------------------------------------
           "'G'"    通用格式.与"'g'"相同,但如果数字太大,则切换为"'E'".无穷大和NaN的表
                    示也是大写的.
        -----------------------------------------------------------------------
           "'n'"    数字.这与"'g'"相同,只是它使用当前区域设置插入适当的数字分隔符.
        -----------------------------------------------------------------------
           "'%'"    百分率.将数字乘以100,并以固定("'f'")格式显示,后跟百分号.
        -----------------------------------------------------------------------
           None     对于"float",这与"'g'"相同,只是当使用定点表示法格式化结果时,它总是
                    至少包含超过小数点的一位数字.使用的精度与忠实地表示给定值所需的精度
                    一样大.对于"Decimal",这与"'g'"或"'g'"相同,具体取决于当前十进制上
                    下文的"context.capitals"的值.整体效果是匹配由其他格式修饰符更改的
                    "str()"的输出.

    Format examples
    ===============

    本节包含"str.format()"语法示例以及与旧"%"格式的比较.
    在大多数情况下,语法类似于旧的"%"格式,添加了"{}"和":"代替"%".例如,"'%03.2f'"可以翻
    译为"'{:03.2f}'".新格式语法还支持新的和不同的选项,如以下示例所示.

    基础输出:
        >>> '{{}}'.format()
        {}
    按位置访问参数:
       >>> '{0}, {1}, {2}'.format('a', 'b', 'c')
       'a, b, c'
       >>> '{}, {}, {}'.format('a', 'b', 'c')
       'a, b, c'
       >>> '{2}, {1}, {0}'.format('a', 'b', 'c')
       'c, b, a'
       >>> '{2}, {1}, {0}'.format(*'abc')# 解包参数序列
       'c, b, a'
       >>> '{0}{1}{0}'.format('abra', 'cad')# 参数的索引可以重复
       'abracadabra'


    按名称访问参数:
       >>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', 
       ... longitude='-115.81W') 'Coordinates: 37.24N, -115.81W'
       >>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
       >>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
       'Coordinates: 37.24N, -115.81W'

    访问参数的属性:
       >>> c = 3-5j
       >>> ('The complex number {0} is formed from the real part {0.real} '
       ...  'and the imaginary part {0.imag}.').format(c)
       'The complex number (3-5j) is formed from the real part 3.0 and the 
        imaginary part -5.0.'
       >>> class Point:
       ...     def __init__(self, x, y):
       ...         self.x, self.y = x, y
       ...     def __str__(self):
       ...         return 'Point({self.x}, {self.y})'.format(self=self)
       ...
       >>> str(Point(4, 2))
       'Point(4, 2)'

    访问参数的项:
       >>> coord = (3, 5)
       >>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
       'X: 3;  Y: 5'

    替换"%s"和"%r":
       >>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 
       ... 'test2')
       "repr() shows quotes: 'test1'; str() doesn't: test2"

    对齐文本并指定宽度:
       >>> '{:<30}'.format('left aligned')
       'left aligned                  '
       >>> '{:>30}'.format('right aligned')
       '                 right aligned'
       >>> '{:^30}'.format('centered')
       '           centered           '
       >>> '{:*^30}'.format('centered')  # 使用 '*' 填充
       '***********centered***********'

    替换"%+f"、"%-f"和"%f"并指定符号:
       >>> '{:+f}; {:+f}'.format(3.14, -3.14)  # 总是表现出来
       '+3.140000; -3.140000'
       >>> '{: f}; {: f}'.format(3.14, -3.14)  # 为正数显示一个空格
       ' 3.140000; -3.140000'
       >>> '{:-f}; {:-f}'.format(3.14, -3.14)  # 只显示负号 -- same as '{:f}; 
       ... {:f}'
       '3.140000; -3.140000'

    替换"%x"和"%o"并将值转换为不同的基数:
       >>> # 该格式还支持二进制数
       >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
       'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
       >>> # 以0x、0o或0b作为前缀：
       >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
       'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

    使用逗号,下划线作为分隔符:
       >>> '{:,}'.format(1234567890)
       '1,234,567,890'
       >>> '{:_}'.format(1234567890)
       1_234_567_890

    表示百分比:
       >>> points = 19
       >>> total = 22
       >>> 'Correct answers: {:.2%}'.format(points/total)
       'Correct answers: 86.36%'

    使用特定于类型的格式:
       >>> import datetime
       >>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
       >>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
       '2010-07-04 12:15:58'

    嵌套参数和更复杂的示例:
       >>> for align, text in zip('<^>', ['left', 'center', 'right']):
       ...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
       ...
       'left<<<<<<<<<<<<'
       '^^^^^center^^^^^'
       '>>>>>>>>>>>right'
       >>>
       >>> octets = [192, 168, 0, 1]
       >>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
       'C0A80001'
       >>>
       >>> width = 5
       >>> for num in range(5,12):
       ...     for base in 'dXob':
       ...         print('{0:{width}{base}}'.format(num, base=base, width=width
       ...         ), end=' ')
       ...     print()
       ...
           5     5     5   101
           6     6     6   110
           7     7     7   111
           8     8    10  1000
           9     9    11  1001
          10     A    12  1010
          11     B    13  1011
"""
"""
# if

if声明

if语句用于条件执行：

   if_stmt ::= "if" assignment_expression ":" suite
               ("elif" assignment_expression ":" suite)*
               ["else" ":" suite]

它通过逐个计算表达式,直到找到一个为真,来选择其中一个套件;然后执行该套件(不执行或评估"if"
语句的其他部分).如果所有表达式都为false,则执行"else"子句的套件(如果存在).
"""
"""
# while

"while" 语句

"while" 语句用于重复执行,只要表达式为true:

   while_stmt ::= "while" assignment_expression ":" suite
                  ["else" ":" suite]

这会重复测试表达式,如果为真,则执行第一个套件;如果表达式为false(可能是第一次测试),则执行
"else"子句的套件(如果存在),循环终止.

在第一个套件中执行的"break"语句终止循环,而不执行"else"子句的套件.在第一个套件中执行的
"continue"语句跳过套件的其余部分并返回测试表达式.
"""
"""
# for

"for"语句

"for"语句用于迭代序列(如字符串、元组或列表)或其他iterable对象的元素:

   for_stmt ::= "for" target_list "in" expression_list ":" suite
                ["else" ":" suite]

表达式列表计算一次;它应该产生一个不可复制的对象.为"expression_list"的结果创建迭代器.然
后,按照迭代器返回的顺序,对迭代器提供的每个项执行一次suite.使用标准分配规则将每个项目依次
分配到目标列表,然后执行suite.当项目用尽时(即序列为空或迭代器引发"StopIteration"异常时),
执行"else"子句中的suite(如果存在),循环终止.

在第一个suite中执行的"break"语句终止循环,而不执行"else"子句的套件.在第一个套件中执行的
"continue"语句跳过suite的其余部分并继续执行下一项,如果没有下一项,则继续执行"else"子句.

for循环对目标列表中的变量进行赋值.这将覆盖以前对这些变量的所有赋值,包括for循环套件中的赋
值:

   for i in range(10):    # 这不会影响for循环
       print(i)           # 因为i将被下一个重写
       i = 5              # 范围内的索引

循环完成时,目标列表中的名称不会被删除,但如果序列为空,则循环根本不会为其分配名称.提示:内置
函数"range()"返回一个整数迭代器,该迭代器适合模拟Pascal的"for i:= a to b do"的效果;例
如,"list(range(3))"返回列表"[0, 1, 2]".

Note:

  当循环修改序列时有一个微妙之处(这只能发生在可变序列中,例如列表).内部计数器用于跟踪下一
  个使用哪个项,并且在每次迭代中递增.当该计数器达到序列长度时,循环终止.这意味着,如果suite
  从序列中删除当前(或上一个)项,则将跳过下一个项(因为它获取已处理的当前项的索引).同样,如果
  suite在当前项之前的序列中插入了一个项,那么下次通过循环将再次处理当前项.这可能导致严重的
  错误,可以通过使用整个序列的一个片段制作临时副本来避免,例如:

     for x in a[:]:
         if x < 0: a.remove(x)
"""
"""
# COMPLEX

虚数字面常量

虚数字面常量由以下词汇定义描述:

   imagnumber ::= (floatnumber | digitpart) ("j" | "J")

虚数字面常量产生实数部分为0.0的复数.复数表示为一对浮点数,并且对其范围有相同的限制.要创建具有
非零实部的复数,请向其添加浮点数,例如"(3+4j)".虚数字面常量的一些示例:

   3.14j   10.j    10j     .001j   1e100j   3.14e-10j   3.14_15_93j
"""
"""
# FLOAT

浮点型字面常量

浮点型字面常量由以下词汇定义描述:

   floatnumber   ::= pointfloat | exponentfloat
   pointfloat    ::= [digitpart] fraction | digitpart "."
   exponentfloat ::= (digitpart | pointfloat) exponent
   digitpart     ::= digit (["_"] digit)*
   fraction      ::= "." digitpart
   exponent      ::= ("e" | "E") ["+" | "-"] digitpart

请注意,整数和指数部分始终使用基数10进行解释.例如,"077e010"是合法的,表示与"77e10"相同的
数字.允许的浮点文字范围取决于实现.与整数文本一样,数字分组支持下划线.

浮点型字面常量的一些示例：

   3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93

在版本3.6中更改:现在允许下划线用于文本中的分组目的.
"""
"""
# NUMBERS

数字字面常量

数字字面常量有三种类型:整数、浮点数和虚数.没有复数(复数可以通过实数和虚数相加形成).

请注意,数字字面常量不包括符号;像"-1"这样的短语实际上是由一元运算符"-"和文字"1"组成的表达式.
"""
"""
# LITERALS

字面常量

Python支持字符串和字节字面常量以及各种数字字面常量:

  literal ::= stringliteral | bytesliteral | integer | floatnumber | imagnumber

对字面常量的求值将生成给定类型(字符串、字节、整数、浮点数、复数)的具有给定值的对象.在浮点数和
虚数(复数)字面常量的情况下,该值可以近似.

所有字面常量都对应于不可变的数据类型,因此对象的标识不如其值重要.对具有相同值的文本(程序文本中
相同的出现或不同的出现)进行多次求值可能会获得相同的对象或具有相同值的不同对象.
"""
"""
# LISTLITERALS

列表显示

列表显示可能是方括号中包含的一系列空表达式：

   list_display ::= "[" [starred_list | comprehension] "]"

列表显示产生一个新的列表对象,内容由表达式列表或理解指定.当提供一个逗号分隔的表达式列表时,
它的元素将从左到右求值,并按该顺序放入列表对象中.当提供comprehension(理解)时,列表由理解
产生的元素构成.
"""
"""
# INTEGER

整数字面常量

整数字面常量由以下词法定义描述：

   integer      ::= decinteger | bininteger | octinteger | hexinteger
   decinteger   ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
   bininteger   ::= "0" ("b" | "B") (["_"] bindigit)+
   octinteger   ::= "0" ("o" | "O") (["_"] octdigit)+
   hexinteger   ::= "0" ("x" | "X") (["_"] hexdigit)+
   nonzerodigit ::= "1"..."9"
   digit        ::= "0"..."9"
   bindigit     ::= "0" | "1"
   octdigit     ::= "0"..."7"
   hexdigit     ::= digit | "a"..."f" | "A"..."F"

除了可以存储在可用内存中的内容外,整数文本的长度没有限制.

在确定文字的数值时忽略下划线.它们可用于对数字进行分组,以增强可读性.一个下划线可以出现在数
字之间,也可以出现在诸如"0x"之类的基本说明符之后.

请注意,不允许在非零十进制数中使用前导零.这是为了用C风格的八进制文字消除歧义,Python在3.0
版之前就使用了这种文字.

整数字面常量的一些示例：

   7     2147483647                        0o177    0b100110111
   3     79228162514264337593543950336     0o377    0xdeadbeef
         100_000_000_000                   0b_1110_0101

在版本3.6中更改:现在允许下划线用于文本中的分组目的.
"""
"""
# DICTIONARYLITERALS

字典显示

字典显示是一系列可能为空的键/值对,用大括号括起来:

   dict_display       ::= "{" [key_datum_list | dict_comprehension] "}"
   key_datum_list     ::= key_datum ("," key_datum)* [","]
   key_datum          ::= expression ":" expression | "**" or_expr
   dict_comprehension ::= expression ":" expression comp_for

字典显示将生成一个新的字典对象.

如果给定了以逗号分隔的键/值对序列,则从左到右对其求值,以定义字典的条目:每个键对象用作字典中
的键,以存储相应的数据.这意味着您可以在键/值列表中多次指定同一键,该键的最终字典值将是最后一
个给定的值.

双星号"**"表示*dictionary unpacking(字典解包)*.其操作数必须是*mapping(映射)*.每个映
射项都将添加到新词典中.稍后的值替换先前的键/值对和早期字典解包已经设置的值.

版本3.5中新增:解包到字典显示.

与列表和集合理解不同,字典理解需要两个用冒号分隔的表达式,后跟通常的"for"和"if"子句.运行理
解时,生成的键和值元素将按生成顺序插入新词典.

(键类型应为*hashable(可哈希)*,这排除了所有可变对象.)未检测到重复键之间的冲突;以给定键值
存储的最后一个数据为准.

在版本3.8中进行了更改:在Python 3.8之前,在字典理解中,键和值的求值顺序没有得到很好的定义.
在CPython中,值是在键之前计算的.从3.8开始,在值之前评估键.
"""
"""
# LISTS

可变序列类型

下表中的操作是在可变序列类型上定义的.提供"collections.abc.MutableSequence"ABC是为了
更容易在自定义序列类型上正确实现这些操作.

在表中,*s*是可变序列类型的实例,*t*是任何可编辑对象,*x*是满足*s*施加的任何类型和值限制的
任意对象(例如,"bytearray"仅接受满足值限制"0 <= x <= 255"的整数).

  Operation(操作)                 Result(结果)                            Notes
-------------------------------------------------------------------------------
 "s[i] = x"                      *s*中的*i*项替换为*x*
-------------------------------------------------------------------------------
 "s[i:j] = t"                    将*s*从*i*到*j*的切片替换
                                 为iterable(可迭代的)*t*
-------------------------------------------------------------------------------
 "del s[i:j]"                    等同于"s[i:j] = []"
-------------------------------------------------------------------------------
 "s[i:j:k] = t"                  "s[i:j:k]"的元素替换为*t*                   (1)
-------------------------------------------------------------------------------
 "del s[i:j:k]"                  从列表中删除"s[i:j:k]"的元素
-------------------------------------------------------------------------------
 "s.append(x)"                   在序列末尾追加*x*(与"s[len(s)
                                 :len(s)] = [x]"相同)
-------------------------------------------------------------------------------
 "s.clear()"                     删除*s*中的所有项目(与"del s[                (5)
                                 :]"相同)
-------------------------------------------------------------------------------
 "s.copy()"                      创建*s*(与"s[:]"相同)的浅层副本              (5)
-------------------------------------------------------------------------------
 "s.extend(t)" or "s += t"       用*t*的内容扩展*s*(大部分内容与
                                 "s[len(s):len(s)] = t"相同)
-------------------------------------------------------------------------------
 "s *= n"                        更新*s*,其内容重复*n*次                      (6)
-------------------------------------------------------------------------------
 "s.insert(i, x)"                在*i*给定的索引处将*x*插入*s*(
                                 与"s[i:i] = [x]"相同)
-------------------------------------------------------------------------------
 "s.pop([i])"                    在*i*处检索项目,并将其从*s*中删除             (2)
-------------------------------------------------------------------------------
 "s.remove(x)"                   从*s*中删除第一项,其中"s[i]"等于*x*           (3)
-------------------------------------------------------------------------------
 "s.reverse()"                   原位反转*s*项                               (4)

Notes:
    1. *t*必须与所替换的切片具有相同的长度.
    2.可选参数*i*默认为"-1",因此默认情况下会删除并返回最后一项.
    3.当在*s*中找不到*x*时,"remove()"将引发"ValueError".
    4."reverse()"方法在反转大序列时修改适当的序列以节省空间.为了提醒用户它是通过副作用
      操作的,它不会返回相反的顺序.
    5.包含"clear()"和"copy()"是为了与不支持切片操作(如"dict"和"set")的可变容器的接口
      保持一致."copy()"不是"collections.abc.MutableSequence"ABC的一部分,但大多数具
      体的可变序列类都提供了它.
        版本3.3中新增了："clear()"和"copy()"方法.
    6.值*n*是一个整数,或者是一个实现"__index__()"的对象.*n*的零值和负值清除序列.序列中
      的项目不被复制;它们被多次引用,如公共序列操作下的"s*n"所述.
"""
"""
# OPERATORS,EXPRESSIONS

下表总结了Python中运算符的优先级,从最高优先级(最大约束)到最低优先级(最小约束).
同一框中的运算符具有相同的优先级.除非明确给出语法,否则运算符是二进制的.同一框中
的运算符从左到右分组(幂运算除外,幂运算从右到左分组).

注意,比较、成员资格测试和身份测试都具有相同的优先级,并且具有从左到右的链接功能,
如比较部分中所述.

        操作符                               描述
-------------------------------------------------------------------------------
     "(expressions)","[expressions]",    元组显示、列表显示、
     "{key:value}","{expressions}"       字典显示、集合显示
-------------------------------------------------------------------------------
     "x[index]","x[index:index]",        取值、切片、
     "x(arguments)","x.attribute"        方法调用、属性引用
-------------------------------------------------------------------------------
     "await"                             等候
-------------------------------------------------------------------------------
     "**"                                求幂[1]
-------------------------------------------------------------------------------
     "+x", "-x", "~x"                    正、负、按位非
-------------------------------------------------------------------------------
     "*", "@", "/", "//", "%"            乘法、矩阵乘法、除法、商、余数[2]
-------------------------------------------------------------------------------
     "+", "-"                            加减法
-------------------------------------------------------------------------------
     "<<", ">>"                          左移,右移
-------------------------------------------------------------------------------
     "&"                                 按位与
-------------------------------------------------------------------------------
     "^"                                 按位异或
-------------------------------------------------------------------------------
     "|"                                 按位或
-------------------------------------------------------------------------------
     "in","not in","is","is not",        比较,包括成员资格测试,
     "<","<=",">",">=","!=","=="         身份测试
-------------------------------------------------------------------------------
     "not"                               布尔非
-------------------------------------------------------------------------------
     "and"                               布尔与
-------------------------------------------------------------------------------
     "or"                                布尔或
-------------------------------------------------------------------------------
     "if" – "else"                       条件表达式
-------------------------------------------------------------------------------
     "lambda"                            Lambda表达式
-------------------------------------------------------------------------------
     ":="                                赋值表达式

-[脚注]-
[1] 幂运算符"**"比其右侧的算术或按位一元运算符绑定得更紧,也就是说,"2**-1"is"0.5".
[2] "%"运算符也用于字符串格式设置;同样的优先顺序也适用.
"""
"""
# POWER

乘方操作符

幂运算符比其左边的一元运算符绑定得更紧;它的绑定不如右边的一元运算符紧密.语法是:

   power ::= (await_expr | primary) ["**" u_expr]

因此,在幂运算符和一元运算符的非偶数化序列中,运算符从右向左求值(这不限制操作数的求值顺序):
"-1**2"导致"-1".

当使用两个参数调用时,幂运算符与内置的"pow()"函数具有相同的语义:它将左参数提升为右参数的
幂.数值参数首先转换为公共类型,结果为该类型.

对于整型操作数,结果的类型与操作数的类型相同,除非第二个参数为负;在这种情况下,所有参数都转
换为float,并传递一个float结果.例如,"10**2"返回"100",但"10**-2"返回"0.01".

将"0.0"提高到负幂会导致"ZeroDivisionError".将负数提高到分数次幂会产生一个"complex(复
数)".(在早期版本中,它引发了一个"ValueError".)
"""
"""
# in

成员资格测试操作

操作员"in"和"not in"测试成员资格.如果*x*是*s*的成员,"x in s"计算为"True",否则为
"False"."x not in s"返回"x in s"的否定.所有内置序列和集合类型都支持此功能,字典也支持此
功能,"in"测试字典是否具有给定的键.对于容器类型,如列表、元组、集合、冻结集、字典或
collections.deque(集合的双队列),表达式"x in y"相当于
"any(x is e or x == e for e in y)".

对于字符串和字节类型,当且仅当*x*是*y*的子字符串时,"x in y"为"True".等效测试为
"y.find(x) != -1".空字符串始终被视为任何其他字符串的子字符串,因此'' in "abc"将返回
"True".

对于定义"__contains__()"方法的用户定义类,如果"y.__contains__(x)"返回真值,则"x in y"
返回"True",否则返回"False".

对于不定义"__contains__()"但定义"__iter__()"的用户定义类,如果在"y"上迭代时生成表达式
"x is z or x == z"为真的某个值"z",则"x in y"为"True".如果在迭代过程中引发异常,就好像
"in"引发了该异常.

最后,尝试了旧式的迭代协议:如果类定义了"__getitem__()","x in y"是"True",当且仅当存在一
个非负整数索引*i*,即"x is y[i] or x == y[i]",并且没有较低的整数索引会引发
"IndexError"异常.(如果引发任何其他异常,则如同"in"引发了该异常).

运算符"not in"定义为具有逆真值"in".
"""
"""
# SLICINGS

切片

切片选择序列对象中的一系列项(例如,字符串、元组或列表).切片可以用作表达式,也可以用作赋值或
"del"语句中的目标.切片的语法:

   slicing      ::= primary "[" slice_list "]"
   slice_list   ::= slice_item ("," slice_item)* [","]
   slice_item   ::= expression | proper_slice
   proper_slice ::= [lower_bound] ":" [upper_bound] [ ":" [stride] ]
   lower_bound  ::= expression
   upper_bound  ::= expression
   stride       ::= expression

这里的形式语法存在歧义:任何看起来像表达式列表的东西也看起来像切片列表,因此任何订阅都可以解
释为切片.与其使语法进一步复杂化,不如定义在本例中,作为订阅的解释优先于作为切片的解释(如果切
片列表不包含正确的切片,则为这种情况),从而消除歧义.

切片的语义如下所示.使用从切片列表构造的键对主对象进行索引(使用与普通订阅相同的
"__getitem__()"方法),如下所示.如果切片列表包含至少一个逗号,则键是包含切片项转换的元组;
否则,单个切片项的转换是关键.作为表达式的切片项的转换就是该表达式.正确切片的转换是一个切片
对象,其"start"、"stop"和"step"属性分别是下限、上限和步幅表达式的值,用"None"替换缺少的
表达式.
"""
"""
# SUBSCRIPTS

订阅

订阅序列(字符串、元组或列表)或映射(字典)对象通常会从集合中选择一项:

   subscription ::= primary "[" expression_list "]"

primary(主对象)必须计算为支持订阅的对象(例如列表或字典).用户定义的对象可以通过定义
"__getitem__()"方法来支持订阅.

对于内置对象,有两种类型的对象支持订阅:

如果主对象是映射,则表达式列表必须计算为其值为映射键之一的对象,并且订阅将在映射中选择与该键
对应的值.(表达式列表是元组,只有一个项除外.)

如果主表达式是一个序列,则表达式列表的计算结果必须为整数或切片.

形式语法对序列中的负索引没有特殊规定;但是,内置序列都提供了一个"__getitem__()"方法,该方
法通过将序列的长度添加到索引中来解释负索引(以便"x[-1]"选择"x"的最后一项).结果值必须是小
于序列中项目数的非负整数,订阅将选择索引为该值的项目(从零开始计数).由于对负索引和切片的支
持出现在对象的"__getitem__()"方法中,因此重写此方法的子类将需要显式添加该支持.

字符串的项是字符.字符不是单独的数据类型,而是正好由一个字符组成的字符串.

订阅某些*classes*或*types*将创建通用别名.在这种情况下,用户定义的类可以通过提供
"__class_getitem__()"类方法来支持订阅.
"""
"""
# PRIVATENAMES

私有名称:标识符(名称)

作为原子出现的标识符是名称.

当名称绑定到一个对象时,对原子的求值将生成该对象.当名称未绑定时,尝试对其求值将
引发"NameError"异常.

**Private name mangling(混乱):当类定义中以文本形式出现的标识符以两个或多个
下划线字符开头,而不是以两个或多个下划线结尾时,它被视为该类的*private name(私
有名称)*.在为私有名称生成代码之前,会将其转换为更长的形式.转换将在名称前面插入
类名,删除前导下划线并插入一个下划线.例如,在名为"Ham"的类中出现的标识符"__spam"
将被转换为"_Ham__spam".此转换独立于使用标识符的语法上下文.如果转换后的名称非常
长(超过255个字符),则可能需要实现定义的截断发生如果类名只包含下划线,则不进行任何
转换.
"""
"""
# ATTRIBUTES

属性引用
属性引用是主引用,后跟句点和名称:

   attributeref ::= primary "." identifier

evaluate(主对象)必须计算为支持属性引用的类型的对象,大多数对象都会这样做.然后要求该对象生
成名称为标识符的属性.可以通过重写"__getattr__()"方法自定义此产品.如果此属性不可用,则引
发异常"AttributeError".否则,生成的对象的类型和值由对象确定.对同一属性引用的多次求值可能
会产生不同的对象.
"""
"""
# CALLABLEMETHODS

模拟可调用对象

object.__call__(self[, args...])

    当实例作为函数"called(调用)"时调用;如果定义了此方法,"x(arg1, arg2, ...)"将转换为
    "type(x).__call__(x, arg1, ...)".
"""
"""
# TRUTHVALUE

真值检验

任何对象都可以测试真值,在"if"或"while"条件下使用,或作为下面布尔运算的操作数.

默认情况下,对象被视为true,除非其类定义了返回"False"的"__bool__()"方法或与对象一起调用
时返回零的"__len__()"方法.以下是大多数被认为是错误的内置对象：

*定义为false的字面常量:"None"和"False".
*任何数字类型的零:"0"、"0.0"、"0j"、"Decimal(0)"、"Fraction(0,1)"
*空序列和集合:"''"、"()"、"[]"、"{}"、"set()"、"range(0)"

除非另有说明,否则具有布尔结果的操作和内置函数始终返回"0"或"False"表示false,返回"1"或
"True"表示true.(重要例外:布尔运算"or"和"and"始终返回其操作数之一.)
"""
"""
# TUPLELITERALS

表达式列表

   expression_list    ::= expression ("," expression)* [","]
   starred_list       ::= starred_item ("," starred_item)* [","]
   starred_expression ::= expression | (starred_item ",")* [starred_item]
   starred_item       ::= assignment_expression | "*" or_expr

除非显示列表或集合的一部分,否则至少包含一个逗号的表达式列表将生成元组.元组的长度是列表中表
达式的数量.表达式从左到右求值.

星号"*"表示*iterable unpacking(迭代拆包)*.其操作数必须是*iterable*.iterable被扩展为
一系列项,这些项包含在解包站点的新元组、列表或集合中.

版本3.5中新增:表达式列表中的可拆分解包.

仅在创建单个元组(又称*单元组*)时才需要尾随逗号;它在所有其他情况下都是可选的.没有尾随逗号
的单个表达式不会创建元组,而是生成该表达式的值.(要创建空元组,请使用一对空括号:"()")
"""
"""
# UNARY

一元算术和位运算

所有一元算术和位运算具有相同的优先级:

   u_expr ::= power | "-" u_expr | "+" u_expr | "~" u_expr

一元"-"(minus(减))运算符产生其数值参数的反运算.

一元"+"(plus(加号))运算符不改变其数值参数.

一元"~"(invert(反转))运算符生成其整数参数的按位反转."x"的位反转定义为"-(x+1)".它只适用
于整数.

在这三种情况下,如果参数的类型不正确,则会引发"TypeError"异常.
"""
"""
# NUMBERMETHODS

模拟数字类型

可以定义以下方法来模拟数值对象.与实现的特定类型的数字不支持的操作相对应的方法(例如,非整数
的按位操作)应保持未定义.

object.__add__(self, other)             +
object.__sub__(self, other)             -
object.__mul__(self, other)             *
object.__matmul__(self, other)          @
object.__truediv__(self, other)         /
object.__floordiv__(self, other)        //
object.__mod__(self, other)             %
object.__divmod__(self, other)          divmod()
object.__pow__(self, other[, modulo])   **
object.__lshift__(self, other)          <<
object.__rshift__(self, other)          >>
object.__and__(self, other)             &
object.__xor__(self, other)             ^
object.__or__(self, other)              |

   调用这些方法是为了实现二进制算术运算("+", "-", "*", "@", "/", "//", "%",
   "divmod()","pow()", "**", "<<", ">>", "&", "^", "|").例如,要计算表达式"x + y",
   其中*x*是具有"__add__()"方法的类的实例,将调用"x.__add__(y)"."__divmod__()"方法应
   等同于使用"__floordiv__()"和"__mod__()";它不应该与"__truediv__()"相关.请注意,如
   果要支持内置"pow()"函数的三元版本,则应将"__pow__()"定义为接受可选的第三个参数.

   如果其中一个方法不支持带有提供参数的操作,则应返回"NotImplemented".

object.__radd__(self, other)                +            
object.__rsub__(self, other)                -                
object.__rmul__(self, other)                *
object.__rmatmul__(self, other)             @
object.__rtruediv__(self, other)            /
object.__rfloordiv__(self, other)           //
object.__rmod__(self, other)                %
object.__rdivmod__(self, other)             divmod()
object.__rpow__(self, other[, modulo])      **
object.__rlshift__(self, other)             <<
object.__rrshift__(self, other)             >>
object.__rand__(self, other)                &
object.__rxor__(self, other)                ^
object.__ror__(self, other)                 |

   调用这些方法是为了实现具有反射(swapped(交换))操作数的二进制算术运算("+", "-", "*",
   "@", "/", "//", "%", "divmod()","pow()", "**", "<<", ">>", "&", "^", "|").
   仅当左操作数不支持相应的操作且操作数类型不同时,才会调用这些函数.例如,要计算表达式
   "x - y",其中*y*是具有"__rsub__()"方法的类的实例,如果"x.__sub__(y)"返回
   *NotImplemented*,则调用"y.__rsub__(x)".

   请注意,三元"pow()"不会尝试调用"__rpow__()"(强制规则将变得太复杂).

   Note:

     如果右操作数的类型是左操作数类型的子类,并且该子类为操作提供了反射方法的不同实现,则将
     在左操作数的非反射方法之前调用此方法.此行为允许子类重写其祖先的操作.

object.__iadd__(self, other)                +=
object.__isub__(self, other)                -=
object.__imul__(self, other)                *=
object.__imatmul__(self, other)             @=
object.__itruediv__(self, other)            /=
object.__ifloordiv__(self, other)           //=
object.__imod__(self, other)                %=
object.__ipow__(self, other[, modulo])      **=
object.__ilshift__(self, other)             <<=
object.__irshift__(self, other)             >>=
object.__iand__(self, other)                &=
object.__ixor__(self, other)                ^=
object.__ior__(self, other)                 |=

   调用这些方法来实现增广算术赋值("+=", "-=", "*=", "@=", "/=", "//=", "%=", "**=",
   "<<=", ">>=", "&=", "^=", "|=").这些方法应该尝试就地执行操作(修改*self*)并返回结
   果(可能是但不一定是*self*).如果未定义特定的方法,则扩充赋值将返回到正常方法.例如,如果
   *x*是具有"__iadd__()"方法的类的实例,"x += y"相当于"x = x.__iadd__(y)".否则,与
   "x + y"的评估一样,将考虑"x.__add__(y)"和"y.__radd__(x)".在某些情况下,扩充赋值可能
   会导致意外错误,但这种行为实际上是数据模型的一部分.

   Note:

     由于"**="的调度机制中存在错误,定义"__ipow__()"但返回"NotImplemented"
     的类将无法返回到"x.__pow__(y)"和"y.__rpow__(x)".Python 3.10中修
     复了此错误.

object.__neg__(self)        -
object.__pos__(self)        +
object.__abs__(self)        abs()
object.__invert__(self)     ~

   调用以实现一元算术运算("-", "+","abs()" and "~").

object.__complex__(self)        complex()
object.__int__(self)            int()
object.__float__(self)          float()

   调用以实现内置函数"complex()"、"int()"和"float()".应返回适当类型的值.

object.__index__(self)          operator.index()

   调用以实现"operator.index()",并且每当Python需要无损地将数值对象转换为整数对象时(例
   如在切片中,或在内置的"bin()"、"hex()"和"oct()"函数中).存在此方法表示数值对象是整数
   类型.必须返回一个整数.

   如果未定义"__int__()"、"__float__()"和"__complex__()",则相应的内置函数"int()"、
   "float()"和"complex()"将返回到"__index__()".

object.__round__(self[, ndigits])       round()
object.__trunc__(self)                  trunc()
object.__floor__(self)                  floor()
object.__ceil__(self)                   ceil()

   调用以实现内置函数"round()"和math函数"trunc()"、"floor()"和"ceil()".除非将
   *ndigits*传递给"__round__()",否则所有这些方法都应将对象的值截断为"整数"(通常为"int
   ").

   如果未定义"__int__()",则内置函数"int()"返回到"__trunc__()".
"""
"""
# UNICODE,STRINGS

字符串和字节字面常量

字符串字面常量由以下词汇定义描述:

   stringliteral   ::= [stringprefix](shortstring  longstring)
   stringprefix    ::= "r"  "u"  "R"  "U"  "f"  "F"  "fr"  "Fr"  "fR" 
                                             "FR"  "rf"  "rF"  "Rf"  "RF"
   shortstring     ::= "'" shortstringitem* "'"  '"' shortstringitem* '"'
   longstring      ::= "'''" longstringitem* "'''" 
                                                   '"""' longstringitem* '"""'
   shortstringitem ::= shortstringchar  stringescapeseq
   longstringitem  ::= longstringchar  stringescapeseq
   shortstringchar ::= <任何源字符,除了 "\" or newline or the quote>
   longstringchar  ::= <任何源字符,除了"\">
   stringescapeseq ::= "\" <任何源字符>

    注释:
       stringliteral:字符串字面常量
       stringprefix:字符串前缀
       shortstring:短字符串
       longstring:长字符串
       shortstringitem:短字符串项目
       longstringitem:长字符串项目
       shortstringchar:短字符串字符
       stringescapeseq:字符串转义序列
       longstringchar:长字符串字符
       quote:引用

   bytesliteral   ::= bytesprefix(shortbytes  longbytes)
   bytesprefix    ::= "b"  "B"  "br"  "Br"  "bR"  "BR"  "rb"  "rB" 
                                                                   "Rb"  "RB"
   shortbytes     ::= "'" shortbytesitem* "'"  '"' shortbytesitem* '"'
   longbytes      ::= "'''" longbytesitem* "'''"  '"""' longbytesitem* '"""'
   shortbytesitem ::= shortbyteschar  bytesescapeseq
   longbytesitem  ::= longbyteschar  bytesescapeseq
   shortbyteschar ::= <任何ASCII字符,除了 "\" or newline or the quote>
   longbyteschar  ::= <任何ASCII字符,除了"\">
   bytesescapeseq ::= "\" <任何ASCII字符>

    注释:
        bytesliteral:字节字面常量
        bytesprefix:字节前缀
        shortbytes:短字节
        longbytes:长字节
        shortbytesitem:短字节项目
        longbytesitem:长字节项目
        shortbyteschar:短字节字符
        longbyteschar:长字节字符
        bytesescapeseq:字节转义序列

这些结果没有指出的一个语法限制是,"stringprefix"或"bytesprefix"与字面常量的其余部分之间
不允许有空格.源字符集由编码声明定义;如果源文件中没有给出编码声明,则为UTF-8;

在纯英语中:这两种类型的文字都可以用匹配的单引号(')或双引号(")括起来.它们也可以用三个单引
号或双引号(通常称为*三引号字符串*)的匹配组括起来.反斜杠(\)字符用于转义具有特殊含义的字符,
例如换行符、反斜杠本身或引号字符.

字节字面常量总是以'b'或'B'作为前缀;它们生成"bytes"类型而不是"str"类型的实例.它们只能包
含ASCII字符;数值大于等于128的字节必须用转义符表示.

字符串和字节字面常量都可以选择前缀字母'r'"或'R';此类字符串称为*raw strings(原始字符串)*
,并将反斜杠视为字面常量字符.因此,在字符串字面常量中,未处理原始字符串中的'\U'和'\u'转义.
由于Python2.x的原始unicode字面常量与Python3.x的行为不同,因此不支持'ur'语法.

版本3.3中新增:原始字节字面常量的'rb'前缀已添加为'br'的同义词.
版本3.3中的新功能:重新引入了对unicode遗留字面常量("u'value'")的支持,以简化Python 2.x
和3.x双代码基的维护.

前缀中带有'f'或'F'的字符串文字是*formatted string literal(格式的字符串字面常量)*;'f'
可以与'r'组合,但不能与'b'或'u'组合,因此可以使用原始格式化字符串,但不能使用格式化字节字面
常量.

在三重引号的字面常量中,允许(并保留)不带换行符的换行符和引号,但以行中的三个不带换行符的引号
终止字面常量.(引号是用于打开字面常量的字符,即'或")

除非有'r'或'R'前缀,否则字符串和字节字面常量中的转义序列将根据与标准C使用的规则类似的规则
进行解释.识别的转义序列为:

 Escape Sequence(转义字符)     Meaning(含义)                               Notes   
-------------------------------------------------------------------------------
 "\newline"                 忽略反斜杠和换行符              
-------------------------------------------------------------------------------
 "\\"                       Backslash(反斜杠)(\)                            
-------------------------------------------------------------------------------
 "\'"                       Single quote(单引号)(')                         
-------------------------------------------------------------------------------
 "\""                       Double quote(双引号)(")
-------------------------------------------------------------------------------
 "\a"                       ASCII Bell(ASCII钟)(BEL)
-------------------------------------------------------------------------------
 "\b"                       ASCII Backspace(ASCII退格)(BS)
-------------------------------------------------------------------------------
 "\f"                       ASCII Formfeed(ASCII格式提要)(FF)
-------------------------------------------------------------------------------
 "\n"                       ASCII Linefeed(ASCII换行符)(LF)
-------------------------------------------------------------------------------
 "\r"                       ASCII Carriage Return(ASCII回车)(CR)
-------------------------------------------------------------------------------
 "\t"                       ASCII Horizontal Tab(ASCII水平制表符)(TAB)
-------------------------------------------------------------------------------
 "\v"                       ASCII Vertical Tab(ASCII垂直制表符)(VT)
-------------------------------------------------------------------------------
 "\ooo"                     八进制值为*ooo*的字符                           (1,3)
-------------------------------------------------------------------------------
 "\xhh"                     十六进制值为*hh*的字符                          (2,3)

仅在字符串字面常量中识别的转义序列为:

 Escape Sequence(转义字符)     Meaning(含义)                               Notes   
-------------------------------------------------------------------------------
 "\N{name}"                  Unicode数据库中名为*name*的字符                  (4)
-------------------------------------------------------------------------------
 "\uxxxx"                    具有16位十六进制值*xxxx*的字符                    (5)
-------------------------------------------------------------------------------
 "\Uxxxxxxxx"                具有32位十六进制值*xxxxxxxx*的字符                (6)

Notes:

1.与标准C一样,最多可接受三个八进制数字.
2.与标准C不同,只需要两个十六进制数字.
3.在字节文字中,十六进制和八进制转义表示具有给定值的字节.在字符串文字中,这些转义表示具有给
  定值的Unicode字符.
4.在版本3.3中更改:添加了对名称别名的支持.
5.只需要四个十六进制数字.
6.任何Unicode字符都可以这样编码.只需要八个十六进制数字.

与标准C不同,所有无法识别的转义序列都保留在字符串中不变,即,*反斜杠保留在结果中*.(此行为在
调试时非常有用:如果转义序列输入错误,则结果输出更容易被识别为已中断.)还需要注意的是,仅在字
符串字面常量中识别的转义序列属于字节字面常量的未识别转义类别.

   在版本3.6中更改:无法识别的转义序列会产生"DeprecationWarning".在未来的Python版本中,
   它们将成为"SyntaxWarning",最终成为"SyntaxError".

即使在原始字面常量中,引号也可以用反斜杠转义,但反斜杠仍保留在结果中;例如,r"\""是由两个字符
组成的有效字符串字面常量:反斜杠和双引号;r"\"不是有效的字符串文字(即使是原始字符串也不能以
奇数个反斜杠结尾).具体来说,*原始文字不能以单个反斜杠结尾*(因为反斜杠将转义以下引号字符).
还要注意,后跟换行符的单个反斜杠被解释为这两个字符作为文字的一部分,*not*作为行的延续.
"""
"""
# SEQUENCEMETHODS,MAPPINGMETHODS

模拟容器类型

可以定义以下方法来实现容器对象.容器通常是序列(如列表或元组)或映射(如字典),但也可以表示其
他容器.第一组方法用于模拟序列或模拟映射;不同之处在于,对于序列,允许的键应该是整数*k*,其中
"0 <= k < N",其中*N*是序列的长度,或者是定义项目范围的切片对象.还建议映射提供方法
"keys()"、"values()"、"items()"、"get()"、"clear()"、"setdefault()"、"pop()"、
"popitem()"、"copy()"、和"update()",其行为类似于Python的标准字典对象.
"collections.abc"模块提供了一个"MutableMapping"抽象基类,以帮助从"__getitem__()"、
"__setitem__()"、"__delitem__()"和"keys()"的基集中创建这些方法.可变序列应该提供方法
"append()"、"count()"、"index()"、"extend()"、"insert()"、"pop()"、"remove()"、
"reverse()"和"sort()",就像Python标准列表对象一样.最后,序列类型应该通过定义下面描述的方
法"__add__()"、"__radd__()"、"__iadd__()"、"__mul__()"、"__rmul__()"和
"__imul__()",来实现加法(意思是串联)和乘法(意思是重复);它们不应定义其他数值运算符.建议映
射和序列都实现"__contains__()"方法,以允许有效使用"in"运算符;对于映射,"in"应该搜索映射
的键;对于序列,它应该搜索所有值.进一步建议映射和序列都实现"__iter__()"方法,以允许通过容器
进行有效迭代;对于映射,"__iter__()"应该迭代对象的键;对于序列,它应该遍历这些值.

object.__len__(self)

   调用以实现内置函数"len()".应返回对象的长度,一个整数">="0.此外,在布尔上下文中,未定义
   "__bool__()"方法且其"__len__()"方法返回零的对象被视为false.

   **CPython实现细节:**在CPython中,长度要求最多为"sys.maxsize".如果长度大于
   "sys.maxsize",则某些功能(如"len()")可能会引发"OverflowError".为了防止通过真值测试
   引发"OverflowError",对象必须定义一个"__bool__()"方法.

object.__length_hint__(self)

   调用以实现"operator.length_hint()".应返回对象的估计长度(可能大于或小于实际长度).长
   度必须为整数">="0.返回值也可以是"NotImplemented",这与"__length_hint__"方法根本不
   存在一样.这种方法纯粹是一种优化,不需要正确性.

   3.4版中的新版本.

object.__getitem__(self, key)

   调用以实现对"self[key]"的评估.对于序列类型,接受的键应该是整数和切片对象.请注意,负索
   引的特殊解释(如果类希望模拟序列类型)取决于"__getitem__()"方法.如果*key(键)*的类型不
   合适,可能会引发"TypeError";如果某个值超出序列的索引集(在对负值进行任何特殊解释之后),
   则应引发"IndexError".对于映射类型,如果缺少*key*(不在容器中),则应引发"KeyError".

   Note:

     "for"循环期望为非法索引引发一个"IndexError",以允许正确检测序列的结尾.

object.__setitem__(self, key, value)

   调用以实现对"self[key]"的赋值.与"__getitem__()"的注释相同.如果对象支持更改键的值,
   或者如果可以添加新键,或者如果可以替换元素,则只能对映射实现此操作.对于不正确的*key*值,
   应引发与"__getitem__()"方法相同的异常.

object.__delitem__(self, key)

   调用以实现删除"self[key]".与"__getitem__()"的注释相同.仅当对象支持删除键时,才应为
   映射实现此功能;如果可以从序列中删除元素,则应为序列实现此功能.对于不正确的*key*值,应引
   发与"__getitem__()"方法相同的异常.

object.__missing__(self, key)

   由"dict"调用"__getitem__()"以在键不在字典中时为dict子类实现"self[key]".

object.__iter__(self)

   当容器需要迭代器时,调用此方法.这个方法应该返回一个新的迭代器对象,它可以遍历容器中的所
   有对象.对于映射,它应该迭代容器的键.

   迭代器对象也需要实现这个方法;他们必须自己返回.

object.__reversed__(self)

   由内置的"reversed()"调用(如果存在)以实现反向迭代.它应该返回一个新的迭代器对象,该对象
   以相反的顺序遍历容器中的所有对象.

   如果未提供"__reversed__()"方法,则内置的"reversed()"将退回到使用序列协议
   ("__len__()"和"__getitem__()").如果支持序列协议的对象能够提供比"reversed()"提供的
   实现更高效的实现,则它们只应提供"__reversed__()".

    成员资格测试操作符("in"和"not in")通常作为通过容器的迭代来实现.但是,容器对象可以为
    以下特殊方法提供更高效的实现,这也不要求对象是可移植的.

object.__contains__(self, item)

   调用以实现成员资格测试操作符.如果*item*在*self*中,则应返回true,否则返回false.对于映
   射对象,应考虑映射的键,而不是值或键项对.

   对于未定义"__contains__()"的对象,成员资格测试首先通过"__iter__()"尝试迭代,然后通过
   "__getitem__()"尝试旧序列迭代协议.
"""
"""
# ATTRIBUTEMETHODS

自定义属性访问
============

可以定义以下方法来自定义,类实例的属性访问(使用、分配或删除"x.name")的含义.

object.__getattr__(self, name)
   当默认属性访问失败且出现"AttributeError"(由于*name*不是实例属性或类树中"self"的属
   性,"__getattribute__()"引发"AttributeError";或者*name*属性的"__get__()"引发
   "AttributeError")时调用.此方法应返回属性值或引发"AttributeError"异常.

   请注意,如果通过正常机制找到该属性,则不会调用"__getattr__()".(这是"__getattr__()"和
   "__setattr__()"之间有意的不对称)这样做是出于效率原因,也是因为否则"__getattr__()"将
   无法访问实例的其他属性.请注意,至少对于实例变量,您可以通过不在实例属性字典中插入任何值(
   而是在另一个对象中插入值)来伪造完全控制.

object.__getattribute__(self, name)

   无条件调用以实现类实例的属性访问.如果该类还定义了"__getattr__()",则后者将不会被调用,
   除非"__getattribute__()"显式调用它或引发"AttributeError".此方法应返回属性值或引发
   "AttributeError"异常.为了避免此方法中的无限递归,它的实现应该始终使用相同的名称调用基
   类方法来访问它所需的任何属性,例如,"object.__getattribute__(self, name)".

   Note:
     当通过语言语法或内置函数进行隐式调用后查找特殊方法时,仍然可以忽略此方法.

   对于某些敏感属性访问,引发一个审核事件"object.__getattr__",参数为"obj"和"name".

object.__setattr__(self, name, value)

   在尝试属性分配时调用.调用它而不是调用正常机制(即,将值存储在实例字典中)*name*是属性名,
   *value*是要分配给它的值.

   如果"__setattr__()"想要分配给实例属性,它应该使用相同的名称调用基类方法,例如
   "object.__setattr__(self, name, value)".

   对于某些敏感属性分配,引发一个审核事件"object.__setattr__",其中包含参数"obj"、
   "name"、"value".

object.__delattr__(self, name)

   与"__setattr__()"类似,但用于属性删除而不是赋值.仅当"del obj.name"对对象有意义时,才
   应实现此操作.

   对于某些敏感属性删除,将引发一个审核事件"object.__delattr__",其中包含参数"obj"和
   "name".

object.__dir__(self)

   在对象上调用"dir()"时调用.必须返回一个序列."dir()"将返回的序列转换为列表并对其进行排
   序.

自定义模块属性访问
================

特殊名称"__getattr__"和"__dir__"也可用于自定义对模块属性的访问.模块级的"__getattr__"
函数应接受一个作为属性名称的参数,并返回计算值或引发"AttributeError".如果通过正常查找在
模块对象上未找到属性,即"object.__getattribute__()",然后在引发"AttributeError"之前,
在模块"__dict__"中搜索"__getattr__".如果找到,将使用属性名调用它,并返回结果.

"__dir__"函数不应接受任何参数,并返回表示模块上可访问名称的字符串序列.如果存在,此函数将覆
盖模块上的标准"dir()"搜索.

为了更细粒度地定制模块行为(设置属性、性质等),可以将模块对象的"__class__"属性设置为
"types.ModuleType"的子类.例如：

   import sys
   from types import ModuleType

   class VerboseModule(ModuleType):
       def __repr__(self):
           return f'Verbose {self.__name__}'

       def __setattr__(self, attr, value):
           print(f'Setting {attr}...')
           super().__setattr__(attr, value)

   sys.modules[__name__].__class__ = VerboseModule

Note:

  定义模块"__getattr__"和设置模块"__class__"仅影响使用属性访问语法进行的查找-直接访问
  模块全局(无论是通过模块内的代码还是通过引用模块的全局字典)不受影响.

  在版本3.5中更改:"__class__"模块属性现在可写.
  版本3.7中新增:"__getattr__"和"__dir__"模块属性.

实现描述符
=========

以下方法仅适用于包含该方法的类的实例(所谓的*descriptor*类)出现在*owner(所有者)*类中时(
描述符必须在所有者的类字典中或在其父类之一的类字典中).在下面的示例中,"the attribute"指
的是其名称是所有者类"__dict__"中属性的键的属性.

object.__get__(self, instance, owner=None)

   调用以获取所有者类的属性(类属性访问)或该类的实例的属性(实例属性访问).可选的*owner*参
   数是所有者类,而*instance*是通过该属性访问的实例,当通过*owner*访问该属性时instance值
   为"None".

   此方法应返回计算的属性值或引发"AttributeError"异常.

object.__set__(self, instance, value)

   调用以将所有者类的实例*instance*上的属性设置为新值*value*.

   注意,添加"__set__()"或"__delete__()"会将描述符的类型更改为"data descriptor(数据
   描述符)".

object.__delete__(self, instance)

   调用以删除所有者类的实例*instance*上的属性.

object.__set_name__(self, owner, name)

   在创建所属类*owner*时调用.描述符已分配给*name*.

   Note:

     "__set_name__()"仅作为"type"构造函数的一部分隐式调用,因此在初始创建后将描述符添加
     到类时,需要使用适当的参数显式调用它：

        class A:
           pass
        descr = custom_descriptor()
        A.attr = descr
        descr.__set_name__(A, 'attr')

"inspect"模块将属性"__objclass__"解释为指定定义此对象的类(适当地设置此属性有助于动态类
属性的运行时自省).对于可调用函数,它可能表示预期或需要给定类型(或子类)的实例作为第一个位置
参数(例如,CPython为在C中实现的未绑定方法设置此属性).

调用描述符
=========

通常,描述符是一个具有"binding behavior"的对象属性,其属性访问已被描述符协议中的方法覆盖:
"__get__()"、"__set__()"和"__delete__()".如果这些方法中的任何一个是为对象定义的,则称
之为描述符.

属性访问的默认行为是从对象的字典中获取、设置或删除属性.例如,"a.x"有一个查找链,从
"a.__dict__['x']"开始,然后是"type(a).__dict__['x']",然后是"type(a)"的基类,不包括元
类.

但是,如果查找的值是定义其中一个描述符方法的对象,那么Python可能会覆盖默认行为并调用描述符
方法.这种情况在优先级链中发生的位置取决于定义了哪些描述符方法以及如何调用它们.

描述符调用的起点是绑定"a.x".参数的组合方式取决于"a"：

直接调用
   最简单也是最不常见的调用是当用户代码直接调用描述符方法时:"x.__get__(a)".

实例绑定
   如果绑定到一个对象实例,"a.x"将转换为调用:
                                   "type(a).__dict__['x'].__get__(a, type(a))".

类绑定
   如果绑定到一个类,"A.x"将转换为调用:"A.__dict__['x'].__get__(None, A)".

超级绑定

    如果"a"是"super"的一个实例,那么绑定"super(B,obj).m()"将在
    "obj.__class__.__mro__"中搜索紧跟在"B"之前的基类"A",然后通过调用调用调用描述符:
    "A.__dict__['m'].__get__(obj, obj.__class__)".

对于实例绑定,描述符调用的优先级取决于定义的描述符方法.描述符可以定义"__get__()"、
"__set__()"和"__delete__()"的任意组合.如果未定义"__get__()",则访问该属性将返回描述符
对象本身,除非该对象的实例字典中有值.如果描述符定义了"__set__()"和/或"__delete__()",则
它是一个数据描述符;如果两者都没有定义,则它是非数据描述符.通常,数据描述符同时定义
"__get__()"和"__set__()",而非数据描述符只定义"__get__()"方法.定义了"__get__()"和
"__set__()"(和/或"__delete__()")的数据描述符始终覆盖实例字典中的重新定义.相反,非数据
描述符可以被实例覆盖.

Python方法(包括"staticmethod()"和"classmethod()")是作为非数据描述符实现的.因此,实例
可以重新定义和重写方法.这允许单个实例获取与同一类的其他实例不同的行为.

"property()"函数作为数据描述符实现.因此,实例不能重写属性的行为.

__slots__
=========

*__slots__*允许我们显式声明数据成员(如属性)并拒绝创建*__dict__*和*__weakref__*(除非在
*__slots__*中显式声明或在父级中可用.)

使用*__dict__*节省的空间可能很大.属性查找速度也可以显著提高.

object.__slots__

    可以为该类变量分配一个字符串、iterable或一系列字符串,这些字符串具有实例使用的变量名
    *__slots__*为声明的变量保留空间,并防止为每个实例自动创建*__dict__*和*__weakref__*

关于使用*__slots__*的注意事项
--------------------------

*从没有*__slots__*的类继承时,实例的*__dict__*和*__weakref__*属性将始终可访问.

*如果没有*__dict__*变量,则无法为实例分配未在*__slots__*定义中列出的新变量.尝试分配给未
 列出的变量名会引发"AttributeError".如果需要动态分配新变量,则在*__slots__*声明中的字符
 串序列中添加"'__dict__'".

*如果每个实例都没有一个*__weakref__*变量,那么定义*__slots__*的类就不支持对其实例的弱引
 用.如果需要弱引用支持,则在*__slots__*声明中的字符串序列中添加"'__weakref__'".

**__slots__*通过为每个变量名创建描述符(实现描述符)在类级别实现.因此,类属性不能用于设置由
 *__slots__*定义的实例变量的默认值;否则,class属性将覆盖描述符赋值.

**__slots__*声明的操作不限于定义它的类.父类中声明的*__slots__*在子类中可用.但是,子类将
 得到一个*__dict__*和*__weakref__*除非它们还定义了*__slots__*(它应该只包含任何
 *additional(附加)*插槽的名称).

*如果一个类定义了一个也在基类中定义的slot,则基类slot定义的实例变量是不可访问的(除非直接
 从基类检索其描述符).这使得程序的含义未定义.将来,可能会添加一个检查以防止出现这种情况.

*非空*__slots__*不适用于从"可变长度"内置类型(如"int"、"bytes"和"tuple")派生的类.

*任何非字符串iterable都可以分配给*__slots__*.也可以使用映射;然而,在将来,可以将特殊含义
 分配给对应于每个键的值.

**__class__*赋值仅在两个类具有相同的*__slots__*时有效.

*可以使用具有多个slot父类的多重继承,但只允许一个父类具有由slot创建的属性(其他基必须具有
 空的slot布局)-违反会引发"TypeError".

*如果一个迭代器用于*__slots__*,则为每个迭代器的值创建一个描述符.但是,*__slots__*属性将
 是一个空迭代器.
"""
"""
# AUGMENTEDASSIGNMENT

增广赋值语句

增广赋值是在单个语句中,二进制操作和赋值语句的组合:

   augmented_assignment_stmt ::= augtarget augop (expression_list 
                                                            | yield_expression)
   augtarget                 ::= identifier | attributeref | subscription 
                                                                     | slicing
   augop                     ::= "+=" | "-=" | "*=" | "@=" | "/=" | "//=" 
                            | "%=" | "**=" | ">>=" | "<<=" | "&=" | "^=" | "|="

扩充赋值计算目标(与普通赋值语句不同,目标不能是解包)和表达式列表,对两个操作数执行特定于赋值
类型的二进制运算,并将结果赋值给原始目标.目标仅评估一次.

像"x += 1"这样的增广赋值表达式可以重写为"x = x + 1",以获得类似但不完全相同的效果.在增强
版本中,"x"只计算一次.此外,在可能的情况下,实际操作是在原地执行的,这意味着不是创建新对象并
将其分配给目标,而是修改旧对象.

与普通赋值不同,增强赋值在计算右侧之前先计算左侧.例如,"a[i] += f(x)"首先查找"a[i]",然后
计算"f(x)"并执行加法,最后将结果写回"a[i]".

除了在一条语句中分配给元组和多个目标之外,由增广赋值语句完成的赋值与普通赋值的处理方式相同.
类似地,除了可能的*in-place*行为外,通过增广赋值执行的二进制操作与普通二进制操作相同.

对于作为属性引用的目标,关于类和实例属性的警告与常规赋值的警告相同.
"""
"""
# BASICMETHODS

基本定制

object.__new__(cls[, ...])

   调用以创建类*cls*的新实例."__new__()"是一个静态方法(有特殊的大小写,因此不需要声明它)
   ,它将请求实例的类作为其第一个参数.其余的参数是传递给对象构造函数表达式(类调用)的参数.
   "__new__()"的返回值应该是新对象实例(通常是*cls*的实例).

   典型的实现通过使用带有适当参数的"super().__new__(cls[, ...])"调用超类的"__new__()"
   方法,然后根据需要修改新创建的实例,然后返回它来创建类的新实例.

   如果在对象构造过程中调用"__new__()",并且它返回一个实例或*cls*的子类,那么新实例的
   "__init__()"方法将像"__init__(self[, ...])"一样被调用,其中*self*是新实例,其余参
   数与传递给对象构造函数的参数相同.

   如果"__new__()"未返回*cls*的实例,则不会调用新实例的"__init__()"方法.

   "__new__()"主要用于允许不可变类型的子类(如int、str或tuple)自定义实例创建.为了自定义
   类的创建,它通常在自定义元类中被重写.

object.__init__(self[, ...])

   在创建实例之后(由"__new__()")调用,但在实例返回给调用方之前调用.参数是传递给类构造函
   数表达式的参数.如果基类有一个"__init__()"方法,则派生类的"__init__()"方法(如果有)必
   须显式调用它,以确保实例的基类部分正确初始化;例如:"super().__init__([args...])".

   因为"__new__()"和"__init__()"在构造对象时一起工作("__new__()"创建对象,
   "__init__()"自定义对象),所以"__init__()"不能返回非"None"值;这样做将导致在运行时引
   发"TypeError".

object.__del__(self)

   当实例即将被销毁时调用.这也称为终结器或(不恰当地)析构函数.如果基类有一个"__del__()"
   方法,则派生类的"__del__()"方法(如果有)必须显式调用它,以确保正确删除实例的基类部分.

   "__del__()"方法可以(尽管不推荐！)通过创建对实例的新引用来推迟实例的销毁.这叫做物体复
   活.当复活的对象即将被销毁时,是否第二次调用"__del__()"取决于实现;当前的*CPython*实
   现只调用它一次.

   当解释器退出时,不能保证为仍然存在的对象调用"__del__()"方法.

   Note:

     "del x"不直接调用"x.__del__()"—前者将"x"的引用计数递减1,后者仅在"x"的引用计数达
     到零时调用.

   **CPython实现细节:**引用循环可以防止对象的引用计数变为零.在这种情况下,*循环垃圾收集
   器*稍后将检测并删除该循环.引用循环的一个常见原因是在局部变量中捕获异常.然后,帧的局部变
   量引用异常,该异常引用其自身的回溯,该回溯引用在回溯中捕获的所有帧的局部变量.

   Warning:

     由于调用"__del__()"方法的情况不稳定,在执行过程中发生的异常将被忽略,并在
     "sys.stderr"中显示一条警告.特别地:

    *在执行任意代码时,包括从任意线程执行任意代码时,可以调用"__del__()".如果"__del__()"
    需要获取锁或调用任何其他阻塞资源,它可能会死锁,因为该资源可能已被中断以执行"__del__()"
    的代码获取.

    *解释器关闭期间可以执行"__del__()".因此,它需要访问的全局变量(包括其他模块)可能已经
    被删除或设置为"None".Python保证在删除其他全局变量之前,从其模块中删除名称以单个下划
    线开头的全局变量;如果不存在对此类全局变量的其他引用,这可能有助于确保导入的模块在调用
    "__del__()"方法时仍然可用.

object.__repr__(self)

   由"repr()"内置函数调用,以计算对象的"official(正式)"字符串表示形式.如果可能的话,这应
   该看起来像一个有效的Python表达式,可以用来重新创建具有相同值的对象(给定适当的环境).如
   果这是不可能的,则应返回格式为"<...some useful description...>"的字符串.返回值必须
   是字符串对象.如果类定义了"__repr__()"而不是"__str__()",那么当需要该类实例的
   "informal(非正式)"字符串表示形式时,也会使用"__str__()".

   这通常用于调试,因此表示信息丰富且明确是很重要的.

object.__str__(self)

   由"str(object)"和内置函数"format()"和"print()"调用,以计算对象的"informal(非正式)"
   或可良好打印的字符串表示形式.返回值必须是字符串对象.

   此方法不同于"object.__repr__()",因为不期望"__str__()"返回有效的Python表达式:可以
   使用更方便或简洁的表示形式.

   由内置类型"object"定义的默认实现调用"object.__repr__()".

object.__bytes__(self)

   由字节调用以计算对象的字节字符串表示形式.这将返回一个"bytes(字节)"对象.

object.__format__(self, format_spec)

   由"format()"内置函数调用,并扩展为对格式化字符串文本的求值和"str.format()"方法,以生
   成对象的"formatted(格式化)"字符串表示形式.*format_spec*参数是一个字符串,包含所需格
   式选项的说明.*format_spec*参数的解释取决于实现"__format__()"的类型,但是大多数类要
   么将格式化委托给其中一个内置类型,要么使用类似的格式化选项语法.

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

   这些就是所谓的"rich comparison(丰富比较)"方法.运算符符号和方法名称之间的对应关系如下
   :"x<y"调用"x.__lt__(y)","x<=y"调用"x.__le__(y)","x==y"调用"x.__eq__(y)","x!=y"
   调用"x.__ne__(y)","x>y"调用"x.__gt__(y)","x>=y"调用"x.__ge__(y)".

   如果富比较方法没有实现给定参数对的操作,则它可能返回单例"NotImplemented".按照惯例,
   "False"和"True"将返回以进行成功比较.但是,这些方法可以返回任何值,因此如果在布尔上下文
   中使用比较运算符(例如,在"if"语句的条件下),Python将调用该值上的"bool()",以确定结果是
   真还是假.

   默认情况下,"object"通过使用"is"实现"__eq__()",在错误比较的情况下返回"NotImplemented"
   "True if x is y else NotImplemented".对于"__ne__()",默认情况下它将委托给
   "__eq__()",并反转结果,除非它是"NotImplemented(未实现的)".比较运算符或默认实现之间
   没有其他隐含关系;例如,"(x<y or x==y)"的真值并不意味着"x<=y".

   这些方法没有交换的参数版本(当左参数不支持该操作而右参数支持该操作时使用);相反,
   "__lt__()"和"__gt__()"是彼此的反映,"__le__()"和"__ne__()".如果操作数的类型不同,
   且右操作数的类型是左操作数类型的直接或间接子类,则右操作数的反射方法具有优先级,否则左操
   作数的方法具有优先级.不考虑虚拟子类化.

object.__hash__(self)

   由内置函数"hash()"调用,用于对散列集合的成员进行操作,包括"set"、"frozenset"和"dict".
   "__hash__()"应返回一个整数.唯一需要的属性是比较相等的对象具有相同的哈希值;建议通过将
   对象组件的哈希值打包到一个元组中并对元组进行哈希处理,将对象组件的哈希值混合在一起,这些
   组件也在对象的比较中发挥作用.例子:

      def __hash__(self):
          return hash((self.name, self.nick, self.color))

   Note:

     "hash()"将从对象的自定义"__hash__()"方法返回的值截断为"Py_ssize_t"大小.在64位构
     建中,这通常是8字节,在32位构建中是4字节.如果对象的"__hash__()"必须在不同位大小的生
     成上进行互操作,请确保检查所有支持的生成上的宽度.一个简单的方法是使用"python -c "导
     入sys;打印(系统哈希信息宽度)”.

   如果一个类没有定义一个"__eq__()"方法,那么它也不应该定义一个"__hash__()"操作;如果它
   定义了"__eq__()"而不是"__hash__()",则其实例将不能作为可哈希集合中的项使用.如果类定
   义可变对象并实现"__eq__()"方法,则不应实现"__hash__()",因为可散列集合的实现要求键的
   散列值是不可变的(如果对象的散列值更改,则它将位于错误的散列桶中).

   用户定义的类默认有"__eq__()"和"__hash__()"方法;使用它们,所有对象都比较不相等(除了它
   们自己),并且"x.__hash__()"返回一个适当的值,使得"x == y"意味着"x is y"和
   "hash(x) == hash(y)".

   重写"__eq__()"且未定义"__hash__()"的类将其"__hash__()"隐式设置为"None".当类的
   "__hash__()"方法为"__hash__()"时,当程序试图检索其哈希值时,该类的实例将引发相应的
   "TypeError",并且在检查"isinstance(obj,collections.abc.Hashable)"时,该类的实例也
   将被正确标识为不可损坏.

   如果重写"__eq__()"的类需要保留父类中"__hash__()"的实现,则必须通过设置
   "__hash__ =<ParentClass>.__hash__"来明确告知解释器这一点.

   如果未重写"__eq__()"的类希望抑制哈希支持,则应在类定义中包含"__hash__ = None".定义自
   己的"__hash__()"并显式引发"TypeError"的类将被
   "isinstance(obj, collections.abc.Hashable)"调用错误地标识为可哈希的.

   Note:

     默认情况下,str和bytes对象的"__hash__()"值用不可预测的随机值"salted".虽然它们在单
     个Python进程中保持不变,但在重复调用Python之间是不可预测的.这是为了提供保护,防止由
     于精心选择的输入导致的拒绝服务,这些输入利用了dict插入的最差性能,O(n^2)复杂性.更改哈
     希值会影响集合的迭代顺序.Python从未保证过这种排序(通常在32位和64位构建之间有所不同)

   在版本3.3中更改:默认情况下启用哈希随机化.

object.__bool__(self)

   调用以实现真值测试和内置操作"bool()";应该返回"False"或"True".未定义此方法时,如果已
   定义,则调用"__len__()",如果结果为非零,则认为该对象为真.如果一个类既不定义"__len__()"
   也不定义"__bool__()",则其所有实例都被视为true.
"""
"""
# break

"break"声明

   break_stmt ::= "break"

"break"只能在语法上嵌套在"for"或"while"循环中,而不能嵌套在该循环中的函数或类定义中.

它终止最近的封闭循环,如果循环有可选的"else"子句,则跳过该子句.

如果"for"循环被"break"终止,则循环控制目标保持其当前值.

当"break"将控制权从带有"finally"子句的"try"语句中传递出去时,"finally"子句将在真正离开
循环之前执行.
"""
"""
# continue

"continue" 声明

   continue_stmt ::= "continue"

"continue"只能在语法上嵌套在"for"或"while"循环中,而不能嵌套在该循环中的函数或类定义中.
它将继续最近的封闭循环的下一个循环.

当"continue"将控制权从带有"finally"子句的"try"语句中传递出去时,"finally"子句将在真正
开始下一个循环周期之前执行.
"""
"""
# CALLS

调用

调用调用具有一系列可能为空的*arguments*的可调用对象(例如,*function*):

   call                 ::= primary "(" [argument_list [","] |comprehension]")"
   argument_list        ::= positional_arguments ["," starred_and_keywords]
                                                       ["," keywords_arguments]
                                | starred_and_keywords ["," keywords_arguments]
                                                           | keywords_arguments
   positional_arguments ::= positional_item ("," positional_item)*
   positional_item      ::= assignment_expression | "*" expression
   starred_and_keywords ::= ("*" expression | keyword_item)
                                       ("," "*" expression | "," keyword_item)*
   keywords_arguments   ::= (keyword_item | "**" expression)
                                      ("," keyword_item | "," "**" expression)*
   keyword_item         ::= identifier "=" expression

位置参数和关键字参数后可能会出现可选的尾随逗号,但不会影响语义.

主对象必须求值为可调用对象(用户定义的函数、内置函数、内置对象的方法、类对象、类实例的方法
,以及所有具有"__call__()"方法的对象都是可调用的).在尝试调用之前,将对所有参数表达式求值.

如果存在关键字参数,则首先将它们转换为位置参数,如下所示.首先,为形式参数创建一个未填充插槽
列表.如果有N个位置参数,则将它们放置在前N个插槽中.接下来,对于每个关键字参数,标识符用于确定
相应的插槽(如果标识符与第一个正式参数名称相同,则使用第一个插槽,依此类推).如果插槽已填充,
则引发"TypeError"异常.否则,参数的值将放置在插槽中,并填充它(即使表达式为"None",也会填充
插槽).处理完所有参数后,仍未填充的插槽将填充函数定义中相应的默认值.(默认值在定义函数时计算
一次;因此,作为默认值使用的可变对象(如列表或字典)将由所有未为相应插槽指定参数值的调用共享;
通常应避免这种情况.)如果有未填充的插槽未指定默认值,则引发"TypeError"异常.否则,已填充插槽
的列表将用作调用的参数列表.

**CPython实现详细信息:**实现可能会提供内置函数,其位置参数没有名称,即使它们是为了文档目的
而命名的,因此不能通过关键字提供.在CPython中,在C中实现的函数使用"PyArg_ParseTuple()"解
析其参数就是这种情况.

如果位置参数多于形式参数槽,则会引发"TypeError"异常,除非存在使用语法"*标识符"的形式参数;
在本例中,该形式参数接收一个包含多余位置参数的元组(如果没有多余位置参数,则接收一个空元组).

如果任何关键字参数与形式参数名称不对应,则会引发"TypeError"异常,除非存在使用语法"**标识符
"的形式参数;在本例中,该形式参数接收一个包含多余关键字参数的字典(使用关键字作为键,参数值
作为对应值),或者如果没有多余关键字参数,则接收一个(新的)空字典.

如果函数调用中出现语法"*expression",则"expression"的计算结果必须为*iterable*.这些
iterable中的元素被视为附加的位置参数.对于调用"f(x1, x2, *y, x3, x4)",如果*y*计算为序
列*y1*, …, *yM*,这相当于使用M+4个位置参数*x1*, *x2*,*y1*, …, *yM*, *x3*, *x4*的调
用.

这样做的结果是,尽管"*expression"语法可能出现在显式关键字参数之后,但它是在关键字参数之前
处理的(以及任何"**expression"参数).因此:

   >>> def f(a, b):
   ...     print(a, b)
   ...
   >>> f(b=1, *(2,))
   2 1
   >>> f(a=1, *(2,))
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: f() got multiple values for keyword argument 'a'
   >>> f(1, *(2,))
   1 2

在同一个调用中使用关键字参数和"*expression"语法是不常见的,因此在实践中不会出现这种混淆.

如果函数调用中出现语法"**expression",则"expression"必须计算为*mapping*,其内容被视为附
加关键字参数.如果关键字已经存在(作为显式关键字参数,或来自另一个解包),则会引发"TypeError"
异常.

使用语法"*identifier(标识符)"或"**identifier(标识符)"的形式参数不能用作位置参数slots
或关键字参数名称.

在版本3.5中更改:函数调用接受任意数量的"*"和"**"解包,位置参数可以跟在iterable解包("*")
之后,关键字参数可以跟在dictionary解包("**")之后.

调用总是返回一些值,可能是"None",除非它引发异常.该值的计算方式取决于可调用对象的类型.

如果是-

用户定义的函数:
   执行函数的代码块,并将参数列表传递给它.代码块要做的第一件事是将形式参数绑定到参数;当代
   码块执行"return"语句时,它指定函数调用的返回值.

内置函数或方法:
   结果由解释程序决定;

类对象:
    将返回该类的新实例.

类实例方法:
    调用相应的用户定义函数,参数列表比调用的参数列表长一个:实例成为第一个参数.

类实例:
    类必须定义一个"__call__()"方法;其效果与调用该方法的效果相同.
"""
"""
# COMPARISON,is

比较

与C不同,Python中的所有比较操作都具有相同的优先级,比任何算术、移位或按位操作的优先级都低.
同样与C不同的是,"a < b < c"等表达式具有数学中的常规解释:

   comparison    ::= or_expr (comp_operator or_expr)*
   comp_operator ::= "<" | ">" | "==" | ">=" | "<=" | "!=" | "is" ["not"]
                                                                 | ["not"] "in"

比较产生布尔值:"True"或"False".

可以任意链接比较,例如,"x < y <= z"等同于"x < y and y <= z",但"y"仅计算一次(但在这两
种情况下,当发现"x < y"为假时,根本不计算"z").

形式上,如果*a*、*b*、*c*、 … 、*y*、*z*是表达式,*op1*、*op2*、 … 、*opN*是比较运算符,
那么"a op1 b op2 c ... y opN z"等同于"a op1 b and b op2 c and ... y opN z",只是
每个表达式最多计算一次.

请注意,"a op1 b op2 c"并不意味着*a*和*c*之间有任何类型的比较,因此,例如,"x < y > z"是
完全合法的(尽管可能并不漂亮).

价值比较
=======

运算符"<"、">"、"=="、">="、"<="和"!="比较两个对象的值.对象不需要具有相同的类型.

对象、值和类型一章指出对象具有值(除类型和标识外).在Python中,对象的值是一个相当抽象的概念:
例如,对象的值没有规范的访问方法.此外,不要求以特定方式构造对象的值,例如,由其所有数据属性组
成.比较运算符实现对象值的特定概念.可以将它们看作是通过比较实现间接定义对象的值.

因为所有类型都是"object"的(直接或间接)子类型,所以它们继承了"object"的默认比较行为.类型
可以通过实现*rich comparison methods*(如"__lt__()")来自定义其比较行为,如基本自定义中
所述.

相等比较("==" and "!=")的默认行为基于对象的标识.因此,具有相同身份的实例的平等性比较导致
平等,而具有不同身份的实例的平等性比较导致不平等.这种默认行为的动机是希望所有对象都是自反
的(即"x is y"意味着"x == y").

未提供默认顺序比较("<"、">"、"<="和">=");尝试将引发"TypeError".这种默认行为的一个动机
是缺少与相等类似的不变量.

默认相等比较的行为,即具有不同标识的实例总是不相等的,可能与需要对对象值和基于值的相等进行合
理定义的类型形成对比.这样的类型将需要定制它们的比较行为,事实上,许多内置类型已经做到了这一
点.

下面的列表描述了最重要的内置类型的比较行为.

*内置数字类型(数字类型-int、float、complex)和标准库类型"fractions.Fraction"和
 "decimal.Decimal"的数量可以在其类型内和类型之间进行比较,但限制是复数不支持顺序比较.在
 所涉及类型的限制范围内,他们在不损失精度的情况下进行数学(algorithmically(算法))正确的比
 较.

  非数字值"float('NaN')"和"decimal.Decimal('NaN')"是特殊的.数字与非数字值的任何有
  序比较都是错误的.一个反直觉的含义是非数字值不等于它们本身.例如,如果"x = float('NaN')"
  、"3 < x"、"x < 3"和"x == x"都为false,而"x != x"为true.此行为符合IEEE 754.

*"None"和"NotImplemented"是单例**PEP 8**建议,单例的比较应始终使用"is"或"is not",而不
 要使用相等运算符.

*二进制序列("bytes"或"bytearray"的实例)可以在其类型内和类型之间进行比较.他们使用元素的
 数字值按字典顺序进行比较.

*字符串("str"的实例)使用其字符的数字Unicode代码点(内置函数"ord()"的结果)按字典顺序进行
 比较.

 字符串和二进制序列不能直接比较.

*序列("tuple"、"list"或"range"的实例)只能在它们的每种类型内进行比较,限制是范围不支持
 顺序比较.在这些类型之间进行相等比较会导致不相等,而在这些类型之间进行排序比较会引发
 "TypeError".

  序列使用对应元素的比较按字典顺序进行比较.内置容器通常假定相同的对象等于它们自己.这使它
  们能够绕过相同对象的相等性测试,以提高性能并保持其内部不变量.

  内置集合之间的字典比较工作如下:

  *对于要比较相等的两个集合,它们必须具有相同的类型,具有相同的长度,并且每对对应的元素必
   须比较相等(例如,"[1,2] == (1,2)"为false,因为类型不同).

  *支持顺序比较的集合的顺序与其第一个不相等元素相同(例如,"[1,2,x] <= [1,2,y]"的值与
   "x <= y")的值相同.如果对应的元素不存在,则首先排序较短的集合(例如,"[1,2] < [1,2,3]"
   为true).

*映射(dict的实例)当且仅当它们具有相等*(key, value)*对时比较相等.键和值的相等比较加强了
 自反性.

  订单比较("<"、">"、"<="和">=")会引发"TypeError".

*集合("set"或"frozenset"的实例)可以在其类型内和类型之间进行比较.

  它们定义了顺序比较运算符来表示子集和超集测试.这些关系不定义总排序(例如,两个集合"{1,2}"
  和"{2,3}"不相等,也不是彼此的子集,也不是彼此的超集).因此,对于依赖于总排序的函数而言,集
  合不是合适的参数(例如,"min()"、"max()"和"sorted()",如果将集合列表作为输入,则会产生未
  定义的结果).

  集合的比较加强了其元素的自反性.

*大多数其他内置类型没有实现比较方法,因此它们继承默认比较行为.

如果可能,自定义比较行为的用户定义类应遵循一些一致性规则:

*相等比较应该是自反的.换句话说,相同的对象应该比较相等:

     "x is y" implies "x == y"

*比较应该是对称的.换句话说,以下表达式应具有相同的结果:

     "x == y" and "y == x"

     "x != y" and "y != x"

     "x < y" and "y > x"

     "x <= y" and "y >= x"

*比较应该是传递性的.以下((non-exhaustive(非详尽))示例说明:

     "x > y and y > z" implies "x > z"

     "x < y and y <= z" implies "x < z"

*反向比较应导致布尔否定.换句话说,以下表达式应具有相同的结果:

     "x == y" and "not x != y"

     "x < y" and "not x >= y" (for total ordering)

     "x > y" and "not x <= y" (for total ordering)

  最后两个表达式适用于完全有序的集合(例如,适用于序列,但不适用于集合或映射).

*"hash()"结果应与等式一致.相等的对象应该具有相同的哈希值,或者标记为不可损坏.

Python不强制执行这些一致性规则.事实上,not-a-number值就是不遵循这些规则的一个例子.

成员资格测试操作
==============

操作符"in"和"not in"测试成员资格.如果*x*是*s*的成员,"x in s"计算为"True",否则为"False
"."x not in s"返回"x in s"的否定.所有内置序列和集合类型都支持此功能,字典也支持此功能,
"in"测试字典是否具有给定的键.对于容器类型,如list、tuple、set、frozenset、dict或
collections.deque,表达式"x in y"相当于"any(x is e or x == e for e in y)".

对于字符串和字节类型,当且仅当*x*是*y*的子字符串时,"x in y"为"True".等效测试为
"y.find(x) != -1".空字符串始终被视为任何其他字符串的子字符串,因此'' in "abc"将返回
"True".

对于定义"__contains__()"方法的用户定义类,如果"y.__contains__(x)"返回真值,则"y in x"
返回"True",否则返回"False".

对于不定义"__contains__()"但定义"__iter__()"的用户定义类,如果在"y"上迭代时生成表达式
"x is z or x == z"为真的某个值"z",则"x in y"为"True".如果在迭代过程中引发异常,就好像
"in"引发了该异常.

最后,尝试了旧式的迭代协议:如果类定义了"__getitem__()","x in y"是"True",当且仅当存在一
个非负整数索引*i*,即"x is y[i] or x == y[i]",并且没有较低的整数索引会引发"IndexError"
异常.(如果引发任何其他异常,则如同"in"引发了该异常).

运算符"not in"定义为具有逆真值"in".

身份比较
=======

运算符"is"和"is not"测试对象的标识:"x is y"为真,当且仅当*x*和*y*是同一对象时.使用
"id()"函数确定对象的标识."x is not y"产生相反的真值.
"""
"""
# DICTIONARIES,MAPPINGS

映射类型 — "dict"

*mapping*对象将*hashable*值映射到任意对象.映射是可变对象.目前只有一种标准映射类型*字典*

字典的键是*almost*任意值.不可*hashable*的值,即包含列表、字典或其他可变类型(通过值而不是
对象标识进行比较)的值,不能用作键.用于键的数字类型遵循数字比较的正常规则:如果两个数字比较相
等(如"1"和"1.0"),则可以互换使用它们来索引相同的词典条目.(但是请注意,由于计算机将浮点数存
储为近似值,因此将它们用作字典键通常是不明智的.)

字典可以通过在大括号内放置逗号分隔的"key:value"对列表来创建,例如:"{jack':4098,
'sjoerd':4127}"或"{4098:'jack',4127:'sjoerd'}",或通过"dict"构造函数来创建.

class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)

    返回从可选位置参数和一组可能为空的关键字参数初始化的新词典.
    可以通过以下几种方式创建词典:

    *在大括号内使用逗号分隔的"key:value"对列表:"{jack':4098,'sjoerd':4127}"或
     "{4098:'jack',4127:'sjoerd'}"

    *使用字典理解:"{}","{x: x ** 2 for x in range(10)}"

    *使用类型构造函数:"dict()","dict([('foo',100),('bar',200)]",
     "dict(foo=100,bar=200)"

   如果没有给出位置参数,将创建一个空字典.如果给定一个位置参数,并且它是一个映射对象,则将创
   建一个字典,其中包含与映射对象相同的键值对.否则,位置参数必须是*iterable*对象.iterable
   中的每个项本身必须是一个具有两个对象的iterable.每个项的第一个对象成为新字典中的键,第
   二个对象成为相应的值.如果某个键出现多次,则该键的最后一个值将成为新字典中的对应值.

   如果给定了关键字参数,则关键字参数及其值将添加到从位置参数创建的词典中.如果已存在要添加
   的键,则关键字参数中的值将替换位置参数中的值.

   为了举例说明,以下示例都返回一个等于"{"one": 1, "two": 2, "three": 3}"的字典:

      >>> a = dict(one=1, two=2, three=3)
      >>> b = {'one': 1, 'two': 2, 'three': 3}
      >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
      >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
      >>> e = dict({'three': 3, 'one': 1, 'two': 2})
      >>> f = dict({'one': 1, 'three': 3}, two=2)
      >>> a == b == c == d == e == f
      True

   在第一个示例中提供关键字参数仅适用于有效Python标识符的键.否则,可以使用任何有效keys.

   这些是字典支持的操作(因此,自定义映射类型也应该支持):

   list(d)

      返回字典*d*中使用的所有键的列表.

   len(d)

      返回字典*d*中的项目数.

   d[key]

      返回键位*key*的*d*值.如果*key*不在映射中,则引发"KeyError".

      如果dict的子类定义了一个方法"__missing__()"并且*key*不存在,那么"d[key]"操作将
      以键*key*作为参数调用该方法.然后,"d[key]"操作返回或引发由"__missing__(key)"调
      用返回或引发的任何内容.没有其他操作或方法调用"__missing__()".如果未定义
      "__missing__()",则会引发"KeyError"."__missing__()"必须是一个方法；它不能是实
      例变量:

         >>> class Counter(dict):
         ...     def __missing__(self, key):
         ...         return 0
         >>> c = Counter()
         >>> c['red']
         0
         >>> c['red'] += 1
         >>> c['red']
         1

      上面的示例显示了"collections.Counter"的部分实现."collections.defaultdict"使
      用了另一个"__missing__"方法.

   d[key] = value

      将"d[key]"设置为*value*.

   del d[key]

      从*d*中删除"d[key]".如果*key*不在映射中,则引发"KeyError".

   key in d

      如果*d*有一个键*key*,则返回"True",否则返回"False".

   key not in d

      相当于"not key in d".

   iter(d)

      返回字典键上的迭代器.这是"iter(d.keys())"的快捷方式.

   clear()

      从字典中删除所有项.

   copy()

      返回字典的浅显副本.

   classmethod fromkeys(iterable[, value])

      创建一个新字典,其中键来自*iterable*,值设置为*value*.

ClassMethodFromKeys(iterable[,value])

      "fromkeys()"是一个返回新字典的类方法*value*默认为"None".所有的值都只引用一个实例
      ,所以将*value*作为一个可变对象(如空列表)通常没有意义.要获得不同的值,请使用dict理
      解.

   get(key[, default])

      如果字典中有*key*,则返回*key*的值,否则返回*default*.如果未给出*default*,则默认
      为"None",因此此方法不会引发"keyrerror".

   items()

      返回字典项("(key, value)"对)的新视图.

   keys()

      返回字典键的新视图.

   pop(key[, default])

      如果字典中有*key*,请将其删除并返回其值,否则返回*default*.如果未给出*default*,并
      且*key*不在字典中,则会引发"KeyError".

   popitem()

      从字典中删除并返回"(key, value)"对.对按后进先出的顺序返回.

      "popitem()"用于在字典上进行破坏性迭代,这在集合算法中经常使用.如果字典为空,调用
      "popitem()"将引发"KeyError".

      在版本3.7中更改:后进先出顺序现在得到保证.在以前的版本中,"popitem()"将返回任意
      key/value对.

   reversed(d)

      返回字典键上的反向迭代器.这是"reversed(d.keys())"的快捷方式.

      3.8版本新特性

   setdefault(key[, default])

      如果字典中有*key*,则返回其值.如果没有,则插入值为*default*的*key*,并返回
      *default*.*default*默认为"None".

   update([other])

      使用*other*中的key/value对更新字典,覆盖现有键.返回"None".

      "update()"接受另一个字典对象或key/value对的iterable(作为元组或其他长度为2的
      iterable).如果指定了关键字参数,则使用这些key/value对更新字典:"d.update(red=1,
      blue=2)".

   values()

      返回字典值的新视图.

      一个"dict.values()"视图与另一个视图之间的相等比较将始终返回"False".这也适用于将
      "dict.values()"与自身进行比较时:

         >>> d = {'a': 1}
         >>> d.values() == d.values()
         False

   d | other

      使用合并键和值*d*和*other*创建一个新字典,这两个值必须都是字典.当*d*和*other*共
      享keys时,*other*的值优先.

      3.9版本新特性

   d |= other

      使用*other*中的键和值更新字典*d*,这可能是key/value对的*mapping*或*iterable*.
      当*d*和*other*共享keys时,*other*的值优先.

      3.9版本新特性

   字典比较相等当且仅当它们具有相同的"(key,value)"对时(无论顺序如何).顺序比较('<'、
   '<='、'>='、'>')会引发"TypeError".

   字典保留插入顺序.请注意,更新keys不会影响顺序.删除后添加的键将插入末尾.

      >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
      >>> d
      {'one': 1, 'two': 2, 'three': 3, 'four': 4}
      >>> list(d)
      ['one', 'two', 'three', 'four']
      >>> list(d.values())
      [1, 2, 3, 4]
      >>> d["one"] = 42
      >>> d
      {'one': 42, 'two': 2, 'three': 3, 'four': 4}
      >>> del d["two"]
      >>> d["two"] = None
      >>> d
      {'one': 42, 'three': 3, 'four': 4, 'two': None}

   在版本3.7中更改:字典顺序保证为插入顺序.此行为是3.6中CPython的一个实现细节.

   字典和字典视图是可逆的.

      >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
      >>> d
      {'one': 1, 'two': 2, 'three': 3, 'four': 4}
      >>> list(reversed(d))
      ['four', 'three', 'two', 'one']
      >>> list(reversed(d.values()))
      [4, 3, 2, 1]
      >>> list(reversed(d.items()))
      [('four', 4), ('three', 3), ('two', 2), ('one', 1)]

   在版本3.8中更改:字典现在是可逆的.

See also:

  "types.MappingProxyType"可用于创建"dict"的只读视图。

字典视图对象
===========

"dict.keys()"、"dict.values()"和"dict.items()"返回的对象是*view objects*.它们提供
字典条目的动态视图,这意味着当字典更改时,视图会反映这些更改.

可以迭代字典视图以生成其各自的数据,并支持成员资格测试:

len(dictview)

   返回字典中的条目数.

iter(dictview)
    在字典中的键、值或项(表示为"(key,value)"的元组)上返回迭代器.

   键和值按插入顺序迭代.这允许使用"zip()": "pairs = zip(d.values(), d.keys())"
   创建"(value, key)"对.创建相同列表的另一种方法是
   "pairs = [(v, k) for (k, v) in d.items()]".

   在字典中添加或删除条目时迭代视图可能会引发"RuntimeError"或无法迭代所有条目.

   在版本3.7中更改:字典顺序保证为插入顺序.

x in dictview

   如果*x*位于基础字典的键、值或项中,则返回"True"(在后一种情况下,*x*应为"(key, value)"
   元组).

reversed(dictview)

   返回字典中键、值或项的反向迭代器.视图将按与插入相反的顺序迭代.

   在版本3.8中更改:字典视图现在是可逆的.

键视图是set-like的,因为它们的条目是唯一且可散列的.如果所有值都是可散列的,因此
"(key, value)"对是唯一且可散列的,那么items视图也是set-like.(由于条目通常不唯一,因此值
视图不被视为集合视图.)对于集合视图,为抽象基类"collections.abc.set"定义的所有操作都可用
(例如,"=="、"<"或"^").

字典视图用法示例:

   >>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
   >>> keys = dishes.keys()
   >>> values = dishes.values()

   >>> # iteration(迭代)
   >>> n = 0
   >>> for val in values:
   ...     n += val
   >>> print(n)
   504

   >>> # 键和值以相同的顺序(插入顺序)迭代
   >>> list(keys)
   ['eggs', 'sausage', 'bacon', 'spam']
   >>> list(values)
   [2, 1, 1, 500]

   >>> # 视图对象是动态的,反映字典的更改
   >>> del dishes['eggs']
   >>> del dishes['sausage']
   >>> list(keys)
   ['bacon', 'spam']

   >>> # 集合运算
   >>> keys & {'eggs', 'bacon', 'salad'}
   {'bacon'}
   >>> keys ^ {'sausage', 'juice'}
   {'juice', 'sausage', 'bacon', 'spam'}
"""
"""
# SEQUENCES,TUPLES

序列类型 — "list", "tuple", "range"

有三种基本的序列类型:lists, tuples, and range.专门章节中描述了为处理二进制数据和文本字
符串而定制的其他序列类型.

公共序列运算
==========

大多数序列类型(可变和不可变)都支持下表中的操作.提供"collections.abc.Sequence" ABC是为
了更容易在自定义序列类型上正确实现这些操作.

此表列出了按升序优先级排序的序列操作.在表中,*s*和*t*是相同类型的序列,*n*、*i*、*j*和*k*
是整数,*x*是满足*s*施加的任何类型和值限制的任意对象.

"in"和"not in"操作与比较操作具有相同的优先级."+"(串联)和"*"(重复)操作与相应的数字操作
具有相同的优先级.

 Operation(运算)                 Result(结果)                              Notes
-------------------------------------------------------------------------------
 "x in s"                    如果*s*项等于*x*,则为"True",否则为"False"        (1)

-------------------------------------------------------------------------------
 "x not in s"                如果*s*项等于*x*,则为"False",否则为"True"        (1)
-------------------------------------------------------------------------------
 "s + t"                     *s*和*t*的串联                               (6)(7)
-------------------------------------------------------------------------------
 "s * n" or "n * s"          相当于将*s*添加到自身*n*次                    (2)(7)
-------------------------------------------------------------------------------
 "s[i]"                      *s*的第*i*项,从0开始                            (3)
-------------------------------------------------------------------------------
 "s[i:j]"                    从*i*到*j*的*s*切片                          (3)(4)
-------------------------------------------------------------------------------
 "s[i:j:k]"                  使用步幅*k*从*i*到*j*的*s*切片                (3)(5)
-------------------------------------------------------------------------------
 "len(s)"                    长度*s*
-------------------------------------------------------------------------------
 "min(s)"                    最小项*s*
-------------------------------------------------------------------------------
 "max(s)"                    最大项目*s*
-------------------------------------------------------------------------------
 "s.index(x[, i[, j]])"      *x*在*s*中首次出现的索引(在索引*i*处或之后,        (8)
                             在索引*j*之前)
-------------------------------------------------------------------------------
 "s.count(x)"                *x*在*s*的总出现次数

相同类型的序列也支持比较.特别是,元组和列表是通过比较相应的元素按字典顺序进行比较的.这意味
着要比较相等,每个元素必须比较相等,并且两个序列必须具有相同的类型和长度.

Notes:

1.虽然"in"和"not in"操作仅用于一般情况下的简单安全壳测试,但一些特殊序列(如"str"、
  "bytes"和"bytearray")也用于子序列测试:

      >>> "gg" in "eggs"
      True

2.小于"0"的*n*值被视为"0"(这将生成与*s*类型相同的空序列).请注意,序列*s*中的项目不会被复
  制;它们被多次引用.这经常困扰着新的Python程序员;考虑:

      >>> lists = [[]] * 3
      >>> lists
      [[], [], []]
      >>> lists[0].append(3)
      >>> lists
      [[3], [3], [3]]

   实际情况是,"[[]]"是一个包含空列表的单元素列表,因此"[[]]*3"的所有三个元素都引用了这个
   空列表.修改"lists"的任何元素都会修改这个列表.您可以通过以下方式创建不同列表的列表:

      >>> lists = [[] for i in range(3)]
      >>> lists[0].append(3)
      >>> lists[1].append(5)
      >>> lists[2].append(7)
      >>> lists
      [[3], [5], [7]]

3.如果*i*或*j*为负,则索引与序列*s*的结尾相关:"len(s) + i" or "len(s) + j"被替换.但请
  注意"-0"仍然是"0".

4.从*i*到*j*的*s*切片被定义为索引为*k*的项目序列,使得"i <= k < j".如果*i*或*j*大于
  "len(s)",请使用"len(s)".如果省略*i*或"None",则使用"0".如果省略*j*或"None",请使用
  "len(s)".如果*i*大于或等于*j*,则切片为空.

5.步幅为*k*的*s*从*i*到*j*的切片被定义为索引为"x = i + n*k"的项目序列,使得
  "0 <= n <(j-i)/k".换句话说,索引是"i"、"i+k"、"i+2*k"、"i+3*k"等,在达到*j*时停止(
  但不包括*j*).当*k*为正时,*i*和*j*如果较大,则减小为"len(s)".当*k*为负时,*i*和*j*如果
  较大,则减小为"len(s)-1".如果省略*i*或*j*或"None",则它们将成为"end"值(结束取决于*k*
  的符号).注意,*k*不能为零.如果*k*为"None",则将其视为"1".

6.连接不可变序列总是产生一个新对象.这意味着通过重复串联建立序列将在总序列长度中产生二次运
  行时成本.要获得线性运行时成本,必须切换到以下备选方案之一:

   *如果串联"str"对象,则可以构建一个列表并在末尾使用"str.join()",或者写入"io.StringIO"
    实例,并在完成后检索其值

   *如果连接"bytes"对象,您可以类似地使用"bytes.join()"或"io.BytesIO",也可以使用
    "bytearray"对象进行就地连接."bytearray"对象是可变的,并且具有有效的过度分配机制

   *如果连接"tuple"对象,则扩展"list"

7.某些序列类型(如"range")只支持遵循特定模式的项序列,因此不支持序列串联或重复.

8.当在*s*中找不到*x*时,"index"将引发"ValueError".并非所有实现都支持传递附加参数*i*和
  *j*.这些参数允许有效地搜索序列的子部分.传递额外的参数大致相当于使用"s[i:j].index(x)",
  只是不复制任何数据,并且返回的索引是相对于序列的开头而不是片段的开头的.

不可变序列类型
============

不可变序列类型通常实现的唯一一个不由可变序列类型实现的操作是对内置"hash()"的支持.

这种支持允许不可变序列(如"tuple"实例)用作"dict"键,并存储在"set"和"frozenset"实例中.

试图散列包含不可破坏值的不可变序列将导致"TypeError".

可变序列类型
==========

下表中的操作是在可变序列类型上定义的.提供"collections.abc.MutableSequence" ABC是为了
更容易在自定义序列类型上正确实现这些操作.

在表中,*s*是可变序列类型的实例,*t*是任何可迭代对象,*x*是满足*s*施加的任何类型和值限制的
任意对象(例如,"bytearray"仅接受满足值限制"0 <= x <= 255"的整数).

 Operation(运算)                 Result(结果)                              Notes
-------------------------------------------------------------------------------
 "s[i] = x"                   *s*中的*i*项替换为*x*
-------------------------------------------------------------------------------
 "s[i:j] = t"                 将*s*从*i*到*j*的切片替换为iterable*t*
                              的内容
-------------------------------------------------------------------------------
 "del s[i:j]"                 与"s[i:j] = []"相同
-------------------------------------------------------------------------------
 "s[i:j:k] = t"               "s[i:j:k]"的元素替换为*t*的元素                 (1)
-------------------------------------------------------------------------------
 "del s[i:j:k]"               从列表中删除"s[i:j:k]"的元素
-------------------------------------------------------------------------------
 "s.append(x)"                在序列末尾追加*x*(与"s[len(s):len(s)] = [x]")
                              相同)
-------------------------------------------------------------------------------
 "s.clear()"                  删除*s*中的所有项目(与"del s[:]"相同)            (5)
-------------------------------------------------------------------------------
 "s.copy()"                   创建*s*(与"s[:]"相同)的浅层副本                  (5)
-------------------------------------------------------------------------------
 "s.extend(t)" or "s += t"    用*t*的内容扩展*s*(大部分内容与
                              "s[len(s):len(s)] = t"相同)
-------------------------------------------------------------------------------
 "s *= n"                     更新*s*,其内容重复*n*次                         (6)
-------------------------------------------------------------------------------
 "s.insert(i, x)"             在*i*给定的索引处将*x*插入*s*
                              (与"s[i:i] = [x]"相同)
-------------------------------------------------------------------------------
 "s.pop([i])"                 在*i*处检索项目,并将其从*s*中删除                (2)
-------------------------------------------------------------------------------
 "s.remove(x)"                从*s*中删除第一项,其中"s[i]"等于*x*              (3)
-------------------------------------------------------------------------------
 "s.reverse()"                在位反转*s*项                                  (4)

Notes:

1.*t*必须与所替换的切片具有相同的长度.

2.可选参数*i*默认为"-1",因此默认情况下最后一项被删除并返回.

3.当在*s*中找不到*x*时,"remove()"将引发"ValueError".

4."reverse()"方法在反转大序列时修改适当的序列以节省空间.为了提醒用户它是通过副作用操作的
  ,它不会返回相反的顺序.

5.包含"clear()"和"copy()"是为了与不支持切片操作(如"dict"和"set")的可变容器的接口保持
  一致."copy()"不是"collections.abc.MutableSequence" ABC的一部分,但大多数具体的可变
  序列类都提供了它.

   版本3.3中新增了:"clear()"和"copy()"方法.

6.值*n*是一个整数,或者是一个实现"__index__()"的对象.*n*的零值和负值清除序列.序列中的项
  目不被复制;它们被多次引用,如公共序列操作下的"s * n"所述.

Lists
=====

列表是可变序列,通常用于存储同质项的集合(其中精确的相似程度因应用程序而异).

class list([iterable])

   列表可以通过几种方式构建:

   *使用一对方括号表示空列表"[]"

   *使用方括号,用逗号分隔项目:"[a]"、"[a、b、c]"

   *使用列表理解:"[x for x in iterable]"

   *使用类型构造函数:"list()" or "list(iterable)"

   构造函数构建一个列表,其项与*iterable*的项相同,且顺序相同*iterable*可以是序列、支持
   迭代的容器或迭代器对象.如果*iterable*已经是一个列表,则会制作并返回一个副本,类似于
   "iterable[:]".例如,"list('abc')"返回"['a', 'b', 'c']"和"list( (1, 2, 3) )"
   返回"[1, 2, 3]".如果未给出任何参数,构造函数将创建一个新的空列表"[]".

   许多其他操作也会生成列表,包括内置的"sorted()".

   列表实现所有公共和可变序列操作.列表还提供了以下附加方法:

   sort(*, key=None, reverse=False)

      此方法只使用项目之间的"<"比较对列表进行排序.异常不会被抑制-如果任何比较操作失败,整
      个排序操作将失败(并且列表可能处于部分修改状态).

      "sort()"接受只能通过关键字传递的两个参数(仅关键字参数):

      *key*指定一个参数的函数,用于从每个列表元素中提取比较键(例如,"key=str.lower").列
      表中每个项目对应的键计算一次,然后用于整个排序过程.默认值"None"表示列表项直接排序,
      而不计算单独的键值.

      "functools.cmp_to_key()"实用程序可用于将2.x样式的*cmp*函数转换为*key*函数.

      *reverse*是一个布尔值.如果设置为"True",则列表元素将被排序,就像每个比较都被反转一
      样.

      此方法在对大型序列进行排序时,为了节省空间,修改了适当的序列.为了提醒用户它的操作有副
      作用,它不会返回排序序列(使用"sorted()"显式请求新的排序列表实例).

      "sort()"方法保证是稳定的.如果排序保证不改变比较相等的元素的相对顺序,则排序是稳定的
      -这有助于在多个过程中进行排序(例如,按部门排序,然后按薪资等级排序).

      **CPython实现详细信息:**在对列表进行排序时,试图改变甚至检查列表的效果是未定义的.
      Python的C实现使列表在持续时间内显示为空,如果能够检测到列表在排序过程中发生了变化,
      则会引发"ValueError".

Tuples
======

元组是不可变的序列,通常用于存储异构数据的集合(例如内置的"enumerate()"生成的2元组).元组
还用于需要不可变的同质数据序列的情况(例如允许存储在"set"或"dict"实例中).

class tuple([iterable])

   元组可以通过多种方式构造:

   *使用一对括号表示空元组:"()"

   *对单元组使用尾随逗号:"a"或"(a,)"

   *用逗号分隔项目:"a,b,c"或"(a,b,c)"

   *使用内置的"tuple()"命令:"tuple()"或"tuple(iterable)"

   构造函数构建一个元组,其项与*iterable*的项相同且顺序相同*iterable*可以是序列、支持迭
   代的容器或迭代器对象.如果*iterable*已经是一个元组,则返回时将保持不变.例如,
   "tuple('abc')"返回"('a', 'b', 'c')"和"tuple( [1, 2, 3] )"返回"(1, 2, 3)".如果
   没有给出参数,构造函数将创建一个新的空元组"()".

   请注意,实际上是逗号构成元组,而不是括号.括号是可选的,除了在空元组的情况下,或者当需要它
   们以避免语法歧义时.例如,"f(a, b, c)"是具有三个参数的函数调用,而"f((a, b, c))"是具有
   三元组作为唯一参数的函数调用.

   元组实现所有公共序列操作.

对于按名称访问比按索引访问更清晰的异构数据集合,"collections.namedtuple()"可能比简单的
tuple对象更合适.


Ranges
======

"range"类型表示一个不可变的数字序列,通常用于在"for"循环中循环特定次数.

class range(stop)
class range(start, stop[, step])

   范围构造函数的参数必须是整数(内置的"int"或任何实现"__index__"特殊方法的对象).如果省
   略*step*参数,则默认为"1".如果省略*start*参数,则默认为"0".如果*step*为零,则引发
   "ValueError".

   对于正*step*,范围"r"的内容由公式"r[i] = start + step*i"确定,其中
   "i >= 0" 并且 "r[i] < stop".

   对于负*step*,范围的内容仍然由公式"r[i] = start + step*i"确定,但约束为"i >= 0"和
   "r[i] > stop".

   如果"r[0]"不满足值约束,则范围对象将为空.范围确实支持负指数,但这些被解释为从正指数确定
   的序列末尾开始的索引.

   允许包含大于"sys.maxsize"的绝对值的范围,但某些功能(如"len()")可能会引发
   "OverflowError".

   Range示例：

      >>> list(range(10))
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      >>> list(range(1, 11))
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      >>> list(range(0, 30, 5))
      [0, 5, 10, 15, 20, 25]
      >>> list(range(0, 10, 3))
      [0, 3, 6, 9]
      >>> list(range(0, -10, -1))
      [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
      >>> list(range(0))
      []
      >>> list(range(1, 0))
      []

   范围实现除串联和重复之外的所有常见序列操作(因为范围对象只能表示遵循严格模式的序列,而重
   复和串联通常会违反该模式).

   start

      *start*参数的值(如果未提供该参数,则为"0")

   stop

      *stop*参数的值

   step

      *step*参数的值(如果未提供参数,则为"1")

与常规的"list"或"tuple"相比,"range"类型的优势在于,"range"对象将始终占用相同(较小)的内
存量,不管它所表示的范围大小如何(因为它只存储"start"、"stop"和"step"值,根据需要计算单个
项和子范围).

范围对象实现"collections.abc.Sequence" ABC,并提供包含测试、元素索引查找、切片和负索引
支持等功能:

>>> r = range(0, 20, 2)
>>> r
range(0, 20, 2)
>>> 11 in r
False
>>> 10 in r
True
>>> r.index(10)
5
>>> r[5]
10
>>> r[:5]
range(0, 10, 2)
>>> r[-1]
18

测试范围对象是否与"=="和"!="相等将它们作为序列进行比较.也就是说,如果两个范围对象表示相同
的值序列,则认为它们相等.(请注意,比较相等的两个范围对象可能具有不同的"start"、"stop"和
"step"属性,例如"range(0) == range(2, 1, 3)"或"range(0, 3,2) == range(0, 4, 2)".)

在版本3.2中更改:执行顺序ABC.支持切片和负索引.在固定时间内测试"int"对象的成员身份,而不是
遍历所有项.

在版本3.3中更改:定义'=='和'!='根据范围对象定义的值序列进行比较(而不是根据对象标识进行比
较).

版本3.3中新增了"start"、"stop"和"step"属性.
"""
"""
# STRINGMETHODS

字符串方法

字符串实现所有公共序列操作,以及下面描述的其他方法.

字符串还支持两种样式的字符串格式,一种提供了很大程度的灵活性和自定义,另一种基于C"printf"
样式的格式,处理的类型范围较窄,更难正确使用,但对于它可以处理的情况(printf样式的字符串格式)
,通常速度更快.

标准库的文本处理服务部分包括许多其他模块,这些模块提供各种与文本相关的实用程序(包括"re"模
块中的正则表达式支持).

str.capitalize()

   返回字符串的副本,第一个字符大写,其余字符小写.

   在版本3.8中进行了更改:第一个字符现在放在基于标题的字符中,而不是大写.这意味着像有向图这样的
   字符将只将其第一个字母大写,而不是完整字符.

str.casefold()

   返回字符串的折叠副本.折叠的字符串可用于无壳匹配.

   大小写折叠类似于小写,但更具攻击性,因为它旨在消除字符串中的所有大小写区别.例如,德语小写
   字母'ß'相当于"ss".因为它已经是小写的,"lower()"对'ß'没有任何作用;"casefold()"将其转
   换为"ss".

   3.3版本的新特性

str.center(width[, fillchar])

   返回长度为*width*的以字符串为中心的字符串.填充使用指定的*fillchar*(默认为ASCII空格)
   完成.如果*width*小于或等于"len(s)",则返回原始字符串.

str.count(sub[, start[, end]])

   返回子字符串*sub*在[*start*, *end*]范围内不重叠的出现次数.可选参数*start*和*end*解
   释为切片表示法.

str.encode(encoding='utf-8', errors='strict')

   以字节对象的形式返回字符串的编码版本.默认编码为'utf-8'*errors*可用于设置不同的错误处
   理方案.*errors*的默认值为"strict",这意味着编码错误会引发"UnicodeError".其他可能的
   值包括"ignore"、"replace"、"xmlcharrefreplace"、"backslashreplace"和通过
   "codecs.register_error()"注册的任何其他名称.

   默认情况下,不会检查*errors*参数以获得最佳性能,而是仅在第一个编码错误时使用.启用Python
   开发模式,或使用调试生成检查*errors*.

   在版本3.1中更改:添加了对关键字参数的支持.
   在版本3.9中更改:*errors*现在在开发模式和调试模式中检查.

str.endswith(suffix[, start[, end]])

   如果字符串以指定的*suffix(后缀)*结尾,则返回"True",否则返回"False".*suffix*也可以是
   要查找的后缀元组.使用可选的*start*,测试从该位置开始.使用可选的*end*,停止在该位置进行
   比较.

str.expandtabs(tabsize=8)

   根据当前列和给定的制表符大小,返回字符串副本,其中所有制表符均替换为一个或多个空格.制表
   符位置每隔*tabsize*个字符出现一次(默认值为8,在第0、8、16列等处给出制表符位置).要展开
   字符串,将当前列设置为零,并逐个字符检查字符串.如果字符是制表符("\t"),则在结果中插入一个
   或多个空格字符,直到当前列等于下一个制表符位置.(制表符本身不被复制.)如果该字符是换行符(
   "\n")或返回符("\r"),则复制该字符,并将当前列重置为零.任何其他字符都会被复制,而当前列将
   递增1,无论打印时字符的表示方式如何.

   >>> '01\t012\t0123\t01234'.expandtabs()
   '01      012     0123    01234'
   >>> '01\t012\t0123\t01234'.expandtabs(4)
   '01  012 0123    01234'

str.find(sub[, start[, end]])

   返回在切片"s[start:end]"中找到子字符串*sub*的字符串中的最低索引.可选参数*start*和
   *end*解释为切片表示法.如果未找到*sub*,则返回"-1".

   Note:

     只有在需要知道*sub*的位置时,才应使用"find()"方法.要检查*sub*是否为子字符串,请使用
     "in"运算符:

        >>> 'Py' in 'Python'
        True

str.format(*args, **kwargs)

   执行字符串格式化操作.调用此方法的字符串可以包含由大括号"{}"分隔的文本或替换字段.每个替
   换字段包含位置参数的数字索引或关键字参数的名称.返回字符串的副本,其中每个替换字段都替换
   为相应参数的字符串值.

   >>> "The sum of 1 + 2 is {0}".format(1+2)
   'The sum of 1 + 2 is 3'

   Note:

     当将数字("int"、"float"、"complex"、"decimal.decimal"和子类)格式化为"n"类型(例
     如:"{:n}.format(1234)")时,函数会临时将"LC_CTYPE"区域设置为"LC_NUMERIC"区域设置
     ,以解码"localeconv()"的"decimal_point"和"thousands_sep"字段(如果它们不是ASCII
     或长于1字节),以及"LC_NUMERIC"区域设置与"LC_CTYPE"区域设置不同.此临时更改会影响其
     他线程.

   在版本3.7中更改:当使用"n"类型格式化数字时,函数会在某些情况下临时将"LC_CTYPE"区域设置
   设置为"LC_NUMERIC"区域设置.

str.format_map(mapping)

   与"str.format(**mapping)"类似,只是"mapping"直接使用,而不是复制到"dict".例如,如果
   "mapping"是dict子类,则这非常有用:

   >>> class Default(dict):
   ...     def __missing__(self, key):
   ...         return key
   ...
   >>> '{name} was born in {country}'.format_map(Default(name='Guido'))
   'Guido was born in country'

   3.2版本新特性

str.index(sub[, start[, end]])

   类似于"find()",但在未找到子字符串时引发"ValueError".

str.isalnum()

   如果字符串中的所有字符都是字母数字且至少有一个字符,则返回"True",否则返回"False".如果
   以下任一项返回"True",则字符"c"为字母数字:"c.isalpha()"、"c.isdecimal()"、
   "c.isdigit()"或"c.isnumeric()".

str.isalpha()

   如果字符串中的所有字符都是字母,并且至少有一个字符,则返回"True",否则返回"False".字母字
   符是在Unicode字符数据库中定义为"Letter"的字符,即具有"Lm"、"Lt"、"Lu"、"Ll"或"Lo"
   之一的一般类别属性的字符.请注意,这与Unicode标准中定义的"Alphabetic"属性不同.

str.isascii()

   如果字符串为空或字符串中的所有字符均为ASCII,则返回"True",否则返回"False".ASCII字符
   的代码点范围为U+0000-U+007F.

   3.7版本新特性

str.isdecimal()

   如果字符串中的所有字符都是十进制字符且至少有一个字符,则返回"True",否则返回"False".十
   进制字符是可用于形成以10为基数的数字的字符,例如U+0660、阿拉伯-印度数字零.形式上,十进
   制字符是Unicode通用类别"Nd"中的字符.

str.isdigit()

   如果字符串中的所有字符都是数字且至少有一个字符,则返回"True",否则返回"False".数字包括
   十进制字符和需要特殊处理的数字,例如兼容上标数字.这包括不能用于形成以10为基数的数字的数
   字,如Kharosthi数字.形式上,数字是一个属性值Numeric_Type=Digit或
   Numeric_Type=Decimal的字符.

str.isidentifier()

   根据语言定义、节标识符和关键字,如果字符串是有效标识符,则返回"True".

  调用"keyword.iskeyword()"以测试字符串"s"是否为保留标识符,例如"def"和"class".

   Example:

      >>> from keyword import iskeyword

      >>> 'hello'.isidentifier(), iskeyword('hello')
      True, False
      >>> 'def'.isidentifier(), iskeyword('def')
      True, True

str.islower()

   如果字符串中所有大小写字符都是小写且至少有一个大小写字符,则返回"True",否则返回"False"

str.isnumeric()

   如果字符串中的所有字符都是数字字符,并且至少有一个字符,则返回"True",否则返回"False".
   数字字符包括数字字符,以及所有具有Unicode数值属性的字符,例如U+2155,普通分数五分之一.
   形式上,数字字符是那些属性值Numeric_Type=Digit、Numeric_Type=Decimal或
   Numeric_Type=Numeric的字符.

str.isprintable()

   如果字符串中的所有字符都可打印或字符串为空,则返回"True",否则返回"False".不可打印字符
   是指在Unicode字符数据库中定义为"Other"或"Separator"的字符,ASCII空格(0x20)除外,该
   空格被认为是可打印的.(请注意,此上下文中的可打印字符是在对字符串调用"repr()"时不应
   转义的字符.它与处理写入"sys.stdout"或"sys.stderr"的字符串无关.)

str.isspace()

   如果字符串中只有空白字符且至少有一个字符,则返回"True",否则返回"False".

   如果在Unicode字符数据库中,字符的一般类别为"Zs"("Separator, space"),或者其双向类为
   "WS"、"B"或"S"之一,则字符为*whitespace*.

str.istitle()

   如果字符串是基于标题的字符串且至少有一个字符,则返回"True",例如,大写字符只能跟在未基于
   标题的字符后面,而小写字符只能跟在大小写的字符后面.否则返回"False".

str.isupper()

   如果字符串中所有大小写字符都是大写且至少有一个大小写字符,则返回"True",否则返回"False".

   >>> 'BANANA'.isupper()
   True
   >>> 'banana'.isupper()
   False
   >>> 'baNana'.isupper()
   False
   >>> ' '.isupper()
   False

str.join(iterable)

   返回一个字符串,该字符串是*iterable*中字符串的串联.如果*iterable*中有任何非字符串值,
   包括"bytes"对象,则会引发"TypeError".元素之间的分隔符是提供此方法的字符串.

str.ljust(width[, fillchar])

   返回长度*width*的字符串中左对齐的字符串.填充使用指定的*fillchar*(默认为ASCII空格)
   完成.如果*width*小于或等于"len(s)",则返回原始字符串.

str.lower()

   返回字符串的副本,其中所有大小写字符都转换为小写.

str.lstrip([chars])

   返回删除前导字符的字符串副本.*chars*参数是一个字符串,指定要删除的字符集.如果省略或
   "None",则*chars*参数默认为删除空白.*chars*参数不是前缀;相反,其值的所有组合都被剥离:

      >>> '   spacious   '.lstrip()
      'spacious   '
      >>> 'www.example.com'.lstrip('owz.')
      'example.com'
      >>> 'Arthur: three!'.lstrip('Arthur: ')
      'ee!'
      >>> 'Arthur: three!'.removeprefix('Arthur: ')
      'three!'

static str.maketrans(x[, y[, z]])

   此静态方法返回可用于"str.translate()"的转换表.

   如果只有一个参数,则必须是将Unicode序号(整数)或字符(长度为1的字符串)映射到Unicode序号
   、字符串(任意长度)或"无"的字典.然后,字符键将转换为序数.

   如果有两个参数,它们必须是长度相等的字符串,并且在生成的字典中,x中的每个字符都将映射到y
   中相同位置的字符.如果有第三个参数,则必须是字符串,其字符将映射到结果中的"None".

str.partition(sep)

   在第一次出现*sep*时拆分字符串,并返回一个3元组,其中包含分隔符前面的部分、分隔符本身以及
   分隔符后面的部分.如果未找到分隔符,则返回一个包含字符串本身的3元组,后跟两个空字符串.

str.removeprefix(prefix, /)

   如果字符串以*prefix(前缀)*字符串开头,则返回"string[len(prefix):]".否则,返回原始字
   符串的副本:

      >>> 'TestHook'.removeprefix('Test')
      'Hook'
      >>> 'BaseTestCase'.removeprefix('Test')
      'BaseTestCase'

   3.9版本新特性

str.removesuffix(suffix, /)

   如果字符串以*suffix(后缀)*字符串结尾,且该*suffix(后缀)*不为空,则返回
   "string[:-len(suffix)]".否则,返回原始字符串的副本:

      >>> 'MiscTests'.removesuffix('Tests')
      'Misc'
      >>> 'TmpDirMixin'.removesuffix('Tests')
      'TmpDirMixin'

   3.9版本型新特性

str.replace(old, new[, count])

   返回字符串的副本,其中所有出现的子字符串*old*替换为*new*.如果给出可选参数*count*,则只
   替换第一次出现的*count*.

str.rfind(sub[, start[, end]])

   返回找到子字符串*sub*的字符串中的最高索引,以便*sub*包含在"s[start:end]"中.可选参数
   *start*和*end*解释为切片表示法.失败时返回"-1".

str.rindex(sub[, start[, end]])

   与"rfind()"类似,但在未找到子字符串*sub*时引发"ValueError".

str.rjust(width[, fillchar])

   返回长度*width*的字符串中右对齐的字符串.填充使用指定的*fillchar*(默认为ASCII空格)完
   成.如果*width*小于或等于"len(s)",则返回原始字符串.

str.rpartition(sep)

   在最后一次出现*sep*时拆分字符串,并返回一个3元组,其中包含分隔符前面的部分、分隔符本身
   以及分隔符后面的部分.如果未找到分隔符,则返回一个包含两个空字符串的3元组,后跟字符串本身.

str.rsplit(sep=None, maxsplit=- 1)

   返回字符串中的单词列表,使用*sep*作为分隔符字符串.如果给定*maxsplit*,则最多完成
   *maxsplit*拆分,*rightmost*.如果未指定*sep*或"None",则任何空白字符串都是分隔符.

str.rstrip([chars])

   返回已删除尾随字符的字符串副本.*chars*参数是一个字符串,指定要删除的字符集.如果省略或
   "None",则*chars*参数默认为删除空白.*chars*参数不是后缀;
   敲黑板:*chars*值的所有组合都被剥离:

      >>> '   spacious   '.rstrip()
      '   spacious'
      >>> 'mississippi'.rstrip('ipz')
      'mississ'
      >>> 'Monty Python'.rstrip(' Python')
      'M'
      >>> 'Monty Python'.removesuffix(' Python')
      'Monty'

str.split(sep=None, maxsplit=- 1)

   返回字符串中的单词列表,使用*sep*作为分隔符字符串.如果给定*maxsplit*,则最多完成
   *maxsplit*拆分(因此,列表最多包含"maxsplit+1"元素).如果未指定*maxsplit*或"-1",则对
   拆分数量没有限制(所有可能的拆分都已进行).

   如果给定*sep*,则连续分隔符不会分组在一起,并被视为分隔空字符串(例如,'1,,2'.split(',')
   返回['1', '', '2']).*sep*参数可能由多个字符组成(例如,'1<>2<>3'.split('<>')返回
   ['1', '2', '3']).使用指定的分隔符拆分空字符串将返回"['']".

   For example:

      >>> '1,2,3'.split(',')
      ['1', '2', '3']
      >>> '1,2,3'.split(',', maxsplit=1)
      ['1', '2,3']
      >>> '1,2,,3,'.split(',')
      ['1', '2', '', '3', '']

   如果未指定*sep*或为"None",则应用不同的拆分算法:连续空格的运行被视为单个分隔符,如果
   字符串具有前导或尾随空格,则结果的开头或结尾将不包含空字符串.因此,使用"None"分隔符拆
   分空字符串或仅包含空格的字符串将返回"[]".

   For example:

      >>> '1 2 3'.split()
      ['1', '2', '3']
      >>> '1 2 3'.split(maxsplit=1)
      ['1', '2 3']
      >>> '   1   2   3   '.split()
      ['1', '2', '3']

str.splitlines([keepends])

   返回字符串中的行列表,在行边界处断开.结果列表中不包括换行符,除非给出了*keepends*,且为
   true.

   此方法在以下线边界上拆分.特别是,边界是*universal newlines(通用换行符)*的超集.

    Representation(表达式)      Description(描述)
  ------------------------------------------------------------
    "\n"                     Line Feed(换行符)
  ------------------------------------------------------------
    "\r"                     Carriage Return(回车)
  ------------------------------------------------------------
    "\r\n"                   Carriage Return + Line Feed(回车+换行)
  ------------------------------------------------------------
    "\v" or "\x0b"           Line Tabulation(水平制表符)
  ------------------------------------------------------------
    "\f" or "\x0c"           Form Feed(分页符)
  ------------------------------------------------------------
    "\x1c"                   File Separator(文件分隔符)
  ------------------------------------------------------------
    "\x1d"                   Group Separator(组分隔符)
  ------------------------------------------------------------
    "\x1e"                   Record Separator(记录分离符)
  ------------------------------------------------------------
    "\x85"                   Next Line
  ------------------------------------------------------------
    "\u2028"                 Line Separator(行分隔符)
  ------------------------------------------------------------
    "\u2029"                 Paragraph Separator(段落分隔符)

   在版本3.2中更改:"\v"和"\f"添加到线边界列表中.

   # For example:
   #   >>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
   #    ['ab c', '', 'de fg', 'kl']
   #    >>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
   #    ['ab c\n', '\n', 'de fg\r', 'kl\r\n']

   与给定分隔符字符串*sep*时的"split()"不同,此方法为空字符串返回一个空列表,并且终端换行
   符不会产生额外的行:

      # >>> "".splitlines()
      # []
      # >>> "One line\n".splitlines()
      # ['One line']

   为了进行比较,"split('\n')"给出:

      # >>> ''.split('\n')
      # ['']
      # >>> 'Two lines\n'.split('\n')
      # ['Two lines', '']

str.startswith(prefix[, start[, end]])

   如果字符串以*prefix(前缀)*开头,则返回"True",否则返回"False".*prefix*也可以是要查找
   的前缀元组.使用可选的*start*,测试从该位置开始的字符串.使用可选的*end*,停止在该位置比
   较字符串.

str.strip([chars])

   返回删除前导字符和尾随字符的字符串副本.*chars*参数是一个字符串,指定要删除的字符集.如
   果省略或"None",则*chars*参数默认为删除空白.*chars*参数不是前缀或后缀;相反,其值的所
   有组合都被剥离:

      >>> '   spacious   '.strip()
      'spacious'
      >>> 'www.example.com'.strip('cmowz.')
      'example'

   从字符串中剥离最外层的前导和尾随*chars*参数值.从前端删除字符,直到到达*chars*中字符集
   不包含的字符串为止.尾端也会发生类似的动作.例如:

      >>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
      >>> comment_string.strip('.#! ')
      'Section 3.2.1 Issue #32'

str.swapcase()

   返回将大写字符转换为小写字符的字符串副本,反之亦然.请注意,
   "s.swapcase().swapcase() == s"不一定正确.

str.title()

   返回字符串的基于标题的版本,其中单词以大写字符开头,其余字符为小写.

   For example:

      >>> 'Hello world'.title()
      'Hello World'

   该算法使用一个简单的独立于语言的定义,将一个单词定义为一组连续的字母.这个定义在许多语境
   中都适用,但它意味着缩略语和所有格中的撇号形成了单词边界,这可能不是期望的结果:

      >>> "they're bill's friends from the UK".title()
      "They'Re Bill'S Friends From The Uk"

   可以使用正则表达式构造撇号的变通方法:

      >>> import re
      >>> def titlecase(s):
      ...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
      ...                   lambda mo: mo.group(0).capitalize(),
      ...                   s)
      ...
      >>> titlecase("they're bill's friends.")
      "They're Bill's Friends."

str.translate(table)

   返回字符串的副本,其中每个字符已通过给定的转换表映射.该表必须是通过"__getitem__()"实
   现索引的对象,通常是*mapping(映射)*或*sequence(序列)*.当使用Unicode序号(整数)编制索
   引时,表对象可以执行以下任一操作:返回Unicode序号或字符串,以将字符映射到一个或多个其他
   字符;返回"None",从返回字符串中删除该字符;或引发"LookupError"异常,以将角色映射到自身.

   您可以使用"str.maketrans()"创建不同格式的字符到字符映射的转换映射.

str.upper()

   返回字符串的副本,其中所有大小写字符都转换为大写.请注意,如果"s"包含未加密字符,或者如果
   生成字符的Unicode类别不是"Lu"(Letter,uppercase),而是"Lt"(Letter, titlecase),则
   "s.upper().isupper()"可能为"False".

str.zfill(width)

   返回由ASCII'0'数字填充的字符串副本,以生成长度*width*的字符串.前导符号前缀("+"/"-")
   是通过在符号字符之后而不是之前插入填充来处理的.如果*width*小于或等于"len(s)",则返回
   原始字符串.

   For example:

      >>> "42".zfill(5)
      '00042'
      >>> "-42".zfill(5)
      '-0042'
"""
"""
# MODULES

模块

模块上唯一的特殊操作是属性访问:"m.name",其中*m*是模块,*name*访问*m*符号表中定义的名称.
模块属性可以被指定.(请注意,"import"语句严格来说不是对模块对象的操作;"import foo"不要求
名为*foo*的模块对象存在,而是要求名为*foo*的模块在某处具有(外部)*definition(定义)*.)

每个模块的一个特殊属性是"__dict__".这是包含模块符号表的字典.修改此字典实际上会更改模块的
符号表,但不可能直接分配到"__dict__"属性(您可以编写"m.__dict__['a'] = 1",它将"m.a"定义
为"1",但您不能编写"m.__dict__ = {}").不建议直接修改"__dict__".

解释器中内置的模块是这样写的:"<module 'sys' (built-in)>".如果从文件加载,它们将被写入
"<module 'os' from '/usr/local/lib/pythonX.Y/os.pyc'>".
"""
"""
# import

"import"关键字

   import_stmt     ::= "import" module ["as" identifier]
                           ("," module ["as" identifier])*
                   | "from" relative_module "import"
                                                 identifier ["as" identifier]
                                            ("," identifier ["as" identifier])*
                   | "from" relative_module "import"
                                 "(" identifier ["as" identifier]
                                ("," identifier ["as" identifier])* [","] ")"
                   | "from" module "import" "*"
   module          ::= (identifier ".")* identifier
   relative_module ::= "."* module | "."+

   注释:
   identifier:标识符

基本导入语句(没有"from"子句)分两步执行:

1.查找模块,必要时加载并初始化它

2.在本地命名空间中为出现"import"语句的作用域定义一个或多个名称.

当语句包含多个子句(用逗号分隔)时,这两个步骤将分别针对每个子句执行,就像这些子句已被分隔为
单独的导入语句一样.

关于导入系统的部分更详细地描述了第一步的详细信息,即查找和加载模块,该部分还描述了可导入的各
种类型的包和模块,以及可用于自定义导入系统的所有挂钩.请注意,此步骤中的故障可能表示找不到模
块,或初始化模块时发生错误,包括执行模块代码.

如果成功检索请求的模块,则将通过以下三种方式之一使其在本地命名空间中可用:

*如果模块名称后面跟着"as",则"as"后面的名称将直接绑定到导入的模块.

*如果未指定其他名称,并且导入的模块是顶级模块,则该模块的名称将绑定在本地命名空间中,作为对
 导入模块的引用

*如果要导入的模块不是顶级模块,则包含该模块的顶级包的名称将绑定在本地命名空间中,作为对顶级
 包的引用.必须使用其完整限定名而不是直接访问导入的模块

"from"表单使用了稍微复杂一些的过程:

1.查找"from"子句中指定的模块,必要时加载并初始化它;

2.对于"import"中指定的每个标识符:

   1.检查导入的模块是否具有该名称的属性

   2.如果没有,请尝试导入具有该名称的子模块,然后再次检查导入的模块是否具有该属性

   3.如果未找到该属性,则引发"ImportError".

   4.否则,对该值的引用将存储在本地命名空间中,如果存在,则使用"as"子句中的名称,否则使用属
     性名称

例子:

   import foo                 # foo imported and bound locally
   import foo.bar.baz         # foo.bar.baz imported, foo bound locally
   import foo.bar.baz as fbb  # foo.bar.baz imported and bound as fbb
   from foo.bar import baz    # foo.bar.baz imported and bound as baz
   from foo import attr       # foo imported and foo.attr bound as attr

如果标识符列表被星号('*')替换,则模块中定义的所有公共名称都将绑定到发生"import"语句的作用
域的本地命名空间中.

模块定义的*public names*是通过检查模块名称空间中名为"__all__"的变量来确定的;如果已定义,
则它必须是由该模块定义或导入的名称组成的字符串序列."__all__"中给出的名称都被视为公共名称,
并且必须存在.如果未定义"__all__",则公共名称集将包括在模块命名空间中找到的所有名称,这些名
称不以下划线字符('_')开头."__all__"应包含整个公共API.其目的是避免意外导出不属于API的项
(例如导入并在模块中使用的库模块).

导入的通配符形式-"from module import *"-仅在模块级别允许.试图在类或函数定义中使用它将
引发"SyntaxError".

指定要导入的模块时,不必指定模块的绝对名称.当一个模块或包包含在另一个包中时,可以在同一个顶
层包中进行相对导入,而不必提及包名.通过在"from"之后的指定模块或包中使用前导点,可以指定向上
遍历当前包层次结构的高度,而无需指定确切的名称.一个前导点表示进行导入的模块所在的当前包.两
个点意味着上一个包级别.三个点是两个级别,以此类推.因此,如果您从"pkg"包中的模块执行
"from.import mod",那么您将最终导入"pkg.mod".如果从"pkg.subpkg1"中执行
"from..subpkg2 import mod",则将导入"pkg.subpkg2.mod".

"importlib.import_module()"用于支持动态确定要加载的模块的应用程序.

引发包含参数"module"、"filename"、"sys.path"、"sys.meta_path"、"sys.path_hooks"的
审核事件"import".

未来声明
=======

*future statement*是编译器的一个指令,指示特定模块应使用语法或语义进行编译,该语法或语义
将在指定的Python未来版本中提供,在该版本中,该特性将成为标准.

future statement旨在简化到Python未来版本的迁移,这些版本会对语言引入不兼容的更改.它允许
在每个模块上使用新功能,然后在该功能成为标准之前发布.

   future_stmt ::= "from" "__future__" "import" feature ["as" identifier]
                                           ("," feature ["as" identifier])*
                   | "from" "__future__" "import" "(" feature ["as" identifier]
                                    ("," feature ["as" identifier])* [","] ")"
   feature     ::= identifier

future statement必须出现在模块顶部附近.只能在future语句之前显示的行有:

* the module docstring (if any),
* comments,
* blank lines,
* other future statements.

唯一需要使用future statement的功能是"annotations(注释)".

future statement启用的所有历史特性仍然可以被Python3识别.该列表包括"absolute_import"、
"division"、"generators"、"generator_stop"、"unicode_literals"、"print_function"
、"nested_scopes"和"with_statement".它们都是冗余的,因为它们始终处于启用状态,并且仅为
向后兼容而保留.

future statement在编译时会得到识别和特别处理:对核心结构语义的更改通常通过生成不同的代码
来实现.甚至可能是新特性引入了新的不兼容语法(例如新的保留字),在这种情况下,编译器可能需要以
不同的方式解析模块.这样的决定不能推迟到运行时.

对于任何给定的版本,编译器都知道定义了哪些功能名称,如果将来的语句包含未知的功能,则会引发编
译时错误.

直接运行时语义与任何导入语句的语义相同:有一个标准模块"__future__",将在执行
future statement时以常规方式导入.

有趣的运行时语义取决于future statement启用的特定功能.

请注意,该声明没有什么特别之处:

   import __future__ [as name]

这不是未来的声明;它是一个普通的import语句,没有特殊的语义或语法限制.

默认情况下,通过调用包含future statement的模块"M"中的内置函数"exec()"和"compile()"编
译的代码将使用与future statement关联的新语法或语义.这可以由"compile()"的可选参数控制

在交互式解释器提示下键入的future statement将在解释器会话的其余时间生效.如果使用"-i"选项
启动解释器,并向解释器传递要执行的脚本名,并且该脚本包含一个future statement,则它将在脚本
执行后启动的交互式会话中生效.
"""
"""
# SPECIALMETHODS

特殊方法

类可以通过定义具有特殊名称的方法来实现由特殊语法(如算术运算或订阅和切片)调用的某些操作.这
是Python对*operator overloading(运算符重载)*的方法,允许类定义它们自己关于语言运算符的
行为.例如,如果一个类定义了一个名为"__getitem__()"的方法,并且"x"是这个类的一个实例,那么
"x[i]"大致相当于"type(x).__getitem__(x,i)".除非另有说明,否则在未定义适当的方法时,尝试
执行操作会引发异常(通常为"AttributeError"或"TypeError").

将特殊方法设置为"None"表示相应的操作不可用.例如,如果一个类将"__iter__()"设置为"None",
则该类是不可iterable的,因此在其实例上调用"iter()"将引发"TypeError"(而不会返回到
"__getitem__()").

当实现一个模拟任何内置类型的类时,重要的是模拟的实现程度必须使其对所建模的对象有意义.例如,
某些序列可以很好地用于检索单个元素,但提取片段可能没有意义.(W3C文档对象模型中的"NodeList"
接口就是一个例子.)

Basic customization(基本定制)
============================

object.__new__(cls[, ...])

   调用以创建类*cls*的新实例."__new__()"是一个静态方法(有特例,因此不需要声明它),它将请
   求实例的类作为其第一个参数.其余的参数是传递给对象构造函数表达式(类调用)的参数.
   "__new__()"的返回值应该是新对象实例(通常是*cls*的实例).

   典型的实现通过使用带有适当参数的"super().__new__(cls[, ...])"调用超类的"__new__()"
   方法,然后根据需要修改新创建的实例,然后返回它来创建类的新实例.

   如果在对象构造过程中调用"__new__()",并且它返回一个实例或*cls*的子类,那么新实例的
   "__init__()"方法将像"__init__(self[, ...])"一样被调用,其中*self*是新实例,其余参
   数与传递给对象构造函数的参数相同.

   如果"__new__()"未返回*cls*的实例,则不会调用新实例的"__init__()"方法.

   "__new__()"主要用于允许不可变类型的子类(如int、str或tuple)自定义实例创建.为了自定义
   类的创建,它通常在自定义元类中被重写.

object.__init__(self[, ...])

   在创建实例之后(由"__new__()"),但在实例返回给调用方之前调用.参数是传递给类构造函数表达
   式的参数.如果基类有一个"__init__()"方法,则派生类的"__init__()"方法(如果有)必须显式
   调用它,以确保实例的基类部分正确初始化;例如:"super().__init__([args...])".

   因为"__new__()"和"__init__()"在构造对象时一起工作("__new__()"创建对象,
   "__init__()"自定义对象),所以"__init__()"不能返回非"None"值;这样做将导致在运行时引
   发"TypeError".

object.__del__(self)

   当实例即将被销毁时调用.这也称为终结器或(不恰当地)析构函数.如果基类有一个"__del__()"
   方法,则派生类的"__del__()"方法(如果有)必须显式调用它,以确保正确删除实例的基类部分.

   "__del__()"方法可以(尽管不推荐!)通过创建对实例的新引用来推迟实例的销毁.这叫做物体复
   活.当复活的对象即将被销毁时,是否第二次调用"__del__()"取决于实现;当前的*CPython*实
   现只调用它一次.

   当解释器退出时,不能保证为仍然存在的对象调用"__del__()"方法.

   Note:

     "del x"不直接调用"x.__del__()"—前者将"x"的引用计数递减1,后者仅在"x"的引用计数达
     到零时调用.

   **CPython实现细节:**引用循环可以防止对象的引用计数变为零.在这种情况下,*循环垃圾收集
   器*稍后将检测并删除该循环.引用循环的一个常见原因是在局部变量中捕获异常.然后,帧的局部变
   量引用异常,该异常引用其自身的回溯,该回溯引用在回溯中捕获的所有帧的局部变量.

   Warning:

     由于调用"__del__()"方法的情况不稳定,在执行过程中发生的异常将被忽略,并在
     "sys.stderr"中显示一条警告.特别地:

    *在执行任意代码时,包括从任意线程执行任意代码时,可以调用"__del__()".如果"__del__()"
    需要获取锁或调用任何其他阻塞资源,它可能会死锁,因为该资源可能已被中断以执行"__del__()"
    的代码获取.

    *解释器关闭期间可以执行"__del__()".因此,它需要访问的全局变量(包括其他模块)可能已经
    被删除或设置为"None".Python保证在删除其他全局变量之前,从其模块中删除名称以单个下划
    线开头的全局变量;如果不存在对此类全局变量的其他引用,这可能有助于确保导入的模块在调用
    "__del__()"方法时仍然可用.

object.__repr__(self)

   由"repr()"内置函数调用,以计算对象的"official(正式)"字符串表示形式.如果可能的话,这应
   该看起来像一个有效的Python表达式,可以用来重新创建具有相同值的对象(给定适当的环境).如
   果这是不可能的,则应返回格式为"<...some useful description...>"的字符串.返回值必须
   是字符串对象.如果类定义了"__repr__()"而不是"__str__()",那么当需要该类实例的
   "informal(非正式)"字符串表示形式时,也会使用"__str__()".

   这通常用于调试,因此表示信息丰富且明确是很重要的.

object.__str__(self)

   由"str(object)"和内置函数"format()"和"print()"调用,以计算对象的"informal(非正式)"
   或可良好打印的字符串表示形式.返回值必须是字符串对象.

   此方法不同于"object.__repr__()",因为不期望"__str__()"返回有效的Python表达式:可以
   使用更方便或简洁的表示形式.

   由内置类型"object"定义的默认实现调用"object.__repr__()".

object.__bytes__(self)

   由字节调用以计算对象的字节字符串表示形式.这将返回一个"bytes(字节)"对象.

object.__format__(self, format_spec)

   由"format()"内置函数调用,并扩展为对格式化字符串文本的求值和"str.format()"方法,以生
   成对象的"formatted(格式化)"字符串表示形式.*format_spec*参数是一个字符串,包含所需格
   式选项的说明.*format_spec*参数的解释取决于实现"__format__()"的类型,但是大多数类要
   么将格式化委托给其中一个内置类型,要么使用类似的格式化选项语法.

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

   这些就是所谓的"rich comparison(丰富比较)"方法.运算符符号和方法名称之间的对应关系如下
   :"x<y"调用"x.__lt__(y)","x<=y"调用"x.__le__(y)","x==y"调用"x.__eq__(y)","x!=y"
   调用"x.__ne__(y)","x>y"调用"x.__gt__(y)","x>=y"调用"x.__ge__(y)".

   如果富比较方法没有实现给定参数对的操作,则它可能返回单例"NotImplemented".按照惯例,
   "False"和"True"将返回以进行成功比较.但是,这些方法可以返回任何值,因此如果在布尔上下文
   中使用比较运算符(例如,在"if"语句的条件下),Python将调用该值上的"bool()",以确定结果是
   真还是假.

   默认情况下,"object"通过使用"is"实现"__eq__()",在错误比较的情况下返回"NotImplemented"
   "True if x is y else NotImplemented".对于"__ne__()",默认情况下它将委托给
   "__eq__()",并反转结果,除非它是"NotImplemented(未实现的)".比较运算符或默认实现之间
   没有其他隐含关系;例如,"(x<y or x==y)"的真值并不意味着"x<=y".

   这些方法没有交换的参数版本(当左参数不支持该操作而右参数支持该操作时使用);相反,
   "__lt__()"和"__gt__()"是彼此的反映,"__le__()"和"__ne__()".如果操作数的类型不同,
   且右操作数的类型是左操作数类型的直接或间接子类,则右操作数的反射方法具有优先级,否则左操
   作数的方法具有优先级.不考虑虚拟子类化.

object.__hash__(self)

   由内置函数"hash()"调用,用于对散列集合的成员进行操作,包括"set"、"frozenset"和"dict".
   "__hash__()"应返回一个整数.唯一需要的属性是比较相等的对象具有相同的哈希值;建议通过将
   对象组件的哈希值打包到一个元组中并对元组进行哈希处理,将对象组件的哈希值混合在一起,这些
   组件也在对象的比较中发挥作用.例子:

      def __hash__(self):
          return hash((self.name, self.nick, self.color))

   Note:

     "hash()"将从对象的自定义"__hash__()"方法返回的值截断为"Py_ssize_t"大小.在64位构
     建中,这通常是8字节,在32位构建中是4字节.如果对象的"__hash__()"必须在不同位大小的生
     成上进行互操作,请确保检查所有支持的生成上的宽度.一个简单的方法是使用"python -c "导
     入sys;打印(系统哈希信息宽度)”.

   如果一个类没有定义一个"__eq__()"方法,那么它也不应该定义一个"__hash__()"操作;如果它
   定义了"__eq__()"而不是"__hash__()",则其实例将不能作为可哈希集合中的项使用.如果类定
   义可变对象并实现"__eq__()"方法,则不应实现"__hash__()",因为可散列集合的实现要求键的
   散列值是不可变的(如果对象的散列值更改,则它将位于错误的散列桶中).

   用户定义的类默认有"__eq__()"和"__hash__()"方法;使用它们,所有对象都比较不相等(除了它
   们自己),并且"x.__hash__()"返回一个适当的值,使得"x == y"意味着"x is y"和
   "hash(x) == hash(y)".

   重写"__eq__()"且未定义"__hash__()"的类将其"__hash__()"隐式设置为"None".当类的
   "__hash__()"方法为"__hash__()"时,当程序试图检索其哈希值时,该类的实例将引发相应的
   "TypeError",并且在检查"isinstance(obj,collections.abc.Hashable)"时,该类的实例也
   将被正确标识为不可损坏.

   如果重写"__eq__()"的类需要保留父类中"__hash__()"的实现,则必须通过设置
   "__hash__ =<ParentClass>.__hash__"来明确告知解释器这一点.

   如果未重写"__eq__()"的类希望抑制哈希支持,则应在类定义中包含"__hash__ = None".定义自
   己的"__hash__()"并显式引发"TypeError"的类将被
   "isinstance(obj, collections.abc.Hashable)"调用错误地标识为可哈希的.

   Note:

     默认情况下,str和bytes对象的"__hash__()"值用不可预测的随机值"salted".虽然它们在单
     个Python进程中保持不变,但在重复调用Python之间是不可预测的.这是为了提供保护,防止由
     于精心选择的输入导致的拒绝服务,这些输入利用了dict插入的最差性能,O(n^2)复杂性.更改哈
     希值会影响集合的迭代顺序.Python从未保证过这种排序(通常在32位和64位构建之间有所不同)

   在版本3.3中更改:默认情况下启用哈希随机化.

object.__bool__(self)

   调用以实现真值测试和内置操作"bool()";应该返回"False"或"True".未定义此方法时,如果已
   定义,则调用"__len__()",如果结果为非零,则认为该对象为真.如果一个类既不定义"__len__()"
   也不定义"__bool__()",则其所有实例都被视为true.

Customizing attribute access(自定义属性访问)
==========================================

可以定义以下方法来自定义,类实例的属性访问(使用、分配或删除"x.name")的含义.

object.__getattr__(self, name)
   当默认属性访问失败且出现"AttributeError"(由于*name*不是实例属性或类树中"self"的属
   性,"__getattribute__()"引发"AttributeError";或者*name*属性的"__get__()"引发
   "AttributeError")时调用.此方法应返回属性值或引发"AttributeError"异常.

   请注意,如果通过正常机制找到该属性,则不会调用"__getattr__()".(这是"__getattr__()"和
   "__setattr__()"之间有意的不对称)这样做是出于效率原因,也是因为否则"__getattr__()"将
   无法访问实例的其他属性.请注意,至少对于实例变量,您可以通过不在实例属性字典中插入任何值(
   而是在另一个对象中插入值)来伪造完全控制.

object.__getattribute__(self, name)

   无条件调用以实现类实例的属性访问.如果该类还定义了"__getattr__()",则后者将不会被调用,
   除非"__getattribute__()"显式调用它或引发"AttributeError".此方法应返回属性值或引发
   "AttributeError"异常.为了避免此方法中的无限递归,它的实现应该始终使用相同的名称调用基
   类方法来访问它所需的任何属性,例如,"object.__getattribute__(self, name)".

   Note:
     当通过语言语法或内置函数进行隐式调用后查找特殊方法时,仍然可以忽略此方法.

   对于某些敏感属性访问,引发一个审核事件"object.__getattr__",参数为"obj"和"name".

object.__setattr__(self, name, value)

   在尝试属性分配时调用.调用它而不是调用正常机制(即,将值存储在实例字典中)*name*是属性名,
   *value*是要分配给它的值.

   如果"__setattr__()"想要分配给实例属性,它应该使用相同的名称调用基类方法,例如
   "object.__setattr__(self, name, value)".

   对于某些敏感属性分配,引发一个审核事件"object.__setattr__",其中包含参数"obj"、
   "name"、"value".

object.__delattr__(self, name)

   与"__setattr__()"类似,但用于属性删除而不是赋值.仅当"del obj.name"对对象有意义时,才
   应实现此操作.

   对于某些敏感属性删除,将引发一个审核事件"object.__delattr__",其中包含参数"obj"和
   "name".

object.__dir__(self)

   在对象上调用"dir()"时调用.必须返回一个序列."dir()"将返回的序列转换为列表并对其进行排
   序.

Customizing module attribute access(自定义模块属性访问)
----------------------------------------------------

特殊名称"__getattr__"和"__dir__"也可用于自定义对模块属性的访问.模块级的"__getattr__"
函数应接受一个作为属性名称的参数,并返回计算值或引发"AttributeError".如果通过正常查找在
模块对象上未找到属性,即"object.__getattribute__()",然后在引发"AttributeError"之前,
在模块"__dict__"中搜索"__getattr__".如果找到,将使用属性名调用它,并返回结果.

"__dir__"函数不应接受任何参数,并返回表示模块上可访问名称的字符串序列.如果存在,此函数将覆
盖模块上的标准"dir()"搜索.

为了更细粒度地定制模块行为(设置属性、性质等),可以将模块对象的"__class__"属性设置为
"types.ModuleType"的子类.例如：

   import sys
   from types import ModuleType

   class VerboseModule(ModuleType):
       def __repr__(self):
           return f'Verbose {self.__name__}'

       def __setattr__(self, attr, value):
           print(f'Setting {attr}...')
           super().__setattr__(attr, value)

   sys.modules[__name__].__class__ = VerboseModule

Note:

  定义模块"__getattr__"和设置模块"__class__"仅影响使用属性访问语法进行的查找-直接访问
  模块全局(无论是通过模块内的代码还是通过引用模块的全局字典)不受影响.

  在版本3.5中更改:"__class__"模块属性现在可写.
  版本3.7中新增:"__getattr__"和"__dir__"模块属性.

Implementing Descriptors(实现描述符)
-----------------------------------

以下方法仅适用于包含该方法的类的实例(所谓的*descriptor*类)出现在*owner(所有者)*类中时(
描述符必须在所有者的类字典中或在其父类之一的类字典中).在下面的示例中,"the attribute"指
的是其名称是所有者类"__dict__"中属性的键的属性.

object.__get__(self, instance, owner=None)

   调用以获取所有者类的属性(类属性访问)或该类的实例的属性(实例属性访问).可选的*owner*参
   数是所有者类,而*instance*是通过该属性访问的实例,当通过*owner*访问该属性时instance值
   为"None".

   此方法应返回计算的属性值或引发"AttributeError"异常.

object.__set__(self, instance, value)

   调用以将所有者类的实例*instance*上的属性设置为新值*value*.

   注意,添加"__set__()"或"__delete__()"会将描述符的类型更改为"data descriptor(数据
   描述符)".

object.__delete__(self, instance)

   调用以删除所有者类的实例*instance*上的属性.

object.__set_name__(self, owner, name)

   在创建所属类*owner*时调用.描述符已分配给*name*.

   Note:

     "__set_name__()"仅作为"type"构造函数的一部分隐式调用,因此在初始创建后将描述符添加
     到类时,需要使用适当的参数显式调用它：

        class A:
           pass
        descr = custom_descriptor()
        A.attr = descr
        descr.__set_name__(A, 'attr')

"inspect"模块将属性"__objclass__"解释为指定定义此对象的类(适当地设置此属性有助于动态类
属性的运行时自省).对于可调用函数,它可能表示预期或需要给定类型(或子类)的实例作为第一个位置
参数(例如,CPython为在C中实现的未绑定方法设置此属性).

Invoking Descriptors(调用描述符)
-------------------------------

通常,描述符是一个具有"binding behavior"的对象属性,其属性访问已被描述符协议中的方法覆盖:
"__get__()"、"__set__()"和"__delete__()".如果这些方法中的任何一个是为对象定义的,则称
之为描述符.

属性访问的默认行为是从对象的字典中获取、设置或删除属性.例如,"a.x"有一个查找链,从
"a.__dict__['x']"开始,然后是"type(a).__dict__['x']",然后是"type(a)"的基类,不包括元
类.

但是,如果查找的值是定义其中一个描述符方法的对象,那么Python可能会覆盖默认行为并调用描述符
方法.这种情况在优先级链中发生的位置取决于定义了哪些描述符方法以及如何调用它们.

描述符调用的起点是绑定"a.x".参数的组合方式取决于"a"：

直接调用
   最简单也是最不常见的调用是当用户代码直接调用描述符方法时:"x.__get__(a)".

实例绑定
   如果绑定到一个对象实例,"a.x"将转换为调用:
                                   "type(a).__dict__['x'].__get__(a, type(a))".

类绑定
   如果绑定到一个类,"A.x"将转换为调用:"A.__dict__['x'].__get__(None, A)".

超级绑定

    如果"a"是"super"的一个实例,那么绑定"super(B,obj).m()"将在
    "obj.__class__.__mro__"中搜索紧跟在"B"之前的基类"A",然后通过调用调用调用描述符:
    "A.__dict__['m'].__get__(obj, obj.__class__)".

对于实例绑定,描述符调用的优先级取决于定义的描述符方法.描述符可以定义"__get__()"、
"__set__()"和"__delete__()"的任意组合.如果未定义"__get__()",则访问该属性将返回描述符
对象本身,除非该对象的实例字典中有值.如果描述符定义了"__set__()"和/或"__delete__()",则
它是一个数据描述符;如果两者都没有定义,则它是非数据描述符.通常,数据描述符同时定义
"__get__()"和"__set__()",而非数据描述符只定义"__get__()"方法.定义了"__get__()"和
"__set__()"(和/或"__delete__()")的数据描述符始终覆盖实例字典中的重新定义.相反,非数据
描述符可以被实例覆盖.

Python方法(包括"staticmethod()"和"classmethod()")是作为非数据描述符实现的.因此,实例
可以重新定义和重写方法.这允许单个实例获取与同一类的其他实例不同的行为.

"property()"函数作为数据描述符实现.因此,实例不能重写属性的行为.

__slots__
---------

*__slots__*允许我们显式声明数据成员(如属性)并拒绝创建*__dict__*和*__weakref__*(除非在
*__slots__*中显式声明或在父级中可用.)

使用*__dict__*节省的空间可能很大.属性查找速度也可以显著提高.

object.__slots__

    可以为该类变量分配一个字符串、iterable或一系列字符串,这些字符串具有实例使用的变量名
    *__slots__*为声明的变量保留空间,并防止为每个实例自动创建*__dict__*和*__weakref__*

Notes on using *__slots__*(关于使用*__slots__*的注意事项)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*从没有*__slots__*的类继承时,实例的*__dict__*和*__weakref__*属性将始终可访问.

*如果没有*__dict__*变量,则无法为实例分配未在*__slots__*定义中列出的新变量.尝试分配给未
 列出的变量名会引发"AttributeError".如果需要动态分配新变量,则在*__slots__*声明中的字符
 串序列中添加"'__dict__'".

*如果每个实例都没有一个*__weakref__*变量,那么定义*__slots__*的类就不支持对其实例的弱引
 用.如果需要弱引用支持,则在*__slots__*声明中的字符串序列中添加"'__weakref__'".

**__slots__*通过为每个变量名创建描述符(实现描述符)在类级别实现.因此,类属性不能用于设置由
 *__slots__*定义的实例变量的默认值;否则,class属性将覆盖描述符赋值.

**__slots__*声明的操作不限于定义它的类.父类中声明的*__slots__*在子类中可用.但是,子类将
 得到一个*__dict__*和*__weakref__*除非它们还定义了*__slots__*(它应该只包含任何
 *additional(附加)*插槽的名称).

*如果一个类定义了一个也在基类中定义的slot,则基类slot定义的实例变量是不可访问的(除非直接
 从基类检索其描述符).这使得程序的含义未定义.将来,可能会添加一个检查以防止出现这种情况.

*非空*__slots__*不适用于从"可变长度"内置类型(如"int"、"bytes"和"tuple")派生的类.

*任何非字符串iterable都可以分配给*__slots__*.也可以使用映射;然而,在将来,可以将特殊含义
 分配给对应于每个键的值.

**__class__*赋值仅在两个类具有相同的*__slots__*时有效.

*可以使用具有多个slot父类的多重继承,但只允许一个父类具有由slot创建的属性(其他基必须具有
 空的slot布局)-违反会引发"TypeError".

*如果一个迭代器用于*__slots__*,则为每个迭代器的值创建一个描述符.但是,*__slots__*属性将
 是一个空迭代器.

Customizing class creation(自定义类创建)
======================================

每当一个类从另一个类继承时,就会在该类上调用*__init_subclass__*.这样,就可以编写更改子类
行为的类.这与类修饰符密切相关,但当类修饰符只影响它们应用到的特定类,"__init_subclass__"
仅适用于定义方法的类的未来子类.

classmethod object.__init_subclass__(cls)

   每当包含类被子类化时,就会调用此方法.*cls*则是新的子类.如果定义为普通实例方法,则此方法
   将隐式转换为类方法.

   传递给新类的关键字参数被传递给父类"__init_subclass__".为与使用"__init_subclass__"
   的其他类兼容,应取出所需的关键字参数,并将其他参数传递给基类,如下所示:

      class Philosopher:
          def __init_subclass__(cls,/,default_name,**kwargs):
              super().__init_subclass__(**kwargs)
              cls.default_name = default_name

      class AustralianPhilosopher(Philosopher,default_name="Bruce"):
          pass

   默认实现"object.__init_subclass__"不执行任何操作,但如果使用任何参数调用它,则会引发
   错误.

   Note:

    元类提示"metaclass"被类型机器的其余部分使用,并且永远不会传递给"__init_subclass__"
    实现.实际的元类(而不是显式提示)可以作为"cls"访问.

   3.6版本新特性

Metaclasses(元类)
-----------------

默认情况下,类是使用"type()"构造的.类主体在新名称空间中执行,并且类名在本地绑定到
"type(name,base,namespace)"的结果.

可以通过在类定义行中传递"metaclass"关键字参数,或者通过从包含此类参数的现有类继承来定制类
创建过程.在下面的示例中,"MyClass"和"MySubclass"都是"Meta"的实例:

   class Meta(type):
       pass

   class MyClass(metaclass=Meta):
       pass

   class MySubclass(MyClass):
       pass

在类定义中指定的任何其他关键字参数都将传递给下面描述的所有元类操作.

执行类定义时,将执行以下步骤:

*解决MRO条目;
*确定合适的元类;
*类名称空间已准备好;
*类主体被执行;
*将创建类对象.

Resolving MRO entries(解析MRO条目)
---------------------------------

如果类定义中出现的base不是"type"的实例,则会在其上搜索"__mro_entries__"方法.如果找到,则
使用原始的bases元组调用它.此方法必须返回将要使用的类的元组,而不是此base.元组可能为空,在
这种情况下,忽略原始base.

Determining the appropriate metaclass(确定适当的元类)
---------------------------------------------------

类定义的适当元类确定如下:

*如果没有给出bases和显式元类,则使用"type()";
*如果给出了一个显式元类,并且它*not*一个"type()"的实例,那么它直接用作元类;
*如果"type()"的实例作为显式元类给出,或者定义了base,则使用最派生的元类.

最派生的元类是从显式指定的元类(如果有)和所有指定base类的元类(即"type(cls)")中选择的.最
派生的元类是这些候选元类中*all*的子类型.如果候选元类中没有一个符合该标准,那么类定义将失败
并显示"TypeError".

Preparing the class namespace(准备类命名空间)
-------------------------------------------

一旦确定了适当的元类,就准备好了类名称空间.如果元类具有"__prepare__"属性,则称为
"namespace = metaclass.__prepare__(name,bases,**kwds)"(其中附加的关键字参数(如果有
)来自类定义)."__prepare__"方法应作为"classmethod()"实现.由"__prepare__"返回的名称空
间被传递到"__new__"中,但当创建最终类对象时,名称空间被复制到新的"dict"中.

如果元类没有"__prepare__"属性,则类名称空间将初始化为空的有序映射.

Executing the class body(执行类主体)
-----------------------------------

类主体(大约)作为"exec(body,globals(),namespace)"执行.与普通调用"exec()"的关键区别在
于,当类定义出现在函数内部时,词法作用域允许类主体(包括任何方法)引用当前和外部作用域中的名称.

但是,即使类定义发生在函数内部,类内部定义的方法仍然无法看到在类作用域中定义的名称.类变量必
须通过实例或类方法的第一个参数访问,或者通过下一节中描述的隐式词汇范围的"__class__"引用访
问.

Creating the class object(创建类对象)
-----------------------------------

一旦通过执行类主体填充了类名称空间,就可以通过调用
"metaclass(name,bases,namespace,**kwds)"来创建类对象(此处传递的其他关键字与传递给
"__prepare__"的关键字相同).

这个类对象将被"super()"的零参数形式引用.如果类主体中的任何方法引用"__class__"或"super"
,则"__class__"是编译器创建的隐式闭包引用.这允许"super()"的零参数形式正确标识基于词法作
用域定义的类,而用于进行当前调用的类或实例则基于传递给该方法的第一个参数进行标识.

**CPython实现详细信息:*在CPython 3.6及更高版本中,"__class__"单元格作为类命名空间中的
"__classcell__"项传递给元类.如果存在,则必须将其传播到"type.__new__"调用,以便正确初始
化该类.否则将导致Python3.8中出现"RuntimeError".

当使用默认元类"type"或任何最终调用"type.__new__"的元类时,在创建类对象后将调用以下附加自
定义步骤:

*首先,"type.__new__"收集类名称空间中定义"__set_name__()"方法的所有描述符;

*第二,所有这些"__set_name__"方法都是通过定义的类和该特定描述符的指定名称来调用的;

*最后,在新类的直接父类上按其方法解析顺序调用"__init_subclass__()" hook.

创建类对象后,将其传递给类定义中包含的类装饰器(如果有),并将生成的对象作为已定义的类绑定到本
地命名空间中.

当通过"type.__new__"创建新类时,作为命名空间参数提供的对象将复制到新的有序映射,原始对象将
被丢弃.新副本包装在一个只读代理中,该代理将成为类对象的"__dict__"属性.

Uses for metaclasses(元类的用法)
------------------------------

元类的潜在用途是无限的.已经探讨过的一些想法包括枚举、日志记录、接口检查、自动委派、自动属
性创建、代理、框架和自动资源锁定/同步.

Customizing instance and subclass checks(自定义实例和子类检查)
===========================================================

以下方法用于重写"isinstance()"和"issubclass()"内置函数的默认行为.

特别是,元类"abc.ABCMeta"实现了这些方法,以便允许将抽象基类(ABCs)作为"虚拟基类"添加到任何
类或类型(包括内置类型),包括其他ABCs.

注释:
    ABC:Abstract Base Classes

class.__instancecheck__(self,instance)

   如果*instance(实例)*被视为*class(类)*的(直接或间接)实例,则返回true.如果已定义,则
   调用以实现"isinstance(instance,class)".

class.__subclasscheck__(self,subclass)

   如果*subclass(子类)*被视为*class(类)*的(直接或间接)子类,则返回true.如果已定义,则调
   用以实现"issubclass(subclass,class)".

注意,这些方法是在类的类型(元类)上查找的.它们不能定义为实际类中的类方法.这与对实例调用的特
殊方法的查找是一致的,只有在这种情况下,实例本身就是一个类.

Emulating generic types(模拟泛型类型)
===================================

通过定义特殊方法,可以实现**PEP 484**(例如"List[int]")指定的通用类语法:

classmethod object.__class_getitem__(cls,key)

   返回一个对象,该对象表示在*key*中找到的泛型类按类型参数的专门化.

该方法是在类对象本身上查找的,当在类主体中定义时,该方法隐式地是一个类方法.注意,此机制主要
保留用于静态类型提示,不鼓励使用其他方法.

Emulating callable objects(模拟可调用对象)
========================================

object.__call__(self[,args...])

   Called when the instance is "called" as a function; if this method
   is defined,"x(arg1,arg2,...)" roughly translates to
   "type(x).__call__(x,arg1,...)".
   当实例作为函数"called"时调用;如果定义了此方法,"x(arg1,arg2,...)"大致转换为
   "type(x).__call__(x,arg1,...)".

Emulating container types(模拟容器类型)
=====================================

可以定义以下方法来实现容器对象.容器通常是序列(如列表或元组)或映射(如字典),但也可以表示其
他容器.第一组方法用于模拟序列或模拟映射;不同之处在于,对于序列,允许的键应该是整数*k*,其中
"0 <= k < N",其中*N*是序列的长度,或者是定义项目范围的切片对象.还建议映射提供方法
"keys()"、"values()"、"items()"、"get()"、"clear()"、"setdefault()"、"pop()"、
"popitem()"、"copy()"、和"update()",其行为类似于Python的标准字典对象.
"collections.abc"模块提供了一个"MutableMapping"抽象基类,以帮助从"__getitem__()"、
"__setitem__()"、"__delitem__()"和"keys()"的基集中创建这些方法.可变序列应该提供方法
"append()"、"count()"、"index()"、"extend()"、"insert()"、"pop()"、"remove()"、
"reverse()"和"sort()",就像Python标准列表对象一样.最后,序列类型应该通过定义下面描述的方
法"__add__()"、"__radd__()"、"__iadd__()"、"__mul__()"、"__rmul__()"和
"__imul__()",来实现加法(意思是串联)和乘法(意思是重复);它们不应定义其他数值运算符.建议映
射和序列都实现"__contains__()"方法,以允许有效使用"in"运算符;对于映射,"in"应该搜索映射
的键;对于序列,它应该搜索所有值.进一步建议映射和序列都实现"__iter__()"方法,以允许通过容器
进行有效迭代;对于映射,"__iter__()"应该迭代对象的键;对于序列,它应该遍历这些值.

object.__len__(self)

   调用以实现内置函数"len()".应返回对象的长度,一个整数">="0.此外,在布尔上下文中,未定义
   "__bool__()"方法且其"__len__()"方法返回零的对象被视为false.

   **CPython实现细节:**在CPython中,长度要求最多为"sys.maxsize".如果长度大于
   "sys.maxsize",则某些功能(如"len()")可能会引发"OverflowError".为了防止通过真值测试
   引发"OverflowError",对象必须定义一个"__bool__()"方法.

object.__length_hint__(self)

   调用以实现"operator.length_hint()".应返回对象的估计长度(可能大于或小于实际长度).长
   度必须为整数">="0.返回值也可以是"NotImplemented",这与"__length_hint__"方法根本不
   存在一样.这种方法纯粹是一种优化,不需要正确性.

   3.4版中的新版本.

object.__getitem__(self, key)

   调用以实现对"self[key]"的评估.对于序列类型,接受的键应该是整数和切片对象.请注意,负索
   引的特殊解释(如果类希望模拟序列类型)取决于"__getitem__()"方法.如果*key(键)*的类型不
   合适,可能会引发"TypeError";如果某个值超出序列的索引集(在对负值进行任何特殊解释之后),
   则应引发"IndexError".对于映射类型,如果缺少*key*(不在容器中),则应引发"KeyError".

   Note:

     "for"循环期望为非法索引引发一个"IndexError",以允许正确检测序列的结尾.

object.__setitem__(self, key, value)

   调用以实现对"self[key]"的赋值.与"__getitem__()"的注释相同.如果对象支持更改键的值,
   或者如果可以添加新键,或者如果可以替换元素,则只能对映射实现此操作.对于不正确的*key*值,
   应引发与"__getitem__()"方法相同的异常.

object.__delitem__(self, key)

   调用以实现删除"self[key]".与"__getitem__()"的注释相同.仅当对象支持删除键时,才应为
   映射实现此功能;如果可以从序列中删除元素,则应为序列实现此功能.对于不正确的*key*值,应引
   发与"__getitem__()"方法相同的异常.

object.__missing__(self, key)

   由"dict"调用"__getitem__()"以在键不在字典中时为dict子类实现"self[key]".

object.__iter__(self)

   当容器需要迭代器时,调用此方法.这个方法应该返回一个新的迭代器对象,它可以遍历容器中的所
   有对象.对于映射,它应该迭代容器的键.

   迭代器对象也需要实现这个方法;他们必须自己返回.

object.__reversed__(self)

   由内置的"reversed()"调用(如果存在)以实现反向迭代.它应该返回一个新的迭代器对象,该对象
   以相反的顺序遍历容器中的所有对象.

   如果未提供"__reversed__()"方法,则内置的"reversed()"将退回到使用序列协议
   ("__len__()"和"__getitem__()").如果支持序列协议的对象能够提供比"reversed()"提供的
   实现更高效的实现,则它们只应提供"__reversed__()".

    成员资格测试操作符("in"和"not in")通常作为通过容器的迭代来实现.但是,容器对象可以为
    以下特殊方法提供更高效的实现,这也不要求对象是可移植的.

object.__contains__(self, item)

   调用以实现成员资格测试操作符.如果*item*在*self*中,则应返回true,否则返回false.对于映
   射对象,应考虑映射的键,而不是值或键项对.

   对于未定义"__contains__()"的对象,成员资格测试首先通过"__iter__()"尝试迭代,然后通过
   "__getitem__()"尝试旧序列迭代协议.

Emulating numeric types(模拟数字类型)
===================================

可以定义以下方法来模拟数值对象.与实现的特定类型的数字不支持的操作相对应的方法(例如,非整数
的按位操作)应保持未定义.

object.__add__(self, other)             +
object.__sub__(self, other)             -
object.__mul__(self, other)             *
object.__matmul__(self, other)          @
object.__truediv__(self, other)         /
object.__floordiv__(self, other)        //
object.__mod__(self, other)             %
object.__divmod__(self, other)          divmod()
object.__pow__(self, other[, modulo])   **
object.__lshift__(self, other)          <<
object.__rshift__(self, other)          >>
object.__and__(self, other)             &
object.__xor__(self, other)             ^
object.__or__(self, other)              |

   调用这些方法是为了实现二进制算术运算("+", "-", "*", "@", "/", "//", "%",
   "divmod()","pow()", "**", "<<", ">>", "&", "^", "|").例如,要计算表达式"x + y",
   其中*x*是具有"__add__()"方法的类的实例,将调用"x.__add__(y)"."__divmod__()"方法应
   等同于使用"__floordiv__()"和"__mod__()";它不应该与"__truediv__()"相关.请注意,如
   果要支持内置"pow()"函数的三元版本,则应将"__pow__()"定义为接受可选的第三个参数.

   如果其中一个方法不支持带有提供参数的操作,则应返回"NotImplemented".

object.__radd__(self, other)                +
object.__rsub__(self, other)                -
object.__rmul__(self, other)                *
object.__rmatmul__(self, other)             @
object.__rtruediv__(self, other)            /
object.__rfloordiv__(self, other)           //
object.__rmod__(self, other)                %
object.__rdivmod__(self, other)             divmod()
object.__rpow__(self, other[, modulo])      **
object.__rlshift__(self, other)             <<
object.__rrshift__(self, other)             >>
object.__rand__(self, other)                &
object.__rxor__(self, other)                ^
object.__ror__(self, other)                 |

   调用这些方法是为了实现具有反射(swapped(交换))操作数的二进制算术运算("+", "-", "*",
   "@", "/", "//", "%", "divmod()","pow()", "**", "<<", ">>", "&", "^", "|").
   仅当左操作数不支持相应的操作且操作数类型不同时,才会调用这些函数.例如,要计算表达式
   "x - y",其中*y*是具有"__rsub__()"方法的类的实例,如果"x.__sub__(y)"返回
   *NotImplemented*,则调用"y.__rsub__(x)".

   请注意,三元"pow()"不会尝试调用"__rpow__()"(强制规则将变得太复杂).

   Note:

     如果右操作数的类型是左操作数类型的子类,并且该子类为操作提供了反射方法的不同实现,则将
     在左操作数的非反射方法之前调用此方法.此行为允许子类重写其祖先的操作.

object.__iadd__(self, other)                +=
object.__isub__(self, other)                -=
object.__imul__(self, other)                *=
object.__imatmul__(self, other)             @=
object.__itruediv__(self, other)            /=
object.__ifloordiv__(self, other)           //=
object.__imod__(self, other)                %=
object.__ipow__(self, other[, modulo])      **=
object.__ilshift__(self, other)             <<=
object.__irshift__(self, other)             >>=
object.__iand__(self, other)                &=
object.__ixor__(self, other)                ^=
object.__ior__(self, other)                 |=

   调用这些方法来实现增广算术赋值("+=", "-=", "*=", "@=", "/=", "//=", "%=", "**=",
   "<<=", ">>=", "&=", "^=", "|=").这些方法应该尝试就地执行操作(修改*self*)并返回结
   果(可能是但不一定是*self*).如果未定义特定的方法,则扩充赋值将返回到正常方法.例如,如果
   *x*是具有"__iadd__()"方法的类的实例,"x += y"相当于"x = x.__iadd__(y)".否则,与
   "x + y"的评估一样,将考虑"x.__add__(y)"和"y.__radd__(x)".在某些情况下,扩充赋值可能
   会导致意外错误,但这种行为实际上是数据模型的一部分.

   Note:

     由于"**="的调度机制中存在错误,定义"__ipow__()"但返回"NotImplemented"
     的类将无法返回到"x.__pow__(y)"和"y.__rpow__(x)".Python 3.10中修
     复了此错误.

object.__neg__(self)        -
object.__pos__(self)        +
object.__abs__(self)        abs()
object.__invert__(self)     ~

   调用以实现一元算术运算("-", "+","abs()" and "~").

object.__complex__(self)        complex()
object.__int__(self)            int()
object.__float__(self)          float()

   调用以实现内置函数"complex()"、"int()"和"float()".应返回适当类型的值.

object.__index__(self)          operator.index()

   调用以实现"operator.index()",并且每当Python需要无损地将数值对象转换为整数对象时(例
   如在切片中,或在内置的"bin()"、"hex()"和"oct()"函数中).存在此方法表示数值对象是整数
   类型.必须返回一个整数.

   如果未定义"__int__()"、"__float__()"和"__complex__()",则相应的内置函数"int()"、
   "float()"和"complex()"将返回到"__index__()".

object.__round__(self[, ndigits])       round()
object.__trunc__(self)                  trunc()
object.__floor__(self)                  floor()
object.__ceil__(self)                   ceil()

   调用以实现内置函数"round()"和math函数"trunc()"、"floor()"和"ceil()".除非将
   *ndigits*传递给"__round__()",否则所有这些方法都应将对象的值截断为"整数"(通常为"int
   ").

   如果未定义"__int__()",则内置函数"int()"返回到"__trunc__()".

With Statement Context Managers(使用语句上下文管理器)
==================================================

*context manager*是一个对象,它定义了在执行"with"语句时要建立的运行时上下文.上下文管理
器处理执行代码块所需的运行时上下文的入口和出口.上下文管理器通常使用"with"语句调用,但也可
以通过直接调用其方法来使用.

上下文管理器的典型用途包括保存和恢复各种全局状态、锁定和解锁资源、关闭打开的文件等.

object.__enter__(self)

   输入与此对象相关的运行时上下文."with"语句将此方法的返回值绑定到语句的"as"子句中指定的
   目标(如果有).

object.__exit__(self,exc_type,exc_value,traceback)

   退出与此对象相关的运行时上下文.这些参数描述导致上下文退出的异常.如果上下文无异常退出,
   则所有三个参数都将为"None".

   如果提供了异常,并且该方法希望抑制该异常(即防止其传播),则该方法应返回真值.否则,在
   退出此方法时将正常处理异常.

   请注意,"__exit__()"方法不应重新释放传入的异常;这是調用者的责任.

Special method lookup(特殊方法查找)
=================================

对于自定义类,只有在对象的类型上定义了特殊方法的隐式调用,而不是在对象的实例字典中定义了特殊
方法的隐式调用,才能保证其正常工作.该行为是以下代码引发异常的原因:

   >>> class C:
   ...     pass
   ...
   >>> c = C()
   >>> c.__len__ = lambda: 5
   >>> len(c)
   Traceback (most recent call last):
     File "<stdin>",line 1,in <module>
   TypeError: object of type 'C' has no len()

这种行为背后的基本原理在于许多特殊方法,如"__hash__()"和"__repr__()",它们由所有对象(包
括类型对象)实现.如果这些方法的隐式查找使用常规查找过程,则在对类型对象本身调用时,它们将失败
:

   >>> 1 .__hash__() == hash(1)
   True
   >>> int.__hash__() == hash(int)
   Traceback (most recent call last):
     File "<stdin>",line 1,in <module>
   TypeError: descriptor '__hash__' of 'int' object needs an argument

以这种方式错误地调用类的未绑定方法有时被称为"metaclass confusion(元类混淆)",通过在查找
特殊方法时绕过实例来避免:

   >>> type(1).__hash__(1) == hash(1)
   True
   >>> type(int).__hash__(int) == hash(int)
   True

除了为了正确性而绕过任何实例属性外,隐式特殊方法查找通常也会绕过对象元类的
"__getattribute__()"方法:

   >>> class Meta(type):
   ...     def __getattribute__(*args):
   ...         print("Metaclass getattribute invoked")
   ...         return type.__getattribute__(*args)
   ...
   >>> class C(object,metaclass=Meta):
   ...     def __len__(self):
   ...         return 10
   ...     def __getattribute__(*args):
   ...         print("Class getattribute invoked")
   ...         return object.__getattribute__(*args)
   ...
   >>> c = C()
   >>> c.__len__()                 # 通过实例显式查找
   Class getattribute invoked
   10
   >>> type(c).__len__(c)          # 通过类型显式查找
   Metaclass getattribute invoked
   10
   >>> len(c)                      # 隐式查找
   10
以这种方式绕过"__getattribute__()"机制为解释器内的速度优化提供了很大的空间,但代价是牺牲
处理特殊方法的灵活性(特殊方法*must*设置在类对象本身上,以便解释器一致地调用).
"""