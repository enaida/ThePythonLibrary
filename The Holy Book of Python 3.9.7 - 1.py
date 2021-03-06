#!/usr/bin/env python
# coding: utf-8

# ## 1. Introduction

# The “Python library” contains several different kinds of components. It contains data types that would normally be considered part of the “core” of a language, such as numbers and lists. For these types, the Python language core defines the form of literals and places some constraints on their semantics, but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like the spelling and priorities of operators.) The library also contains built-in functions and exceptions — objects that can be used by all Python code without the need of an import statement.
# 
# 
# The bulk of the library, however, consists of a collection of modules. There are many ways to dissect this collection. Some modules are written in C and built in to the Python interpreter; others are written in Python and imported in source form. Some modules provide interfaces that are highly specific to Python, like printing a stack trace; some provide interfaces that are specific to particular operating systems, such as access to specific hardware; others provide interfaces that are specific to a particular application domain, like the World Wide Web. Some modules are available in all versions and ports of Python; others are only available when the underlying system supports or requires them; yet others are available only when a particular configuration option was chosen at the time when Python was compiled and installed.

# ## 2. Built-in functions

# **abs (x)**
# > Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing \_\_abs\_\_(). If the argument is a complex number, its magnitude is returned. 
# 
# **all (iterable)**
# > Return True if all elements of the iterable are true (or if the iterable is empty).
# 
# **any (iterable)**
# > Return True if any element of the iterable is true. If the iterable is empty, return False.
# 
# **bool ([x ])**
# > Return a Boolean value. If x is false or omitted, this returns False; otherwise it returns True.
# 
# **breakpoint (\*args, \*\*kws)**
# > This function drops you into the debugger at the call site.
# 
# **callable (object)** 
# > Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a \_\_call\_\_() method.
# 
# **chr (i)**
# > Return the string representing a character whose Unicode code point is the integer i. For example, chr (97) returns the string 'a', while chr (8364) returns the string '€'. This is the inverse of **ord ()**. The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.
# 
# **@classmethod**
# > Transform a method into a class method. A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:
# 
# ```python
# class C:
#     @classmethod
#     def f(cls, arg1, arg2, ...): ...
# ```
# 
# > The @classmethod form is a function decorator – see function for details. A class method can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument. Class methods are different than C++ or Java static methods. If you want those, see staticmethod() in this section. For more information on class methods, see types. Changed in version 3.9: Class methods can now wrap other descriptors such as property(). 
# 
# **delattr (object, name)**
# > This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.
# 
# **class dict (\*\*kwarg)** or **class dict (mapping, **kwarg)** or **class dict (iterable, **kwarg)**
# > Create a new dictionary. The dict object is the dictionary class. See dict and Mapping Types — dict for documentation about this class.
# 
# **dir ([object])**
# > Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object. If the object has a method named \_\_dir\_\_(), this method will be called and must return the list of attributes. This allows objects that implement a custom \_\_getattr\_\_() or \_\_getattribute\_\_() function to customize the way dir() reports their attributes. If the object does not provide \_\_dir\_\_(), the function tries its best to gather information from the object’s \_\_dict\_\_ attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may be inaccurate when the object has a custom \_\_getattr\_\_().
# The default dir() mechanism behaves differently with different types of objects, as it attempts to produce
# the most relevant, rather than complete, information:
# ```
# > • If the object is a module object, the list contains the names of the module’s attributes.
# > • If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.
# > • Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.
# ```
# > The resulting list is sorted alphabetically. For example:
# ```python
# > import struct
# > dir() # show the names in the module namespace
# ['__builtins__', '__name__', 'struct']
# dir(struct) # show the names in the struct module
# ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__initializing__', 
# '__loader__', '__name__', '__package__', '_clearcache', 'calcsize', 'error', 'pack', 'pack_into', 'unpack', 'unpack_from']
# class Shape:
#     def __dir__(self):
#         return ['area', 'perimeter', 'location']
# s = Shape()
# dir(s)
# ['area', 'location', 'perimeter']
# ```
# Note: Because dir() is supplied primarily as a convenience for use at an interactive prompt, it tries to
# supply an interesting set of names more than it tries to supply a rigorously or consistently defined set of names,
# and its detailed behavior may change across releases. For example, metaclass attributes are not in the result list
# when the argument is a class.

