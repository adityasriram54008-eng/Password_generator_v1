import random as rd

def get_ll(l):
    with open("Lletters.txt", "r") as file:
        mems = file.readlines()
        mems = rd.choice(mems)
        write_(mems)

def get_ul(l):
    with open("Uletters.txt", "r") as file:
        mems = file.readlines()
        mems = rd.choice(mems)
        write_(mems)

def get_n(l):
    with open("numbers.txt", "r") as file:
        mems = file.readlines()
        mems = rd.choice(mems)
        write_(mems)

def get_ss(l):
    with open("special_characters.txt", "r") as file:
        mems = file.readlines()
        mems = rd.choice(mems)
        write_(mems)

def write_(args):
    with open("password.txt", "a") as file:
        file.writelines(args)

def display():
    with open("password.txt", "r") as file:
        r = file.readline()
    return r