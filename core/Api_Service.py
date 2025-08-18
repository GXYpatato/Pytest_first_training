from pytest_training.core.rest_clinet_new import RestClient
from pytest_training.utils.assert_util import AssertUtil
import allure

from pytest_training.utils.extract_util import ExtractUtil


class ApiService:
    def __init__(self):
        self.session = RestClient()
        self.extract = ExtractUtil()

    def handle_case(self, test_data, login_token=None):
        # 获取url
        url = self.extract.extract_url(test_data['request_info']['url'])
        # 获取method
        method = test_data['request_info']['method']
        # 获取header
        headers = test_data['request_info']['headers']
        if login_token:
            headers.update(login_token)  # header中加入token

        # 获取title
        allure_title = test_data['request_info']['case_title']
        # 给allure
        allure.dynamic.title(allure_title)

        # 获取case_info
        case_info = test_data['case_info']
        # 获取validate
        validate = case_info.pop("validate", None)
        # 获取extract
        extract1 = case_info.pop("extract", None)
        res1 = self.session.do_request(url=url, method=method, headers=headers, **case_info)
        # 将extract写入yaml
        self.extract.extract_data(res1, extract1)
        # 断言逻辑
        AssertUtil().validate_response(res1, validate)
        return res1
