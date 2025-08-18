from pytest_excise.core.rest_clinet import RestClient
from pytest_excise.utils.read_data import base_data


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self,url,**kwargs):
        return self.get(base_data.read_data()['Meike_url']['base_url']+url,params=kwargs)


    def get_code(self,**kwargs):
        return self.post("/code/",**kwargs)

    def register_mobile(self,**kwargs):
        return self.post("/users/",**kwargs)

api_util = Api()

