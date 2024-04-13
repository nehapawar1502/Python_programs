class MyClass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"value is {self._value}")
    # below method is used for the getter   
    @property 
    def ten_value(self):
        return 10* self._value
    # below method is used for the setter
    @ten_value.setter
    def ten_value(self, new_value):
        self_value = new_value/10
    
obj = MyClass(10)
print(obj._value)
obj.ten_value = 67
print(obj.ten_value)
obj.show()