import random as rd

def get_ll(gen):
    with open("Lletters.txt", "r") as file:
        letters = file.readlines()
        letters = rd.choice(letters)
        write_(letters.strip())
        gen+=1
        return gen

def get_ul(gen):
    with open("Uletters.txt", "r") as file:
        letters = file.readlines()
        letters = rd.choice(letters)
        write_(letters.strip())
        gen += 1
        return gen

def get_n(gen):
    with open("numbers.txt", "r") as file:
        letters = file.readlines()
        letters = rd.choice(letters)
        write_(letters.strip())
        gen += 1
        return gen

def get_ss(gen):
    with open("special_characters.txt", "r") as file:
        letters = file.readlines()
        letters = rd.choice(letters)
        write_(letters.strip())
        gen += 1
        return gen

def randomizer(selected,gen):
    selected = rd.choice(selected)
    if selected == "uc":
        gen = get_ul(gen)
        return gen
    if selected == "lc":
        gen = get_ll(gen)
        return gen
    if selected == "n":
        gen = get_n(gen)
        return gen
    if selected == "sc":
        gen = get_ss(gen)
        return gen

def write_(args):
    with open("password.txt", "a") as file:
        file.writelines(args)

def display():
    with open("password.txt", "r") as file:
        content = file.readline()
    return content