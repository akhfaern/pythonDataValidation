from testBaseClass import TestBaseClass

data = {
    'id': 1,
    'ipAddress': '192.168.1.1',
    'option': {
        'name': 'murat',
        'key': 'yalin'
    },
    'option_list': [
        {'id': 1, 'http': 'request'},
        {'id': 2, 'http': ''}
    ],
    'list2': ['murat']
}

testClass = TestBaseClass(data)

print(testClass.is_validated())
print(testClass.get_validation_errors())
print(testClass.get_data())
