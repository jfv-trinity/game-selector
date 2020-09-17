

def game_generator():
    print("fix me")


def adding_game():
    game = ""

    print("Type in game name then hit enter to add next game.\n""When you are done adding games type: stop")
    while game != "stop":
        print("Number of games on list:")
        print(len(application_gamelist))
        print(application_gamelist)
        print("\nEnter game name here:")
        game = input()
        if game != "stop":
            application_gamelist.append(game)
 

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
        print("What would you like to select?")
        ui_selection = input("1:").strip()
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
