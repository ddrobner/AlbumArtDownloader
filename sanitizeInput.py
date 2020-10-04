class sanitizer():
    def __init__(self):
        pass

    def sanitize(self, text):
        sanitized = text
        badstrings = [
            ';',
            '$',
            '&&',
            '../',
            '<',
            '>',
            '%3C',
            '%3E',
            '\'',
            '--',
            '1,2',
            '\x00',
            '`',
            '(',
            ')',
            'file://',
            'input://'
            '"'
        ]
        for badstr in badstrings:
            if badstr in sanitized:
                sanitized = sanitized.replace(badstr, '')
        return sanitized
