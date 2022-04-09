from src.validator import Validator
from typing import Union


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

    def __add_validation_error(self, v: str, error_value: str, v_key: str = None):
        if v_key is not None:
            if v not in self.__validation_errors:
                self.__validation_errors[v] = {}
            self.__validation_errors[v][v_key] = error_value
        else:
            self.__validation_errors[v] = error_value

    def __check_is_required(self, validation_rule: Union[str, tuple]):
        if type(validation_rule) is tuple:
            is_required = validation_rule[1]
            validation_rule = validation_rule[0]
            return validation_rule, is_required
        else:
            return validation_rule, "NOTREQUIRED"

    def __validate_dict(self, v: str, value: dict, validation_rules: dict) -> bool:
        if len(value) != len(validation_rules):
            self.__validation_errors[v] = 'length error'
            return False
        for key in validation_rules:
            v_value = value.get(key, None)
            if v_value is None:
                self.__add_validation_error(v, "Value required", key)
            self.__validate_str(
                v, str(v_value), validation_rule=validation_rules[key], v_key=key)
        return True

    def __validate_str(self, v: str, value: str, validation_rule: Union[str, tuple], v_key: str = None) -> bool:
        validation_rule, is_required = self.__check_is_required(
            validation_rule=validation_rule)
        if is_required == "REQUIRED" and str(value).strip() == "":
            self.__add_validation_error(v, "Value required", v_key)
            return False
        if str(value).strip() != "" and not self.__validator.validate(str(value), validation_rule):
            self.__add_validation_error(v, value, v_key)
            return False
        return True

    def __validate_int(self, v: str, value: int) -> bool:
        if type(value) is not int:
            self.__validation_errors[v] = value
            return False
        return True

    def __validate_bool(self, v: str, value: bool) -> bool:
        if type(value) is not bool:
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
                elif annotation is bool:
                    self.__validate_bool(v=v, value=value)
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
