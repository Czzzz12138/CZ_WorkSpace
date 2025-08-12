#这里是 Python 的函数内容
# 目录
## 1.函数定义与调用
## 2.函数参数
## 3.返回值
## 4.作用域
## 5.匿名函数
## 6.高阶函数
## 7.装饰器与闭包
## 8.函数糖
## 9.递归函数

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

# 函数可以有返回值 使用 return 语句返回结果 碰到return时函数结束
# 函数可以返回多个值 返回元组 
def min_max(numbers):
    return min(numbers), max(numbers)#这时返回的是一个元组
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


# 2.函数参数
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
def person_info(name, age, **kwargs):   #**kwargs：
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
