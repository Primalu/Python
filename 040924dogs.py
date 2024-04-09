"""
    Creating and using a Dog SuperClass 🐕
    and a herding dog sub class 🐏🐏🐏

    and instantiating (making objects)
"""


class Dog:
    # dog is a Super class of the Herding_Dog class
    def __init__(self, color, coat, size, name):
        self.color = color
        self.coat = coat
        self.size = size
        self.name = name

    def bark(self):
        print("Woof!")

    def happy(self):
        print("Wag wag")

    def __str__(self):
        return f"Dog: Color: {self.color}, Coat: {self.coat}, Size: {self.size}, Name: {self.name}"


class HerdingDog(Dog):
    def __init__(self, color, coat, size, name, favorite_toy):
        super().__init__(color, coat, size, name)
        self.favorite_toy = favorite_toy

    def __str__(self):
        return super().__str__() + " " + self.favorite_toy + ", with herding skills"

    def herding(self):
        print("Run, I'm going to chase you.")


def main():

    print("\n\n")
    ollie = Dog("Fawn", "Short", "Large", "Ollie")
    print("Ollie: ")
    ollie.bark()
    ollie.happy()
    print(ollie)

    print("\n\n")
    print("Nessie:")
    nessie = HerdingDog("Black", "Short", "Large",
                        "Nessie", "Minty World Ball")
    nessie.herding()
    print(nessie)
    print("\n\n")


main()
