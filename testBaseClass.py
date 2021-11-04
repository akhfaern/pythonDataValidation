from src.baseDataClass import BaseDataClass


class TestBaseClass(BaseDataClass):
    id: int = 0  # int
    ipAddress: str = "IP_REGEX"  # str
    option: dict = {'name': 'NAME_REGEX', 'key': 'FULL_NAME_REGEX'}  # dict
    option_list: list = [
        {'id': 'NUMBER_REGEX', 'http': 'REQUEST_RESPONSE_REGEX'}]  # dict list
    list2: list = [['str', 'NAME_REGEX']]  # string list
