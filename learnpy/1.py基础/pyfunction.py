#这里是 Python 的函数内容
# 目录
## 1.函数定义与调用
## 2.函数参数
## 3.返回值
## 4.函数嵌套
## 5.作用域
## 6.匿名函数
## 7.内置函数
## 8.拆包
## 9.闭包与装饰器及函数糖

# 1.函数定义与调用
# 函数是 Python 中的基本代码组织单元
# 函数可以封装一段可重用的代码逻辑

# 函数定义使用 def 关键字，后跟函数名和参数列表
# 函数可以有多个参数，也可以没有参数
# 函数可以有默认参数，允许在调用时省略某些参数
# 函数可以有可变参数，允许传递任意数量的位置参数
# 函数可以有关键字参数，允许传递任意数量的键值对参数
# 函数可以嵌套定义，允许在一个函数内部定义另一个函数

# 函数调用时使用函数名和括号

# 函数可以有返回值，使用 return 语句返回结果 碰到return时函数结束
# 函数可以返回多个值，使用元组或列表返回

# 函数可以作为参数传递
# 函数可以作为返回值


# 函数定义
# 函数是 Python 中的基本代码组织单元
# 函数可以封装一段可重用的代码逻辑

# 定义一个函数
def greet(name):
    print("Hello,", name)
# 调用函数
greet("Alice")
greet("Bob")

# 函数可以有参数
# 函数可以有多个参数
def add(a, b):
    return a + b
result = add(3, 5)
print("Sum:", result)
# 函数可以有默认参数 不定义时使用默认值
def multiply(a, b=1):
    return a * b
result = multiply(4)
print("Product with default b:", result)
# 函数可以有可变参数 
def concatenate(*args):
    return " ".join(args)
result = concatenate("Hello", "world", "from", "Python")
print("Concatenated string:", result)
# 函数可以有关键字参数
def person_info(name, age, **kwargs):   
    info = {"name": name, "age": age}
    info.update(kwargs)
    return info
info = person_info("Alice", 30, city="New York", job="Engineer")
print("Person info:", info)

# 函数可以嵌套定义
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
add_five = outer_function(5)
print("Add five:", add_five(10))  # 输出: Add five: 15

# 2.返回值
# 函数可以有返回值 使用 return 语句返回结果 碰到return时函数结束
# 函数可以返回多个值 返回元组 
def min_max(numbers):
    return min(numbers), max(numbers)#这时返回的是一个元组
min_val, max_val = min_max([1, 2, 3, 4, 5])
print("Min:", min_val, "Max:", max_val)
# 函数可以返回多个值 返回列表
def min_max(numbers):
    return [min(numbers), max(numbers)]
min_val, max_val = min_max([1, 2, 3, 4, 5])
print("Min:", min_val, "Max:", max_val)

# 函数可以作为参数传递
def apply_function(func, value):
    return func(value)  
result = apply_function(lambda x: x * 2, 10)
print("Applied function result:", result)  # 输出: Applied function result: 20
# 函数可以作为返回值，这时返回的是一个函数的引用
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
double = create_multiplier(2)
triple = create_multiplier(3)
print("Double 5:", double(5))  # 输出: Double 5: 10
print("Triple 5:", triple(5))  # 输出: Triple 5: 15


# 3.函数参数
# 函数参数可以分为位置参数、默认参数、可变参数和关键字参数

# 位置参数是最常见的参数类型，按顺序传递，又叫必需参数
def subtract(a, b):
    return a - b
result = subtract(10, 5)
print("Subtraction result:", result)  # 输出: Subtraction result: 5

# 默认参数在函数定义时指定，如果调用时未提供该参数，则使用默认值
def divide(a, b=1):
    return a / b
result = divide(10)
print("Division with default b:", result)  # 输出: Division with default b: 10.0

# 可变参数是允许传递任意数量的位置参数，常用于不确定参数个数的场景
def concatenate(*args):     # *args将实参所有的位置参数接收，放在一个元组中
    return " ".join(args)
result = concatenate("Hello", "world", "from", "Python")
print("Concatenated string:", result)
# 输出: Concatenated string: Hello world from Python

# 关键字参数是允许传递任意数量的键值对参数
# 
def person_info(name, age, **kwargs):   #**kwargs：将实参所有的关键字参数接收，放在一个字典中
    info = {"name": name, "age": age}
    info.update(kwargs)
    return info
