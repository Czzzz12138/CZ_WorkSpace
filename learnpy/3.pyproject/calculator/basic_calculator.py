"""
简化版计算器 - 适合初学者
这个版本更容易理解，逐步展示了计算器的核心概念
"""

def add(a, b):
    """加法函数"""
    return a + b

def subtract(a, b):
    """减法函数"""
    return a - b

def multiply(a, b):
    """乘法函数"""
    return a * b

def divide(a, b):
    """除法函数"""
    if b == 0:
        return "错误：不能除以零！"
    return a / b

def get_numbers():
    """获取两个数字"""
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        return num1, num2
    except ValueError:
        print("请输入有效的数字！")
        return None, None

def basic_calculator():
    """基础计算器函数"""
    print("🧮 简单计算器")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 退出")
    
    while True:
        choice = input("\n请选择操作 (1-5): ")
        
        if choice == '5':
            print("再见！")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is None or num2 is None:
                continue
            
            if choice == '1':
                result = add(num1, num2)
                print(f"结果: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"结果: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"结果: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"结果: {num1} / {num2} = {result}")
        else:
            print("无效选择，请重新输入！")

if __name__ == "__main__":   # 入口函数
    basic_calculator()
