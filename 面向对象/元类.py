"""
python一切都是对象
元类：实例化产生类的类
元类    --  实例化 --》类--〉实例化--》对象

"""
class Mytype(type):
    def __init__(cls,*args,**kwargs):
        pass
    def __new__(cls,*args,**kwargs):
        print('Mytype.__new__')
        return type.__new__(cls,*args,**kwargs)
    def __call__(self, *args, **kwargs):
        human_obj = self.__new__(self)

        self.__init__(human_obj, *args, **kwargs)
        
        return human_obj



class Human(metaclass=Mytype):
    '''
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print('name:',self.name,'age:',self.age)

    def __new__(cls,*args,**kwargs):

        obj = super().__new__(cls)
        return obj
class Human2:
    '''
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print('name:',self.name,'age:',self.age)
obj = Human('sdsa',123)
print(obj)