# **divmod (a, b)**
# > Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).
# 
# **enumerate (iterable, start = 0)**
# > Return an enumerate object. Iterable must be a sequence, an iterator, or some other object which supports iteration. The \_\_next\_\_() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
# ```python
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# list(enumerate(seasons, start = 1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# ```
# Equivalent to:
# ```python
# def enumerate(sequence, start = 0):
#    n = start
#    for elem in sequence:
#       yield n, elem
#       n += 1
# ```
# 
# **exec (object[, globals[, locals] ])**
# > This function supports dynamic execution of Python code....
# 
# **filter (function, iterable)**
# > Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed. Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None. See itertools.filterfalse() for the complementary function that returns elements of iterable for which function returns false.
# 
# **class float ([x ])**
# > Return a floating point number constructed from a number or string x. If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or a positive or negative infinity. More precisely, the input must conform to the following grammar after leading and trailing whitespace characters are removed:
# ```
# sign ::= "+" | "-"
# infinity ::= "Infinity" | "inf"
# nan ::= "nan"
# numeric_value ::= floatnumber | infinity | nan
# numeric_string ::= [sign] numeric_value
# ```
# > Here floatnumber is the form of a Python floating-point literal, described in floating. Case is not significant, so, for example, “inf”, “Inf”, “INFINITY” and “iNfINity” are all acceptable spellings for positive infinity. Otherwise, if the argument is an integer or a floating point number, a floating point number with the same value (within Python’s floating point precision) is returned. If the argument is outside the range of a Python float, an OverflowError will be raised.
# For a general Python object x, float(x) delegates to x.\_\_float\_\_(). If \_\_float\_\_() is not defined
# then it falls back to \_\_index\_\_(). If no argument is given, 0.0 is returned. Examples:
# ```python
# float('+1.23')
# 1.23
# float(' -12345\n')
# -12345.0
# float('1e-003')
# 0.001
# float('+1E6')
# 1000000.0
# float('-Infinity')
# -inf
# ```
# 
# **format (value[, format_spec ])**
# > Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument, however there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language. The default format_spec is an empty string which usually gives the same effect as calling str(value).
# 
# **class frozenset ([iterable ])**
# > Return a new frozenset object, optionally with elements taken from iterable.
# 
# **getattr (object, name[, default])**
# > Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised. Note: Since private name mangling happens at compilation time, one must manually mangle a private attribute’s (attributes with two leading underscores) name in order to retrieve it with getattr().
# 
# **globals ()**
# > Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).
# 
# **hasattr (object, name)**
# > The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not.
# 
# **hash (object)**
# > Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0). Note: For objects with custom \_\_hash\_\_() methods, note that hash() truncates the return value based on the bit width of the host machine. See \_\_hash\_\_() for details.
# 
# **help ([object])**
# > Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated. Note that if a slash(/) appears in the parameter list of a function, when invoking help(), it means that the parameters prior to the slash are positional-only. For more info, see the FAQ entry on positional-only parameters. This function is added to the built-in namespace by the site module.
# 
# **id (object)**
# > Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value. CPython implementation detail: This is the address of the object in memory.
# 
# **input ([prompt])**
# > If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
# ```python
# s = input('--> ')
# --> Monty Python's Flying Circus
# s
# "Monty Python's Flying Circus"
# ```
# If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.
# 
# **class int ([x ])**
# > Return an integer object constructed from a number or string x, or return 0 if no arguments are given.
# 
# **isinstance (object, classinfo)**
# > Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual)
# subclass thereof. If object is not an object of the given type, the function always returns False.
# 
# **issubclass (class, classinfo)**
# > Return True if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case return True if class is a subclass of any entry in classinfo. In any other case, a TypeError exception is raised.
# 
# **iter (object[, sentinel])**
# > Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iteration protocol (the \_\_iter\_\_() method), or it must support the sequence protocol (the \_\_getitem\_\_() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its \_\_next\_\_() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned. See also Iterator Types.
# 
# **len (s)**
# > Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set). CPython implementation detail: len raises OverflowError on lengths larger than sys.maxsize, such as range(2 ** 100).
# 
# **class list ([iterable ])**
# > Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.
# 
# **locals ()**
# > Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks. Note that at the module level, locals() and globals() are the same dictionary. Note: The contents of this dictionary should not be modified; changes may not affect the values of local and
# free variables used by the interpreter.

