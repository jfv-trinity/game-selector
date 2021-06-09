import random

#Methods used:
def printgamelist():
    application_gamelist.sort()
    print(application_gamelist)


def game_generator():
    userpicking = True
    if userpicking is True:
        print("------------------------------------------------------------\n \n"
              "[1] Pick Random Game \n"
              "[2] Modify pick chances \n"
              "[3] Return to menu \n"
              "[4] Close program \n")
        print("\nType the number of the option you wish to select.")
        ui_selection = input("Selecting option: ").strip()
        if ui_selection == "1":
            print("Hey that's a pretty good game.... You got ", random.sample(application_gamelist, 1))
            print("Press enter when done viewing")
            userdone = input()
            if userdone == "":
                return
            elif userdone is not "":
                print("I guess you don't want to leave hu? I get it. Its a pretty good UI")

        elif ui_selection == "2":
            print("Add generator_Modifications")
        elif ui_selection == "3":
            return
        elif ui_selection == "4":
            exit()


def adding_game():

    failedentries = 0
    game = "Empty"

    print("\n------------------------------------------------------------")
    print("Type the game name you wish to add then hit enter to add game.")
    print("When you are done hit enter twice or type: stop")
    print("\n")
    print("Current number of games on list: " + (str(len(application_gamelist))))
    application_gamelist.sort()
    print(application_gamelist)
    while game != "stop":
        print("\n\nEnter game title: ", end='')
        game = input()
        if game != "stop" and game != "":
            failedentries = 0
            application_gamelist.append(game)
            application_gamelist.sort()
            print(application_gamelist)
        if failedentries == 1:
            return
        if game == "":
            failedentries = 1
            print("press enter again to return to menu")


def deleting_game():
    user_wants_to_go_back_to_main_menu = False
    game_removal = 'Empty Shell'

    print("\n------------------------------------------------------------")
    print("Type the game you wish to remove. When done type stop or press enter twice.")
    print("Current number of games on list: " + (str(len(application_gamelist))))
    print("\n")
    application_gamelist.sort()
    print(application_gamelist)
    while game_removal is not "return":
        # make into a switch case later.
        print("\nEnter game title: ", end='')
        game_removal = input()
        if game_removal == 'return' or user_wants_to_go_back_to_main_menu is True:
            break
        if game_removal == '':
            print('press enter again to return to main menu')
            user_wants_to_go_back_to_main_menu = True
        for game in application_gamelist:
            if game_removal == game:
                application_gamelist.remove(game_removal)
                print("game has been removed")
                print("\nUpdated List: ")
                print(application_gamelist)
                break


def view_list():
    userviewing = True
    print("\n------------------------------------------------------------")
    print("Current number of games on list: " + (str(len(application_gamelist))))
    print(application_gamelist)
    while userviewing is True:
        print("\nHit enter when done viewing to return to menu")
        userchoice = input()
        if userchoice == "":
            userviewing = False


def clear_list():
    application_gamelist.clear()
    print("------------------------------------------------------------\n")
    print("List Cleared\n")


#Add Description feature when hovering over lines 12-17 in UI, this feature allows more detailed descriptions.
def main_menu():
    local_gamelist = open("Game_List.txt", "r")
    for line in local_gamelist.readlines():
        line = line.strip()
        if line:
            application_gamelist.append(line)
    local_gamelist.close()

    closing = True
    while closing:
        print("------------------------------------------------------------\n \n"
        "[1] Get help picking a game \n"
        "[2] Add a game \n"
        "[3] Delete a game \n"
        "[4] See list \n"
        "[5] Clear list \n"
        "[6] Close program \n")
        print("\nType the number of the option you wish to select.")
        ui_selection = input("Selecting option: ").strip()
        if ui_selection == "1":
            game_generator()
        elif ui_selection == "2":
            adding_game()
        elif ui_selection == "3":
            deleting_game()
        elif ui_selection == "4":
            view_list()
        elif ui_selection == "5":
            clear_list()
        elif ui_selection == "6":
            closing = False
    local_gamelist = open("Game_List.txt", "w")
    temp = str('')
    for game in application_gamelist:
        temp = (temp + game + "\n")
    local_gamelist.write(temp)
    local_gamelist.close()

#Global Variables used:
application_gamelist = []


main_menu()
