from src.baseDataClass import BaseDataClass


class TestBaseClass(BaseDataClass):
    id: int = 0  # int
    enabled: bool = True, "REQUIRED"  # bool
    option_if_enabled: str = "NAME_REGEX", "REQUIREDIF_enabled_is_TRUE"
    httpmethod: str = "REQUEST_RESPONSE_REGEX"
    httpmethod_conditioned_option: str = "NAME_REGEX", "REQUIREDIF_httpmethod_in_request,response"
    ipAddress: str = "IP_REGEX", "REQUIRED"  # str
    ipAddressPort: str = "IP_PORT_REGEX", "REQUIRED"  # str
    port: int = "NUMBERBETWEEN_1_65535", "REQUIRED"  # int
    option: dict = {'name': 'NAME_REGEX', 'key': 'FULL_NAME_REGEX'}  # dict
    optionlistchecked: bool = True, "REQUIRED"
    option_list: list = [{'id': 'NUMBER_REGEX', 'http': (
        'REQUEST_RESPONSE_REGEX', 'REQUIRED')}], "REQUIREDIF_option-list-checked_is_true"  # dict list
    list2: list = [['str', 'NAME_REGEX']]  # string list
