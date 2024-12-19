class Person:
    def __init__(self, name: str):
        """
        Ініціалізувати екземпляр Людини.
        
        :param name: Ім'я господаря.
        """
        self.name = name

    def feed_cat(self, cat):
        """
        Нагодувати кота.
        
        :param cat: Об'єкт кота.
        """
        print(f"{self.name} нагодував кота {cat.name}.")
        cat.react_to_feeding()

class Cat:
    def __init__(self, name: str):
        """
        Ініціалізувати екземпляр Кота.
        
        :param name: Ім'я кота.
        """
        self.name = name

    def react_to_feeding(self):
        """
        Реакція кота на годування.
        """
        print(f"Кіт {self.name} муркоче від радощів.")

def main():
    # Створення об'єктів Людини і Кота
    owner = Person("Матвій")
    cat = Cat("Пума")

    # Людина годує кота
    owner.feed_cat(cat)

if __name__ == "__main__":
    main()
