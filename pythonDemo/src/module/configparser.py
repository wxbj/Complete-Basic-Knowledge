"""
NAME
    configparser - Configuration file parser.

MODULE REFERENCE
    https://docs.python.org/3.9/library/configparser

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    A configuration file consists of sections, lead by a "[section]" header,
    and followed by "name: value" entries, with continuations and such in
    the style of RFC 822.

    Intrinsic defaults can be specified by passing them into the
    ConfigParser constructor as a dictionary.

    class:

    ConfigParser -- responsible for parsing a list of
                        configuration files, and managing the parsed database.

        methods:

        __init__(defaults=None, dict_type=_default_dict, allow_no_value=False,
                 delimiters=('=', ':'), comment_prefixes=('#', ';'),
                 inline_comment_prefixes=None, strict=True,
                 empty_lines_in_values=True, default_section='DEFAULT',
                 interpolation=<unset>, converters=<unset>):
            Create the parser. When `defaults' is given, it is initialized into the
            dictionary or intrinsic defaults. The keys must be strings, the values
            must be appropriate for %()s string interpolation.

            When `dict_type' is given, it will be used to create the dictionary
            objects for the list of sections, for the options within a section, and
            for the default values.

            When `delimiters' is given, it will be used as the set of substrings
            that divide keys from values.

            When `comment_prefixes' is given, it will be used as the set of
            substrings that prefix comments in empty lines. Comments can be
            indented.

            When `inline_comment_prefixes' is given, it will be used as the set of
            substrings that prefix comments in non-empty lines.

            When `strict` is True, the parser won't allow for any section or option
            duplicates while reading from a single source (file, string or
            dictionary). Default is True.

            When `empty_lines_in_values' is False (default: True), each empty line
            marks the end of an option. Otherwise, internal empty lines of
            a multiline option are kept as part of the value.

            When `allow_no_value' is True (default: False), options without
            values are accepted; the value presented for these is None.

            When `default_section' is given, the name of the special section is
            named accordingly. By default it is called ``"DEFAULT"`` but this can
            be customized to point to any other valid section name. Its current
            value can be retrieved using the ``parser_instance.default_section``
            attribute and may be modified at runtime.

            When `interpolation` is given, it should be an Interpolation subclass
            instance. It will be used as the handler for option value
            pre-processing when using getters. RawConfigParser objects don't do
            any sort of interpolation, whereas ConfigParser uses an instance of
            BasicInterpolation. The library also provides a ``zc.buildbot``
            inspired ExtendedInterpolation implementation.

            When `converters` is given, it should be a dictionary where each key
            represents the name of a type converter and each value is a callable
            implementing the conversion from string to the desired datatype. Every
            converter gets its corresponding get*() method on the parser object and
            section proxies.

        sections()
            Return all the configuration section names, sans DEFAULT.

        has_section(section)
            Return whether the given section exists.

        has_option(section, option)
            Return whether the given option exists in the given section.

        options(section)
            Return list of configuration options for the named section.

        read(filenames, encoding=None)
            Read and parse the iterable of named configuration files, given by
            name.  A single filename is also allowed.  Non-existing files
            are ignored.  Return list of successfully read files.

        read_file(f, filename=None)
            Read and parse one configuration file, given as a file object.
            The filename defaults to f.name; it is only used in error
            messages (if f has no `name' attribute, the string `<???>' is used).

        read_string(string)
            Read configuration from a given string.

        read_dict(dictionary)
            Read configuration from a dictionary. Keys are section names,
            values are dictionaries with keys and values that should be present
            in the section. If the used dictionary type preserves order, sections
            and their keys will be added in order. Values are automatically
            converted to strings.

        get(section, option, raw=False, vars=None, fallback=_UNSET)
            Return a string value for the named option.  All % interpolations are
            expanded in the return values, based on the defaults passed into the
            constructor and the DEFAULT section.  Additional substitutions may be
            provided using the `vars' argument, which must be a dictionary whose
            contents override any pre-existing defaults. If `option' is a key in
            `vars', the value from `vars' is used.

        getint(section, options, raw=False, vars=None, fallback=_UNSET)
            Like get(), but convert value to an integer.

        getfloat(section, options, raw=False, vars=None, fallback=_UNSET)
            Like get(), but convert value to a float.

        getboolean(section, options, raw=False, vars=None, fallback=_UNSET)
            Like get(), but convert value to a boolean (currently case
            insensitively defined as 0, false, no, off for False, and 1, true,
            yes, on for True).  Returns False or True.

        items(section=_UNSET, raw=False, vars=None)
            If section is given, return a list of tuples with (name, value) for
            each option in the section. Otherwise, return a list of tuples with
            (section_name, section_proxy) for each section, including DEFAULTSECT.

        remove_section(section)
            Remove the given file section and all its options.

        remove_option(section, option)
            Remove the given option from the given section.

        set(section, option, value)
            Set the given option.

        write(fp, space_around_delimiters=True)
            Write the configuration state in .ini format. If
            `space_around_delimiters' is True (the default), delimiters
            between keys and values are surrounded by spaces.

CLASSES
    builtins.object
        Interpolation
            BasicInterpolation
            ExtendedInterpolation
            LegacyInterpolation
    collections.abc.MutableMapping(collections.abc.Mapping)
        ConverterMapping
        RawConfigParser
            ConfigParser
                SafeConfigParser
        SectionProxy
    Error(builtins.Exception)
        DuplicateOptionError
        DuplicateSectionError
        InterpolationError
            InterpolationDepthError
            InterpolationMissingOptionError
            InterpolationSyntaxError
        NoOptionError
        NoSectionError
        ParsingError
            MissingSectionHeaderError

    class BasicInterpolation(Interpolation)
     |  Interpolation as implemented in the classic ConfigParser.
     |
     |  The option values can contain format strings which refer to other values in
     |  the same section, or values in the special default section.
     |
     |  For example:
     |
     |      something: %(dir)s/whatever
     |
     |  would resolve the "%(dir)s" to the value of dir.  All reference
     |  expansions are done late, on demand. If a user needs to use a bare % in
     |  a configuration file, she can escape it by writing %%. Other % usage
     |  is considered a user error and raises `InterpolationSyntaxError'.
     |
     |  Method resolution order:
     |      BasicInterpolation
     |      Interpolation
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  before_get(self, parser, section, option, value, defaults)
     |
     |  before_set(self, parser, section, option, value)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Interpolation:
     |
     |  before_read(self, parser, section, option, value)
     |
     |  before_write(self, parser, section, option, value)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Interpolation:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class ConfigParser(RawConfigParser)
     |  ConfigParser(defaults=None, dict_type=<class 'dict'>, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section='DEFAULT', interpolation=<object object at 0x0000018E8DA18960>, converters=<object object at 0x0000018E8DA18960>)
     |
     |  ConfigParser implementing interpolation.
     |
     |  Method resolution order:
     |      ConfigParser
     |      RawConfigParser
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  add_section(self, section)
     |      Create a new section in the configuration.  Extends
     |      RawConfigParser.add_section by validating if the section name is
     |      a string.
     |
     |  set(self, section, option, value=None)
     |      Set an option.  Extends RawConfigParser.set by validating type and
     |      interpolation syntax on the value.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset()
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from RawConfigParser:
     |
     |  __contains__(self, key)
     |
     |  __delitem__(self, key)
     |
     |  __getitem__(self, key)
     |
     |  __init__(self, defaults=None, dict_type=<class 'dict'>, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section='DEFAULT', interpolation=<object object at 0x0000018E8DA18960>, converters=<object object at 0x0000018E8DA18960>)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self)
     |
     |  __len__(self)
     |
     |  __setitem__(self, key, value)
     |
     |  defaults(self)
     |
     |  get(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>)
     |      Get an option value for a given section.
     |
     |      If `vars' is provided, it must be a dictionary. The option is looked up
     |      in `vars' (if provided), `section', and in `DEFAULTSECT' in that order.
     |      If the key is not found and `fallback' is provided, it is used as
     |      a fallback value. `None' can be provided as a `fallback' value.
     |
     |      If interpolation is enabled and the optional argument `raw' is False,
     |      all interpolations are expanded in the return values.
     |
     |      Arguments `raw', `vars', and `fallback' are keyword only.
     |
     |      The section DEFAULT is special.
     |
     |  getboolean(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |
     |  getfloat(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |
     |  getint(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |      # getint, getfloat and getboolean provided directly for backwards compat
     |
     |  has_option(self, section, option)
     |      Check for the existence of a given option in a given section.
     |      If the specified `section' is None or an empty string, DEFAULT is
     |      assumed. If the specified `section' does not exist, returns False.
     |
     |  has_section(self, section)
     |      Indicate whether the named section is present in the configuration.
     |
     |      The DEFAULT section is not acknowledged.
     |
     |  items(self, section=<object object at 0x0000018E8DA18960>, raw=False, vars=None)
     |      Return a list of (name, value) tuples for each option in a section.
     |
     |      All % interpolations are expanded in the return values, based on the
     |      defaults passed into the constructor, unless the optional argument
     |      `raw' is true.  Additional substitutions may be provided using the
     |      `vars' argument, which must be a dictionary whose contents overrides
     |      any pre-existing defaults.
     |
     |      The section DEFAULT is special.
     |
     |  options(self, section)
     |      Return a list of option names for the given section name.
     |
     |  optionxform(self, optionstr)
     |
     |  popitem(self)
     |      Remove a section from the parser and return it as
     |      a (section_name, section_proxy) tuple. If no section is present, raise
     |      KeyError.
     |
     |      The section DEFAULT is never returned because it cannot be removed.
     |
     |  read(self, filenames, encoding=None)
     |      Read and parse a filename or an iterable of filenames.
     |
     |      Files that cannot be opened are silently ignored; this is
     |      designed so that you can specify an iterable of potential
     |      configuration file locations (e.g. current directory, user's
     |      home directory, systemwide directory), and all existing
     |      configuration files in the iterable will be read.  A single
     |      filename may also be given.
     |
     |      Return list of successfully read files.
     |
     |  read_dict(self, dictionary, source='<dict>')
     |      Read configuration from a dictionary.
     |
     |      Keys are section names, values are dictionaries with keys and values
     |      that should be present in the section. If the used dictionary type
     |      preserves order, sections and their keys will be added in order.
     |
     |      All types held in the dictionary are converted to strings during
     |      reading, including section names, option names and keys.
     |
     |      Optional second argument is the `source' specifying the name of the
     |      dictionary being read.
     |
     |  read_file(self, f, source=None)
     |      Like read() but the argument must be a file-like object.
     |
     |      The `f' argument must be iterable, returning one line at a time.
     |      Optional second argument is the `source' specifying the name of the
     |      file being read. If not given, it is taken from f.name. If `f' has no
     |      `name' attribute, `<???>' is used.
     |
     |  read_string(self, string, source='<string>')
     |      Read configuration from a given string.
     |
     |  readfp(self, fp, filename=None)
     |      Deprecated, use read_file instead.
     |
     |  remove_option(self, section, option)
     |      Remove an option.
     |
     |  remove_section(self, section)
     |      Remove a file section.
     |
     |  sections(self)
     |      Return a list of section names, excluding [DEFAULT]
     |
     |  write(self, fp, space_around_delimiters=True)
     |      Write an .ini-format representation of the configuration state.
     |
     |      If `space_around_delimiters' is True (the default), delimiters
     |      between keys and values are surrounded by spaces.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from RawConfigParser:
     |
     |  converters
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RawConfigParser:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from RawConfigParser:
     |
     |  BOOLEAN_STATES = {'0': False, '1': True, 'false': False, 'no': False, ...
     |
     |  NONSPACECRE = re.compile('\\S')
     |
     |  OPTCRE = re.compile('\n        (?P<option>.*?)           ...          ...
     |
     |  OPTCRE_NV = re.compile('\n        (?P<option>.*?)           ...       ...
     |
     |  SECTCRE = re.compile('\n        \\[                       ...         ...
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |
     |  pop(self, key, default=<object object at 0x0000018E8DA18160>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |
     |  update(self, other=(), /, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |
     |  __hash__ = None
     |
     |  __reversed__ = None
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Iterable:
     |
     |  __class_getitem__ = GenericAlias(...) from abc.ABCMeta
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).

    class ConverterMapping(collections.abc.MutableMapping)
     |  ConverterMapping(parser)
     |
     |  Enables reuse of get*() methods between the parser and section proxies.
     |
     |  If a parser class implements a getter directly, the value for the given
     |  key will be ``None``. The presence of the converter name here enables
     |  section proxies to find and use the implementation on the parser class.
     |
     |  Method resolution order:
     |      ConverterMapping
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __delitem__(self, key)
     |
     |  __getitem__(self, key)
     |
     |  __init__(self, parser)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self)
     |
     |  __len__(self)
     |
     |  __setitem__(self, key, value)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  GETTERCRE = re.compile('^get(?P<name>.+)$')
     |
     |  __abstractmethods__ = frozenset()
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |
     |  pop(self, key, default=<object object at 0x0000018E8DA18160>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |
     |  popitem(self)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair
     |      as a 2-tuple; but raise KeyError if D is empty.
     |
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |
     |  update(self, other=(), /, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |
     |  __contains__(self, key)
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  get(self, key, default=None)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |
     |  items(self)
     |      D.items() -> a set-like object providing a view on D's items
     |
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |
     |  __hash__ = None
     |
     |  __reversed__ = None
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Iterable:
     |
     |  __class_getitem__ = GenericAlias(...) from abc.ABCMeta
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).

    class DuplicateOptionError(Error)
     |  DuplicateOptionError(section, option, source=None, lineno=None)
     |
     |  Raised by strict parsers when an option is repeated in an input source.
     |
     |  Current implementation raises this exception only when an option is found
     |  more than once in a single file, string or dictionary.
     |
     |  Method resolution order:
     |      DuplicateOptionError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, section, option, source=None, lineno=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class DuplicateSectionError(Error)
     |  DuplicateSectionError(section, source=None, lineno=None)
     |
     |  Raised when a section is repeated in an input source.
     |
     |  Possible repetitions that raise this exception are: multiple creation
     |  using the API or in strict parsers when a section is found more than once
     |  in a single input file, string or dictionary.
     |
     |  Method resolution order:
     |      DuplicateSectionError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, section, source=None, lineno=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class ExtendedInterpolation(Interpolation)
     |  Advanced variant of interpolation, supports the syntax used by
     |  `zc.buildout'. Enables interpolation between sections.
     |
     |  Method resolution order:
     |      ExtendedInterpolation
     |      Interpolation
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  before_get(self, parser, section, option, value, defaults)
     |
     |  before_set(self, parser, section, option, value)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Interpolation:
     |
     |  before_read(self, parser, section, option, value)
     |
     |  before_write(self, parser, section, option, value)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Interpolation:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class Interpolation(builtins.object)
     |  Dummy interpolation that passes the value through with no changes.
     |
     |  Methods defined here:
     |
     |  before_get(self, parser, section, option, value, defaults)
     |
     |  before_read(self, parser, section, option, value)
     |
     |  before_set(self, parser, section, option, value)
     |
     |  before_write(self, parser, section, option, value)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class InterpolationDepthError(InterpolationError)
     |  InterpolationDepthError(option, section, rawval)
     |
     |  Raised when substitutions are nested too deeply.
     |
     |  Method resolution order:
     |      InterpolationDepthError
     |      InterpolationError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, option, section, rawval)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class InterpolationError(Error)
     |  InterpolationError(option, section, msg)
     |
     |  Base class for interpolation-related exceptions.
     |
     |  Method resolution order:
     |      InterpolationError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, option, section, msg)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class InterpolationMissingOptionError(InterpolationError)
     |  InterpolationMissingOptionError(option, section, rawval, reference)
     |
     |  A string substitution required a setting which was not available.
     |
     |  Method resolution order:
     |      InterpolationMissingOptionError
     |      InterpolationError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, option, section, rawval, reference)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class InterpolationSyntaxError(InterpolationError)
     |  InterpolationSyntaxError(option, section, msg)
     |
     |  Raised when the source text contains invalid syntax.
     |
     |  Current implementation raises this exception when the source text into
     |  which substitutions are made does not conform to the required syntax.
     |
     |  Method resolution order:
     |      InterpolationSyntaxError
     |      InterpolationError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods inherited from InterpolationError:
     |
     |  __init__(self, option, section, msg)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class LegacyInterpolation(Interpolation)
     |  Deprecated interpolation used in old versions of ConfigParser.
     |  Use BasicInterpolation or ExtendedInterpolation instead.
     |
     |  Method resolution order:
     |      LegacyInterpolation
     |      Interpolation
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  before_get(self, parser, section, option, value, vars)
     |
     |  before_set(self, parser, section, option, value)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Interpolation:
     |
     |  before_read(self, parser, section, option, value)
     |
     |  before_write(self, parser, section, option, value)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Interpolation:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

    class MissingSectionHeaderError(ParsingError)
     |  MissingSectionHeaderError(filename, lineno, line)
     |
     |  Raised when a key-value pair is found before any section header.
     |
     |  Method resolution order:
     |      MissingSectionHeaderError
     |      ParsingError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, filename, lineno, line)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from ParsingError:
     |
     |  append(self, lineno, line)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from ParsingError:
     |
     |  filename
     |      Deprecated, use `source'.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class NoOptionError(Error)
     |  NoOptionError(option, section)
     |
     |  A requested option was not found.
     |
     |  Method resolution order:
     |      NoOptionError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, option, section)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class NoSectionError(Error)
     |  NoSectionError(section)
     |
     |  Raised when no section matches a requested option.
     |
     |  Method resolution order:
     |      NoSectionError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, section)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class ParsingError(Error)
     |  ParsingError(source=None, filename=None)
     |
     |  Raised when a configuration file does not follow legal syntax.
     |
     |  Method resolution order:
     |      ParsingError
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, source=None, filename=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  append(self, lineno, line)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  filename
     |      Deprecated, use `source'.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Error:
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __str__ = __repr__(self)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
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
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
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

    class RawConfigParser(collections.abc.MutableMapping)
     |  RawConfigParser(defaults=None, dict_type=<class 'dict'>, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section='DEFAULT', interpolation=<object object at 0x0000018E8DA18960>, converters=<object object at 0x0000018E8DA18960>)
     |
     |  ConfigParser that does not do interpolation.
     |
     |  Method resolution order:
     |      RawConfigParser
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __contains__(self, key)
     |
     |  __delitem__(self, key)
     |
     |  __getitem__(self, key)
     |
     |  __init__(self, defaults=None, dict_type=<class 'dict'>, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section='DEFAULT', interpolation=<object object at 0x0000018E8DA18960>, converters=<object object at 0x0000018E8DA18960>)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self)
     |
     |  __len__(self)
     |
     |  __setitem__(self, key, value)
     |
     |  add_section(self, section)
     |      Create a new section in the configuration.
     |
     |      Raise DuplicateSectionError if a section by the specified name
     |      already exists. Raise ValueError if name is DEFAULT.
     |
     |  defaults(self)
     |
     |  get(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>)
     |      Get an option value for a given section.
     |
     |      If `vars' is provided, it must be a dictionary. The option is looked up
     |      in `vars' (if provided), `section', and in `DEFAULTSECT' in that order.
     |      If the key is not found and `fallback' is provided, it is used as
     |      a fallback value. `None' can be provided as a `fallback' value.
     |
     |      If interpolation is enabled and the optional argument `raw' is False,
     |      all interpolations are expanded in the return values.
     |
     |      Arguments `raw', `vars', and `fallback' are keyword only.
     |
     |      The section DEFAULT is special.
     |
     |  getboolean(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |
     |  getfloat(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |
     |  getint(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |      # getint, getfloat and getboolean provided directly for backwards compat
     |
     |  has_option(self, section, option)
     |      Check for the existence of a given option in a given section.
     |      If the specified `section' is None or an empty string, DEFAULT is
     |      assumed. If the specified `section' does not exist, returns False.
     |
     |  has_section(self, section)
     |      Indicate whether the named section is present in the configuration.
     |
     |      The DEFAULT section is not acknowledged.
     |
     |  items(self, section=<object object at 0x0000018E8DA18960>, raw=False, vars=None)
     |      Return a list of (name, value) tuples for each option in a section.
     |
     |      All % interpolations are expanded in the return values, based on the
     |      defaults passed into the constructor, unless the optional argument
     |      `raw' is true.  Additional substitutions may be provided using the
     |      `vars' argument, which must be a dictionary whose contents overrides
     |      any pre-existing defaults.
     |
     |      The section DEFAULT is special.
     |
     |  options(self, section)
     |      Return a list of option names for the given section name.
     |
     |  optionxform(self, optionstr)
     |
     |  popitem(self)
     |      Remove a section from the parser and return it as
     |      a (section_name, section_proxy) tuple. If no section is present, raise
     |      KeyError.
     |
     |      The section DEFAULT is never returned because it cannot be removed.
     |
     |  read(self, filenames, encoding=None)
     |      Read and parse a filename or an iterable of filenames.
     |
     |      Files that cannot be opened are silently ignored; this is
     |      designed so that you can specify an iterable of potential
     |      configuration file locations (e.g. current directory, user's
     |      home directory, systemwide directory), and all existing
     |      configuration files in the iterable will be read.  A single
     |      filename may also be given.
     |
     |      Return list of successfully read files.
     |
     |  read_dict(self, dictionary, source='<dict>')
     |      Read configuration from a dictionary.
     |
     |      Keys are section names, values are dictionaries with keys and values
     |      that should be present in the section. If the used dictionary type
     |      preserves order, sections and their keys will be added in order.
     |
     |      All types held in the dictionary are converted to strings during
     |      reading, including section names, option names and keys.
     |
     |      Optional second argument is the `source' specifying the name of the
     |      dictionary being read.
     |
     |  read_file(self, f, source=None)
     |      Like read() but the argument must be a file-like object.
     |
     |      The `f' argument must be iterable, returning one line at a time.
     |      Optional second argument is the `source' specifying the name of the
     |      file being read. If not given, it is taken from f.name. If `f' has no
     |      `name' attribute, `<???>' is used.
     |
     |  read_string(self, string, source='<string>')
     |      Read configuration from a given string.
     |
     |  readfp(self, fp, filename=None)
     |      Deprecated, use read_file instead.
     |
     |  remove_option(self, section, option)
     |      Remove an option.
     |
     |  remove_section(self, section)
     |      Remove a file section.
     |
     |  sections(self)
     |      Return a list of section names, excluding [DEFAULT]
     |
     |  set(self, section, option, value=None)
     |      Set an option.
     |
     |  write(self, fp, space_around_delimiters=True)
     |      Write an .ini-format representation of the configuration state.
     |
     |      If `space_around_delimiters' is True (the default), delimiters
     |      between keys and values are surrounded by spaces.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  converters
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  BOOLEAN_STATES = {'0': False, '1': True, 'false': False, 'no': False, ...
     |
     |  NONSPACECRE = re.compile('\\S')
     |
     |  OPTCRE = re.compile('\n        (?P<option>.*?)           ...          ...
     |
     |  OPTCRE_NV = re.compile('\n        (?P<option>.*?)           ...       ...
     |
     |  SECTCRE = re.compile('\n        \\[                       ...         ...
     |
     |  __abstractmethods__ = frozenset()
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |
     |  pop(self, key, default=<object object at 0x0000018E8DA18160>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |
     |  update(self, other=(), /, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |
     |  __hash__ = None
     |
     |  __reversed__ = None
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Iterable:
     |
     |  __class_getitem__ = GenericAlias(...) from abc.ABCMeta
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).

    class SafeConfigParser(ConfigParser)
     |  SafeConfigParser(*args, **kwargs)
     |
     |  ConfigParser alias for backwards compatibility purposes.
     |
     |  Method resolution order:
     |      SafeConfigParser
     |      ConfigParser
     |      RawConfigParser
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset()
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from ConfigParser:
     |
     |  add_section(self, section)
     |      Create a new section in the configuration.  Extends
     |      RawConfigParser.add_section by validating if the section name is
     |      a string.
     |
     |  set(self, section, option, value=None)
     |      Set an option.  Extends RawConfigParser.set by validating type and
     |      interpolation syntax on the value.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from RawConfigParser:
     |
     |  __contains__(self, key)
     |
     |  __delitem__(self, key)
     |
     |  __getitem__(self, key)
     |
     |  __iter__(self)
     |
     |  __len__(self)
     |
     |  __setitem__(self, key, value)
     |
     |  defaults(self)
     |
     |  get(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>)
     |      Get an option value for a given section.
     |
     |      If `vars' is provided, it must be a dictionary. The option is looked up
     |      in `vars' (if provided), `section', and in `DEFAULTSECT' in that order.
     |      If the key is not found and `fallback' is provided, it is used as
     |      a fallback value. `None' can be provided as a `fallback' value.
     |
     |      If interpolation is enabled and the optional argument `raw' is False,
     |      all interpolations are expanded in the return values.
     |
     |      Arguments `raw', `vars', and `fallback' are keyword only.
     |
     |      The section DEFAULT is special.
     |
     |  getboolean(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |
     |  getfloat(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |
     |  getint(self, section, option, *, raw=False, vars=None, fallback=<object object at 0x0000018E8DA18960>, **kwargs)
     |      # getint, getfloat and getboolean provided directly for backwards compat
     |
     |  has_option(self, section, option)
     |      Check for the existence of a given option in a given section.
     |      If the specified `section' is None or an empty string, DEFAULT is
     |      assumed. If the specified `section' does not exist, returns False.
     |
     |  has_section(self, section)
     |      Indicate whether the named section is present in the configuration.
     |
     |      The DEFAULT section is not acknowledged.
     |
     |  items(self, section=<object object at 0x0000018E8DA18960>, raw=False, vars=None)
     |      Return a list of (name, value) tuples for each option in a section.
     |
     |      All % interpolations are expanded in the return values, based on the
     |      defaults passed into the constructor, unless the optional argument
     |      `raw' is true.  Additional substitutions may be provided using the
     |      `vars' argument, which must be a dictionary whose contents overrides
     |      any pre-existing defaults.
     |
     |      The section DEFAULT is special.
     |
     |  options(self, section)
     |      Return a list of option names for the given section name.
     |
     |  optionxform(self, optionstr)
     |
     |  popitem(self)
     |      Remove a section from the parser and return it as
     |      a (section_name, section_proxy) tuple. If no section is present, raise
     |      KeyError.
     |
     |      The section DEFAULT is never returned because it cannot be removed.
     |
     |  read(self, filenames, encoding=None)
     |      Read and parse a filename or an iterable of filenames.
     |
     |      Files that cannot be opened are silently ignored; this is
     |      designed so that you can specify an iterable of potential
     |      configuration file locations (e.g. current directory, user's
     |      home directory, systemwide directory), and all existing
     |      configuration files in the iterable will be read.  A single
     |      filename may also be given.
     |
     |      Return list of successfully read files.
     |
     |  read_dict(self, dictionary, source='<dict>')
     |      Read configuration from a dictionary.
     |
     |      Keys are section names, values are dictionaries with keys and values
     |      that should be present in the section. If the used dictionary type
     |      preserves order, sections and their keys will be added in order.
     |
     |      All types held in the dictionary are converted to strings during
     |      reading, including section names, option names and keys.
     |
     |      Optional second argument is the `source' specifying the name of the
     |      dictionary being read.
     |
     |  read_file(self, f, source=None)
     |      Like read() but the argument must be a file-like object.
     |
     |      The `f' argument must be iterable, returning one line at a time.
     |      Optional second argument is the `source' specifying the name of the
     |      file being read. If not given, it is taken from f.name. If `f' has no
     |      `name' attribute, `<???>' is used.
     |
     |  read_string(self, string, source='<string>')
     |      Read configuration from a given string.
     |
     |  readfp(self, fp, filename=None)
     |      Deprecated, use read_file instead.
     |
     |  remove_option(self, section, option)
     |      Remove an option.
     |
     |  remove_section(self, section)
     |      Remove a file section.
     |
     |  sections(self)
     |      Return a list of section names, excluding [DEFAULT]
     |
     |  write(self, fp, space_around_delimiters=True)
     |      Write an .ini-format representation of the configuration state.
     |
     |      If `space_around_delimiters' is True (the default), delimiters
     |      between keys and values are surrounded by spaces.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from RawConfigParser:
     |
     |  converters
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from RawConfigParser:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from RawConfigParser:
     |
     |  BOOLEAN_STATES = {'0': False, '1': True, 'false': False, 'no': False, ...
     |
     |  NONSPACECRE = re.compile('\\S')
     |
     |  OPTCRE = re.compile('\n        (?P<option>.*?)           ...          ...
     |
     |  OPTCRE_NV = re.compile('\n        (?P<option>.*?)           ...       ...
     |
     |  SECTCRE = re.compile('\n        \\[                       ...         ...
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |
     |  pop(self, key, default=<object object at 0x0000018E8DA18160>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |
     |  update(self, other=(), /, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |
     |  __hash__ = None
     |
     |  __reversed__ = None
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Iterable:
     |
     |  __class_getitem__ = GenericAlias(...) from abc.ABCMeta
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).

    class SectionProxy(collections.abc.MutableMapping)
     |  SectionProxy(parser, name)
     |
     |  A proxy for a single section from a parser.
     |
     |  Method resolution order:
     |      SectionProxy
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __contains__(self, key)
     |
     |  __delitem__(self, key)
     |
     |  __getitem__(self, key)
     |
     |  __init__(self, parser, name)
     |      Creates a view on a section of the specified `name` in `parser`.
     |
     |  __iter__(self)
     |
     |  __len__(self)
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __setitem__(self, key, value)
     |
     |  get(self, option, fallback=None, *, raw=False, vars=None, _impl=None, **kwargs)
     |      Get an option value.
     |
     |      Unless `fallback` is provided, `None` will be returned if the option
     |      is not found.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  name
     |
     |  parser
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __abstractmethods__ = frozenset()
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |
     |  pop(self, key, default=<object object at 0x0000018E8DA18160>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |
     |  popitem(self)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair
     |      as a 2-tuple; but raise KeyError if D is empty.
     |
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |
     |  update(self, other=(), /, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  items(self)
     |      D.items() -> a set-like object providing a view on D's items
     |
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |
     |  __hash__ = None
     |
     |  __reversed__ = None
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Iterable:
     |
     |  __class_getitem__ = GenericAlias(...) from abc.ABCMeta
     |      Represent a PEP 585 generic type
     |
     |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).

DATA
    DEFAULTSECT = 'DEFAULT'
    MAX_INTERPOLATION_DEPTH = 10
    __all__ = ['NoSectionError', 'DuplicateOptionError', 'DuplicateSection...

FILE
    d:\software\python\python39\lib\configparser.py
"""