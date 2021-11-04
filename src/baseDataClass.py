from src.validator import Validator


class BaseDataClass:
    def __init__(self, data: dict) -> None:
        self.__data = data
        self.__validator = Validator()
        self.__validation_errors = {}

    def get_data(self) -> dict:
        class_vars = self.__class__.__dict__
        r_dict = {}
        for v in class_vars:
            if v[0:2] != "__":
                r_dict[v] = self.__data.get(v)
        return r_dict

    def __validate_dict(self, v: str, value: dict, validation_rules: dict) -> bool:
        if len(value) != len(validation_rules):
            self.__validation_errors[v] = 'length error'
            return False
        for key in validation_rules:
            v_value = value.get(key, None)
            if v_value == None:
                if v not in self.__validation_errors:
                    self.__validation_errors[v] = {}
                self.__validation_errors[v][key] = v_value
                return False
            if str(v_value).strip() != "" and not self.__validator.validate(str(v_value), validation_rules[key]):
                if v not in self.__validation_errors:
                    self.__validation_errors[v] = {}
                self.__validation_errors[v][key] = value
        return True

    def __validate_str(self, v: str, value: str, validation_rule: str) -> bool:
        if str(value).strip() != "" and not self.__validator.validate(str(value), validation_rule):
            self.__validation_errors[v] = value
            return False
        return True

    def __validate_int(self, v: str, value: int) -> bool:
        if not type(value) is int:
            self.__validation_errors[v] = value
            return False
        return True

    def __validate_data(self) -> None:
        self.__validation_errors = {}
        class_vars = self.__class__.__dict__
        annotations = class_vars.get('__annotations__', None)
        for v in class_vars:
            if v[0:2] != "__":
                value = self.__data.get(v)
                validation = class_vars[v]
                annotation = annotations[v]
                if not isinstance(value, annotation):
                    self.__validation_errors[v] = value
                elif annotation is str:
                    self.__validate_str(
                        v=v, value=value, validation_rule=validation)
                elif annotation is int:
                    self.__validate_int(v=v, value=value)
                elif annotation is dict:
                    self.__validate_dict(
                        v=v, value=value, validation_rules=validation)
                elif annotation is list:
                    if isinstance(validation[0], dict):
                        for list_val in value:
                            self.__validate_dict(
                                v=v, value=list_val, validation_rules=validation[0])
                    elif isinstance(validation[0], list):
                        val_type = validation[0][0]
                        validation_rule = validation[0][1]
                        for list_val in value:
                            if val_type == 'str':
                                self.__validate_str(
                                    v=v, value=list_val, validation_rule=validation_rule)
                            if val_type == 'int':
                                self.__validate_int(v=v, value=list_val)
                    else:
                        if v not in self.__validation_errors:
                            self.__validation_errors[v] = {}
                        self.__validation_errors[v][validation[0]
                                                    ] = 'unknown type'

    def is_validated(self) -> bool:
        self.__validate_data()
        return len(self.__validation_errors) == 0

    def get_validation_errors(self) -> dict:
        return self.__validation_errors