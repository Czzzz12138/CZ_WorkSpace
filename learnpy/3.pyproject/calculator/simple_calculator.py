"""
简单计算器项目
功能：
1. 基本四则运算 (+, -, *, /)
2. 连续计算功能
3. 历史记录
4. 错误处理
5. 用户友好的界面
"""

import datetime  # datetime 模块用于处理日期和时间


class SimpleCalculator:
    """简单计算器类"""
    
    def __init__(self):
        """初始化计算器"""
        self.history = []  # 存储计算历史
        self.last_result = 0  # 存储上次计算结果
        
    def add(self, a, b):
        """加法运算"""
        return a + b
    
    def subtract(self, a, b):
        """减法运算"""
        return a - b
    
    def multiply(self, a, b):
        """乘法运算"""
        return a * b
    
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("除数不能为零！")
        return a / b
    
    def calculate(self, num1, operator, num2):
        """执行计算"""
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        
        if operator not in operations:
            raise ValueError("不支持的运算符！")
        
        result = operations[operator](num1, num2)
        
        # 记录历史
        calculation = f"{num1} {operator} {num2} = {result}"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"[{timestamp}] {calculation}")
        
        self.last_result = result
        return result
    
    def show_history(self):
        """显示计算历史"""
        if not self.history:
            print("📝 暂无计算历史")
            return
        
        print("\n📝 计算历史:")
        print("-" * 50)
        for record in self.history[-10:]:  # 显示最近10条记录
            print(record)
        print("-" * 50)
    
    def clear_history(self):
        """清除历史记录"""
        self.history.clear()
        print("✅ 历史记录已清除")
    
    def get_number_input(self, prompt):
        """安全地获取数字输入"""
        while True:
            try:
                user_input = input(prompt).strip()
                
                # 检查是否使用上次结果
                if user_input.lower() == 'ans':
                    return self.last_result
                
                return float(user_input)
            except ValueError:
                print("❌ 请输入有效的数字！")
    
    def get_operator_input(self):
        """获取运算符输入"""
        valid_operators = ['+', '-', '*', '/']
        while True:
            operator = input("请输入运算符 (+, -, *, /): ").strip()
            if operator in valid_operators:
                return operator
            print("❌ 请输入有效的运算符 (+, -, *, /)！")
    
    def run(self):
        """运行计算器主程序"""
        print("🧮 欢迎使用简单计算器！")
        print("=" * 40)
        print("💡 提示:")
        print("  • 输入 'ans' 可以使用上次计算结果")
        print("  • 输入 'history' 查看计算历史")
        print("  • 输入 'clear' 清除历史记录")
        print("  • 输入 'quit' 退出程序")
        print("=" * 40)
        
        while True:
            try:
                print(f"\n当前结果: {self.last_result}")
                
                # 获取用户选择
                choice = input("\n请选择操作 (计算/history/clear/quit): ").strip().lower()
                
                if choice == 'quit':
                    print("👋 感谢使用计算器，再见！")
                    break
                elif choice == 'history':
                    self.show_history()
                    continue
                elif choice == 'clear':
                    self.clear_history()
                    continue
                
                # 执行计算
                print("\n🔢 开始计算:")
                num1 = self.get_number_input("请输入第一个数字 (或输入 'ans' 使用上次结果): ")
                operator = self.get_operator_input()
                num2 = self.get_number_input("请输入第二个数字 (或输入 'ans' 使用上次结果): ")
                
                result = self.calculate(num1, operator, num2)
                
                print(f"\n✅ 计算结果: {num1} {operator} {num2} = {result}")
                
                # 询问是否继续
                continue_calc = input("\n是否继续计算？(y/n): ").strip().lower()
                if continue_calc == 'n':
                    print("👋 感谢使用计算器，再见！")
                    break
                    
            except ValueError as e:
                print(f"❌ 错误: {e}")
            except KeyboardInterrupt:
                print("\n\n👋 程序被用户中断，再见！")
                break
            except Exception as e:
                print(f"❌ 发生未知错误: {e}")


def main():
    """主函数"""
    calculator = SimpleCalculator()
    calculator.run()


if __name__ == "__main__":
    main()