info = person_info("Alice", 30, city="New York", job="Engineer")
print("Person info:", info)
# 输出: Person info: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# 函数参数可以有默认值和可变参数的组合
def person_info(name, age, city="Unknown", **kwargs):
    info = {"name": name, "age": age, "city": city}
    info.update(kwargs)
    return info
info = person_info("Alice", 30, city="New York", job="Engineer")
print("Person info with default city:", info)
# 输出: Person info with default city: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# 4.函数嵌套
# 嵌套定义：函数可以嵌套定义，允许在一个函数内部定义另一个函数
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function#注意这里的缩进

add_five = outer_function(5)
print("Add five:", add_five(10))  # 输出: Add five: 15
# 输出: Add five: 15
# 嵌套调用：函数可以嵌套调用，允许在一个函数内部调用另一个函数

# 嵌套调用示例：在一个函数内部调用另一个函数
def square(x): 
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

result = sum_of_squares(3, 4)
print("Sum of squares:", result)  # 输出: Sum of squares: 25

# 5.作用域
# 作用域是 Python 中的一个重要概念，它决定了变量的可见性和生命周期
# 作用域可以分为全局作用域和局部作用域
# 全局作用域：全局作用域中的变量可以在整个程序中访问
# 局部作用域：局部作用域中的变量只能在函数内部访问

#全局变量：在函数外部定义的变量，可以在整个程序中访问
x = 10
def my_function1():
    print(x)
my_function1()
print(x)

#局部变量：在函数内部定义的变量，只能在函数内部访问 
def my_function2():
    x = 20
    print(x)
my_function2()
print(x)#这里x的值没有改变

#global关键字：在函数内部定义的变量，可以在函数外部访问
def my_function3():
    global x   #global关键字用于声明变量是全局变量 注意语法：global 变量名（可以同时声明多个变量）
    x = 20
    print(x)
my_function3()
print(x)#这里x的值改变了    

#nonlocal关键字：在函数内部定义的变量，可以在函数内部访问 
# 注意：nonlocal关键字只能用于嵌套函数中，不能用于全局作用域
# 其作用只改变嵌套函数中上一层变量的值，不会改变全局变量的值
def outer_function():
    x = 10
    def inner_function():
        nonlocal x #nonlocal关键字用于声明变量是嵌套函数中上一层变量 注意语法：nonlocal 变量名（可以同时声明多个变量）
        x = 20
        print(x)
    inner_function()
    print(x)
outer_function()
print(x)#这里x的值是全局变量 没有改变
# 输出: 20 20 10

# 6.匿名函数
# 匿名函数是一种没有名字的函数，通常用于简单的函数
# 匿名函数使用 lambda 关键字定义，语法：lambda 参数: 表达式
# 匿名函数只能包含一个表达式，不能包含多个表达式
# 匿名函数没有名字，不能被其他函数调用
# 匿名函数可以作为参数传递给其他函数

# 基本语法：函数名 = lambda 参数: 表达式
# 示例：
add = lambda x, y: x + y
print(add(1, 2))
# 输出: 3

# 匿名函数的参数可以有多个，也可以没有参数
# 可以是可变参数（*args），关键字参数（**kwargs），默认参数（要放在非默认参数后）
# 示例：
add = lambda *args, **kwargs: sum(args) + sum(kwargs.values())
print(add(1, 2, 3, 4, 5, a=6, b=7))
# 输出: 33
# 示例：
add = lambda x, y=1: x + y
print(add(1)) 
# 输出: 2

# lambda结合if判断
add = lambda x, y: x + y if x > y else x - y #其实就是三目运算符
print(add(1, 2))
# 输出: -1  


# 7.内置函数
# 内置函数是 Python 中预定义的函数，可以直接使用，不需要导入模块
# 内置函数可以分为以下几类：
# 数学函数：abs绝对值、pow幂、round四舍五入、max最大值、min最小值、sum求和、len长度、sorted排序、reversed反转、zip合并、map映射、filter过滤、reduce归约
# 字符串函数：str字符串、len长度、upper大写、lower小写、capitalize首字母大写、title每个单词首字母大写、strip去除空格、split分割、
#            join合并、replace替换、find查找、count计数、startswith是否以指定字符串开头、endswith是否以指定字符串结尾
# 列表函数：list列表、append添加、extend扩展、insert插入、remove删除、pop弹出、clear清空、sort排序、reverse反转
# 字典函数：dict字典、keys键、values值、items键值对、get获取、pop弹出、popitem随机弹出、clear清空、update更新
# 集合函数：set集合、add添加、remove删除、discard删除、clear清空、union并集、intersection交集、difference差集、symmetric_difference对称差集
# 文件函数：open打开、close关闭、read读取、write写入、seek移动、tell当前位置、flush刷新、truncate截断
# 时间函数：time时间、datetime日期时间、timedelta时间差、sleep睡眠、strftime格式化、strptime解析

