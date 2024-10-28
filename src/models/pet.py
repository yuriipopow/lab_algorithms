from  models.kind import Kind


class Pet:
    def __init__(self, name: str, kind: Kind, breed: str, age: int, greeting: str, mass: float):
        self.name:str = name
        self.breed: str = breed
        self.kind: Kind = kind
        self.age:int = age
        self.greeting: str = greeting
        self.mass:float = mass


    def are_friends(self, *other_pets) -> list:
        friends: list[Pet] = []
        for pet in other_pets:
            if type(pet) is Pet and abs(self.age - pet.age) <= 2:
                friends.append(pet)
            else:
                continue

        return friends


    def is_polite(self) -> bool:
        return  "hello" in self.greeting.lower()


    def __str__(self):
        return f"{self.name} is a {self.kind} ({self.breed}) and is {self.age} years old. {self.greeting}"
