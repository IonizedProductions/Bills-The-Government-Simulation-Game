import os
from os import system, name
from time import sleep
def hel():
    clear()
    print("Welcome to the help screen for Bills!")
    print("Please select one of the subjects!")
    print("1 - Start year")
    print("2 - How laws work")
    print("3 - How Money works")
    print("4 - Exit")
    ex = input(">")
    if ex == "1":
        print("WIP")
        sleep(10)
        hel()
    if ex == "2":
        print("WIP")
        sleep(10)
        hel()
    if ex == "3":
        print("WIP")
        sleep(10)
        hel()
    if ex == "4":
        clear()
        menu()
    if ex == "change":
        clear()
        changelog()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class MinsterBuilder():
    def __init__(self):
        self.charisma = 10
        self.smarts = 10
        self.military = 10
    def build(self):
        clear()
        nm = input("Your name please: ")
        clear()
        print("your name is: ", nm)
        party = input("please chose between (1)Democrat or (2)Republican. please type the number: ")
        if party == "1":
            pp = "Democratic"
            self.military = self.military - 4
            self.smarts = self.smarts + 3
            self.charisma = self.charisma + 1
            print("your party is:", pp)
            print("your atributes are: ")
            print("CHA: ", self.charisma)
            print("SMA: ", self.smarts)
            print("MIL: ", self.military)
        if party == "2":
            pp = "Republican"
            self.military = self.military + 4
            self.smarts = self.smarts - 2
            self.charisma = self.charisma - 4
            print("your party is: ", pp)
            print("your atributes are: ")
            print("CHA: ", self.charisma)
            print("SMA: ", self.smarts)
            print("MIL: ", self.military)
        if pp == "Republican" or "Democratic":
            sleep(10)
            print("now begining the game")
            begin()
        else:
            print("Sorry you failed to select a party. Exiting now...")
            sleep(5)
            os._exit(1)



def checkpoint():
    clear()
    print("Work in progress")
    sleep(5)
    begin()
def changelog():
    print("========================================================")
    print("|                Version 0.1.1 Changelog               |")
    print("|                -Added Basic voter Functionality      |")
    print("|                -Added Basic End turn system          |")
    print("|                -Added 'Minister Builder'             |")
    print("|                                                      |")
    print("========================================================")
    sleep(10)
    menu()
def excepts():
    print("No input detected. Please use one of the responses")
    sleep(5)
    menu()
def main_menu():
    print("******MAIN MENU*******")
    print("Welcome to Bills. The government simulation game!")
    print("Please type 'Begin', 'Help', 'Updates', or 'Exit'")
    ip = input(">")
    if ip == "Begin":
        intro()
    if ip == "Updates":
        clear()
        changelog()
    if ip == "Help":
        hel()
    if ip == "Exit":
        exit()
    else:
        excepts()
def menu():
    clear()
    main_menu()
class yearticks:
    def __init__(self):
        self.year = 1997
        print(self.year)
    def yeartick(self):
        self.year = self.year + 1
        print(self.year)
    def yeartick2(self):
        self.year = self.year + 1
        print(self.year)
    def yeartick3(self):
        self.year = self.year + 1
        print(self.year)
    def yeartick4(self):
        self.year = self.year + 1
        print(self.year)
    def yearelection(self):
        if self.year == 2001:
            print("Its election year! Time to see if you will win!")
def intro():
    minbuild = MinsterBuilder()
    minbuild.build()
class voter:
    def __init__(self):
        self.totalvoters = 12000000
        self.playervoters = self.totalvoters / 3
    def votededuct(self):
        self.playervoters = self.playervoters - 25000
        print("Total ammount of voters in country: ", self.totalvoters)
        print("Total that will vote for you: ", self.playervoters)
    def voterinfo(self):
        print("Total ammount of voters in country: ", self.totalvoters)
        print("Total that will vote for you: ", self.playervoters)


def begin():
    clear()

    class GameStatus:
        def __init__(self):
            self.money = 10000000
            print(self.money)
        def reduce_moneysmall(self):
            self.money = self.money - 1000
            print(self.money)
            if self.money <= -90000:
                game_over()
        def reduce_moneymed(self):
            self.money = self.money - 10000
            print(self.money)
            if self.money <= -90000:
                game_over()
        def reduce_moneybig(self):
            self.money = self.money - 100000
            print(self.money)
            if self.money <= -90000:
                game_over()
    clear()
    vot = voter()

    print("Welcome to Polveta, Prime minister!")
    print("You have just come to power through the elction that is every 4 years.")
    print("the current year is: ")
    year_tick = yearticks()
    print("Current budget: ")
    game_status = GameStatus()
    print("New budget with expenses: ")
    game_status.reduce_moneymed()
    en = input("Please say 'end turn' to proceed to the next year or type 'votes' to see current voters\n")
    if en == "end turn":
        print("Current year: ")
        year_tick.yeartick()
    if en == "votes":
        clear()
        vot.voterinfo()
        print("Please type 1 to go back")
        lx = input(">")
        if lx == "1":
            begin()

    lo = input("Type end turn or type voteadj to see the new voter scores. If you wish to save your spot type 's' to save.\n")
    if lo == "end turn":
        print("Current year: ")
        year_tick.yeartick()
    if lo == "s" ^ "S":
        checkpoint()
    if lo == "voteadj":
        clear()
        vot.votededuct()
        print("Please type 1 to go back")
        lr = input(">")
        if lr == "1":
            begin()
    li = input("please type end turn again please\n")
    if li == "end turn":
        print("Current year: ")
        year_tick.yeartick()
    lx = input("please type end turn again\n")
    if lx == "end turn":
        print("Current year: ")
        year_tick.yeartick()
    year_tick.yearelection()
    game_over()


def game_over():
    print("Game over. Try again? Type 'Y'")
    be = input(">")
    if be == "Y":
        main_menu()
    else:
        os._exit(1)

def exit():
    os._exit(1)

menu()
