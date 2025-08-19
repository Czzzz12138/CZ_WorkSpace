#这里是python 面向对象编程
# 面向对象编程（Object-Oriented Programming，OOP）是一种编程范式，它将数据和操作数据的方法封装在一起，形成一个对象。
# 面向对象编程的三大特性：封装、继承、多态
# 面向对象编程的四大基本特征：抽象、封装、继承、多态
# 面向对象编程的五大基本原则：单一职责原则、开闭原则、里氏替换原则、依赖倒置原则、接口隔离原则
# 面向对象编程的六大基本概念：类、对象、属性、方法、继承、多态

#目录：
# 1.类与对象
# 2.类的继承
## 3.类的多态
## 4.类的封装
## 5.类的静态方法
## 6.类的类方法
## 7.类的实例方法
## 8.类的属性
## 9.类的实例属性

#1.类与对象
#类的定义
#类是对象的蓝图，定义了对象的属性和方法。
#类的定义使用class关键字，后面跟类名和冒号。


class Dog:
    def __init__(self, name, age):    #self参数 代表类的实例本身
        self.name = name               #self 是作为类自己的一个索引，不管你在定义类的时候                             
        self.age = age                    #想要获取这个类的什么属性或功能，都可以通过 self 来获取

    def bark(self):
        print(self.name + "在汪汪!")

# 创建对象
dog1 = Dog("小白", 3)
dog2 = Dog("小黑", 5)

# 访问属性
print(dog1.name)  # 输出：小白
print(dog2.age)   # 输出：5

# 调用方法
dog1.bark()       # 输出：汪汪!

#2.类的继承
#继承是面向对象编程的一种机制，它允许一个类继承另一个类的属性和方法，从而实现代码的重用。
#在Python中，继承通过在类定义时指定父类来实现。

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(self.name + "在汪汪!")

class Cat(Animal):
    def speak(self):
        print(self.name + "在喵喵!")

# 创建对象
dog1 = Dog("小白", 3)
cat1 = Cat("小黑", 5)

# 调用方法
dog1.speak()  # 输出：小白在汪汪!
cat1.speak()  # 输出：小黑在喵喵!

#再看一个例子
class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time
    
    def get_info(self):
        return self.name + " is created at " + self.create_time

class Video(File):  # 继承了 File 的属性和功能
    def __init__(self, name, window_size=(1080, 720)):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name, create_time="today")   #super() 函数用于调用父类的方法
        self.window_size = window_size

class Text(File): # 继承了 File 的属性和功能
    def __init__(self, name, language="zh-cn"):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name, create_time="today") 
        self.language = language
    
    # 也可以在子类里复用父类功能
    def get_more_info(self):
        return self.get_info() + ", using language of " + self.language

v = Video("my_video")
t = Text("my_text")
print(v.get_info())     # 调用父类的功能
print(t.create_time)    # 调用父类的属性
print(t.language)       # 调用自己的属性
print(t.get_more_info()) # 调用自己加工父类的功能
