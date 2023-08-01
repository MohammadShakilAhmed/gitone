#Abstractmethod and AbstractClass
from abc import ABCMeta, abstractmethod
class car(Metaclass = ABCMeta):
  @abstractmethod
  def engine(self):
    pass
class bmw(car):
  def __init__(self,name,brand):
    self.name  = name
    self.brand = brand
  def engine(self):
    print(f"car name is {self.name} and brad is {self.brand}")

if __name__ == '__main__:
 b = bmw("X5" ,"BMW")
 b.engine()
