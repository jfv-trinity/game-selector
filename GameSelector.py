

def game_generator():
    print("fix me")


def adding_game():

    failedentries = False
    game = "Empty"

    print("\nType the game name you wish to add then hit enter to add game.\n")
    print("When you are done hit enter twice or type: stop\n")
    print("Current number of games on list: " + (str(len(application_gamelist))))
    application_gamelist.sort()
    print(application_gamelist)
    while game != "stop":
        print("\nEnter game title: ", end='')
        game = input()
        if game != "stop" and game != "":
            failedentries = 0
            application_gamelist.append(game)
            application_gamelist.sort()
            print(application_gamelist)
        if failedentries == 1:
            return
            print("returned")
        if game == "":
            failedentries = 1
            print("press enter again to return to menu")



 

def deleting_game():
    game = ""

    while game is not "stop":
        print(len(application_gamelist))
        print(application_gamelist)
        print("\nEnter game name here:")
        game = input()
        if game == "stop":
            return
        elif application_gamelist.count(game):
            application_gamelist.remove(game)
        else:
            print("Not on list but we took it off anyway! :D")


def view_list():
    print(application_gamelist)


def clear_list():
    application_gamelist.clear()


#Add Description feature when hovering over lines 12-17 in UI, this feature allows more detailed descriptions.
def main_menu():
    find_gamelist = open("Game_List.txt", "r")
    for line in find_gamelist.readlines():
        line = line.strip()
        if line:
            application_gamelist.append(line)
    find_gamelist.close()

    closing = True
    while closing:
        print(""
        "[1] Get help picking a game \n"
        "[2] Add a game \n"
        "[3] Delete a game \n"
        "[4] See list \n"
        "[5] Clear list \n"
        "[6] Close program \n")
        print("Type the number of the option you wish to select.")
        ui_selection = input("option: ").strip()
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
    find_gamelist = open("Game_List.txt", "w")
    temp = str('')
    for game in application_gamelist:
        temp = (temp + game + "\n")
    find_gamelist.write(temp)
    find_gamelist.close()


application_gamelist = []


main_menu()
