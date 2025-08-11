#这里是 Python 的基础语法01
#目录
## 1.注释与文档字符串
## 2.print函数
## 3.变量
## 4.数据类型
## 5.类型转换
## 6.占位符与格式化输出
## 7.f格式化字符串
## 8.运算符
## 9.运算符优先级
## 10.输入函数
## 11.转义字符
## 12.代码风格
## 13.常见错误


# 1.注释与文档字符串

#  我是单行注释


# 文档字符串（docstring）用于为模块、类、函数或方法提供说明 也叫 多行注释
# 文档字符串使用三引号（''' 或 """）括起来，通常放在定义的第一行
''' 
这是多行注释
可以有多行
'''

#CTRL + / 可以注释或取消注释选中的行
#CTRL + Z 可以撤销上一步操作
#CTRL + F 可以查找


# 2.print函数
'''
(function) def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None
'''

#例子
print("Hello, World!")

print(
    "Hello, cz!","Hello, cz!","Hello, cz!",
    sep=" | ",
    end="\t",
)

print(
    "Hello, cz!","Hello, cz!","Hello, cz!",
    sep=" | ",
    end="\n",
)

#3.变量
# 变量是用来存储数据的容器
# 在 Python 中，变量不需要声明类型，可以直接赋值

# 变量名的命名规则：
## 1.只能包含字母、数字和下划线
## 2.不能以数字开头
## 3.不能是 Python 的保留字（如 if、else、while 等）
##    python 保留字可以通过 import keyword; print(keyword.kwlist) 查看
       # 关键字列表
import keyword
print(keyword.kwlist)

## 4.变量名区分大小写（如 myVar 和 myvar 是不同的变量名）
## 5.变量名不能包含空格
## 6.变量名不能使用特殊字符（如 @、#、$ 等）


# 变量名的命名规范：
## 1.使用小写字母和下划线分隔单词（如 my_variable）
## 2.使用驼峰命名法（如 myVariable）大/小驼峰 
## 3.使用大写字母开头的类名（如 MyClass）
## 4.使用全大写字母的常量名（如 MY_CONSTANT）
## 5.变量名应该具有描述性，能够清楚地表达变量的含义

# 例子
name = "cz"
age = 18    
height = 1.755
print("Name:", name)
print("Age:", age)      
print("Height:", height)

# 4.数据类型
# Python 中有多种数据类型，包括整数、浮点数、字符串、布尔值等
# type() 函数可以用来查看变量的数据类型
print("Type of name:", type(name))       # 输出: Type of name: <class 'str'>
print("Type of age:", type(age))         # 输出: Type of age: <class 'int'>
print("Type of height:", type(height))   # 输出: Type of height: <class 'float'>

# 整数类型  int
num1 = 10  

# 浮点数类型  float    
# 浮点数是带小数点的数字
num2 = 3.14     

# 字符串类型  str
# 字符串是由字符组成的文本数据  
# 字符串可以用单引号或双引号括起来
greeting = "Hello, World!"
message = '''
             Hello, cz!
             
             Welcome to Python programming.
          '''  # 三引号可以表示多行字符串

# 布尔类型  bool
# 布尔值只有两个可能的值：True 和 False (注意首字母大写)
# 布尔值通常用于条件判断
# bool值可以当作整形使用，True 等于 1，False 等于 0
print("True as int:", int(True))   # 输出: True as int: 1
print("False as int:", int(False)) # 输出: False as int: 0
print("True + 1:", True + 1)       # 输出: True  +  1: 2
print("False + 1:", False + 1)     # 输出: False +  1: 1
# 布尔值可以通过比较运算符（如 ==、!=、>、< 等）来生成
# 布尔值也可以通过逻辑运算符（如 and、or、not）来组合
is_true = True
is_false = False

# 复数 complex
# 复数由实部和虚部组成，虚部用 j 或 J 表示
complex_num = 2 + 3j


