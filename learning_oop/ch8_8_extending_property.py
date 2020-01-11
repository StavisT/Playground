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
