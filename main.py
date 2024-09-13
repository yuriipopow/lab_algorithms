from models.home import Home


def main():
    home: Home = Home()
    print(home)
    home.sort_by_age()
    print(f"\n{home}\n")
    print(f"\n{home.pets[0].is_polite()}\n")
    print(f"\n{[str(pet) for pet in home.pets[0].are_friends(home.pets[1], home.pets[2], home.pets[3])]}\n")


if __name__ == "__main__":
    main()