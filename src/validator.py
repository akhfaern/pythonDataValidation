import re


class Validator:
    def __init__(self) -> None:
        self.NAME_REGEX = "^[a-zA-Z0-9ğüşöçıİĞÜŞÖÇI_-]{0,256}$"
        self.FILE_NAME_REGEX = "^[^\\\\\\/:\\*\\!?`'&$;\"<>\\|]+$"
        self.PASSWORD_REGEX = "^.*$"
        self.NUMBER_REGEX = "^[-+]?[0-9]+$"
        self.REQUEST_RESPONSE_REGEX = "^(request|response)$"
        self.FULL_NAME_REGEX = "^([a-zA-Z0-9ğüşöçİĞÜŞÖÇ ]{1,30}|[a-zA-Z0-9ğüşöçİĞÜŞÖÇ]+\\s{1,30}[a-zA-Z0-9ğüşöçİĞÜŞÖÇ]{1,30}|[a-zA-Z0-9ğüşöçİĞÜŞÖÇ]+\\s{1}[a-zA-Z0-9ğüşöçİĞÜŞÖÇ]{3,30}\\s{1}[a-zA-Z0-9ğüşöçİĞÜŞÖÇ]{1,30})$"
        self.EMAIL_REGEX = "^[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

        self.PORT_REGEX = "^()([0-9]|[1-5]?[0-9]{2,4}|6[1-4][0-9]{3}|65[1-4][0-9]{2}|655[1-2][0-9]|6553[1-5])$"
        self.IP_REGEX = "^(?:(?:^|\\.)(?:2(?:5[0-5]|[0-4]\\d)|1?\\d?\\d)){4}$"
        self.IP_PORT_REGEX = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"
        self.URL_REGEX = "^(http:\\/\\/www\\.|https:\\/\\/www\\.|http:\\/\\/|https:\\/\\/)?[a-z0-9]+([\\-\\.]{1}[a-z0-9]+)*\\.[a-z]{2,5}(:[0-9]{1,5})?(\\/.*)?$"

        self.DATE_TIME_REGEX = "^(?=\\d)(?:(?:31(?!.(?:0?[2469]|11))|(?:30|29)(?!.0?2)|29(?=.0?2.(?:(?:(?:1[6-9]|[2-9]\\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(?:\\x20|$))|(?:2[0-8]|1\\d|0?[1-9]))([-./])(?:1[012]|0?[1-9])\\1(?:1[6-9]|[2-9]\\d)?\\d\\d(?:(?=\\x20\\d)\\x20|$))?(((0?[1-9]|1[012])(:[0-5]\\d){0,2}(\\x20[AP]M))|([01]\\d|2[0-3])(:[0-5]\\d){1,2})?$"
        self.NO_SPECIAL_CHAR_REGEX = "^[a-zA-Z0-9_()-]{1,48}$"

        self.DOMAIN_REGEX = "^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\\.)+[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]$"
        self.HTTP_HTTPS_REGEX = "^(http|https)://"

    def validate(self, test_string: str, pattern: str) -> bool:
        p = re.compile(self.__dict__.get(pattern), re.IGNORECASE)
        matched = p.match(test_string)
        return bool(matched)

    def validate_list(self, testing: list) -> bool:
        for k, v in testing:
            if isinstance(k, str) and k.strip() != '':
                t = self.validate(k, v)
                if not t:
                    return False
            elif isinstance(k, list):
                for b in k:
                    t = self.validate(b, v)
                    if not t:
                        return False
        return True
