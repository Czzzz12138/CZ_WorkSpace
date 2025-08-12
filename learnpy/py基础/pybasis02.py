#这里是 Python 的基础语法02
# 目录
## 1.if语句
## 2.for循环
## 3.while循环
## 4.break和continue语句
## 5.列表list
## 6.元组tuple，集合set和字典dict
## 7.字符串编码
## 8.可变与不可变对象
## 9.深浅拷贝

# 1.if语句
# if 语句用于根据条件执行不同的代码块
# if 条件:
#     # 条件为 True 时执行的代码块
# else:
#     # 条件为 False 时执行的代码块
# 格式 如下：
print("if语句代码输出")
# if 语句用于根据条件执行不同的代码块
a = input("请输入一个数字a：")
a = int(a)  # 将输入转换为整数
if a > 0:
    print("a 是正数")
else:
    print("a 不是正数")


# elif 可以用于检查多个条件
print("elif代码输出")
b = input("请输入另一个数字b：")
b = int(b)  # 将输入转换为整数
if b > 0:
    print("b 是正数")
elif b == 0:
    print("b 是零")
else:
    print("b 是负数")
# if 语句可以嵌套使用
print("嵌套if语句代码输出")
if a > 0:
    print("a 是正数")
    if b > 0:
        print("b 也是正数")
    else:
        print("b 不是正数")
# if 语句可以使用逻辑运算符组合多个条件
print("if逻辑运算符代码输出")
is_true = True
is_false = False
if is_true and not is_false:
    print("条件为真")
# if 语句可以使用比较运算符比较多个值
print("if比较运算符代码输出") 
a = 10
b = 5
if a > b:
    print("a 大于 b")
# if 语句可以使用布尔值直接判断
print("if布尔值判断代码输出") 
if is_true:
    print("is_true 为真")
if not is_false:
    print("is_false 为假")
# if 语句可以使用三元表达式简化条件判断
print("if三元表达式代码输出")
result = "正数" if a > 0 else "非正数"
print("a 是:", result)
# if 语句可以使用 pass 语句占位 
# pass 语句用于占位，不执行任何操作
# 这在需要保留代码结构但暂时不执行任何操作时有用
# pass 语句可以用于占位符代码
print("if占位符代码输出")
if a > 0:
    pass
print(" ")


# 2.for循环
# for 循环用于遍历序列（如列表、元组、字符串等）
# 格式   for 变量 in 可迭代对象:
#              # 执行的代码块  
# 
#可迭代对象是指可以逐个访问其元素的对象，如列表、元组、字符串、字典等

# for 循环可以使用 range() 函数生成数字序列 
#range() 函数生成一个指定范围的整数序列
#class range(start, stop[, step])
#range(stop) 默认从 0 开始
#range(start, stop) 指定起始和结束值 包括起始值，不包括结束值
#range(start, stop[, step]) 指定起始、结束和步长
# range() 函数返回一个可迭代对象，可以用于 for 循环
print("for循环range代码输出")
for i in range(5):
    print("当前数字是:", i)

# for 循环可以遍历列表
print("for循环列表代码输出")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print("列表中的元素是:", item)  

# for 循环可以遍历字符串
print("for循环字符串代码输出")
my_string = "Hello"
for char in my_string:
    print("字符串中的字符是:", char)

# for 循环可以使用 enumerate() 函数获取索引和值
print("for循环enumerate代码输出")
for index, char in enumerate(my_string):
    print("索引:", index, "字符:", char)

# for 循环可以使用 zip() 函数同时遍历多个序列
print("for循环zip代码输出")
for item, char in zip(my_list, my_string):
    print("列表元素:", item, "字符串字符:", char)
print(" ")

# 3.while循环
# while 循环用于在条件为 True 时重复执行代码块
# 格式 while 条件:
            # 执行的代码块
print("while循环代码输出")
count = 0
while count < 5:
    print("当前计数是:", count)
    count += 1
print(" ")
# while循环嵌套
print("嵌套while循环代码输出")
i = 0
while i < 3:
    print("外层循环:", i)
    j = 0
    while j < 2:
        print("  内层循环:", j)
        j += 1
    i += 1
print(" ")

