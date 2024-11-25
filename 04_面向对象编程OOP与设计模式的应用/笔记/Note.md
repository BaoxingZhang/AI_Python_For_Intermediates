From: https://gamma.app/docs/OOP-m4y912u69aj3wk6?mode=doc

# 模块四_面向对象编程（OOP）与设计模式



## 学习目标

1. 借助大模型掌握 OOP
2. 继承
3. 设计模式与代码复用的提升
4. Llama-Index 的深入应用



## 一、借助大模型掌握 OOP

### 1.1 classmethod 与 staticmethod

使用 `classmethod` 创建**工厂方法**是一个常见的**设计模式**，特别是在需要根据不同的条件创建类的实例时。工厂方法可以让你在不直接调用类构造函数的情况下创建对象。

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(size="Medium", toppings=["Tomato", "Mozzarella", "Basil"])

    @classmethod
    def pepperoni(cls):
        return cls(size="Large", toppings=["Tomato", "Mozzarella", "Pepperoni"])

    @classmethod
    def custom(cls, size, toppings):
        return cls(size=size, toppings=toppings)

    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"

# 使用工厂方法创建不同类型的披萨
margherita_pizza = Pizza.margherita()
pepperoni_pizza = Pizza.pepperoni()
custom_pizza = Pizza.custom(size="Small", toppings=["Tomato", "Mozzarella", "Mushrooms"])

print(margherita_pizza)  # 输出: Pizza(size=Medium, toppings=['Tomato', 'Mozzarella', 'Basil'])
print(pepperoni_pizza)   # 输出: Pizza(size=Large, toppings=['Tomato', 'Mozzarella', 'Pepperoni'])
print(custom_pizza)      # 输出: Pizza(size=Small, toppings=['Tomato', 'Mozzarella', 'Mushrooms'])
```



不使用`classmethod`,直接调用类的构造函数

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"

# 直接调用构造函数创建不同类型的披萨
margherita_pizza = Pizza(size="Medium", toppings=["Tomato", "Mozzarella", "Basil"])
pepperoni_pizza = Pizza(size="Large", toppings=["Tomato", "Mozzarella", "Pepperoni"])
custom_pizza = Pizza(size="Small", toppings=["Tomato", "Mozzarella", "Mushrooms"])

print(margherita_pizza)  # 输出: Pizza(size=Medium, toppings=['Tomato', 'Mozzarella', 'Basil'])
print(pepperoni_pizza)   # 输出: Pizza(size=Large, toppings=['Tomato', 'Mozzarella', 'Pepperoni'])
print(custom_pizza)      # 输出: Pizza(size=Small, toppings=['Tomato', 'Mozzarella', 'Mushrooms'])
```



**问题**：

**1 重复代码**：

每次创建对象时，都需要重复提供相同的参数。例如，创建 `margherita_pizza` 和 `pepperoni_pizza` 时，必须手动指定 `size` 和 `toppings`。

**2 易出错**：

如果参数较多或初始化逻辑复杂，手动提供所有参数容易出错。例如，可能会忘记某个参数或提供错误的值。

**3 缺乏抽象**：

直接调用构造函数缺乏抽象，不能很好地表达创建对象的意图。例如，`Pizza(size="Medium", toppings=["Tomato", "Mozzarella", "Basil"])` 不如 `Pizza.margherita()` 直观。



#### 类方法与工厂方法

**1 类方法**：

`@classmethod` 装饰器用于定义类方法。类方法的第一个参数是 `cls`，表示类本身。

`margherita` 和 `pepperoni` 是两个类方法，它们分别创建特定类型的披萨对象。它们通过调用 `cls(size, toppings)` 来创建 `Pizza` 类的实例，而不直接调用构造函数 `__init__`。



**2 工厂方法**：

工厂方法是一种设计模式，用于创建对象，而不直接调用类的构造函数。在这个例子中，`margherita`、`pepperoni` 和 `custom` 都是工厂方法。