# 5.类型转换
# Python 支持多种类型转换，可以将一种数据类型转换为另一种数据类型
# int() 函数可以将字符串或浮点数转换为整数
# float() 函数可以将整数或字符串转换为浮点数
# str() 函数可以将整数或浮点数转换为字符串  
# 例子
num_str = "123"  # 字符串类型
num_int = int(num_str)  # 转换为整数
num_float = float(num_str)  # 转换为浮点数
tuple(num_str)  # 转换为元组（每个字符为一个元素）
list(num_str)  # 转换为列表（每个字符为一个元素）  list(可迭代对象)
chr(num_int)  # 转换为字符（ASCII码对应的字符）
print("String to int:", num_int)  # 输出: String to int: 123
print("String to float:", num_float)  # 输出: String to float: 123.0
print("String to tuple:", tuple(num_str))  # 输出: String to tuple: ('1', '2', '3')
print("String to list:", list(num_str))  # 输出: String to list: ['1', '2', '3']
print("String to char:", chr(1))  # 输出: String to char: {对应的字符}


# 6.占位符与格式化输出
# 占位符是一种特殊的符号，用于在字符串中表示变量的位置
# Python 中常用的占位符有 %s、%d、%f 等
# %s 用于表示字符串
# %d 用于表示整数
# %f 用于表示浮点数
# %% 用于表示百分号
# 占位符可以通过 % 运算符与变量结合使用

# 例子
name = "cz"
age = 18
height = 1.755
print("Name: %s" % name)  # 输出: Name: cz

print("Age: %d" % age)    # 输出: Age: 18
#%4d 表示整数至少占4个字符宽度，不足的部分用空格补齐，右对齐
print("Age: %4d" % age)   # 输出: Age:   18 (前面有两个空格)
#%-4d 表示整数至少占4个字符宽度，不足的部分用空格补齐，左对齐
print("Age: %-4d" % age)  # 输出: Age: 18   (后面有两个空格)
#04d 表示整数至少占4个字符宽度，不足的部分用0补齐，右对齐
print("Age: %04d" % age)  # 输出: Age: 0018 (前面有两个0)

print("Height: %f" % height)  # 输出: Height: 1.755000 默认6位小数
# 可以指定浮点数的精度
print("Height: %.2f" % height)  # 输出: Height: 1.75(保留两位小数 五舍六入)
# 也可以同时使用多个占位符
print("Name: %s, Age: %d, Height: %.2f" % (name, age, height))
# 输出: Name: cz, Age: 18, Height: 1.75

# 7.f格式化字符串
# 格式化字符串是一种更现代、更灵活的字符串格式化方法
# Python 3.6 及以上版本支持 f-string 格式化字符串
# f-string 以 f 或 F 开头，字符串中可以直接嵌入变量或表达式
# 格式： f"字符串 {变量或表达式} 字符串"
# 可以在大括号中使用冒号指定格式

# 例子
name = "cz"
age = 18
height = 1.755
print(f"Name: {name}")  # 输出: Name: cz    
print(f"Age: {age}")    # 输出: Age: 18
print(f"Height: {height:.2f}")  # 输出: Height: 1.75 (保留两位小数 五舍六入)
# 也可以在大括号中使用表达式
print(f"Name: {name}, Age: {age}, Height: {height:.2f}")
# 输出: Name: cz, Age: 18, Height: 1.75

# 8.运算符
# Python 支持多种运算符，包括算术运算符、比较运算符、逻辑运算符、赋值运算符等

