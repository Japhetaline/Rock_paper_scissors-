def rock_paper_scissors() -> None:
    import random;
    wins = [1, 2, 3];
    wins_descriptions = ["once", "twice", "thrice"];
    wins_dict = dict(zip(wins, wins_descriptions));
    options = ["R", "P", "S"];
    options_desciptions = ["Rock", "Paper", "Scissors"];
    options_dict = dict(zip(options, options_desciptions));

    again_bool = True;
    while(again_bool):
        print("Winning Rules of the Rock Paper Scissor game are as follows: \n"
                                +"Rock vs Paper -> Paper wins \n"
                                + "Rock vs Scissor -> Rock wins \n"
                                +"paper vs Scissor -> Scissor wins \n");
        
        print("Play by typing a letter");
        print("R: Rock, P: Paper, S: Scissors");

        computer_choice = "";
        player_wins = 0;

        for i in range(3):
        
            while True:
                player_choice = input("Play: ");
                if player_choice.upper() not in options:
                    print(f"Player ({player_choice})");
                    print("Error! Please enter a valid character\n\n");
                    continue;
                else:
                    computer_choice = random.choice(options);
                    
                    if player_choice.upper() == computer_choice:
                        print(f"Player ({player_choice}): CPU ({computer_choice})");
                        print("A draw game.");
                        print("Please try again!\n\n")
                        continue;
                    else:
                        if player_choice.upper() == "R":
                            if computer_choice == "S":
                                print(f"Player ({player_choice}): CPU ({computer_choice})");
                                print(f"{options_dict[player_choice.upper()]} crushes {options_dict[computer_choice]}\n\n");
                                player_wins += 1;
                            elif computer_choice == "P":
                                print(f"Player ({player_choice}): CPU ({computer_choice})");
                                print(f"{options_dict[computer_choice]} covers {options_dict[player_choice.upper()]}\n\n");
                        elif player_choice.upper() == "P":
                            if computer_choice == "R":
                                print(f"Player ({player_choice}): CPU ({computer_choice})");
                                print(f"{options_dict[player_choice.upper()]} covers {options_dict[computer_choice]}\n\n");
                                player_wins += 1;
                            elif computer_choice == "S":
                                print(f"Player ({player_choice}): CPU ({computer_choice})");
                                print(f"{options_dict[computer_choice]} cuts {options_dict[player_choice.upper()]}\n\n");
                        elif player_choice.upper() == "S":
                            if computer_choice == "R":
                                print(f"Player ({player_choice}): CPU ({computer_choice})");
                                print(f"{options_dict[computer_choice]} crushes {options_dict[player_choice.upper()]}\n\n");
                            elif computer_choice == "P":
                                print(f"Player ({player_choice}): CPU ({computer_choice})");
                                print(f"{options_dict[player_choice.upper()]} cuts {options_dict[computer_choice]}\n\n");
                                player_wins += 1;
                        break;
        if player_wins == 3:
            print("Emphatic win.")
            print(f"You smashed {wins_dict[player_wins]}!\n\n");
        elif player_wins == 2:
            print("Congrats. You won the game!");
        elif player_wins == 1:
            print("Oops. You lost the game.");
            print("Try again!\n\n");
        elif player_wins == 0:
            print("Comprehensive lost.")
            print(f"You were thrashed three times!");
            print("Try again!\n\n");

        print("Do you want to play again?");
        again = input("'Y' for 'Yes', 'N' for 'No': ").lower();
        print("\n\n")
        if again.lower() != "y":
            again_bool = False;


rock_paper_scissors();