# 4.break和continue语句
# break 语句用于跳出循环
# break 语句会立即终止循环，不再执行循环中的剩余代码
# break 语句通常用于在满足特定条件时提前退出循环
print("break代码输出")
for i in range(5):
    if i == 3:
        break
    print("当前数字是:", i)
print(" ")
# continue 语句用于跳过当前循环的剩余部分
# continue 语句会跳过当前迭代的剩余代码，直接进入下一次循环
# continue 语句通常用于在满足特定条件时跳过某些迭代
# 在continue之前要修改循环变量，否则会导致死循环
print("continue代码输出")
for i in range(5):
    if i == 3:
        continue
    print("当前数字是:", i)
print(" ")

# 5.列表list
# 列表是 Python 中的可变序列，可以存储多个元素
# 列表使用方括号 [] 定义，元素之间用逗号分隔
print("列表代码输出")
my_list = [1, 2, 3, 4, 5]
# 列表可以包含不同类型的元素
mixed_list = [1, "hello", 3.14, True]   
# 列表支持索引和切片操作
print("第一个元素:", my_list[0])  # 输出: 第一个元素: 1
print("最后一个元素:", my_list[-1])  # 输出: 最后一个元素: 5
print("切片:", my_list[1:4])  # 输出: 切片: [2, 3, 4]
# 列表支持添加、删除和修改元素
my_list.append(6)  # 添加元素
print("添加元素后:", my_list)
my_list.insert(3, 0)  # 插入元素
print("插入元素后:", my_list)
my_list.extend([7, 8])  # 扩展列表，添加多个元素
print("扩展列表后:", my_list)

my_list.remove(2)  # 删除指定元素 重复默认删第一个
print("删除指定元素后:", my_list)
my_list.pop()  # 默认删除最后一个元素
print("删除最后一个元素后:", my_list)
del my_list[3]  # 删除指定索引的元素  也可以删除列表del my_list
print("删除指定索引元素后:", my_list)
my_list[0] = 10  # 修改元素
print("修改元素后:", my_list)   

# 列表支持排序和反转
my_list.sort()  # 升序排序
print("排序后:", my_list)  # 输出: 排序后: [0, 3, 4, 5, 6, 7, 8, 10]
my_list.sort(reverse=True)  # 降序排序
print("降序排序后:", my_list)  # 输出: 降序排序后: [10, 8, 7, 6, 5, 4, 3, 0]
my_list.reverse()  # 反转列表
print("反转后:", my_list)  # 输出: 反转后: [0, 3, 4, 5, 6, 7, 8, 10]

# 列表支持检查元素是否存在
print("是否包含 3:", 3 in my_list)  # 输出: 是否包含 3: True
print("是否包含 9:", 9 in my_list)  # 输出: 是否包含 9: False

# 列表支持多种内置方法
print("列表长度:", len(my_list))  # 输出: 列表长度: 5
print("最大值:", max(my_list))  # 输出: 最大值: 10
print("最小值:", min(my_list))  # 输出: 最小值: 3
print("列表求和:", sum(my_list))  # 输出: 列表求和: 30

# 列表推导式
# 列表推导式是一种简洁的创建列表的方法
# 可以使用列表推导式来生成新的列表
# 格式: [表达式 for 变量 in 可迭代对象 (if 条件)]
squared = [x**2 for x in my_list if x % 2 == 0]  # 生成偶数的平方列表
print("偶数的平方列表:", squared)

# 列表嵌套，就是列表中包含其他列表
# 列表嵌套可以用于存储多维数据
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_list:
    for item in sublist:
        print("嵌套列表中的元素是:", item)

print(" ")

