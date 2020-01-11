# Notes from Python cookbok 3. ed.
The notes below are taken from the python cookbook. The notes are more or less direct citation from the book for me to remember better what I have read.

## Chapter 8: Classes and objects

### 8.5: encapsulating names in a class
Encapsulate "private" data on instances of a class --> Python uses certain naming conventions.
1. Any name starting with a single leading underscore (_) should always be assumed to be internal implementation. Example:


```
class A:
    def __init__(self):
    self._internal = 0 # An internal attribute
    self.public = 1 # A public attribute

    def public_method(self):
    """
    A public method
    """
    ...

    def _internal_method(self):
    """
    an internal method
    """
```
**Remark:** python does not prevent someone from accessing internal names.

2. Any name starting with two leading underscores (\_\_) should alwyas be assumed to be private. Additionally, python renames these attributes to \_\<class\>\_\_\<private_attrbitute\>. example:

```
class C(B):
    def __init__(self):
        super().__init()
        self.__private = 1 # Does not override B.__private
    # Does not override B.__private_method()
    def __private_method(self):
    ...
```
### Recommendations for naming convention
For most code you should probably just make nonpublic names start with a single underscore. If, however you know that your code will invlve subclassing and there are internal attributes that should be hidden from subclasses, use double underscores. 

### Clashing with reserved names
Variables clashing with names of reserved words: use a single trailing underscore. Example:
```
lambda_ = 2.0
```

### 8.6 Creating managed attributes
Add extra processing (e.g. type checking or validation) to the getting or setting of an instance attribute

A simple way to do this is to define it as aproperty. The example below shows how simle type checking can be done by defining a property. The example is also implemented in ch8_6_managed_attributes.py

```
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Cant delete attribute")

```

A result of this code is that it is not possible to create an instance of Person where the input argument is not a string:

```

$ feil_person = Person(9)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~/Documents/github/Playground/learning_oop/ch8_notebook.py in 
----> 1 feil_person = Person(9)

~/Documents/github/Playground/learning_oop/ch8_6_managed_attributes.py in __init__(self, first_name)
      1 class Person:
      2     def __init__(self, first_name):
----> 3         self.first_name = first_name
      4 
      5     # Getter function

~/Documents/github/Playground/learning_oop/ch8_6_managed_attributes.py in first_name(self, value)
     12     def first_name(self, value):
     13         if not isinstance(value, str):
---> 14             raise TypeError("Expected string")
     15         self._first_name = value
     16 

TypeError: Expected string

```