这些工厂方法根据不同的条件（如披萨的类型和配料）创建 `Pizza` 类的实例。



`staticmethod` 的作用是定义一个与类相关但不依赖于类或实例的状态的方法。它通常用于封装一些逻辑，这些逻辑在概念上属于类，但不需要访问类或实例的属性和方法。



#### staticmethod **主要特点**

1. **不依赖类或实例**：

2. - `staticmethod` 不需要访问类属性或实例属性，因此它不接受 `cls` 或 `self` 作为参数。

3. **逻辑上的归属**：

4. - 尽管 `staticmethod` 不依赖于类或实例，但它在逻辑上属于类。例如，某些实用函数或辅助方法可以用 `staticmethod` 实现。

5. **使用装饰器**：

6. - 使用 `@staticmethod` 装饰器来定义静态方法



### 1.2 私有属性与名称改写

- 实例属性 `__dict__` 是一个字典对象，它包含了实例的所有可变属性。
- 通过访问 `__dict__`，你可以查看和修改实例的属性。

![](../assets/20241125191615.png)


#### 问题：Python 的类属性和实例属性有什么区别？

#### 1. 定义位置与作用范围

**类属性**
- 定义在类中，属于类本身。
- 在所有实例之间共享，也就是说，类的所有实例都可以访问同一个类属性。
- 修改类属性会影响所有实例（除非某个实例显式覆盖它）。

**定义方式**
```python
class MyClass:
    class_attribute = "I am a class attribute"
```

**实例属性**

- 定义在类的实例中，属于某个具体的实例。
- 每个实例都有独立的实例属性，不会互相影响。
- 通常在 `__init__` 方法中定义，也可以动态添加到实例中。

```python
class MyClass:
    def __init__(self, value):
        self.instance_attribute = value
```

#### 2. 访问方式

类属性可以通过类名或实例访问：
```python
print(MyClass.class_attribute)  # 通过类名访问
obj = MyClass()
print(obj.class_attribute)  # 通过实例访问
```

实例属性只能通过实例访问：
```python
obj = MyClass("I am an instance attribute")
print(obj.instance_attribute)
```

#### 3. 存储位置

- 类属性存储在类的命名空间中（`MyClass.__dict__`）。
- 实例属性存储在实例的命名空间中（`obj.__dict__`）。

```python
print(MyClass.__dict__)  # 类的命名空间
print(obj.__dict__)      # 实例的命名空间
```

#### 4. 修改行为
**修改类属性**
- 通过类名修改会影响所有实例。
- 通过实例修改时，会创建一个新的实例属性，而不是修改原来的类属性。

```python
class MyClass:
    class_attribute = "I am a class attribute"

obj1 = MyClass()
obj2 = MyClass()

# 修改类属性
MyClass.class_attribute = "Modified class attribute"
print(obj1.class_attribute)  # 输出: Modified class attribute
print(obj2.class_attribute)  # 输出: Modified class attribute

# 通过实例修改
obj1.class_attribute = "Instance-specific attribute"
print(obj1.class_attribute)  # 输出: Instance-specific attribute (实例覆盖了类属性)
print(obj2.class_attribute)  # 输出: Modified class attribute

```

**修改实例属性**
- 修改实例属性只会影响当前实例，不影响其他实例或类属性。

```python
class MyClass:
    def __init__(self, value):
        self.instance_attribute = value

obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

obj1.instance_attribute = "Modified Object 1"
print(obj1.instance_attribute)  # 输出: Modified Object 1
print(obj2.instance_attribute)  # 输出: Object 2

```

#### 5. 使用场景

- 类属性适用于需要共享的属性，例如常量、默认值、计数器等。
- 实例属性适用于需要独立存储每个对象的数据。


### 1.3 猴子补丁

猴子补丁是一种在运行时动态修改模块、类或函数的方法，用于增强功能或修复缺陷。

