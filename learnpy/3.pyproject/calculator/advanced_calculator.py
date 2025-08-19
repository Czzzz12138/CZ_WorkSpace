"""
高级计算器 - 支持复杂表达式计算
使用Python的eval函数（注意：在实际应用中需要谨慎使用eval）
"""

import re # 正则表达式模块
import math

class AdvancedCalculator:
    """高级计算器类"""
    
    def __init__(self):
        self.history = []
        
        # 支持的数学函数
        self.math_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'abs': abs,
            'round': round,
            'pi': math.pi,
            'e': math.e
        }
    
    def is_safe_expression(self, expression):
        """检查表达式是否安全（简单的安全检查）"""
        # 允许的字符：数字、运算符、括号、小数点、数学函数
        allowed_pattern = r'^[0-9+\-*/().%^sincotaglbrqtxpe\s]+$'
        
        # 危险的关键词
        dangerous_keywords = ['import', 'exec', 'eval', 'open', 'file', '__']
        
        # 检查是否包含危险关键词
        for keyword in dangerous_keywords:
            if keyword in expression.lower():
                return False
        
        # 检查字符是否在允许范围内
        return bool(re.match(allowed_pattern, expression.replace(' ', '')))
    
    def preprocess_expression(self, expression):
        """预处理表达式"""
        # 替换一些常用符号
        expression = expression.replace('^', '**')  # 幂运算
        expression = expression.replace('π', 'pi')  # π符号
        
        # 添加数学函数支持
        for func_name in self.math_functions:
            if func_name in expression:
                expression = expression.replace(func_name, f'math.{func_name}')
        
        return expression
    
    def calculate_expression(self, expression):
        """计算数学表达式"""
        try:
            # 安全检查
            if not self.is_safe_expression(expression):
                return "错误：表达式包含不安全的内容！"
            
            # 预处理表达式
            processed_expr = self.preprocess_expression(expression)
            
            # 创建安全的命名空间
            safe_dict = {
                "__builtins__": {},
                "math": math,
                "pi": math.pi,
                "e": math.e
            }
            
            # 计算结果
            result = eval(processed_expr, safe_dict)   # 使用 eval 计算表达式 
            
            # 记录历史
            self.history.append(f"{expression} = {result}")
            
            return result
            
        except ZeroDivisionError:
            return "错误：除以零！"
        except ValueError as e:
            return f"错误：数学错误 - {e}"
        except SyntaxError:
            return "错误：表达式语法错误！"
        except Exception as e:
            return f"错误：{e}"
    
    def show_help(self):
        """显示帮助信息"""
        help_text = """
🔢 高级计算器帮助
==================

基本运算符:
  +  加法       -  减法
  *  乘法       /  除法
  ** 幂运算     %  取余
  () 括号

数学函数:
  sin(x), cos(x), tan(x)  - 三角函数
  sqrt(x)                 - 平方根
  log(x), log10(x)        - 对数函数
  exp(x)                  - 指数函数
  abs(x)                  - 绝对值
  round(x)                - 四舍五入

常数:
  pi - 圆周率 (3.14159...)
  e  - 自然常数 (2.71828...)

示例:
  2 + 3 * 4
  sqrt(16) + sin(pi/2)
  2**3 + log10(100)
  (5 + 3) * 2 - 1
==================
        """
        print(help_text)
    
    def run(self):
        """运行高级计算器"""
        print("🔢 高级计算器")
        print("输入 'help' 查看帮助")
        print("输入 'history' 查看历史")
        print("输入 'quit' 退出")
        print("=" * 30)
        
        while True:
            try:
                user_input = input("\n请输入表达式: ").strip()
                
                if user_input.lower() == 'quit':
                    print("再见！")
                    break
                elif user_input.lower() == 'help':
                    self.show_help()
                    continue
                elif user_input.lower() == 'history':
                    if self.history:
                        print("\n计算历史:")
                        for i, record in enumerate(self.history[-10:], 1):
                            print(f"{i}. {record}")
                    else:
                        print("暂无历史记录")
                    continue
                
                if user_input:
                    result = self.calculate_expression(user_input)
                    print(f"结果: {result}")
                    
            except KeyboardInterrupt:
                print("\n程序被中断，再见！")
                break

def main():
    """主函数"""
    calculator = AdvancedCalculator()
    calculator.run()

if __name__ == "__main__":
    main()
