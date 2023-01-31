"""
NAME
    pickle - Create portable serialized representations of Python objects.

MODULE REFERENCE
    https://docs.python.org/3.9/library/pickle

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    See module copyreg for a mechanism for registering custom picklers.
    See module pickletools source for extensive comments.

    Classes:

        Pickler
        Unpickler

    Functions:

        dump(object, file)
        dumps(object) -> string
        load(file) -> object
        loads(bytes) -> object

    Misc variables:

        __version__
        format_version
        compatible_formats

CLASSES
    builtins.Exception(builtins.BaseException)
        _pickle.PickleError
            _pickle.PicklingError
            _pickle.UnpicklingError
    builtins.object
        _pickle.Pickler
        _pickle.Unpickler
        PickleBuffer

    class PickleBuffer(builtins.object)
     |  Wrapper for potentially out-of-band buffers
     |
     |  Methods defined here:
     |
     |  raw(self, /)
     |      Return a memoryview of the raw memory underlying this buffer.
     |      Will raise BufferError is the buffer isn't contiguous.
     |
     |  release(self, /)
     |      Release the underlying buffer exposed by the PickleBuffer object.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

    class PickleError(builtins.Exception)
     |  Method resolution order:
     |      PickleError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class Pickler(builtins.object)
     |  Pickler(file, protocol=None, fix_imports=True, buffer_callback=None)
     |
     |  This takes a binary file for writing a pickle data stream.
     |
     |  The optional *protocol* argument tells the pickler to use the given
     |  protocol; supported protocols are 0, 1, 2, 3, 4 and 5.  The default
     |  protocol is 4. It was introduced in Python 3.4, and is incompatible
     |  with previous versions.
     |
     |  Specifying a negative protocol version selects the highest protocol
     |  version supported.  The higher the protocol used, the more recent the
     |  version of Python needed to read the pickle produced.
     |
     |  The *file* argument must have a write() method that accepts a single
     |  bytes argument. It can thus be a file object opened for binary
     |  writing, an io.BytesIO instance, or any other custom object that meets
     |  this interface.
     |
     |  If *fix_imports* is True and protocol is less than 3, pickle will try
     |  to map the new Python 3 names to the old module names used in Python
     |  2, so that the pickle data stream is readable with Python 2.
     |
     |  If *buffer_callback* is None (the default), buffer views are
     |  serialized into *file* as part of the pickle stream.
     |
     |  If *buffer_callback* is not None, then it can be called any number
     |  of times with a buffer view.  If the callback returns a false value
     |  (such as None), the given buffer is out-of-band; otherwise the
     |  buffer is serialized in-band, i.e. inside the pickle stream.
     |
     |  It is an error if *buffer_callback* is not None and *protocol*
     |  is None or smaller than 5.
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __sizeof__(self, /)
     |      Returns size in memory, in bytes.
     |
     |  clear_memo(self, /)
     |      Clears the pickler's "memo".
     |
     |      The memo is the data structure that remembers which objects the
     |      pickler has already seen, so that shared or recursive objects are
     |      pickled by reference and not by value.  This method is useful when
     |      re-using picklers.
     |
     |  dump(self, obj, /)
     |      Write a pickled representation of the given object to the open file.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  bin
     |
     |  dispatch_table
     |
     |  fast
     |
     |  memo
     |
     |  persistent_id

    class PicklingError(PickleError)
     |  Method resolution order:
     |      PicklingError
     |      PickleError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from PickleError:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class Unpickler(builtins.object)
     |  Unpickler(file, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=())
     |
     |  This takes a binary file for reading a pickle data stream.
     |
     |  The protocol version of the pickle is detected automatically, so no
     |  protocol argument is needed.  Bytes past the pickled object's
     |  representation are ignored.
     |
     |  The argument *file* must have two methods, a read() method that takes
     |  an integer argument, and a readline() method that requires no
     |  arguments.  Both methods should return bytes.  Thus *file* can be a
     |  binary file object opened for reading, an io.BytesIO object, or any
     |  other custom object that meets this interface.
     |
     |  Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
     |  which are used to control compatibility support for pickle stream
     |  generated by Python 2.  If *fix_imports* is True, pickle will try to
     |  map the old Python 2 names to the new names used in Python 3.  The
     |  *encoding* and *errors* tell pickle how to decode 8-bit string
     |  instances pickled by Python 2; these default to 'ASCII' and 'strict',
     |  respectively.  The *encoding* can be 'bytes' to read these 8-bit
     |  string instances as bytes objects.
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __sizeof__(self, /)
     |      Returns size in memory, in bytes.
     |
     |  find_class(self, module_name, global_name, /)
     |      Return an object from a specified module.
     |
     |      If necessary, the module will be imported. Subclasses may override
     |      this method (e.g. to restrict unpickling of arbitrary classes and
     |      functions).
     |
     |      This method is called whenever a class or a function object is
     |      needed.  Both arguments passed are str objects.
     |
     |  load(self, /)
     |      Load a pickle.
     |
     |      Read a pickled object representation from the open file object given
     |      in the constructor, and return the reconstituted object hierarchy
     |      specified therein.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  memo
     |
     |  persistent_load

    class UnpicklingError(PickleError)
     |  Method resolution order:
     |      UnpicklingError
     |      PickleError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from PickleError:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

FUNCTIONS
    dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
        Write a pickled representation of obj to the open file object file.

        This is equivalent to ``Pickler(file, protocol).dump(obj)``, but may
        be more efficient.

        The optional *protocol* argument tells the pickler to use the given
        protocol; supported protocols are 0, 1, 2, 3, 4 and 5.  The default
        protocol is 4. It was introduced in Python 3.4, and is incompatible
        with previous versions.

        Specifying a negative protocol version selects the highest protocol
        version supported.  The higher the protocol used, the more recent the
        version of Python needed to read the pickle produced.

        The *file* argument must have a write() method that accepts a single
        bytes argument.  It can thus be a file object opened for binary
        writing, an io.BytesIO instance, or any other custom object that meets
        this interface.

        If *fix_imports* is True and protocol is less than 3, pickle will try
        to map the new Python 3 names to the old module names used in Python
        2, so that the pickle data stream is readable with Python 2.

        If *buffer_callback* is None (the default), buffer views are serialized
        into *file* as part of the pickle stream.  It is an error if
        *buffer_callback* is not None and *protocol* is None or smaller than 5.

    dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
        Return the pickled representation of the object as a bytes object.

        The optional *protocol* argument tells the pickler to use the given
        protocol; supported protocols are 0, 1, 2, 3, 4 and 5.  The default
        protocol is 4. It was introduced in Python 3.4, and is incompatible
        with previous versions.

        Specifying a negative protocol version selects the highest protocol
        version supported.  The higher the protocol used, the more recent the
        version of Python needed to read the pickle produced.

        If *fix_imports* is True and *protocol* is less than 3, pickle will
        try to map the new Python 3 names to the old module names used in
        Python 2, so that the pickle data stream is readable with Python 2.

        If *buffer_callback* is None (the default), buffer views are serialized
        into *file* as part of the pickle stream.  It is an error if
        *buffer_callback* is not None and *protocol* is None or smaller than 5.

    load(file, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=())
        Read and return an object from the pickle data stored in a file.

        This is equivalent to ``Unpickler(file).load()``, but may be more
        efficient.

        The protocol version of the pickle is detected automatically, so no
        protocol argument is needed.  Bytes past the pickled object's
        representation are ignored.

        The argument *file* must have two methods, a read() method that takes
        an integer argument, and a readline() method that requires no
        arguments.  Both methods should return bytes.  Thus *file* can be a
        binary file object opened for reading, an io.BytesIO object, or any
        other custom object that meets this interface.

        Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
        which are used to control compatibility support for pickle stream
        generated by Python 2.  If *fix_imports* is True, pickle will try to
        map the old Python 2 names to the new names used in Python 3.  The
        *encoding* and *errors* tell pickle how to decode 8-bit string
        instances pickled by Python 2; these default to 'ASCII' and 'strict',
        respectively.  The *encoding* can be 'bytes' to read these 8-bit
        string instances as bytes objects.

    loads(data, /, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=())
        Read and return an object from the given pickle data.

        The protocol version of the pickle is detected automatically, so no
        protocol argument is needed.  Bytes past the pickled object's
        representation are ignored.

        Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
        which are used to control compatibility support for pickle stream
        generated by Python 2.  If *fix_imports* is True, pickle will try to
        map the old Python 2 names to the new names used in Python 3.  The
        *encoding* and *errors* tell pickle how to decode 8-bit string
        instances pickled by Python 2; these default to 'ASCII' and 'strict',
        respectively.  The *encoding* can be 'bytes' to read these 8-bit
        string instances as bytes objects.

DATA
    ADDITEMS = b'\x90'
    APPEND = b'a'
    APPENDS = b'e'
    BINBYTES = b'B'
    BINBYTES8 = b'\x8e'
    BINFLOAT = b'G'
    BINGET = b'h'
    BININT = b'J'
    BININT1 = b'K'
    BININT2 = b'M'
    BINPERSID = b'Q'
    BINPUT = b'q'
    BINSTRING = b'T'
    BINUNICODE = b'X'
    BINUNICODE8 = b'\x8d'
    BUILD = b'b'
    BYTEARRAY8 = b'\x96'
    DEFAULT_PROTOCOL = 4
    DICT = b'd'
    DUP = b'2'
    EMPTY_DICT = b'}'
    EMPTY_LIST = b']'
    EMPTY_SET = b'\x8f'
    EMPTY_TUPLE = b')'
    EXT1 = b'\x82'
    EXT2 = b'\x83'
    EXT4 = b'\x84'
    FALSE = b'I00\n'
    FLOAT = b'F'
    FRAME = b'\x95'
    FROZENSET = b'\x91'
    GET = b'g'
    GLOBAL = b'c'
    HIGHEST_PROTOCOL = 5
    INST = b'i'
    INT = b'I'
    LIST = b'l'
    LONG = b'L'
    LONG1 = b'\x8a'
    LONG4 = b'\x8b'
    LONG_BINGET = b'j'
    LONG_BINPUT = b'r'
    MARK = b'('
    MEMOIZE = b'\x94'
    NEWFALSE = b'\x89'
    NEWOBJ = b'\x81'
    NEWOBJ_EX = b'\x92'
    NEWTRUE = b'\x88'
    NEXT_BUFFER = b'\x97'
    NONE = b'N'
    OBJ = b'o'
    PERSID = b'P'
    POP = b'0'
    POP_MARK = b'1'
    PROTO = b'\x80'
    PUT = b'p'
    READONLY_BUFFER = b'\x98'
    REDUCE = b'R'
    SETITEM = b's'
    SETITEMS = b'u'
    SHORT_BINBYTES = b'C'
    SHORT_BINSTRING = b'U'
    SHORT_BINUNICODE = b'\x8c'
    STACK_GLOBAL = b'\x93'
    STOP = b'.'
    STRING = b'S'
    TRUE = b'I01\n'
    TUPLE = b't'
    TUPLE1 = b'\x85'
    TUPLE2 = b'\x86'
    TUPLE3 = b'\x87'
    UNICODE = b'V'
    __all__ = ['PickleError', 'PicklingError', 'UnpicklingError', 'Pickler...

FILE
    d:\software\python\python39\lib\pickle.py
"""