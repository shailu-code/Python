import random 

# List of fruits and related information
Fruits = {
    'apple': 'It is a common fruit that comes in various colors such as red, green, and yellow. It is known for its sweet and crunchy taste.',
    'pear': 'It is a sweet and juicy fruit with a distinctive bell-like shape. It comes in various colors such as green, red, and yellow.',
    'peach': 'It is a soft and fuzzy fruit with a sweet and juicy flesh. It is known for its fragrant aroma and velvety skin.',
    'plum': 'It is a small, round fruit with smooth skin and sweet or tart flesh. It comes in various colors such as red, purple, and yellow.',
    'cherry': 'It is a small round fruit with a hard seed inside and is often dark red or black when ripe. It is known for its sweet and tangy flavor.',
    'apricot': 'It is a small, yellowish-orange fruit with a velvety skin and sweet flesh. It is known for its delicate flavor and soft texture.',
    'nectarine': 'It is a smooth-skinned variety of peach with a sweet and juicy flesh. It is similar in taste and appearance to peaches but lacks the fuzzy skin.',
    'mango': 'It is a tropical fruit with a sweet taste and juicy flesh. It is known for its rich flavor, vibrant color, and tropical aroma.',
    'kiwi': 'It is a small, brown fruit with fuzzy skin and bright green flesh. It has a sweet and tangy flavor and is rich in vitamin C.',
    'papaya': 'It is a tropical fruit with orange flesh and black seeds inside. It is known for its sweet and musky flavor and is often eaten fresh or used in salads and smoothies.',
    'banana': 'It is a long curved fruit that is yellow when ripe and grows in clusters. It has a creamy texture and sweet flavor.',
    'grape': 'It is a small round fruit that grows in clusters and comes in different colors such as green, red, or purple. It can be eaten fresh or used to make wine.',
    'orange': 'It is a round citrus fruit with a thick skin and juicy, sweet flesh. It is known for its high vitamin C content and refreshing taste.',
    'strawberry': 'It is a small red fruit with seeds on its surface and is often used in desserts. It has a sweet and slightly tart flavor.',
    'watermelon': 'It is a large, round fruit with green skin and juicy red flesh. It is known for its refreshing taste and high water content.',
    'pineapple': 'It is a tropical fruit with a tough outer skin and sweet juicy flesh inside. It has a tangy and sweet flavor.',
    'blueberry': 'It is a small round fruit with a dark blue color and sweet flavor. It is often used in baking or eaten fresh as a snack.',
    'raspberry': 'It is a small red fruit with a tart and slightly sweet flavor. It is often used in jams, sauces, or eaten fresh.',
    'blackberry': 'It is a dark purple fruit with a sweet and tangy flavor. It is often used in pies, cobblers, or eaten fresh.',
    'cranberry': 'It is a small red fruit with a tart flavor. It is often used in juices, sauces, or dried as a snack.',
    'lemon': 'It is a citrus fruit with a sour taste and yellow skin. It is often used in cooking and beverages.',
    'lime': 'It is a citrus fruit with a tart flavor and green skin. It is commonly used in cooking and cocktails.',
    'fig': 'It is a small, pear-shaped fruit with sweet flesh and a soft skin. It can be eaten fresh or dried.',
    'avocado': 'It is a pear-shaped fruit with a creamy texture and nutty flavor. It is often used in salads and spreads.',
    'guava': 'It is a tropical fruit with a green or yellow skin and sweet, fragrant flesh. It is often eaten fresh or used in jams.',
    'passionfruit': 'It is a round fruit with a tough outer rind and aromatic seeds inside. It has a sweet and tangy flavor.',
    'lychee': 'It is a small, round fruit with a rough, red shell and sweet, white flesh. It is often eaten fresh or used in desserts.',
    'dragonfruit': 'It is a tropical fruit with bright pink skin and white or red flesh speckled with black seeds. It has a mild, sweet flavor.',
    'persimmon': 'It is a orange or red fruit with a sweet, honey-like flavor and smooth texture. It is often eaten fresh or dried.',
    'pomegranate': 'It is a round fruit with a tough outer skin and juicy, red seeds inside. It has a sweet and tangy flavor.',
    'jackfruit': 'It is a large, spiky fruit with sweet, yellow flesh and seeds. It is often used in cooking as a meat substitute.',
    'coconut': 'It is a tropical fruit with a hard, brown shell and sweet, white flesh inside. It is used in cooking and beverages.',
    'tangerine': 'It is a small citrus fruit with a thin, easy-to-peel skin and sweet, juicy flesh. It is similar to oranges but smaller.',
    'cantaloupe': 'It is a round melon with a rough, netted skin and sweet, orange flesh. It is often eaten fresh or used in fruit salads.'
}

