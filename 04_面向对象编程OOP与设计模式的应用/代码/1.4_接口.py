from abc import ABC, abstractmethod
import csv
import json
import os

# 获取脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        """处理数据的抽象方法，子类必须实现"""
        pass

    def load_data(self, file_path):
        """加载数据的通用方法"""
        with open(file_path, 'r', encoding='utf-8') as file:
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

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Debug print statements
print(f"Script location: {current_dir}")
print(f"Looking for CSV file at: {os.path.join(current_dir, 'data.csv')}")


# 使用示例
csv_processor = CSVDataProcessor()
csv_data = csv_processor.load_data(os.path.join(script_dir, 'data.csv'))
processed_csv_data = csv_processor.process(csv_data)
print("Processed CSV Data:", processed_csv_data)

json_processor = JSONDataProcessor()
json_data = json_processor.load_data(os.path.join(script_dir, 'data.json'))
processed_json_data = json_processor.process(json_data)
print("Processed JSON Data:", processed_json_data)