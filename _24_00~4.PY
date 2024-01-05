############### Blackjack Project v12.05 #####################

import random, decimal, time

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

points_counter = 0

# def main_Black_function():

# continue_playing = True
# while continue_playing == True:
def playing_again():
    print(logo)

    is_bust = False

    # Notes Lobby: ? for any question or anything to review
    # TODO 1: Things to fix still
    # Keep playing? y, loop again
    # ASCII graphics
    # Hit or stay after:
    '''
    Do you want to Hit or Stay? (H or S): h
    You got dealt a Queen
    Womp womp. You went over. Bust. You lose
    '''

    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~     Welcome to Blackjack!     ~~ ")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print("The dealer dealt your first card")

    # GPT notes:
    '''
    Here are some issues in the provided code:

    Variable Initialization: Many variables are declared but not initialized with values or aren't being used throughout the code. This can lead to unnecessary complexity and confusion.

    Inconsistent Indentation: The code has inconsistent indentation, which can lead to syntax errors. Make sure all blocks of code are consistently indented.

    Logic Errors: There appear to be logic errors in determining when a player goes bust. The standard rule in blackjack is that a player busts when their total exceeds 21, but your code checks for 22.

    Infinite Loop: The code contains nested while loops, and there's a potential for an infinite loop if the conditions for ending the loop aren't met correctly.

    Unused Code: There are many commented-out sections of code that are not needed for the game to function. These should be removed to improve code readability.

    Lack of Documentation: The code lacks comments and explanations, which can make it challenging to understand the purpose of various sections and variables.

    Undefined Variables: Several variables are declared but never used, such as Human_current_total, Computer_current_total, Human_endgame_total, Computer_endgame_total, and others. It's important to remove unnecessary variables to keep the code clean.

    Missing Game Logic: The code lacks the main game logic, such as determining the winner, handling ties, and allowing for multiple rounds of the game.

    Error Handling: The code lacks error handling for invalid user input, which can result in exceptions if the user enters unexpected input.

    Variable Naming: Variable names like new_random_card_value_drawn, hidden_index_for_card_Ace, and hidden_index_for_card_Jack are confusing and not following standard naming conventions. Variable names should be clear and descriptive.

    To fix these issues and create a functional blackjack game, you should review the game rules and logic, clean up unnecessary code, and ensure that the code follows proper coding conventions and indentation.
    '''

    # Make range 2-14, 11 is the ONLY Ace

    # Blackjack ASCII logo, imported here:

    ############### Our Blackjack House Rules #####################
    # Blackjack Rules: in order for the Human to win vs the Computer,

    ## The deck is unlimited in size.
    ## There are no jokers.
    ## The Jack/Queen/King all count as 10.
    ## The the Ace can count as 11 or 1.
    ## Use the following list as the deck of cards:
    ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ## The cards in the list have equal probability of being drawn.
    ## Cards are not removed from the deck as they are drawn.
    ## The computer is the dealer.

    Human_current_total = ""
    Computer_current_total = ""

    Human_endgame_total = ""
    Computer_endgame_total = ""

    Human_player = ""
    Computer_player = ""

    new_random_card_value_drawn = ""

    face_card = ""

    Win_Condition = ""  # Human must have more than the dealer/PC as their total, BUT be 21 or less than 21. If 22 or more = Bust.

    deck_size = 1000

    is_22_or_more = False

    # Ace = 1 or 11, 2-9 = that number, 10 = 10, Jack = 12, Queen = 13, King = 14
    # Values during the game, to determine who has the higher amount:

    '''
    real_Jack_value = 10
    real_Queen_value = 10
    real_King_value = 10
    real_Ace_value = 1 or 11
    '''
    True_point_value = 0

    hidden_index_for_card = ""
    hidden_index_for_card_Ace = 10.1
    hidden_index_for_card_Jack = 10.2
    hidden_index_for_card_Queen = 10.3
    hidden_index_for_card_King = 10.4

    # useable index numbers:
    '''

    2-9 = 2-9
    10 = 10
    Ace.11 = 11
    Jack = 12
    Queen = 13
    King = 14
    '''

    # 1-14
    start_of_game_card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # 13 cards total with each equal chance of being drawn:

    # def determine_face_card():
    #     if new_random_card_value_drawn == 11:
    #         face_card = "Ace"
    #     if new_random_card_value_drawn == 10:
    #         face_card = random.choice(10, "Jack", "Queen", "King")

    # global points_counter   # should I make this global?
      # should I make this global (here)?
    cards_dealt_to_you_per_round = 0


    continue_playing = True
    while continue_playing:

        # def start_a_new_round():
        # Dealing of the cards:
        drawn_random_card = random.randint(2, 14)

        #Ace (use if other block doesn't work)
        # if drawn_random_card == 1:
        #     face_card = "Ace"
        #     print(f"You got dealt an {face_card}")
        #     Ace_choice = input("Please pick either 1 or 11 to apply to the total. (1 or 11): ")      #choose A.1 OR A.11
        #     if Ace_choice == 1:
        #         points_counter += 1
        #     elif Ace_choice == 11:
        #         points_counter += 11

        # for card_range_iteration in range(2-9):
        #2
            # if drawn_random_card == card_range_iteration:
            #     face_card = card_range_iteration
        if drawn_random_card == 1 or drawn_random_card == 11:
            face_card = "Ace"

            Ace_choice = int(input(f"Nice! You got an {face_card}. You can pick to add 1 or 11 to your total. (1 or 11): "))
            if Ace_choice == 1:
                True_point_value = Ace_choice
                global points_counter
                points_counter += True_point_value
                if points_counter >= 22:
                    print("Womp womp. You went over. Bust. You lose")
                    is_bust = True
                    game_on=True
                elif is_bust==False:
                    Hit_or_Stay = input("Do you want to Hit or Stay? (H or S): ").upper()
                    if Hit_or_Stay == "H":
                        continue_playing = True
                    elif Hit_or_Stay != "S":
                        continue_playing = False
                    # continue_playing = False
                    # game_on = True
                else:
                    print(f"Your points so far this round is {points_counter}")
            else:
                True_point_value = Ace_choice
                points_counter += True_point_value
                if points_counter >= 22:
                    print("Womp womp. You went over. Bust. You lose")
                    is_bust = True
                    break
                else:
                    print(f"Your points so far this round is {points_counter}")

        elif drawn_random_card == 2 or drawn_random_card == 3 or drawn_random_card == 4 or drawn_random_card == 5 or drawn_random_card == 6 or drawn_random_card == 7 or drawn_random_card == 8 or drawn_random_card == 9 or drawn_random_card == 10:
            print(f"You got dealt a {drawn_random_card}")
            points_counter += drawn_random_card
            if points_counter >= 22:
                print("Womp womp. You went over. Bust. You lose")
                continue_playing = False
            else:
                print(f"Your points so far this round is {points_counter}")

        elif drawn_random_card == 12:
            face_card = "Jack"
            print(f"You got dealt a {face_card}")
            points_counter += 10
            if points_counter >= 22:
                print("Womp womp. You went over. Bust. You lose")
                continue_playing = False
            else:
                print(f"Your points so far this round is {points_counter}")

        elif drawn_random_card == 13:
            face_card = "Queen"
            print(f"You got dealt a {face_card}")
            points_counter += 10
            if points_counter >= 22:
                print("Womp womp. You went over. Bust. You lose")
                continue_playing = False
            else:
                print(f"Your points so far this round is {points_counter}")

        elif drawn_random_card == 14:
            face_card = "King"
            print(f"You got dealt a {face_card}")
            points_counter += 10
            if points_counter >= 22:
                print("Womp womp. You went over. Bust. You lose")
                continue_playing = False
            else:
                print(f"Your points so far this round is {points_counter}")

        # print(draw_random_card)
        elif points_counter >= 22:
            print("That's game, buddy. Try again.")
            break

        '''
        ########################## how do you want to apply the 1 or 11?
        if new_random_card_value_drawn == 10:
            hidden_index_for_card = random.randrange(101, 104) / 10
            # decimal.Decimal(random.randrange(101, 389)) / 100
            print(f"The hidden value is: {hidden_index_for_card}")
            # Ace values:
            if hidden_index_for_card == 10.1:
                real_value = 1 or 11
                face_card = "Ace"
            # 10.1 = Ace.1, 10.2 = Ace.11
    
            # Jack values:
            elif hidden_index_for_card == 10.2:
                real_value = 10
                face_card = "Jack"
            # Queen values:
            elif hidden_index_for_card == 10.3:
                real_value = 10
                face_card = "Queen"
            # King values:
            elif hidden_index_for_card == 10.4:
                real_value = 10
                face_card = "King"
    
            random_face_card = decimal.Decimal(random.randrange(100, 103)) / 10
            # print(f"The random face card is: {random_face_card}")
            print(f"The face card is a: {face_card}")
            print(f"The dealer deals a card to you. It has a True point value of: {new_random_card_value_drawn}")
            points_counter += new_random_card_value_drawn
            print(f"So far this round, you have {points_counter} points.")
            '''

            # end of 1st card drawn:

            # start of 2nd card drawn:
            # hit_or_stay_option = input(f"Do you want to hit or stay? (H or S)").upper()
            # if hit_or_stay_option == "H":
            #     cards_dealt_to_you_per_round += 1
            #     start_a_new_round()
        if is_bust==True:   #or  # if is_bust:
            print("Oh noes! You went over 21!")
            # game_on=True
        else:
            Hit_or_Stay = input(f"Do you want to Hit or Stay? (H or S): ").upper()
            if Hit_or_Stay == "H":
                continue_playing = True
            else:                       ################################## user stops, and computer starts their card draws:  ##############################################
                # 1-14
                start_of_game_card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                # 13 cards total with each equal chance of being drawn:

                # def determine_face_card():
                #     if new_random_card_value_drawn == 11:
                #         face_card = "Ace"
                #     if new_random_card_value_drawn == 10:
                #         face_card = random.choice(10, "Jack", "Queen", "King")

                computer_points_counter = 0
                cards_dealt_to_you_per_round = 0

                computer_continue_playing = True
                while computer_continue_playing == True:

                    # def start_a_new_round():
                    # Dealing of the cards:
                    drawn_random_card = random.randint(2, 14)

                    # Ace (use if other block doesn't work)
                    # if drawn_random_card == 1:
                    #     face_card = "Ace"
                    #     print(f"You got dealt an {face_card}")
                    #     Ace_choice = input("Please pick either 1 or 11 to apply to the total. (1 or 11): ")      #choose A.1 OR A.11
                    #     if Ace_choice == 1:
                    #         points_counter += 1
                    #     elif Ace_choice == 11:
                    #         points_counter += 11

                    # for card_range_iteration in range(2-9):
                    # 2
                    # if drawn_random_card == card_range_iteration:
                    #     face_card = card_range_iteration
                    print("The dealer flips over their next card")
                    time.sleep(1.5)
                    if drawn_random_card == 1 or drawn_random_card == 11:
                        face_card = "Ace"
                        True_point_value = 11
                        print(f"It drew an Ace. That's {True_point_value} points!")

                        computer_points_counter += True_point_value
                        if computer_points_counter >= 22:
                            print("Computer went over! You win!")
                            computer_continue_playing = False
                            continue_playing = False
                        elif computer_points_counter >= 14 and computer_points_counter < 22:
                            print(f"The dealer points so far this round is {computer_points_counter}")
                            computer_continue_playing = True



                    elif drawn_random_card == 2 or drawn_random_card == 3 or drawn_random_card == 4 or drawn_random_card == 5 or drawn_random_card == 6 or drawn_random_card == 7 or drawn_random_card == 8 or drawn_random_card == 9 or drawn_random_card == 10:
                        print(f"It got dealt a {drawn_random_card}")
                        computer_points_counter += drawn_random_card
                        if computer_points_counter >= 22:
                            print("Computer went over! You win!")
                            computer_continue_playing = False
                            continue_playing = False
                        elif computer_points_counter >= 14 and computer_points_counter < 22:
                            print(f"The dealer points so far this round is {computer_points_counter}")
                            computer_continue_playing = True


                    elif drawn_random_card == 12:
                        face_card = "Jack"
                        print(f"It got dealt a {face_card}")
                        computer_points_counter += 10
                        if computer_points_counter >= 22:
                            print("Computer went over! You win!")
                            computer_continue_playing = False
                            continue_playing = False
                        elif computer_points_counter >= 14 and computer_points_counter < 22:
                            print(f"The dealer points so far this round is {computer_points_counter}")
                            computer_continue_playing = True
        #TODO                # else: #missing this last statement ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



                    elif drawn_random_card == 13:
                        face_card = "Queen"
                        print(f"It got dealt a {face_card}")
                        computer_points_counter += 10
                        if computer_points_counter >= 22:
                            print("Computer went over! You win!")
                            computer_continue_playing = False
                            continue_playing = False
                        elif computer_points_counter >= 14 and computer_points_counter < 22:
                            print(f"The dealer points so far this round is {computer_points_counter}")
                            computer_continue_playing = True


                    elif drawn_random_card == 14:
                        face_card = "King"
                        print(f"It got dealt a {face_card}")
                        computer_points_counter += 10
                        if computer_points_counter >= 22:
                            computer_continue_playing = False
                            continue_playing = False
                        elif computer_points_counter >= 14 and computer_points_counter < 22:
                            print(f"The dealer points so far this round is {computer_points_counter}")
                            computer_continue_playing = True
                        elif computer_points_counter >= 17 and computer_points_counter < 22:
                            print(f"The dealer Stays at {computer_points_counter} points")
                            Hit_or_Stay = "S"
                            computer_continue_playing = False
                            if computer_continue_playing == False and Hit_or_Stay == "S":
                                if computer_points_counter > points_counter:
                                    print(f"The dealer beat you, score of {computer_points_counter} to your score of: {points_counter}")
                                    print("Sorry but the dealer beat you with a higher score. Better luck next time.")
                                    continue_playing = False
                                    break
                                elif computer_points_counter == points_counter:
                                    print("It looks like it's a Draw! You tied")
                                    continue_playing = False

                if computer_points_counter >= 22:
                    print("Bahahaha. The computer went Bust. What a loser it must be. You win!")
                    computer_continue_playing = False
                    continue_playing = False

        if points_counter >= 22:
            print("Bust: Sorry, you lose.")
            is_bust=True
            # computer_continue_playing = False  #these 3 here and below are not needed
            # continue_playing = False
        # else:
# Game Loop
game_on = True
while game_on:
    playing_again()
    # game_on = True
    while True:
        keep_playing = input(f"Do you want to keep playing? (Y or N): ").upper()
        if keep_playing == "Y" or keep_playing == "y":
            # global points_counter
            points_counter = 0
            # playing_again()
            break
            # continue_playing = True
        elif keep_playing == "N" or keep_playing == "n":
            # continue_playing = False
            print("Ok, thanks for playing! Have a great day! :)")
            game_on = False
            break
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")

# playing_again()