# **map (function, iterable, ...)**
# > Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().
# 
# **max (iterable, *[, key, default])**
# 
# **max (arg1, arg2, *args[, key ])**
# > Return the largest item in an iterable or the largest of two or more arguments. If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned. There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.
# 
# **min (iterable, *[, key, default])**
# **min (arg1, arg2, *args[, key ])**
# >Return the smallest item in an iterable or the smallest of two or more arguments. If one positional argument is provided, it should be an iterable. The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments is returned. There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty. If the iterable is empty and default is not provided, a ValueError is raised.
# 
# **next (iterator[, default])**
# > Retrieve the next item from the iterator by calling its \_\_next\_\_() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.
# 
# **class object**
# > Return a new featureless object. object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments. Note: object does not have a \_\_dict\_\_, so you can’t assign arbitrary attributes to an instance of the object class.
# 
# **open (file, mode = ’r’, buffering = -1, encoding = None, errors = None, newline = None, closefd = True, opener = None)**
# > Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. See tut-files for more examples of how to use this function. file is a path-like object giving the pathname (absolute or relative to the current working directory) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed, unless closefd is set to False.). mode is an optional string that specifies the mode in which the file is opened. It defaults to 'r' which means open for reading in text mode. Other common values are 'w' for writing (truncating the file if it already exists), 'x' for exclusive creation and 'a' for appending (which on some Unix systems, means that all writes append to the end of the file regardless of the current seek position). In text mode, if encoding is not specified the encoding used is platform dependent: locale.getpreferredencoding(False) is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave encoding unspecified.)
# ```
# The available modes are:
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open for updating (reading and writing)
# ```
# More on other parameters in documentation....
# 
# **pow (base, exp[, mod ])**
# > Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod). The two-argument form pow(base, exp) is equivalent to using the power operator: base\*\*exp.
# 
# **print (*objects, sep = ’ ’, end = ’\n’, file = sys.stdout, flush = False)**
# > Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments. All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end. The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead. Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.
# 
# **class property (fget = None, fset = None, fdel = None, doc = None)**
# > Return a property attribute. fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.
# 
# **class range (stop)** or **class range (start, stop[, step ])**
# > Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.
# 
# **repr (object)**
# > Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a \_\_repr\_\_() method.
# 
# **reversed (seq)**
# > Return a reverse iterator. seq must be an object which has a \_\_reversed\_\_() method or supports the sequence protocol (the \_\_len\_\_() method and the \_\_getitem\_\_() method with integer arguments starting at 0).
# 
# **round (number[, ndigits])**
# > Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input. For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power
# minus ndigits; if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). Any integer value is valid for ndigits (positive, zero, or negative). The return value is an integer if ndigits is omitted or None. Otherwise the return value has the same type as number. Note: The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See tut-fp-issues for more information.
# 
# **class set ([iterable ])**
# > Return a new set object, optionally with elements taken from iterable. set is a built-in class.
# 
# **setattr (object, name, value)**
# > This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123. Note: Since private name mangling happens at compilation time, one must manually mangle a private attribute’s (attributes with two leading underscores) name in order to set it with setattr().
# 
# **class slice (stop)** or **class slice (start, stop[, step ])**
# > Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default).
# 
# **sorted (iterable, *, key = None, reverse = False)**
# > Return a new sorted list from the items in iterable. Has two optional arguments which must be specified as keyword arguments.
# key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly). reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed. The built-in sorted() function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade). For sorting examples and a brief sorting tutorial, see sortinghowto.
# 
# **@staticmethod**
# > Transform a method into a static method. A static method does not receive an implicit first argument. To declare a static method, use this idiom:
# ```python
# class C:
# @staticmethod
# def f(arg1, arg2, ...): ...
# ```
# > The @staticmethod form is a function decorator – see function for details. A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()). Static methods in Python are similar to those found in Java or C++. Also see classmethod() for a variant that is useful for creating alternate class constructors. Like all decorators, it is also possible to call staticmethod as a regular function and do something with its result. This is needed in some cases where you need a reference to a function from a class body and you want to avoid the automatic transformation to instance method. For these cases, use this idiom:
# ```python
# class C:
# builtin_open = staticmethod(open)
# ```
# > For more information on static methods, see types.
# 
# **class str (object=”)** or **class str (object=b”, encoding=’utf-8’, errors=’strict’)**
# > Return a str version of object. See str() for details. str is the built-in string class.
# 
# **sum (iterable, /, start = 0)**
# > Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string. For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence). To add floating point values with extended precision, see math.fsum(). To concatenate a series of iterables, consider using itertools.chain(). Changed in version 3.8: The start parameter can be specified as a keyword argument.
# 
# **super ([type[, object-or-type ] ])**
# > Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing
# inherited methods that have been overridden in a class.
# 
# **class tuple ([iterable ])**
# > Rather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.
# 
# **class type (object)** or **class type (name, bases, dict, **kwds)**
# > With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.\_\_class\_\_. The isinstance() built-in function is recommended for testing the type of an object, because it takes
# subclasses into account. With three arguments, return a new type object....
# 
# **vars ([object])**
# > Return the \_\_dict\_\_ attribute for a module, class, instance, or any other object with a \_\_dict\_\_ attribute. Objects such as modules and instances have an updateable \_\_dict\_\_ attribute; however, other objects may have write restrictions on their \_\_dict\_\_ attributes (for example, classes use a types. MappingProxyType to prevent direct dictionary updates). Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored. A TypeError exception is raised if an object is specified but it doesn’t have a \_\_dict\_\_ attribute (for example, if its class defines the \_\_slots\_\_ attribute).
# 
# **zip (*iterables)**
# > Make an iterator that aggregates elements from each of the iterables. Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
# 
# **\_\_import\_\_ (name, globals = None, locals = None, fromlist = (), level = 0)**
# > Note: This is an advanced function that is not needed in everyday Python programming, unlike importlib.import_module().
# This function is invoked by the import statement. It can be replaced (by importing the builtins module and assigning to builtins.\_\_import\_\_) in order to change semantics of the import statement, but doing so is **strongly** discouraged as it is usually simpler to use import hooks (see PEP 302) to attain the same goals and does not cause issues with code which assumes the default import implementation is in use. Direct use of \_\_import\_\_() is also discouraged in favor of importlib.import_module(). The function imports the module name, potentially using the given globals and locals to determine how to interpret the name in a package context. The fromlist gives the names of objects or submodules that should be imported from the module given by name. The standard implementation does not use its locals argument at all, and uses its globals only to determine the package context of the import statement. level specifies whether to use absolute or relative imports. 0 (the default) means only perform absolute imports. Positive values for level indicate the number of parent directories to search relative to the directory of the module calling \_\_import\_\_() (see PEP 328 for the details). When the name variable is of the form package.module, normally, the top-level package (the name up till the first dot) is returned, not the module named by name. However, when a non-empty fromlist argument is given, the module named by name is returned.

