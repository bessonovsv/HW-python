class Mailing:
    def __init__(self, to_address, from_address, cost, track):

        self.Address = to_address
        self.Address_1 = from_address
        self.Num = cost
        self.Str = track

    def __str__(self):

        return f"Отправление {self.Str} из {self.Address_1} в {self.Address}.\
 Стоимость {self.Num} рублей."
