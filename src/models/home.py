from models.pet import Pet
from models.kind import Kind

class Home:
    def __init__(self):
        self.pets: list[Pet] = [
            Pet("Buddy", Kind.DOG, "Golden Retriever", 2, "Hello, I'm Buddy!", 30.0),
            Pet("Lucy", Kind.CAT, "Siamese", 1, "Hello, I'm Lucy!", 10.0),
            Pet("Bella", Kind.BIRD, "Parrot", 3, "Hello, I'm Bella!", 0.5),
            Pet("Nemo", Kind.FISH, "Clownfish", 1, "Hello, I'm Nemo!", 0.1)
        ]


    def adopt(self, pet: Pet) -> None:
        self.pets.append(pet)


    def __str__(self) -> str:
        return "\n".join([str(pet) for pet in self.pets])



    def sort_by_age(self) -> None:
        for n in range(len(self.pets) - 1, 0, -1):
            for i in range(n):
                if self.pets[i].age > self.pets[i + 1].age:
                    self.pets[i].age, self.pets[i + 1].age = self.pets[i + 1].age, self.pets[i].age
