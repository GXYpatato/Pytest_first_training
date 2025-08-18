import yaml
import os


class YamlUtil:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data/")

    def read_extract_yaml(self):
        with open(self.data_path + "extract.yaml", "r", encoding='utf-8') as f:
            value = yaml.safe_load(f)
            return value

    def read_test_testcase_yaml(self, yaml_name, key_name=None):
        with open(self.data_path + yaml_name, "r", encoding='utf-8') as f:
            value = yaml.safe_load(f)
            if key_name:
                value = value[key_name]
            return value

    def extract_case(self, yaml_name, key_name):
        # 对yaml里的数据进行组装，格式：request_info+case_info
        case_value = self.read_test_testcase_yaml(yaml_name, key_name)[0]
        new_case = []
        for value in case_value["case_info"]:
            new_case.append({"request_info": case_value["request_info"], "case_info": value})
        return new_case


    def write_extract_yaml(self, data1):
        """
        智能写入YAML文件，支持：
        1. 文件为空时直接写入
        2. 文件不为空时合并数据（更新重复key，追加新key）
        :param data1: 要写入的数据字典
        """
        filepath = os.path.join(self.data_path, "extract.yaml")

        # 读取现有的YAML内容
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                existing_data = yaml.safe_load(f)
                # 如果文件存在但内容为空或格式错误
                if existing_data is None:
                    existing_data = {}
        except (FileNotFoundError, yaml.YAMLError):
            existing_data = {}  # 文件不存在或格式错误时当作空数据处理

        # 合并数据：新数据覆盖旧数据
        merged_data = {**existing_data, **data1}

        # 一次性写入合并后的数据
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.safe_dump(merged_data, f, allow_unicode=True, sort_keys=False)

    def clear_extract(self):
        #清理extract.yaml
        with open(self.data_path + "extract.yaml", "a", encoding='utf-8') as f:
            f.truncate()

if __name__ == '__main__':
    data = YamlUtil().extract_case("user_center.yaml", "user_login_new")
    print(data)