# 6.元组tuple，集合set和字典dict
# 元组、集合和字典是 Python 中的三种常用数据结构
# 元组是不可变的序列，使用圆括号 () 定义
# 注意元组中只有一个元素时，需要在元素后面加逗号，如 tua=(1,) 否则会被认为是普通的括号运算tua=(1)，不视为元组
# 元组的元素不能修改，但可以包含不同类型的元素,类型也可以是列表或字典或者其他元组
# 元组支持索引和切片操作
# 元组可以用于存储多个值 可以重复
# 元组可以用于函数参数传递
# 元组可以用于函数返回多个值
print("元组代码输出")
my_tuple = (1, 2, 3)
print("元组:", my_tuple)
# 访问元组中的元素
print("第一个元素:", my_tuple[0])  # 输出: 第一个元素: 1
print("最后一个元素:", my_tuple[-1])  # 输出: 最后一个元素: 3
# 元组支持切片操作
print("切片:", my_tuple[1:3])  # 输出: 切片: (2, 3)
print(" ")
# 列表和元组的区别  
# 列表是可变的，可以修改元素；元组是不可变的，不能修改元素
# 元组的长度是固定的，不能添加或删除元素
#count() index() len() max() min() sum()和列表类似
#格式化输出的%()的()的本质是元组  例如print("姓名:%s,年龄:%d" %("小明",20)) 其中的("小明",20)就是一个元组

# 集合是无序的唯一元素集合，使用花括号 {} 定义
# 集合中的元素是唯一的，不允许重复
# 集合不支持索引和切片操作
# 集合可以用于查找和存储多个唯一值 
# 集合支持添加和删除元素
# 集合可以用于去重
# 集合的常用操作包括并集、交集和差集
# 集合可以用于数学运算
# 集合的常用方法包括 add()、remove() 和 union()还有 intersection()、difference()
print("集合代码输出")
my_set = {1, 2, 3, 3}
print("集合:", my_set)
# 添加元素
my_set.add(4)
print("添加元素后:", my_set)
# 删除元素
my_set.remove(2)
print("删除元素后:", my_set)
# 集合的并集、交集和差集
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("并集:", set_a.union(set_b))  # 输出: 并集: {1, 2, 3, 4, 5}  也可以使用 | 运算符
print("交集:", set_a.intersection(set_b))  # 输出: 交集: {3} 也可以使用 & 运算符
print("差集:", set_a.difference(set_b))  # 输出: 差集: {1, 2} 也可以使用 - 运算符
# 集合的推导式
# 集合推导式是一种简洁的创建新的集合的方法
# 集合推导式的格式: {表达式 for 变量 in 可迭代对象}
squared_set = {x**2 for x in my_set}
print("平方集合:", squared_set)
# 集合可以用于去重
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print("去重后的集合:", my_set)
# 集合可以用于快速查找数据
print("是否包含 3:", 3 in my_set)
print("是否包含 6:", 6 in my_set)
print("集合的长度:", len(my_set))  # 输出: 集合的长度: 5
print("集合的最大值:", max(my_set))  # 输出: 集合的最大值: 5
# 集合的最小值和求和
print("集合的最小值:", min(my_set))  # 输出: 集合的最小值: 1
print("集合的求和:", sum(my_set))  # 输出: 集合的求和: 15
print("集合的平方:", squared_set)
print("集合的平方和:", sum(squared_set))  # 输出: 集合的平方和: 55
print(" ")

# 字典是键值对的集合，使用花括号 {} 定义
# 字典使用键（key）来访问对应的值（value）
# 什么是键值对？键值对是由键和对应的值组成的
# 什么是键？键可以理解为变量，值可以理解为变量的值
# 字典中的键是唯一的，值可以是任意类型
# 字典支持索引操作，可以通过键访问对应的值
# 字典可以用于存储多个键值对
# 字典可以用于快速查找和存储数据
# 字典的常用方法包括 keys()、values() 和 items()
# 字典可以用于存储复杂数据结构
# 字典可以用于 JSON 数据的解析和生成
# 字典可以用于存储配置和参数
# 字典可以用于存储对象的属性和方法
# 字典可以用于存储数据的映射关系 关联关系
# 字典的键必须是不可变类型（如字符串、数字、元组等） 可以是任何类型
print("字典代码输出")
my_dict = {"name": "Alice", "age": 30}
print("字典:", my_dict)
# 访问字典中的值
print("姓名:", my_dict["name"])  # 输出: 姓名: Alice
print("年龄:", my_dict["age"])  # 输出: 年龄: 30
# 使用 get() 方法访问字典中的值
print("使用 get() 方法访问年龄:", my_dict.get("age"))  # 输出: 使用 get() 方法访问年龄: 30
print("使用 get() 方法访问不存在的键:", my_dict.get("gender", "未知"))  # 输出: 使用 get() 方法访问不存在的键: 未知
# 修改字典中的值
my_dict["age"] = 31
# 添加键值对
my_dict["city"] = "New York"   #键名存在就是修改，不存在就是添加
print("添加城市后:", my_dict)  # 输出: 添加城市后: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# 删除键值对
del my_dict["age"]      #del也可以删除整个字典 del my_dict 之后my_dict就不存在了
print("删除年龄后:", my_dict)  # 输出: 删除年龄后: {'name': 'Alice', 'city': 'New York'}
pop = my_dict.pop("city", "未知")  # 删除并返回指定键的值
print("删除城市后:", my_dict)  # 输出: 删除城市后: {'name': 'Alice'}
print("删除的城市:", pop)  # 输出: 删除的城市: New York
# clear = my_dict.clear()  # 清空字典
# print("清空字典后:", my_dict)  # 输出: 清空字典后: {}

