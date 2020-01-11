# Chapter 8: Classes and objects
**Notes from Python cookbok 3. ed.**
The notes below are taken from the python cookbook. The notes are more or less direct citation from the book for me to remember better what I have read. 

## 8.5: encapsulating names in a class
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

## 8.6 Creating managed attributes
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
### Computed attributes from properties
properties can also be a way to store computed attributes. These are attributes not actually stored, but computed on demand. Example:

```
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

```

```
$ c = Circle(4.0)
$ c.radius
4.0
$ c.area
50.26548
$ c.perimeter
25.1327
```
**Notice:** the properties are not method calls, hence there are no (). 


### Avoid repetitive property definitions
example:
```
class BadPerson:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

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

    # Repeated property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name

    # Setter function
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        self._last_name = value

    # Deleter function (optional)
    @last_name.deleter
    def last_name(self):
        raise AttributeError("Cant delete attribute")
```

This often leads to bloated, error prone and ugly code. There are better ways to achieve this using descriptors or closures. See chapter 8.9 and 9.21.

# 8.7 Calling a method on a parent class
Invoke a method in a parent class in place of a method that has been override in a subclass

To call a method in a parent (or subclass), use the super() function. Example:

```
class A:
    def spam(self):
        print("A.spam")

class B(A):
    def spam(self):
        print("B.spam")
        super().spam()  # call parent spam()    
```

A very common use of super() is in the handling of the __init__() method to make sure that parents are properly initialized:

```
class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
```

another common use of super() is in code that overrides any of Python's special methods. example:

```
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    #delegate attribute lookup to internal obj
    def __getattr(self, name):
        return getattr(self._obj, name)
    
    # delegate attribute assignment
    def __setattr(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name,value) # call original __setattr__
        else:
            setattr(self._obj, name, value)
```
### Recommendations when using super():
1. Make sure that all methods with teh same name in an inheritance hierarcy have compatible calling signature (same niber of arguments, argument names). This ensures that super will not get tripped up if it tries to invoke a method on a class that is not a direct parent.
2. It is usually a good idea to make sure the topmost class provides implementation of the method so that the chain of lookups that occur along the MRO get terminated by an actual method of some sort

Blog post about super():

https://rhettinger.wordpress.com/2011/05/26/super-considered-super/


## 8.8 Extending a property in a subclass
See ch8_8_extending_property.py

Within a subclass, extend the functionality of a property defined in a parent class

```
class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        self._name = value

    # Deleter function (optional)
    @name.deleter
    def name(self):
        raise AttributeError("Cant delete attribute")


# extending the property:
class SubPerson1(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value):
        print("setting name to", value)
        super(SubPerson1, SubPerson1).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubPerson1, SubPerson1).name.__delete__(self)

# extending only parts of the property: getter only
class SubPerson2(Person):
    @Person.name.getter
    def name(self):
        print("Getting name")
        return super().name

# extending only parts of the property: setter only
class SubPerson3(Person):
    @Person.name.setter
    def name(self, value):
        print("setting name to")
        return super(SubPerson3, SubPerson3).name.__set__(self, value)


```



# 8.9 Creating a new kind of class or instance attribute
ch8_9_new_class_or_instance_attribute.py

Create a new kind of instance attribute type with some extra functionality such as type checking


If you want to create an entirely new kind of instance attribute, define it functionality in the form of a descriptor class:

```
# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        instance.__dict__[self.name]
    
    def __delete__(self, instance):
        del instance.__dict__[self.name]
```

A descriptor is a class that implements the three core attribute access operations (get, set and delete) in the form \_\_get\_\_(), \_\_set\_\_() and \_\_delete\_\_() special methods. The underlying dictionary of the instance is then manipulated as appropriate.

To use a descriptor, instances of the decriptor are placed into a class definition as class variables:

```
# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        instance.__dict__[self.name]
    
    def __delete__(self, instance):
        del instance.__dict__[self.name]
```


```
class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
```
One confusion with descriptors is that they can only be defined at the class level, not on a per instance basis. Thus, code like this will not work:

```
# Does NOT work
class BadPoint:
    def __init__(self, x, y):
        self.x = Integer('x')
        self.y = Integer('y')
        self.x = x
        self.y = y
```



```
# descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("Expected " + str(self.expected_type))
        instance.__dict__[self.name]
```

question: is it possible to have a dictionary as input where a descriptor for a type-checked attribute is used?

