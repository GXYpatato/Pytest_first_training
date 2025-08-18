from jsonpath_ng import parse


class AssertUtil:


    @staticmethod
    def equals(check_value, expect_value):
        """相等"""
        assert check_value == expect_value, f'{check_value} == {expect_value}'

    @staticmethod
    def less_than(check_value, expect_value):
        """小于"""
        assert check_value < expect_value, f'{check_value} < {expect_value})'

    @staticmethod
    def less_than_or_equals(check_value, expect_value):
        """小于等于"""
        assert check_value <= expect_value, f'{check_value} <= {expect_value})'

    @staticmethod
    def greater_than(check_value, expect_value):
        """大于"""
        assert check_value > expect_value, f'{check_value} > {expect_value})'

    @staticmethod
    def greater_than_or_equals(check_value, expect_value):
        """大于等于"""
        assert check_value >= expect_value, f'{check_value} >= {expect_value})'

    @staticmethod
    def not_equals(check_value, expect_value):
        """不等于"""
        assert check_value != expect_value, f'{check_value} != {expect_value})'

    @staticmethod
    def contains(check_value, expect_value):
        """包含"""
        assert expect_value in check_value, f'{expect_value} in {check_value})'

    @staticmethod
    def startswith(check_value, expect_value):
        """以什么开头"""
        assert str(check_value).startswith(str(expect_value)), f'{str(check_value)} startswith {str(expect_value)})'

    @staticmethod
    def endswith(check_value, expect_value):
        """以什么结尾"""
        assert str(check_value).endswith(str(expect_value)), f'{str(check_value)} endswith {str(expect_value)})'

    @staticmethod
    def length(check_value, expect_value):
        """校验数量"""
        if not isinstance(check_value,list):
            check_value = [check_value]
            #extract_by_jsonpath有Bug,假如我们要断言订单数量，当订单数等于1时，获得的是订单的订单号，而不是订单数
            #且订单号是个int型，如：88856，没有length方法，所以套一层[]
        assert len(check_value) == expect_value, f'{str(check_value)} == {str(expect_value)})'


    def extract_by_jsonpath(self, extract_value: dict, extract_expression: str):
        """
        extract_value示例值是{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDM4NzEzODgsInVzZXJuYW1lIjoiMTU5NTk5OTYxNjMiLCJleHAiOjE3NTY4Njk5MDgsImVtYWlsIjoiMjgyNTM2ODE4QHFxLmNvbSJ9.X0rnEHrqjTtSXdjJ3KaiAenjvVdHawI-LpTmKfTFx20"}
        extract_expression示例值是$.token
        相当于用jsonpath语法去取extract_value的$.token
        返回的结果就是"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lk...."
        """

        """
        根据jsonpath获取值
        :param extract_value: res.json() 响应数据
        :param extract_expression: $.token  JSONPath表达式
        :return: 提取的值
        """
        # try:
        #     jsonpath_expr = parse(extract_expression)
        #     matches = jsonpath_expr.find(extract_value)
        #
        #     if not matches:
        #         return None
        #     elif len(matches) == 1:
        #         return matches[0].value
        #     else:
        #         return [match.value for match in matches]
        # except Exception as e:
        #     raise ValueError(f"JSONPath提取失败: {e}")

        if not isinstance(extract_expression, str):
            return extract_expression
        jsonpath_expr = parse(extract_expression)
        matches = jsonpath_expr.find(extract_value)
        if not matches:
            return null
        elif len(matches) == 1:
            return matches[0].value
        else:
            return [match.value for match in matches]
        #遇到的问题：返回的是对象而不是实际的值，错误写法：return matches[0]，正确写法：return matches[0].value
        #遇到的问题：返回的是对象而不是实际的值，错误写法：return matches，正确写法：[match.value for match in matches]

    def validate_response(self, response, validate_check):
        """校验结果"""
        for check in validate_check:
            for check_type, check_value in check.items():
                # 实际结果
                actual_value = self.extract_by_jsonpath(response, check_value[0]) #check_value[0]实际上指的是$.token
                # 预期结果
                expect_value = check_value[1] #check_value[0]实际上指的是"eyJ0eX"

                if check_type in ["eq", "equals", "equal"]:
                    self.equals(actual_value, expect_value)
                elif check_type in ["lt", "less_than"]:
                    self.less_than(actual_value, expect_value)
                elif check_type in ["le", "less_or_equals"]:
                    self.less_than_or_equals(actual_value, expect_value)
                elif check_type in ["gt", "greater_than"]:
                    self.greater_than(actual_value, expect_value)
                elif check_type in ["ne", "not_equal"]:
                    self.not_equals(actual_value, expect_value)
                elif check_type in ["contains"]:
                    self.contains(actual_value, expect_value)
                elif check_type in ["startswith"]:
                    self.startswith(actual_value, expect_value)
                elif check_type in ["endswith"]:
                    self.endswith(actual_value, expect_value)
                elif check_type in ["length"]:
                    self.length(actual_value, expect_value)
                else:
                    print(f'{check_type}  not valid check type')
