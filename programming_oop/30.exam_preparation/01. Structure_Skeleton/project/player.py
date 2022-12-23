class Player:
    INITIAL_STAMINA = 100
    USED_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = INITIAL_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Name not valid!")

        if value in self.USED_NAMES:
            raise Exception(f"Name {value} is already used!")

        self.USED_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError(f"The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError(f"Stamina not valid!")

        self.__stamina = value

    @property
    def __need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.__need_sustenance}"

    @__need_sustenance.setter
    def __need_sustenance(self, value):
        self._need_sustenance = value