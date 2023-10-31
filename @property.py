class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def ten_value(self):
      return 10* self._value

  @ten_value.setter
  def ten_value(self, newvalue):
     self._value = newvalue


obj1 = MyClass(100)
print(obj1._value)
obj1.show()
obj1.ten_value = 1000
print(obj1._value)
obj1.show()
