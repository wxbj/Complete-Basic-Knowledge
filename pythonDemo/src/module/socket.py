"""
NAME
    socket

MODULE REFERENCE
    https://docs.python.org/3.9/library/socket

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides socket operations and some related functions.
    On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
    On other systems, it only supports IP. Functions specific for a
    socket are available as methods of the socket object.

    Functions:

    socket() -- create a new socket object
    socketpair() -- create a pair of new socket objects [*]
    fromfd() -- create a socket object from an open file descriptor [*]
    send_fds() -- Send file descriptor to the socket.
    recv_fds() -- Recieve file descriptors from the socket.
    fromshare() -- create a socket object from data received from socket.share() [*]
    gethostname() -- return the current hostname
    gethostbyname() -- map a hostname to its IP number
    gethostbyaddr() -- map an IP number or hostname to DNS info
    getservbyname() -- map a service name and a protocol name to a port number
    getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
    ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
    htons(), htonl() -- convert 16, 32 bit int from host to network byte order
    inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
    inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
    socket.getdefaulttimeout() -- get the default timeout value
    socket.setdefaulttimeout() -- set the default timeout value
    create_connection() -- connects to an address, with an optional timeout and
                           optional source address.

     [*] not available on all platforms!

    Special objects:

    SocketType -- type object for socket objects
    error -- exception raised for I/O errors
    has_ipv6 -- boolean value indicating if IPv6 is supported

    IntEnum constants:

    AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
    SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

    Integer constants:

    Many other constants may be defined; these may be used in calls to
    the setsockopt() and getsockopt() methods.

CLASSES
    builtins.Exception(builtins.BaseException)
        builtins.OSError
            gaierror
            herror
            timeout
    builtins.object
        _socket.socket
            socket
    enum.IntEnum(builtins.int, enum.Enum)
        AddressFamily
        SocketKind

    class AddressFamily(enum.IntEnum)
     |  AddressFamily(value, names=None, *, module=None, qualname=None, type=None, start=1)
     |
     |  An enumeration.
     |
     |  Method resolution order:
     |      AddressFamily
     |      enum.IntEnum
     |      builtins.int
     |      enum.Enum
     |      builtins.object
     |
     |  Data and other attributes defined here:
     |
     |  AF_APPLETALK = <AddressFamily.AF_APPLETALK: 16>
     |
     |  AF_BLUETOOTH = <AddressFamily.AF_BLUETOOTH: 32>
     |
     |  AF_INET = <AddressFamily.AF_INET: 2>
     |
     |  AF_INET6 = <AddressFamily.AF_INET6: 23>
     |
     |  AF_IPX = <AddressFamily.AF_IPX: 6>
     |
     |  AF_IRDA = <AddressFamily.AF_IRDA: 26>
     |
     |  AF_LINK = <AddressFamily.AF_LINK: 33>
     |
     |  AF_SNA = <AddressFamily.AF_SNA: 11>
     |
     |  AF_UNSPEC = <AddressFamily.AF_UNSPEC: 0>
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from enum.Enum:
     |
     |  name
     |      The name of the Enum member.
     |
     |  value
     |      The value of the Enum member.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from enum.EnumMeta:
     |
     |  __members__
     |      Returns a mapping of member name->value.
     |
     |      This mapping lists all enum members, including aliases. Note that this
     |      is a read-only view of the internal mapping.

    class SocketKind(enum.IntEnum)
     |  SocketKind(value, names=None, *, module=None, qualname=None, type=None, start=1)
     |
     |  An enumeration.
     |
     |  Method resolution order:
     |      SocketKind
     |      enum.IntEnum
     |      builtins.int
     |      enum.Enum
     |      builtins.object
     |
     |  Data and other attributes defined here:
     |
     |  SOCK_DGRAM = <SocketKind.SOCK_DGRAM: 2>
     |
     |  SOCK_RAW = <SocketKind.SOCK_RAW: 3>
     |
     |  SOCK_RDM = <SocketKind.SOCK_RDM: 4>
     |
     |  SOCK_SEQPACKET = <SocketKind.SOCK_SEQPACKET: 5>
     |
     |  SOCK_STREAM = <SocketKind.SOCK_STREAM: 1>
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from enum.Enum:
     |
     |  name
     |      The name of the Enum member.
     |
     |  value
     |      The value of the Enum member.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from enum.EnumMeta:
     |
     |  __members__
     |      Returns a mapping of member name->value.
     |
     |      This mapping lists all enum members, including aliases. Note that this
     |      is a read-only view of the internal mapping.

    SocketType = class socket(builtins.object)
     |  socket(family=AF_INET, type=SOCK_STREAM, proto=0) -> socket object
     |  socket(family=-1, type=-1, proto=-1, fileno=None) -> socket object
     |
     |  Open a socket of the given type.  The family argument specifies the
     |  address family; it defaults to AF_INET.  The type argument specifies
     |  whether this is a stream (SOCK_STREAM, this is the default)
     |  or datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,
     |  specifying the default protocol.  Keyword arguments are accepted.
     |  The socket is created as non-inheritable.
     |
     |  When a fileno is passed in, family, type and proto are auto-detected,
     |  unless they are explicitly set.
     |
     |  A socket object represents one endpoint of a network connection.
     |
     |  Methods of socket objects (keyword arguments not allowed):
     |
     |  _accept() -- accept connection, returning new socket fd and client address
     |  bind(addr) -- bind the socket to a local address
     |  close() -- close the socket
     |  connect(addr) -- connect the socket to a remote address
     |  connect_ex(addr) -- connect, return an error code instead of an exception
     |  dup() -- return a new socket fd duplicated from fileno()
     |  fileno() -- return underlying file descriptor
     |  getpeername() -- return remote address [*]
     |  getsockname() -- return local address
     |  getsockopt(level, optname[, buflen]) -- get socket options
     |  gettimeout() -- return timeout or None
     |  listen([n]) -- start listening for incoming connections
     |  recv(buflen[, flags]) -- receive data
     |  recv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)
     |  recvfrom(buflen[, flags]) -- receive data and sender's address
     |  recvfrom_into(buffer[, nbytes, [, flags])
     |    -- receive data and sender's address (into a buffer)
     |  sendall(data[, flags]) -- send all data
     |  send(data[, flags]) -- send data, may not send all of it
     |  sendto(data[, flags], addr) -- send data to a given address
     |  setblocking(bool) -- set or clear the blocking I/O flag
     |  getblocking() -- return True if socket is blocking, False if non-blocking
     |  setsockopt(level, optname, value[, optlen]) -- set socket options
     |  settimeout(None | float) -- set or clear the timeout
     |  shutdown(how) -- shut down traffic in one or both directions
     |  if_nameindex() -- return all network interface indices and names
     |  if_nametoindex(name) -- return the corresponding interface index
     |  if_indextoname(index) -- return the corresponding interface name
     |
     |   [*] not available on all platforms!
     |
     |  Methods defined here:
     |
     |  __del__(...)
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  bind(...)
     |      bind(address)
     |
     |      Bind the socket to a local address.  For IP sockets, the address is a
     |      pair (host, port); the host must refer to the local host. For raw packet
     |      sockets the address is a tuple (ifname, proto [,pkttype [,hatype [,addr]]])
     |
     |  close(...)
     |      close()
     |
     |      Close the socket.  It cannot be used after this call.
     |
     |  connect(...)
     |      connect(address)
     |
     |      Connect the socket to a remote address.  For IP sockets, the address
     |      is a pair (host, port).
     |
     |  connect_ex(...)
     |      connect_ex(address) -> errno
     |
     |      This is like connect(address), but returns an error code (the errno value)
     |      instead of raising an exception when an error occurs.
     |
     |  detach(...)
     |      detach()
     |
     |      Close the socket object without closing the underlying file descriptor.
     |      The object cannot be used after this call, but the file descriptor
     |      can be reused for other purposes.  The file descriptor is returned.
     |
     |  fileno(...)
     |      fileno() -> integer
     |
     |      Return the integer file descriptor of the socket.
     |
     |  getblocking(...)
     |      getblocking()
     |
     |      Returns True if socket is in blocking mode, or False if it
     |      is in non-blocking mode.
     |
     |  getpeername(...)
     |      getpeername() -> address info
     |
     |      Return the address of the remote endpoint.  For IP sockets, the address
     |      info is a pair (hostaddr, port).
     |
     |  getsockname(...)
     |      getsockname() -> address info
     |
     |      Return the address of the local endpoint. The format depends on the
     |      address family. For IPv4 sockets, the address info is a pair
     |      (hostaddr, port).
     |
     |  getsockopt(...)
     |      getsockopt(level, option[, buffersize]) -> value
     |
     |      Get a socket option.  See the Unix manual for level and option.
     |      If a nonzero buffersize argument is given, the return value is a
     |      string of that length; otherwise it is an integer.
     |
     |  gettimeout(...)
     |      gettimeout() -> timeout
     |
     |      Returns the timeout in seconds (float) associated with socket
     |      operations. A timeout of None indicates that timeouts on socket
     |      operations are disabled.
     |
     |  ioctl(...)
     |      ioctl(cmd, option) -> long
     |
     |      Control the socket with WSAIoctl syscall. Currently supported 'cmd' values are
     |      SIO_RCVALL:  'option' must be one of the socket.RCVALL_* constants.
     |      SIO_KEEPALIVE_VALS:  'option' is a tuple of (onoff, timeout, interval).
     |      SIO_LOOPBACK_FAST_PATH: 'option' is a boolean value, and is disabled by default
     |
     |  listen(...)
     |      listen([backlog])
     |
     |      Enable a server to accept connections.  If backlog is specified, it must be
     |      at least 0 (if it is lower, it is set to 0); it specifies the number of
     |      unaccepted connections that the system will allow before refusing new
     |      connections. If not specified, a default reasonable value is chosen.
     |
     |  recv(...)
     |      recv(buffersize[, flags]) -> data
     |
     |      Receive up to buffersize bytes from the socket.  For the optional flags
     |      argument, see the Unix manual.  When no data is available, block until
     |      at least one byte is available or until the remote end is closed.  When
     |      the remote end is closed and all data is read, return the empty string.
     |
     |  recv_into(...)
     |      recv_into(buffer, [nbytes[, flags]]) -> nbytes_read
     |
     |      A version of recv() that stores its data into a buffer rather than creating
     |      a new string.  Receive up to buffersize bytes from the socket.  If buffersize
     |      is not specified (or 0), receive up to the size available in the given buffer.
     |
     |      See recv() for documentation about the flags.
     |
     |  recvfrom(...)
     |      recvfrom(buffersize[, flags]) -> (data, address info)
     |
     |      Like recv(buffersize, flags) but also return the sender's address info.
     |
     |  recvfrom_into(...)
     |      recvfrom_into(buffer[, nbytes[, flags]]) -> (nbytes, address info)
     |
     |      Like recv_into(buffer[, nbytes[, flags]]) but also return the sender's address info.
     |
     |  send(...)
     |      send(data[, flags]) -> count
     |
     |      Send a data string to the socket.  For the optional flags
     |      argument, see the Unix manual.  Return the number of bytes
     |      sent; this may be less than len(data) if the network is busy.
     |
     |  sendall(...)
     |      sendall(data[, flags])
     |
     |      Send a data string to the socket.  For the optional flags
     |      argument, see the Unix manual.  This calls send() repeatedly
     |      until all data is sent.  If an error occurs, it's impossible
     |      to tell how much data has been sent.
     |
     |  sendto(...)
     |      sendto(data[, flags], address) -> count
     |
     |      Like send(data, flags) but allows specifying the destination address.
     |      For IP sockets, the address is a pair (hostaddr, port).
     |
     |  setblocking(...)
     |      setblocking(flag)
     |
     |      Set the socket to blocking (flag is true) or non-blocking (false).
     |      setblocking(True) is equivalent to settimeout(None);
     |      setblocking(False) is equivalent to settimeout(0.0).
     |
     |  setsockopt(...)
     |      setsockopt(level, option, value: int)
     |      setsockopt(level, option, value: buffer)
     |      setsockopt(level, option, None, optlen: int)
     |
     |      Set a socket option.  See the Unix manual for level and option.
     |      The value argument can either be an integer, a string buffer, or
     |      None, optlen.
     |
     |  settimeout(...)
     |      settimeout(timeout)
     |
     |      Set a timeout on socket operations.  'timeout' can be a float,
     |      giving in seconds, or None.  Setting a timeout of None disables
     |      the timeout feature and is equivalent to setblocking(1).
     |      Setting a timeout of zero is the same as setblocking(0).
     |
     |  share(...)
     |      share(process_id) -> bytes
     |
     |      Share the socket with another process.  The target process id
     |      must be provided and the resulting bytes object passed to the target
     |      process.  There the shared socket can be instantiated by calling
     |      socket.fromshare().
     |
     |  shutdown(...)
     |      shutdown(flag)
     |
     |      Shut down the reading side of the socket (flag == SHUT_RD), the writing side
     |      of the socket (flag == SHUT_WR), or both ends (flag == SHUT_RDWR).
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
     |  family
     |      the socket family
     |
     |  proto
     |      the socket protocol
     |
     |  timeout
     |      the socket timeout
     |
     |  type
     |      the socket type

    error = class OSError(Exception)
     |  Base class for I/O related errors.
     |
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |
     |  Built-in subclasses:
     |      BlockingIOError
     |      ChildProcessError
     |      ConnectionError
     |      FileExistsError
     |      ... and 7 other subclasses
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
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
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __repr__(self, /)
     |      Return repr(self).
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
     |  Data descriptors inherited from BaseException:
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

    class gaierror(builtins.OSError)
     |  Method resolution order:
     |      gaierror
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
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
     |  __repr__(self, /)
     |      Return repr(self).
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

    class herror(builtins.OSError)
     |  Method resolution order:
     |      herror
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
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
     |  __repr__(self, /)
     |      Return repr(self).
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

    class socket(_socket.socket)
     |  socket(family=-1, type=-1, proto=-1, fileno=None)
     |
     |  A subclass of _socket.socket adding the makefile() method.
     |
     |  Method resolution order:
     |      socket
     |      _socket.socket
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, *args)
     |
     |  __getstate__(self)
     |
     |  __init__(self, family=-1, type=-1, proto=-1, fileno=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __repr__(self)
     |      Wrap __repr__() to reveal the real class name and socket
     |      address(es).
     |
     |  accept(self)
     |      accept() -> (socket object, address info)
     |
     |      Wait for an incoming connection.  Return a new socket
     |      representing the connection, and the address of the client.
     |      For IP sockets, the address info is a pair (hostaddr, port).
     |
     |  close(self)
     |      close()
     |
     |      Close the socket.  It cannot be used after this call.
     |
     |  detach(self)
     |      detach() -> file descriptor
     |
     |      Close the socket object without closing the underlying file descriptor.
     |      The object cannot be used after this call, but the file descriptor
     |      can be reused for other purposes.  The file descriptor is returned.
     |
     |  dup(self)
     |      dup() -> socket object
     |
     |      Duplicate the socket. Return a new socket object connected to the same
     |      system resource. The new socket is non-inheritable.
     |
     |  get_inheritable(self)
     |      Get the inheritable flag of the socket
     |
     |  makefile(self, mode='r', buffering=None, *, encoding=None, errors=None, newline=None)
     |      makefile(...) -> an I/O stream connected to the socket
     |
     |      The arguments are as for io.open() after the filename, except the only
     |      supported mode values are 'r' (default), 'w' and 'b'.
     |
     |  sendfile(self, file, offset=0, count=None)
     |      sendfile(file[, offset[, count]]) -> sent
     |
     |      Send a file until EOF is reached by using high-performance
     |      os.sendfile() and return the total number of bytes which
     |      were sent.
     |      *file* must be a regular file object opened in binary mode.
     |      If os.sendfile() is not available (e.g. Windows) or file is
     |      not a regular file socket.send() will be used instead.
     |      *offset* tells from where to start reading the file.
     |      If specified, *count* is the total number of bytes to transmit
     |      as opposed to sending the file until EOF is reached.
     |      File position is updated on return or also in case of error in
     |      which case file.tell() can be used to figure out the number of
     |      bytes which were sent.
     |      The socket must be of SOCK_STREAM type.
     |      Non-blocking sockets are not supported.
     |
     |  set_inheritable(self, inheritable)
     |      Set the inheritable flag of the socket
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  family
     |      Read-only access to the address family for this socket.
     |
     |  type
     |      Read-only access to the socket type.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _socket.socket:
     |
     |  __del__(...)
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  bind(...)
     |      bind(address)
     |
     |      Bind the socket to a local address.  For IP sockets, the address is a
     |      pair (host, port); the host must refer to the local host. For raw packet
     |      sockets the address is a tuple (ifname, proto [,pkttype [,hatype [,addr]]])
     |
     |  connect(...)
     |      connect(address)
     |
     |      Connect the socket to a remote address.  For IP sockets, the address
     |      is a pair (host, port).
     |
     |  connect_ex(...)
     |      connect_ex(address) -> errno
     |
     |      This is like connect(address), but returns an error code (the errno value)
     |      instead of raising an exception when an error occurs.
     |
     |  fileno(...)
     |      fileno() -> integer
     |
     |      Return the integer file descriptor of the socket.
     |
     |  getblocking(...)
     |      getblocking()
     |
     |      Returns True if socket is in blocking mode, or False if it
     |      is in non-blocking mode.
     |
     |  getpeername(...)
     |      getpeername() -> address info
     |
     |      Return the address of the remote endpoint.  For IP sockets, the address
     |      info is a pair (hostaddr, port).
     |
     |  getsockname(...)
     |      getsockname() -> address info
     |
     |      Return the address of the local endpoint. The format depends on the
     |      address family. For IPv4 sockets, the address info is a pair
     |      (hostaddr, port).
     |
     |  getsockopt(...)
     |      getsockopt(level, option[, buffersize]) -> value
     |
     |      Get a socket option.  See the Unix manual for level and option.
     |      If a nonzero buffersize argument is given, the return value is a
     |      string of that length; otherwise it is an integer.
     |
     |  gettimeout(...)
     |      gettimeout() -> timeout
     |
     |      Returns the timeout in seconds (float) associated with socket
     |      operations. A timeout of None indicates that timeouts on socket
     |      operations are disabled.
     |
     |  ioctl(...)
     |      ioctl(cmd, option) -> long
     |
     |      Control the socket with WSAIoctl syscall. Currently supported 'cmd' values are
     |      SIO_RCVALL:  'option' must be one of the socket.RCVALL_* constants.
     |      SIO_KEEPALIVE_VALS:  'option' is a tuple of (onoff, timeout, interval).
     |      SIO_LOOPBACK_FAST_PATH: 'option' is a boolean value, and is disabled by default
     |
     |  listen(...)
     |      listen([backlog])
     |
     |      Enable a server to accept connections.  If backlog is specified, it must be
     |      at least 0 (if it is lower, it is set to 0); it specifies the number of
     |      unaccepted connections that the system will allow before refusing new
     |      connections. If not specified, a default reasonable value is chosen.
     |
     |  recv(...)
     |      recv(buffersize[, flags]) -> data
     |
     |      Receive up to buffersize bytes from the socket.  For the optional flags
     |      argument, see the Unix manual.  When no data is available, block until
     |      at least one byte is available or until the remote end is closed.  When
     |      the remote end is closed and all data is read, return the empty string.
     |
     |  recv_into(...)
     |      recv_into(buffer, [nbytes[, flags]]) -> nbytes_read
     |
     |      A version of recv() that stores its data into a buffer rather than creating
     |      a new string.  Receive up to buffersize bytes from the socket.  If buffersize
     |      is not specified (or 0), receive up to the size available in the given buffer.
     |
     |      See recv() for documentation about the flags.
     |
     |  recvfrom(...)
     |      recvfrom(buffersize[, flags]) -> (data, address info)
     |
     |      Like recv(buffersize, flags) but also return the sender's address info.
     |
     |  recvfrom_into(...)
     |      recvfrom_into(buffer[, nbytes[, flags]]) -> (nbytes, address info)
     |
     |      Like recv_into(buffer[, nbytes[, flags]]) but also return the sender's address info.
     |
     |  send(...)
     |      send(data[, flags]) -> count
     |
     |      Send a data string to the socket.  For the optional flags
     |      argument, see the Unix manual.  Return the number of bytes
     |      sent; this may be less than len(data) if the network is busy.
     |
     |  sendall(...)
     |      sendall(data[, flags])
     |
     |      Send a data string to the socket.  For the optional flags
     |      argument, see the Unix manual.  This calls send() repeatedly
     |      until all data is sent.  If an error occurs, it's impossible
     |      to tell how much data has been sent.
     |
     |  sendto(...)
     |      sendto(data[, flags], address) -> count
     |
     |      Like send(data, flags) but allows specifying the destination address.
     |      For IP sockets, the address is a pair (hostaddr, port).
     |
     |  setblocking(...)
     |      setblocking(flag)
     |
     |      Set the socket to blocking (flag is true) or non-blocking (false).
     |      setblocking(True) is equivalent to settimeout(None);
     |      setblocking(False) is equivalent to settimeout(0.0).
     |
     |  setsockopt(...)
     |      setsockopt(level, option, value: int)
     |      setsockopt(level, option, value: buffer)
     |      setsockopt(level, option, None, optlen: int)
     |
     |      Set a socket option.  See the Unix manual for level and option.
     |      The value argument can either be an integer, a string buffer, or
     |      None, optlen.
     |
     |  settimeout(...)
     |      settimeout(timeout)
     |
     |      Set a timeout on socket operations.  'timeout' can be a float,
     |      giving in seconds, or None.  Setting a timeout of None disables
     |      the timeout feature and is equivalent to setblocking(1).
     |      Setting a timeout of zero is the same as setblocking(0).
     |
     |  share(...)
     |      share(process_id) -> bytes
     |
     |      Share the socket with another process.  The target process id
     |      must be provided and the resulting bytes object passed to the target
     |      process.  There the shared socket can be instantiated by calling
     |      socket.fromshare().
     |
     |  shutdown(...)
     |      shutdown(flag)
     |
     |      Shut down the reading side of the socket (flag == SHUT_RD), the writing side
     |      of the socket (flag == SHUT_WR), or both ends (flag == SHUT_RDWR).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _socket.socket:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _socket.socket:
     |
     |  proto
     |      the socket protocol
     |
     |  timeout
     |      the socket timeout

    class timeout(builtins.OSError)
     |  Method resolution order:
     |      timeout
     |      builtins.OSError
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
     |  Methods inherited from builtins.OSError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __reduce__(...)
     |      Helper for pickle.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.OSError:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.OSError:
     |
     |  characters_written
     |
     |  errno
     |      POSIX exception code
     |
     |  filename
     |      exception filename
     |
     |  filename2
     |      second exception filename
     |
     |  strerror
     |      exception strerror
     |
     |  winerror
     |      Win32 exception code
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
     |  __repr__(self, /)
     |      Return repr(self).
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

FUNCTIONS
    close(...)
        close(integer) -> None

        Close an integer socket file descriptor.  This is like os.close(), but for
        sockets; on some platforms os.close() won't work for socket file descriptors.

    create_connection(address, timeout=<object object at 0x000002CFF1FA89B0>, source_address=None)
        Connect to *address* and return the socket object.

        Convenience function.  Connect to *address* (a 2-tuple ``(host,
        port)``) and return the socket object.  Passing the optional
        *timeout* parameter will set the timeout on the socket instance
        before attempting to connect.  If no *timeout* is supplied, the
        global default timeout setting returned by :func:`getdefaulttimeout`
        is used.  If *source_address* is set it must be a tuple of (host, port)
        for the socket to bind as a source address before making the connection.
        A host of '' or port 0 tells the OS to use the default.

    create_server(address, *, family=<AddressFamily.AF_INET: 2>, backlog=None, reuse_port=False, dualstack_ipv6=False)
        Convenience function which creates a SOCK_STREAM type socket
        bound to *address* (a 2-tuple (host, port)) and return the socket
        object.

        *family* should be either AF_INET or AF_INET6.
        *backlog* is the queue size passed to socket.listen().
        *reuse_port* dictates whether to use the SO_REUSEPORT socket option.
        *dualstack_ipv6*: if true and the platform supports it, it will
        create an AF_INET6 socket able to accept both IPv4 or IPv6
        connections. When false it will explicitly disable this option on
        platforms that enable it by default (e.g. Linux).

        >>> with create_server(('', 8000)) as server:
        ...     while True:
        ...         conn, addr = server.accept()
        ...         # handle new connection

    dup(...)
        dup(integer) -> integer

        Duplicate an integer socket file descriptor.  This is like os.dup(), but for
        sockets; on some platforms os.dup() won't work for socket file descriptors.

    fromfd(fd, family, type, proto=0)
        fromfd(fd, family, type[, proto]) -> socket object

        Create a socket object from a duplicate of the given file
        descriptor.  The remaining arguments are the same as for socket().

    fromshare(info)
        fromshare(info) -> socket object

        Create a socket object from the bytes object returned by
        socket.share(pid).

    getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
        Resolve host and port into list of address info entries.

        Translate the host/port argument into a sequence of 5-tuples that contain
        all the necessary arguments for creating a socket connected to that service.
        host is a domain name, a string representation of an IPv4/v6 address or
        None. port is a string service name such as 'http', a numeric port number or
        None. By passing None as the value of host and port, you can pass NULL to
        the underlying C API.

        The family, type and proto arguments can be optionally specified in order to
        narrow the list of addresses returned. Passing zero as a value for each of
        these arguments selects the full range of results.

    getdefaulttimeout(...)
        getdefaulttimeout() -> timeout

        Returns the default timeout in seconds (float) for new socket objects.
        A value of None indicates that new socket objects have no timeout.
        When the socket module is first imported, the default is None.

    getfqdn(name='')
        Get fully qualified domain name from name.

        An empty argument is interpreted as meaning the local host.

        First the hostname returned by gethostbyaddr() is checked, then
        possibly existing aliases. In case no FQDN is available, hostname
        from gethostname() is returned.

    gethostbyaddr(...)
        gethostbyaddr(host) -> (name, aliaslist, addresslist)

        Return the true host name, a list of aliases, and a list of IP addresses,
        for a host.  The host argument is a string giving a host name or IP number.

    gethostbyname(...)
        gethostbyname(host) -> address

        Return the IP address (a string of the form '255.255.255.255') for a host.

    gethostbyname_ex(...)
        gethostbyname_ex(host) -> (name, aliaslist, addresslist)

        Return the true host name, a list of aliases, and a list of IP addresses,
        for a host.  The host argument is a string giving a host name or IP number.

    gethostname(...)
        gethostname() -> string

        Return the current host name.

    getnameinfo(...)
        getnameinfo(sockaddr, flags) --> (host, port)

        Get host and port for a sockaddr.

    getprotobyname(...)
        getprotobyname(name) -> integer

        Return the protocol number for the named protocol.  (Rarely used.)

    getservbyname(...)
        getservbyname(servicename[, protocolname]) -> integer

        Return a port number from a service name and protocol name.
        The optional protocol name, if given, should be 'tcp' or 'udp',
        otherwise any protocol will match.

    getservbyport(...)
        getservbyport(port[, protocolname]) -> string

        Return the service name from a port number and protocol name.
        The optional protocol name, if given, should be 'tcp' or 'udp',
        otherwise any protocol will match.

    has_dualstack_ipv6()
        Return True if the platform supports creating a SOCK_STREAM socket
        which can handle both AF_INET and AF_INET6 (IPv4 / IPv6) connections.

    htonl(...)
        htonl(integer) -> integer

        Convert a 32-bit integer from host to network byte order.

    htons(...)
        htons(integer) -> integer

        Convert a 16-bit unsigned integer from host to network byte order.
        Note that in case the received integer does not fit in 16-bit unsigned
        integer, but does fit in a positive C int, it is silently truncated to
        16-bit unsigned integer.
        However, this silent truncation feature is deprecated, and will raise an
        exception in future versions of Python.

    if_indextoname(...)
        if_indextoname(if_index)

        Returns the interface name corresponding to the interface index if_index.

    if_nameindex(...)
        if_nameindex()

        Returns a list of network interface information (index, name) tuples.

    if_nametoindex(...)
        if_nametoindex(if_name)

        Returns the interface index corresponding to the interface name if_name.

    inet_aton(...)
        inet_aton(string) -> bytes giving packed 32-bit IP representation

        Convert an IP address in string format (123.45.67.89) to the 32-bit packed
        binary format used in low-level network functions.

    inet_ntoa(...)
        inet_ntoa(packed_ip) -> ip_address_string

        Convert an IP address from 32-bit packed binary format to string format

    inet_ntop(...)
        inet_ntop(af, packed_ip) -> string formatted IP address

        Convert a packed IP address of the given family to string format.

    inet_pton(...)
        inet_pton(af, ip) -> packed IP address string

        Convert an IP address from string format to a packed string suitable
        for use with low-level network functions.

    ntohl(...)
        ntohl(integer) -> integer

        Convert a 32-bit integer from network to host byte order.

    ntohs(...)
        ntohs(integer) -> integer

        Convert a 16-bit unsigned integer from network to host byte order.
        Note that in case the received integer does not fit in 16-bit unsigned
        integer, but does fit in a positive C int, it is silently truncated to
        16-bit unsigned integer.
        However, this silent truncation feature is deprecated, and will raise an
        exception in future versions of Python.

    setdefaulttimeout(...)
        setdefaulttimeout(timeout)

        Set the default timeout in seconds (float) for new socket objects.
        A value of None indicates that new socket objects have no timeout.
        When the socket module is first imported, the default is None.

    socketpair(family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, proto=0)
        socketpair([family[, type[, proto]]]) -> (socket object, socket object)
        Create a pair of socket objects from the sockets returned by the platform
        socketpair() function.
        The arguments are the same as for socket() except the default family is AF_UNIX
        if defined on the platform; otherwise, the default is AF_INET.

DATA
    AF_APPLETALK = <AddressFamily.AF_APPLETALK: 16>
    AF_BLUETOOTH = <AddressFamily.AF_BLUETOOTH: 32>
    AF_DECnet = 12
    AF_INET = <AddressFamily.AF_INET: 2>
    AF_INET6 = <AddressFamily.AF_INET6: 23>
    AF_IPX = <AddressFamily.AF_IPX: 6>
    AF_IRDA = <AddressFamily.AF_IRDA: 26>
    AF_LINK = <AddressFamily.AF_LINK: 33>
    AF_SNA = <AddressFamily.AF_SNA: 11>
    AF_UNSPEC = <AddressFamily.AF_UNSPEC: 0>
    AI_ADDRCONFIG = <AddressInfo.AI_ADDRCONFIG: 1024>
    AI_ALL = <AddressInfo.AI_ALL: 256>
    AI_CANONNAME = <AddressInfo.AI_CANONNAME: 2>
    AI_NUMERICHOST = <AddressInfo.AI_NUMERICHOST: 4>
    AI_NUMERICSERV = <AddressInfo.AI_NUMERICSERV: 8>
    AI_PASSIVE = <AddressInfo.AI_PASSIVE: 1>
    AI_V4MAPPED = <AddressInfo.AI_V4MAPPED: 2048>
    BDADDR_ANY = '00:00:00:00:00:00'
    BDADDR_LOCAL = '00:00:00:FF:FF:FF'
    BTPROTO_RFCOMM = 3
    CAPI = <capsule object "_socket.CAPI">
    EAI_AGAIN = 11002
    EAI_BADFLAGS = 10022
    EAI_FAIL = 11003
    EAI_FAMILY = 10047
    EAI_MEMORY = 8
    EAI_NODATA = 11001
    EAI_NONAME = 11001
    EAI_SERVICE = 10109
    EAI_SOCKTYPE = 10044
    INADDR_ALLHOSTS_GROUP = -536870911
    INADDR_ANY = 0
    INADDR_BROADCAST = -1
    INADDR_LOOPBACK = 2130706433
    INADDR_MAX_LOCAL_GROUP = -536870657
    INADDR_NONE = -1
    INADDR_UNSPEC_GROUP = -536870912
    IPPORT_RESERVED = 1024
    IPPORT_USERRESERVED = 5000
    IPPROTO_AH = 51
    IPPROTO_CBT = 7
    IPPROTO_DSTOPTS = 60
    IPPROTO_EGP = 8
    IPPROTO_ESP = 50
    IPPROTO_FRAGMENT = 44
    IPPROTO_GGP = 3
    IPPROTO_HOPOPTS = 0
    IPPROTO_ICLFXBM = 78
    IPPROTO_ICMP = 1
    IPPROTO_ICMPV6 = 58
    IPPROTO_IDP = 22
    IPPROTO_IGMP = 2
    IPPROTO_IGP = 9
    IPPROTO_IP = 0
    IPPROTO_IPV4 = 4
    IPPROTO_IPV6 = 41
    IPPROTO_L2TP = 115
    IPPROTO_MAX = 256
    IPPROTO_ND = 77
    IPPROTO_NONE = 59
    IPPROTO_PGM = 113
    IPPROTO_PIM = 103
    IPPROTO_PUP = 12
    IPPROTO_RAW = 255
    IPPROTO_RDP = 27
    IPPROTO_ROUTING = 43
    IPPROTO_SCTP = 132
    IPPROTO_ST = 5
    IPPROTO_TCP = 6
    IPPROTO_UDP = 17
    IPV6_CHECKSUM = 26
    IPV6_DONTFRAG = 14
    IPV6_HOPLIMIT = 21
    IPV6_HOPOPTS = 1
    IPV6_JOIN_GROUP = 12
    IPV6_LEAVE_GROUP = 13
    IPV6_MULTICAST_HOPS = 10
    IPV6_MULTICAST_IF = 9
    IPV6_MULTICAST_LOOP = 11
    IPV6_PKTINFO = 19
    IPV6_RECVRTHDR = 38
    IPV6_RECVTCLASS = 40
    IPV6_RTHDR = 32
    IPV6_TCLASS = 39
    IPV6_UNICAST_HOPS = 4
    IPV6_V6ONLY = 27
    IP_ADD_MEMBERSHIP = 12
    IP_DROP_MEMBERSHIP = 13
    IP_HDRINCL = 2
    IP_MULTICAST_IF = 9
    IP_MULTICAST_LOOP = 11
    IP_MULTICAST_TTL = 10
    IP_OPTIONS = 1
    IP_RECVDSTADDR = 25
    IP_TOS = 3
    IP_TTL = 4
    MSG_BCAST = <MsgFlag.MSG_BCAST: 1024>
    MSG_CTRUNC = <MsgFlag.MSG_CTRUNC: 512>
    MSG_DONTROUTE = <MsgFlag.MSG_DONTROUTE: 4>
    MSG_ERRQUEUE = <MsgFlag.MSG_ERRQUEUE: 4096>
    MSG_MCAST = <MsgFlag.MSG_MCAST: 2048>
    MSG_OOB = <MsgFlag.MSG_OOB: 1>
    MSG_PEEK = <MsgFlag.MSG_PEEK: 2>
    MSG_TRUNC = <MsgFlag.MSG_TRUNC: 256>
    MSG_WAITALL = <MsgFlag.MSG_WAITALL: 8>
    NI_DGRAM = 16
    NI_MAXHOST = 1025
    NI_MAXSERV = 32
    NI_NAMEREQD = 4
    NI_NOFQDN = 1
    NI_NUMERICHOST = 2
    NI_NUMERICSERV = 8
    RCVALL_MAX = 3
    RCVALL_OFF = 0
    RCVALL_ON = 1
    RCVALL_SOCKETLEVELONLY = 2
    SHUT_RD = 0
    SHUT_RDWR = 2
    SHUT_WR = 1
    SIO_KEEPALIVE_VALS = 2550136836
    SIO_LOOPBACK_FAST_PATH = 2550136848
    SIO_RCVALL = 2550136833
    SOCK_DGRAM = <SocketKind.SOCK_DGRAM: 2>
    SOCK_RAW = <SocketKind.SOCK_RAW: 3>
    SOCK_RDM = <SocketKind.SOCK_RDM: 4>
    SOCK_SEQPACKET = <SocketKind.SOCK_SEQPACKET: 5>
    SOCK_STREAM = <SocketKind.SOCK_STREAM: 1>
    SOL_IP = 0
    SOL_SOCKET = 65535
    SOL_TCP = 6
    SOL_UDP = 17
    SOMAXCONN = 2147483647
    SO_ACCEPTCONN = 2
    SO_BROADCAST = 32
    SO_DEBUG = 1
    SO_DONTROUTE = 16
    SO_ERROR = 4103
    SO_EXCLUSIVEADDRUSE = -5
    SO_KEEPALIVE = 8
    SO_LINGER = 128
    SO_OOBINLINE = 256
    SO_RCVBUF = 4098
    SO_RCVLOWAT = 4100
    SO_RCVTIMEO = 4102
    SO_REUSEADDR = 4
    SO_SNDBUF = 4097
    SO_SNDLOWAT = 4099
    SO_SNDTIMEO = 4101
    SO_TYPE = 4104
    SO_USELOOPBACK = 64
    TCP_FASTOPEN = 15
    TCP_KEEPCNT = 16
    TCP_KEEPIDLE = 3
    TCP_KEEPINTVL = 17
    TCP_MAXSEG = 4
    TCP_NODELAY = 1
    __all__ = ['fromfd', 'getfqdn', 'create_connection', 'create_server', ...
    errorTab = {6: 'Specified event object handle is invalid.', 8: 'Insuff...
    has_ipv6 = True

FILE
    d:\software\python\python39\lib\socket.py
"""