例如，网络库 gevent 对部分 Python 标准库进行了猴子补丁，以实现一种轻量级并发模型，而无需依赖线程或 async/await。

```python
import time

class MyClass:
    def original_method(self):
        return "这是原始方法"

# 定义一个新的方法，用于替换原始方法
def patched_method(self):
    print("开始执行新方法")
    start_time = time.time()
    
    # 调用原始方法
    original_result = original_method_backup(self)
    
    end_time = time.time()
    print("新方法执行完毕")
    print(f"执行时间: {end_time - start_time} 秒")
    
    return original_result

# 备份原始方法
original_method_backup = MyClass.original_method

# 使用猴子补丁替换原始方法
MyClass.original_method = patched_method

# 创建实例并调用被补丁的方法
instance = MyClass()
print(instance.original_method())
```

* 猴子补丁应谨慎使用，因为它可能导致代码难以维护和调试。

### 1.4 接口与类型检查

1. 在 Python 中没有`interface`关键字。我们使用抽象基类（ABC）来定义接口，并在运行时显式检查类型（静态类型检查工具也支持）。
2. 抽象基类补充了鸭子类型，提供了一种定义接口的方式。

```python
from abc import ABC, abstractmethod
import csv
import json

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        """处理数据的抽象方法，子类必须实现"""
        pass

    def load_data(self, file_path):
        """加载数据的通用方法"""
        with open(file_path, 'r') as file:
            return file.read()

class CSVDataProcessor(DataProcessor):
    def process(self, data):
        """实现处理CSV数据的方法"""
        reader = csv.reader(data.splitlines())
        processed_data = [row for row in reader]
        return processed_data

class JSONDataProcessor(DataProcessor):
    def process(self, data):
        """实现处理JSON数据的方法"""
        return json.loads(data)

# 使用示例
csv_processor = CSVDataProcessor()
csv_data = csv_processor.load_data('data.csv')
processed_csv_data = csv_processor.process(csv_data)
print("Processed CSV Data:", processed_csv_data)

json_processor = JSONDataProcessor()
json_data = json_processor.load_data('data.json')
processed_json_data = json_processor.process(json_data)
print("Processed JSON Data:", processed_json_data)
```

1. 定义抽象基类：
    - `DataProcessor`继承自`ABC`，并定义了一个抽象方法`process`。所有子类必须实现这个方法。
    - `load_data`是一个通用方法，用于从文件中加载数据。
2. 实现具体子类：
    - `CSVDataProcessor`和`JSONDataProcessor`分别继承自`DataProcessor`，并实现了`process`方法。
    - `CSVDataProcessor`使用`csv`模块处理`CSV`数据。
    - `JSONDataProcessor`使用`json`模块处理`JSON`数据。
3. 使用具体子类：
    - 创建`CSVDataProcessor`和`JSONDataProcessor`的实例。
    - 使用`load_data`方法加载数据文件。
    - 使用`process`方法处理加载的数据。



### 1.5 静态协议与类型注解

- 类型注解：显式标明数据类型，提高代码可读性和静态分析能力，有助于大型项目的代码维护

```python
from abc import ABC, abstractmethod
import csv
import json
from typing import List, Any

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: str) -> Any:
        """处理数据的抽象方法，子类必须实现"""
        pass

    def load_data(self, file_path: str) -> str:
        """加载数据的通用方法"""
        with open(file_path, 'r') as file:
            return file.read()

class CSVDataProcessor(DataProcessor):
    def process(self, data: str) -> List[List[str]]:
        """实现处理CSV数据的方法"""
        reader = csv.reader(data.splitlines())
        processed_data = [row for row in reader]
        return processed_data

class JSONDataProcessor(DataProcessor):
    def process(self, data: str) -> Any:
        """实现处理JSON数据的方法"""
        return json.loads(data)
```






## 二、设计模式的应用

