from pytest_training.utils.YamlUtil import YamlUtil
from pytest_training.utils.assert_util import AssertUtil
from pytest_training.utils.log_util import logger


class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtil()

    def extract_data(self, res, extract):
        """
        根据extract表达式，获取接口内容并存入yaml
        :param res:res.json()
        :param extract:eg $.token
        :return:
        """
        if extract:
            for key, expression in extract.items():
                try:
                    value = self.jsonpath_util.extract_by_jsonpath(res, expression)
                    # 写入yaml
                    self.yaml_util.write_extract_yaml({key: value})
                except Exception as e:
                    logger.error(f"变量{key}写入extract.yaml失败，请检查，error={e}")

    def get_extract_data(self, key):
        """从extract.yaml中获取内容"""
        try:
            data = self.yaml_util.read_extract_yaml()
            return data[key]
        except Exception as e:
            logger.error(f"从yaml中根据key获取不到内容，error={e}")

    def extract_url(self, url):
        # /orders/${get_extract_data(order_id)}/
        if '{' and '}' in url:
            return self.process_data(url)
        return url

    def process_data(self, data):
        # /orders/${get_extract_data(order_id)}/中把get_extract_data()和order_id
        if '${' and '}' in data:
            start_index = data.index('$')
            end_index1 = data.index('}')
            end_index2 = data.index('(')
            # 获取函数中的方法:get_extract_data(order_id)
            func_full_name = data[start_index:end_index1 + 1]
            # 获取函数名
            func_name = data[start_index + 2:end_index2]
            #
            func_params = data[end_index2 + 1:end_index1 - 1]
            # *func_params.split(',')不支持函数为int型
            # extract_data = getattr(self,func_name)(*func_params.split(','))

            # 先进行getattr
            extract_data = getattr(self, func_name, None)
            # 改进参数处理：只有当func_params有内容时才split
            if func_params and func_params.strip():
                func_params_list = func_params.split(',')
                # 尝试转换数字
                func_params_list = [int(param) if param.strip().isdigit() else param.strip() for param in
                                    func_params_list]
                extract_data = extract_data(*func_params_list)
            else:
                # 无参数情况
                extract_data = extract_data()
            data = data.replace(func_full_name,str(extract_data))  # 把${get_extract_data(order_id)}替换成实际的函数get_extract_data(oder_id)的执行结果，得到理想的url
            return data
        return data

    def test_add(self):
        return "1111"


if __name__ == '__main__':
    # print(getattr(ExtractUtil(), "get_extract_value")("2222"))
    # print(f"extract_value={ExtractUtil().get_extract_data('order_id')}")
    print(f"a+b={ExtractUtil().process_data('${test_add()}')}")
