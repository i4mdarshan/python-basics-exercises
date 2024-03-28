population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def print_population():
    for key,value in population.items():
        print(f"{key} => {value}")

def search(country):
    if country in population:
        print(f"{country} => {population[country]}")
    else:
        print("No records available")
    return

def add(country, population_num):
    if country in population:
        print("Country already exists in dict")
        return
    p = float(population_num)
    population[country] = p 
    print_population()
    return

def remove(country):
    if country in population:
        del population[country]
        print_population()
    else:
        print("No records available")
    return

def main():
    print("Select the action to be performed from below")
    print("1. Print the population dict")
    print("2. Add entry in the population dict")
    print("3. Remove entry using country from population dict")
    print("4. Query country and print population")
    userip = input()

    if userip == "1":
        print_population()
        return
    elif userip == "2":
        countryip = input("Enter country name: ")
        country = countryip.lower()
        popip = input("Enter population: ")
        add(country,popip) 
        return
    elif userip == "3":
        countryip = input("Enter country name: ")
        country = countryip.lower()
        remove(country)
        return
    elif userip == "4":
        countryip = input("Enter country name: ")
        country = countryip.lower()
        search(country)
        return
    else:
        print("Entered choice is invalid")

if __name__ == '__main__':
    main()