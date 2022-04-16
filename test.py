from testBaseClass import TestBaseClass

data = {
    'id': 1,
    'ipAddress': '192.168.1.1',
    'ipAddressPort': '192.168.1.1:80',
    'enabled': False,
    'option_if_enabled': '',
    'httpmethod': 'request',
    'httpmethod_conditioned_option': 'condition',
    'port': 65535,
    'option': {
        'name': 'murat',
        'key': 'yalin'
    },
    'option_list_checked': True,
    'option_list': [
        {'id': 1, 'http': 'request'},
        {'id': 2, 'http': 'response'}
    ],
    'list2': ['murat']
}

testClass = TestBaseClass(data)

print(testClass.is_validated())
print(testClass.get_validation_errors())
print(testClass.get_data())