# 字典的键值对可以使用 items() 方法遍历
# 遍历字典
for key, value in my_dict.items():
    print(f"{key}: {value}")
# 输出:
# name: Alice
# city: New York
# 字典的常用方法包括 keys()、values() 和 items()
print("所有键:", my_dict.keys())  # 输出: 所有键: dict_keys(['name', 'city'])
print("所有值:", my_dict.values())  # 输出: 所有值: dict_values(['Alice', 'New York'])
print("所有项:", my_dict.items())  # 输出: 所有项: dict_items([('name', 'Alice'), ('city', 'New York')])
print(" ")

# 7.字符串编码
# Python 中的字符串是 Unicode 编码的
# Unicode 是一种字符编码标准，可以表示世界上几乎所有的字符
# Python 3 默认使用 UTF-8 编码  
# UTF-8 是一种可变长度的字符编码，可以表示 Unicode 字符集中的所有字符
# Python 中的字符串可以使用 encode() 方法进行编码   
# encode() 方法将字符串编码为指定的编码格式
# 格式: str.encode(encoding='utf-8', errors='strict')
# Python 中的字符串可以使用 decode() 方法进行解码
# decode() 方法将字节串解码为字符串
# 格式: bytes.decode(encoding='utf-8', errors='strict')
# Python 中的字符串可以使用 bytes() 函数进行编码
# bytes() 函数将字符串编码为字节串
# 格式: bytes(str, encoding='utf-8', errors='strict')
# Python 中的字符串可以使用 str() 函数进行解码
# str() 函数将字节串解码为字符串
# 格式: str(bytes, encoding='utf-8', errors='strict')
# Python 中的字符串可以使用 encode() 和 decode() 方法进行编码和解码
# Python 中的字符串可以使用 bytes() 和 str() 函数进行编码和解码
# Python 中的字符串可以使用 encode() 方法进行编码
# 例子
print("字符串编码和解码代码输出")
s = "Hello, World!"
# 编码
b = s.encode(encoding='utf-8', errors='strict')
print("编码后的字节串:", b)
# 解码
s2 = b.decode(encoding='utf-8', errors='strict')
print("解码后的字符串:", s2)



# 8.可变与不可变对象
# 可变对象：可变对象是指在创建后可以修改其内容的对象
# 不可变对象：不可变对象是指在创建后不能修改其内容的对象
# 可变对象：列表、字典、集合
# 不可变对象：元组、字符串、数字
# 可变对象的内存本质：可变对象的内存本质是对象的引用，而不是对象的值
# 不可变对象的内存本质：不可变对象的内存本质是对象的值，而不是对象的引用，
# 可变对象的修改：可变对象的修改是修改对象的引用，而不是修改对象的值
# 不可变对象的修改：不可变对象的修改是修改对象的值，而不是修改对象的引用


# 9.深拷贝与浅拷贝
# 深拷贝：深拷贝是指在拷贝对象时，拷贝对象的引用，而不是拷贝对象的值
# 浅拷贝：浅拷贝是指在拷贝对象时，拷贝对象的值，而不是拷贝对象的引用
# 深拷贝的本质：深拷贝的本质是对象的引用，而不是对象的值
# 浅拷贝的本质：浅拷贝的本质是对象的值，而不是对象的引用
# 深拷贝的修改：深拷贝的修改是修改对象的引用，而不是修改对象的值
# 浅拷贝的修改：浅拷贝的修改是修改对象的值，而不是修改对象的引用

