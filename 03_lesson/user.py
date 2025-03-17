class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.last = last_name

    def get_name(self):
        return self.name

    def get_last(self):
        return self.last

    def get_user_info(self):
        return f"Name: {self.name}, Last: {self.last}"