# 算术运算符用于进行数学计算
a = 10
b = 3
# + 加法
print("Addition:", a + b)            # 输出: Addition: 13
# - 减法
print("Subtraction:", a - b)         # 输出: Subtraction: 7
# * 乘法
print("Multiplication:", a * b)      # 输出: Multiplication: 30
# / 除法
print("Division:", a / b)            # 输出: Division: 3.3333333333333335
# % 取模
print("Modulus:", a % b)             # 输出: Modulus: 1
# ** 幂运算
print("Exponentiation:", a ** b)   # 输出: Exponentiation: 1000
# // 地板除法 (向下取整除法)
print("Floor division:", a // b)  # 输出: Floor division: 3


# 比较运算符用于比较两个值的大小或相等性
# == 等于
print("Equal:", a == b)            # 输出: Equal: False
# != 不等于
print("Not equal:", a != b)        # 输出: Not equal: True
# > 大于
print("Greater than:", a > b)     # 输出: Greater than: True
# < 小于
print("Less than:", a < b)        # 输出: Less than: False
# >= 大于等于
print("Greater than or equal:", a >= b)  # 输出: Greater than or equal: True
# <= 小于等于
print("Less than or equal:", a <= b)     # 输出: Less than or equal: False

# 逻辑运算符用于组合多个布尔表达式
# and 逻辑与
print("And:", is_true and is_false)      # 输出: And: False
# or 逻辑或
print("Or:", is_true or is_false)        # 输出: Or: True
# not 逻辑非
print("Not:", not is_true)               # 输出: Not: False

# 赋值运算符用于给变量赋值
# = 赋值
c = a + b
print("c:", c)                           # 输出: c: 13
# += 加法赋值
c += 5
print("c after += 5:", c)                # 输出: c after += 5: 18
# -= 减法赋值
c -= 3
print("c after -= 3:", c)                # 输出: c after -= 3: 15           
# *= 乘法赋值
c *= 2
print("c after *= 2:", c)                # 输出: c after *= 2: 30
# /= 除法赋值
c /= 3
print("c after /= 3:", c)                # 输出: c after /= 3: 10.0 
# %= 取模赋值
c %= 4
print("c after %= 4:", c)                # 输出: c after %= 4: 2.0
# **= 幂赋值
c **= 3
print("c after **= 3:", c)                # 输出: c after **= 3: 8.0
# //= 地板除赋值
c //= 3
print("c after //= 3:", c)                # 输出: c after //= 3: 2.0    

# 字符串运算符用于对字符串进行操作
# + 字符串连接
str1 = "Hello"
str2 = "World"
print("String concatenation:", str1 + " " + str2)  # 输出: String concatenation: Hello World
# * 字符串重复
print("String repetition:", str1 * 3)  # 输出: String repetition: HelloHelloHello
# []和[:](包前不包后)  字符串索引  
print("First character of str1:", str1[0])  # 输出: First character of str1: H
print("First two characters of str1:", str1[0:2])  # 输出: First two characters of str1: He
# len() 字符串长度
print("Length of str1:", len(str1))  # 输出: Length of str1: 5

# in 字符串包含
print("Is 'Hello' in str1?", "Hello" in str1)  # 输出: Is 'Hello' in str1? True
# not in 字符串不包含
print("Is 'Python' not in str1?", "Python" not in str1)  # 输出: Is 'Python' not in str1? True
# 其他运算符
# is 对象标识符比较
print("Is str1 is str2?", str1 is str2)  # 输出: Is str1 is str2? False
print("Is str1 is str1?", str1 is str1)  # 输出: Is str1 is str1? True
# is not 对象标识符不比较
print("Is str1 is not str2?", str1 is not str2)  # 输出: Is str1 is not str2? True
print("Is str1 is not str1?", str1 is not str1)  # # 输出: Is str1 is not str1? False


# 9.运算符优先级
# 运算符优先级决定了在一个表达式中，哪些运算先进行，哪些运算后进行
# Python 中的运算符优先级从高到低依次为：
# 1. 括号 ()
# 2. 幂运算 **
# 3. 乘法、除法、取模、地板除法 * / % //
# 4. 加法、减法 + -
# 5. 比较运算符 < <= > >= == !=
# 6. 逻辑运算符 and or not
# 7. 赋值运算符 = += -= *= /= %= **= //=    
# 当多个运算符具有相同的优先级时，按从左到右的顺序进行计算
# 例子
x = 10
y = 5
z = 2
result = x + y - z * 2 / 2 ** 2
print("Result:", result)  # 输出: Result: 12.0
# 计算过程：
# 1. 先计算幂运算 2 ** 2 = 4
# 2. 再计算乘法 z * 2 = 4
# 3. 然后计算除法 4 / 4 = 1.0
# 4. 最后计算加法和减法 10 + 5 - 1.0 = 14.0
# 可以使用括号来改变运算顺序
result = (x + y - z) * 2 / 2 ** 2
print("Result with parentheses:", result)  # 输出: Result with parentheses: 6.0
# 计算过程：
# 1. 先计算括号内的表达式 (x + y - z) = 13
# 2. 再计算幂运算 2 ** 2 = 4
# 3. 然后计算乘法 13 * 2 = 26
# 4. 最后计算除法 26 / 4 = 6.5

# 10.输入函数
# input() 函数用于从控制台获取用户输入
name = input("请输入你的名字: ")
age = input("请输入你的年龄: ")
print(f"你好，{name}！你今年 {age} 岁。")
# input() 函数返回的用户输入数据类型是字符串
# 如果需要将输入转换为其他数据类型，可以使用类型转换函数
age = int(age)  # 将年龄转换为整数
print(f"明年你 {age + 1} 岁。")

# 11.转义字符
# 转义字符用于在字符串中表示一些特殊字符
# 例如：\n 表示换行，\t 表示制表符 ，\\ 表示反斜杠
print("Hello\nWorld")  # 输出: Hello
                       #      World
print("Hello\tWorld")  # 输出: Hello    World
print("Hello\\World")  # 输出: Hello\World

# 12.代码风格
# Python 有一套官方的代码风格指南，称为 PEP 8
# 遵循 PEP 8 可以提高代码的可读性和一致性
# 主要内容包括：
# 1. 缩进：使用 4 个空格进行缩进，不要使用制表符（Tab）
# 2. 行长度：每行代码的长度不超过 79 个字符
# 3. 空行：函数和类之间使用两个空行，类内部方法之间使用一个空行
# 4. 代码块：使用冒号（:）和缩进来表示代码块
# 5. 命名规范：变量名、函数名使用小写字母，单词之间用下划线分隔；类名使用大写字母开头的驼峰式命名法
# 6. 注释：注释应清晰、简洁，必要时使用文档字符串（docstring）进行说明
# 7. 空格使用：避免在逗号、冒号、分号等符号前使用空格，在这些符号后使用一个空格
# 8. 导入顺序：标准库导入、第三方库导入、自定义模块导入，且每组导入之间用一个空行分隔
# 9. 避免使用不必要的括号、分号等符号
# 10. 使用一致的引号风格，单引号或双引号均可，但要保持一致
# 11. 使用 f-string 进行字符串格式化，避免使用 % 或 str.format
# 12. 使用类型注解来提高代码的可读性和可维护性
# 13. 避免使用过于复杂的表达式，保持代码简洁


# 13.常见错误
# 1. 语法错误（SyntaxError）：代码不符合 Python 语法规则
# 2. 名称错误（NameError）：使用了未定义的变量或函数
# 3. 类型错误（TypeError）：对不支持的操作数类型执行了操作
# 4. 索引错误（IndexError）：访问了列表、元组或字符串中不存在的索引
# 5. 值错误（ValueError）：传递给函数的参数类型正确，但值不合适
# 6. 属性错误（AttributeError）：访问了对象不存在的属性或方法
# 7. 导入错误（ImportError）：导入了不存在的模块或包
# 8. 缩进错误（IndentationError）：代码块的缩进不正确
# 9. 零除错误（ZeroDivisionError）：除数为零时发生的错误
# 10. 文件未找到错误（FileNotFoundError）：尝试打开不存在的文件
# 11. 键错误（KeyError）：访问字典中不存在的键时发生的错误
# 12. 内存错误（MemoryError）：程序运行时内存不足
# 13. 断言错误（AssertionError）：断言语句失败时引发的错误
# 14. 异常处理错误（Exception Handling Error）：在异常处理过程中发生的错误
# 15. 语义错误（Semantic Error）：代码逻辑错误，导致程序行为不符合预期
# 16. 运行时错误（Runtime Error）：程序运行过程中发生的错误
# 17. 缺少冒号错误（Missing Colon Error）：在需要冒号的地方缺少冒号
# 18. 不匹配的括号错误（Mismatched Parentheses Error）：括号不匹配
# 19. 不正确的缩进错误（Incorrect Indentation Error）：代码块缩进不正确
# 20. 非法字符错误（Illegal Character Error）：代码中包含非法字符
# 21. 未闭合的字符串错误（Unclosed String Error）：字符串未正确闭合
#     ......