#查看所有的内置函数
import builtins
print(dir(builtins))#dir()函数可以查看所有的内置函数


# 8.拆包
# 拆包是 Python 中的一种操作，它可以将一个序列（如列表、元组、字典）拆分成多个变量
# 拆包的语法是：变量1, 变量2, ... = 序列
# 拆包的语法是：变量1, 变量2, ... = 序列

a, b, c = [1, 2, 3]
print(a, b, c)
# 输出: 1 2 3

a, b, c = (1, 2, 3)
print(a, b, c)
# 输出: 1 2 3

a,*b = [1, 2, 3, 4, 5]
print(a, b)

# 9.闭包与装饰器及函数糖

# 函数作为返回值：闭包
# 闭包：闭包是函数内部定义的函数，可以访问函数内部的变量
# 闭包的语法是：def outer_function():
#                def inner_function():
#                    print(x)
#                return inner_function   #返回的是inner_function的引用
#                inner_function = outer_function()
#                inner_function()       #调用的是inner_function
# 闭包的语法是：def outer_function():
def outer_function():
    x = 10
    def inner_function():
        print(x)
    return inner_function

outer_function()()    #这里返回的是inner_function的引用
# 相当于:
# inner_function = outer_function()
# inner_function()    #这里调用的是inner_function
# 输出: 10


# 装饰器：装饰器是函数，可以装饰其他函数
# 装饰器是函数，可以装饰其他函数，装饰器可以添加新的功能
# 函数糖是装饰器的语法糖，可以简化装饰器的使用

# 装饰器的语法是：def decorator(func):
#                def wrapper(*args, **kwargs):
#                    print("Before function")
#                    func(*args, **kwargs)
#                    print("After function")
#                return wrapper
# 原理： 
#        # 装饰器函数接收一个函数作为参数，返回一个函数
#        # 装饰器函数内部定义一个函数，这个函数内部调用被装饰的函数
#        # 装饰器函数返回这个内部函数
#        # 被装饰的函数被装饰器函数装饰后，被装饰的函数被内部函数替换，内部函数可以添加新的功能
#        # 在上面这个例子中，被装饰的函数是func，装饰器函数是decorator，内部函数是wrapper
#例子
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        func(*args, **kwargs)
        print("After function")
    return wrapper
# 使用装饰器
@decorator##函数糖
def func():
    print("Hello, world!")
func()
# 输出: Before function Hello, world! After function

#使用装饰器 相当于decorator(func)()
decorator(func)()
# 输出: Before function Hello, world! After function


# 一个稍微复杂一点的装饰器例子：带参数的装饰器，并统计被装饰函数的调用次数

def count_calls(prefix="调用"):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"{prefix}第{count}次: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@count_calls("执行")  #函数糖，表示用count_calls装饰器装饰say_hello函数xx
def say_hello(name):
    print(f"你好, {name}!")

@count_calls("运行")
def add(a, b):
    print(f"{a} + {b} = {a + b}")

say_hello("小明")    #相当于count_calls("执行")(say_hello)("小明")，
                    #先执行count_calls("执行")，返回decorator函数，再执行decorator(say_hello)，返回wrapper函数，再执行wrapper("小明")
say_hello("小红")
add(3, 5)               #相当于count_calls("运行")(add)(3, 5)，
                    #先执行count_calls("运行")，返回decorator函数，再执行decorator(add)，返回wrapper函数，再执行wrapper(3, 5)
add(10, 20)
add(1, 2)

# 输出示例:
# 执行第1次: say_hello
# 你好, 小明!
# 执行第2次: say_hello
# 你好, 小红!
# 运行第1次: add
# 3 + 5 = 8
# 运行第2次: add
# 10 + 20 = 30
# 运行第3次: add
# 1 + 2 = 3



