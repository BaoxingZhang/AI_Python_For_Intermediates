PPT: [ https://gamma.app/docs/OOP-m4y912u69aj3wk6](https://gamma.app/docs/OOP-m4y912u69aj3wk6)

#### 练习题 1：使用 classmethod 创建工厂方法

题目： 设计一个日志记录系统，包含一个 Logger 类。该类应包含一个类方法 get_logger，用于根据不同的日志级别（如 INFO、DEBUG、ERROR）创建不同的日志记录器实例。每个日志记录器实例应具有一个 log 方法，用于记录日志消息。

要求：

1. 实现 Logger 类及其子类 InfoLogger、DebugLogger 和 ErrorLogger。
2. 实现 get_logger 类方法，根据传入的日志级别返回相应的日志记录器实例。
3. 每个日志记录器实例应实现 log 方法，输出格式为 [LEVEL] message。

示例：

复制代码

```python
logger = Logger.get_logger("INFO")
logger.log("This is an info message")  # 输出: [INFO] This is an info message
```

#### 练习题 2：猴子补丁

题目： 假设你正在使用一个第三方库，该库的某个类 ExternalClass 有一个方法 calculate，但该方法存在一个已知的错误。你需要在不修改第三方库源码的情况下修复这个错误。

要求：

1. 创建一个猴子补丁，修复 ExternalClass.calculate 方法的错误。
2. 确保猴子补丁在应用启动时自动生效。
3. 编写测试代码，验证猴子补丁是否正确修复了错误。

示例：

复制代码

```python
# 原始方法
# class ExternalClass:
#     def calculate(self, x, y):
#         return x + y  # 错误：应为 x * y
 
# 猴子补丁
def patched_calculate(self, x, y):
    return x * y
 
ExternalClass.calculate = patched_calculate
 
# 测试代码
instance = ExternalClass()
assert instance.calculate(2, 3) == 6
```

#### 练习题 3：接口与类型检查

题目： 设计一个支付系统，包含一个支付接口 PaymentProcessor，定义一个 process_payment 方法。然后实现两个具体的支付处理器 CreditCardProcessor 和 PayPalProcessor，分别处理信用卡支付和 PayPal 支付。

要求：

1. 使用抽象基类（ABC）定义 PaymentProcessor 接口。
2. 实现 CreditCardProcessor 和 PayPalProcessor 类，分别继承 PaymentProcessor 并实现 process_payment 方法。
3. 编写一个函数 process_all_payments，接受一个支付处理器列表，并调用每个处理器的 process_payment 方法。

示例：

复制代码

```python
from abc import ABC, abstractmethod
from typing import List
 
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass
 
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of {amount}")
 
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of {amount}")
 
def process_all_payments(processors: List[PaymentProcessor], amount: float) -> None:
    for processor in processors:
        processor.process_payment(amount)
 
# 测试代码
processors = [CreditCardProcessor(), PayPalProcessor()]
process_all_payments(processors, 100.0)
```

#### 练习题 4：静态协议与类型注解

题目： 设计一个数据转换系统，包含一个数据转换器接口 DataTransformer，定义一个 transform 方法。然后实现两个具体的数据转换器 CSVTransformer 和 JSONTransformer，分别处理 CSV 和 JSON 数据的转换。

要求：

1. 使用 Protocol 定义 DataTransformer 接口，并使用类型注解。
2. 实现 CSVTransformer 和 JSONTransformer 类，分别实现 transform 方法。
3. 编写一个函数 apply_transformation，接受一个数据转换器实例和数据，并调用转换器的 transform 方法。

示例：

复制代码

```python
from typing import Protocol, List, Dict, Any
 
class DataTransformer(Protocol):
    def transform(self, data: str) -> Any:
        pass
 
class CSVTransformer:
    def transform(self, data: str) -> List[List[str]]:
        import csv
        reader = csv.reader(data.splitlines())
        return [row for row in reader]
 
class JSONTransformer:
    def transform(self, data: str) -> Dict[str, Any]:
        import json
        return json.loads(data)
 
def apply_transformation(transformer: DataTransformer, data: str) -> Any:
    return transformer.transform(data)
 
# 测试代码
csv_data = "name,age\nAlice,30\nBob,25"
json_data = '{"name": "Alice", "age": 30}'
 
csv_transformer = CSVTransformer()
json_transformer = JSONTransformer()
 
print(apply_transformation(csv_transformer, csv_data))
print(apply_transformation(json_transformer, json_data))
```