from models.home import Home


def main():
    home: Home = Home()
    print(home)
    home.sort_by_age()
    print(f"\n{home}\n")
    print(f"\n{home.pets[0].is_polite()}\n")
    tuple_of_pets_for_friendship: tuple = (home.pets[1], home.pets[2], home.pets[3])
    friends = home.pets[0].are_friends(*tuple_of_pets_for_friendship)
    for pet in friends:
        print(f"this is friend {pet.name}")


if __name__ == "__main__":
    main()