def Hangman_game():
    word = random.choice(list(Fruits.keys()))                                   # Choose a random fruit from the dictionary

    Max_Wrong = 3
    print("\n     ------- Let's play Hangman Game --------\n")
    print("--->You have to guess a Fruit name----- one letter at a time\n")
    print(f'-->You have {Max_Wrong} wrong tries allowed.')
    print(f'-->The word has {len(word)} letters.\n')
    print(f'-->Hint: {Fruits[word]}\n')                                         #Fruit --> dictionary

    for _ in word: 
        print('_', end=' ') 
    print()                                                                     #leaving blank space

    letterGuessed = '' 
    Tries = 0
    flag = 0
    try: 
        while Tries < Max_Wrong and flag == 0: 
            print() 

            guess = str(input('Enter a letter to guess: ')) 

            if not guess.isalpha():                                             #letter is an alphabet or not
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1:                                                #if 2 or more letter are choosed at a time
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter')                   #if guessed letter is already guessed
                continue

            if guess in word: 
                k = word.count(guess)                                           #Count number of times  the guessed letter is in the word choosed by computer
                for _ in range(k): 
                    letterGuessed += guess                                      #Adding the guessed letter multiple times in 'correct-guessed' if it appears multiple times
            else:
                print(f'Wrong letter "{guess}".')
                Tries += 1                                                      #Increaasing the wrong guess counter
                print(f'You have {Max_Wrong - Tries} wrong tries left.')

            for char in word: 
                if char in letterGuessed and set(letterGuessed) != set(word): 
                    print(char, end=' ')                                        #Printing correctly guessed letters
                elif set(letterGuessed) == set(word): 
                    print("The word is: ", word )                               #here we can use "end()" function also.
                    flag = 1                                                    #Set the flag to indicate winning
                    print('Congratulations, You won!') 
                    break 
                else:                                                           # Keeping underscores for unguessed letters
                    print(' _', end=' ')                                         #end=' ' part tells the print function to print a space character () instead of a newline at the end. This keeps the cursor on the same line, allowing you to print something else on the same line without a break.

        if Tries >= Max_Wrong and set(letterGuessed) != set(word): 
            print() 
            print('You ran out of chances! Try again..') 
            print('The word was {}'.format(word)) 


    except KeyboardInterrupt: 
        print()                                                                 #leave a blank line 
        print('Bye! Try again.') 
        exit()

# Bulls & Cow Game
def Bulls_Cow():
    print("       -------Let's Play Bulls & Cow Game--------\n")
    print("Rules:-\n")
    print("Bull--> Guessed digit is right and at right place\n")
    print("Cow--> Guessed digit is right but at wrong place\n")
    print("Press numbers without giving whitespaces -- &-- and type 5 digit number at once")

    def getDigits(num):
        return [int(i) for i in str(num)]

    def Duplicates(num):
        list_num = getDigits(num)
        if len(list_num) == len(set(list_num)):
            return True
        else:
            return False

    def generateNum():
        while True:
            num = random.randint(10000, 100000)
            if Duplicates(num):
                return num

    def numOfBullsCows(num, guess):
        count = [0, 0]
        list_num = getDigits(num)
        list_guess = getDigits(guess)

        for i, j in zip(list_num, list_guess):
            if j in list_num:
                if j == i:
                    count[0] += 1
                else:
                    count[1] += 1
        return count

    num = generateNum()
    print("--A 5 digit number of all different digits is already generated--\n\n")
    tries = int(input('Enter number of tries to guess the number: '))

    while tries > 0:
        guess = int(input("Enter your guess: "))

        if not Duplicates(guess):
            print("Entered number is having repeated digits. ----Try again----")
            continue
        if guess < 10000 or guess > 100000:
            print("Enter 5 digit number only. Try again----")
            continue

        count = numOfBullsCows(num, guess)
        print(f"{count[0]} bulls, {count[1]} cows")
        tries -= 1

        if count[0] == 5:
            print("---congratulations---You guessed it right!")
            break
    else:
        print(f"You ran out of tries. Number was {num}")

# Rock, Paper, Scissors game
def Rock_Paper_Scissors():
    print("\n------------Let's Play Rock Paper & scissor------------\n")
    print("Rules:-\n")
    print("--> Rock smashes scissors\n")
    print("--> Paper covers rock\n")
    print("--> Scissors cuts paper\n\n")

    choice = input("Enter a choice (rock, paper, scissors): ")
    actions = ["rock", "paper", "scissors"]
    computer = random.choice(actions)
    print(f"\nYou choosed {choice}, computer choosed {computer}.\n")

    if choice == computer:
        print(f"Both players selected {choice}. It's a tie!")
    elif choice == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif choice == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif choice == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

def game_selector(choice):
    switcher = {
        1: Hangman_game,
        2: Bulls_Cow,
        3: Rock_Paper_Scissors,
        
    }
    selected_game = switcher.get(choice)
    if selected_game:
        selected_game()                    # Execute the selected game function
    else:
        print("Invalid choice")

# Main loop
while True:
    print("\n\n     -------------- PYTHON PROJECT --------------\n")
    print("\nChoose a game:")
    print("1. Hangman")
    print("2. Bulls & Cow Game")
    print("3. Rock, Paper, Scissors")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("\n-------------- Thanks for playing! -----------------")
        break
    else:
        game_selector(choice)

    play_again = input("\nDo you want to play another game? (y/n): ")
    if play_again.lower() != "y":
        print("\n-------------- Thanks for playing! -----------------")
        break
