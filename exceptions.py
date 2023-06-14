class WrongDataFormatException(Exception):
    def __init__(self, code, data=None):
        self.data = data
        self.code = code
        self.types = {1: "10 чисел в формате 1234567890 или 11 в формате 81234567890",
                      2: "f или m",
                      3: "валидная дата в формате ДД.ММ.ГГГГ",
                      4: "Не опознан номер телефона. Необходимый формат: "
                         "10 чисел в формате 1234567890 или 11 в формате 81234567890"}

    def __str__(self):
        if self.data:
            return f"Код ошибки: 2\n" \
                   f"Неверный формат данных.\n" \
                   f"Требуется {self.types[self.code]}, введено {self.data}\n"
        return f"{self.types[self.code]}"


class WrongLenException(Exception):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"Код ошибки: 1\n" \
               f"Неверное количество данных.\n" \
               f"Требуется 6, введено {self.length}\n"


class ReadOnlyException(Exception):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"Код ошибки: 3\n" \
               f"Запись не удалась.\n" \
               f"Файл защищён от записи.\n"