# ## 3. Built-in constants

# A small number of constants live in the built-in namespace. They are:
# 
# **False**
# > The false value of the bool type. Assignments to False are illegal and raise a SyntaxError.
# 
# **True**
# > he true value of the bool type. Assignments to True are illegal and raise a SyntaxError.
# 
# **None**
# >The sole value of the type NoneType. None is frequently used to represent the absence of a value, as when default arguments are not passed to a function. Assignments to None are illegal and raise a SyntaxError.
# 
# **NotImplemented**
# >Special value which should be returned by the binary special methods (e.g. \_\_eq\_\_(), \_\_lt\_\_(),\_\_add\_\_(), \_\_rsub\_\_(), etc.) to indicate that the operation is not implemented with respect to the other type; may be returned by the in-place binary special methods (e.g. \_\_imul\_\_(), \_\_iand\_\_(), etc.) for the same purpose. It should not be evaluated in a boolean context. Note: When a binary (or in-place) method returns NotImplemented the interpreter will try the reflected operation on the other type (or some other fallback, depending on the operator). If all attempts return NotImplemented, the interpreter will raise an appropriate exception. Incorrectly returning NotImplemented will result in a misleading error message or the NotImplemented value being returned to Python code. See Implementing the arithmetic operations for examples. Note: NotImplementedError and NotImplemented are not interchangeable, even though they have similar names and purposes. See NotImplementedError for details on when to use it.
# 
# **Ellipsis**
# > The same as the ellipsis literal “...”. Special value used mostly in conjunction with extended slicing syntax for user-defined container data types.
# 
# **\_\_debug\_\_**
# > This constant is true if Python was not started with an -O option. See also the assert statement.
# 
# <div class="alert alert-block alert-info">
# <b>Note:</b> The names None, False, True and __debug__ cannot be reassigned (assignments to them, even as an attribute name, raise SyntaxError), so they can be considered “true” constants.
# </div>

# ### 3.1. Constants added by the site module

# The site module (which is imported automatically during startup, except if the -S command-line option is given) adds several constants to the built-in namespace. They are useful for the interactive interpreter shell and should not be used in programs.
# 
# **quit** (code = None)
# 
# **exit** (code = None)
# > Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”, and when called, raise SystemExit with the specified exit code.
# 
# **copyright**
# 
# **credits**
# > Objects that when printed or called, print the text of copyright or credits, respectively.
# 
# **license**
# > Object that when printed, prints the message “Type license() to see the full license text”, and when called, displays the full license text in a pager-like fashion (one screen at a time).

# In[ ]:




