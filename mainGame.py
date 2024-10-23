#Name: Hangman Advanced Game
import random
import sqlite3 
from getpass import getpass #for hiding password while input
from encABC import enc #to interact with another Erika Encryption/Decryption ABC files within this folder, the 'enc' is a function
from decABC import decABC
from InputErrorHandle import ctype
from InputErrorHandle import boundary
import time
import subprocess

#sql init
conn = sqlite3.connect('HM_game_data.db')
cursor = conn.cursor()


#ASCII texts

logreg = '''
  _                       _                __    ____                   _         _                 
 | |       ___     __ _  (_)  _ __        / /   |  _ \    ___    __ _  (_)  ___  | |_    ___   _ __ 
 | |      / _ \   / _` | | | | '_ \      / /    | |_) |  / _ \  / _` | | | / __| | __|  / _ \ | '__|
 | |___  | (_) | | (_| | | | | | | |    / /     |  _ <  |  __/ | (_| | | | \__ \ | |_  |  __/ | |   
 |_____|  \___/   \__, | |_| |_| |_|   /_/      |_| \_\  \___|  \__, | |_| |___/  \__|  \___| |_|   
                  |___/                                         |___/                               
'''
hm_adv = '''
  _   _                                                            _          _                                             _   _ 
 | | | |   __ _   _ __     __ _   _ __ ___     __ _   _ __        / \      __| | __   __   __ _   _ __     ___    ___    __| | | |
 | |_| |  / _` | | '_ \   / _` | | '_ ` _ \   / _` | | '_ \      / _ \    / _` | \ \ / /  / _` | | '_ \   / __|  / _ \  / _` | | |
 |  _  | | (_| | | | | | | (_| | | | | | | | | (_| | | | | |    / ___ \  | (_| |  \ V /  | (_| | | | | | | (__  |  __/ | (_| | |_|
 |_| |_|  \__,_| |_| |_|  \__, | |_| |_| |_|  \__,_| |_| |_|   /_/   \_\  \__,_|   \_/    \__,_| |_| |_|  \___|  \___|  \__,_| (_)
                          |___/                                                                                                   
'''
customization = '''
  _              _     _            ____                 _                         _                _ 
 | |       ___  | |_  ( )  ___     / ___|  _   _   ___  | |_    ___    _ __ ___   (_)  ____   ___  | |
 | |      / _ \ | __| |/  / __|   | |     | | | | / __| | __|  / _ \  | '_ ` _ \  | | |_  /  / _ \ | |
 | |___  |  __/ | |_      \__ \   | |___  | |_| | \__ \ | |_  | (_) | | | | | | | | |  / /  |  __/ |_|
 |_____|  \___|  \__|     |___/    \____|  \__,_| |___/  \__|  \___/  |_| |_| |_| |_| /___|  \___| (_)
                                                                                                      
'''
youWin = '''
 __   __                               _           _        __  
 \ \ / /   ___    _   _    __      __ (_)  _ __   | |    _  \ \ 
  \ V /   / _ \  | | | |   \ \ /\ / / | | | '_ \  | |   (_)  | |
   | |   | (_) | | |_| |    \ V  V /  | | | | | | |_|    _   | |
   |_|    \___/   \__,_|     \_/\_/   |_| |_| |_| (_)   (_)  | |
                                                            /_/ 
'''
youLost = '''
 __   __                    _                 _                __
 \ \ / /   ___    _   _    | |   ___    ___  | |_         _   / /
  \ V /   / _ \  | | | |   | |  / _ \  / __| | __|       (_) | | 
   | |   | (_) | | |_| |   | | | (_) | \__ \ | |_   _     _  | | 
   |_|    \___/   \__,_|   |_|  \___/  |___/  \__| (_)   (_) | | 
                                                              \_\
'''
#Variables section
wordlen = 0
singleSlotted = [] #answer converted to a list
lives = 5
letter_to_be_replaced_index = []
singleSlotted__WildCard = []
correctGuess = 0
usedHint = 0
score = 0
currentUser = '1'
currentUserName = ''
availableWordsPool = []
reqDifficulty = 0
streak = 0
difficultyHi = 5
difficultyLo = 1
streakMode = 1
guessed = ['']
##array doyouknowthat this is to show the plot twists or povs while starting the game, just like the loading screen of Duolingo.
doYouKnowThat = ['In order to use a hint by revealing a random letter in the word, input the number 1. This costs you 11 marks.', 'In order to use a tip by giving you the description of the word, press 2. This costs you 17 marks.','In vocab levels, level 1,2,3,4,5 are designated for S1,S2,S3,S4,S5 students respectively.','You can add, edit and delete the words in the word bank in the Customize Your Wordbank.',"If you would like to return to a previous menu during any inputting stage, input 0 there."]

#Variables for storing temporary values, in which they are used in the middle of a program
int_temp1 = 0
str_temp1 = ''

hangman_stages = [
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / 
       |
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  
       |
    """,
    """
       -----
       |   |
       |   O
       |   |
       |
       |
    """,
    """
       -----
       |   |
       |   O
       |   
       |
       |
    """,
    """
       -----
       |   |
       |   
       |
       |
       |
    """,
    """
       -----
       |   
       |
       |
       |
       |
    """
]
#==================== print texts with colors functions zone
#Different colors of words are added at different scenarios, e.g. print_wrong gives out words in red, this imply errors (e.g. inputting wrong passwords). print_lose gives out words in white in red color, this implies fatal things, e.g. loosing the game/deleting entire leaderboard. print_tip gives out words in blue. It doesn't only for giving out tips, the function is sometimes used for decorations to make this game more vivid. print_hi_streak gives out blue words in yellow background. It looks so encouraging for players who have achieved high streaks.
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
PURPLE= "\033[35m"  

def print_tip(tip):
    print(f"{BLUE}{tip}{RESET}")

def print_correct(message):
    print(f"{GREEN}{message}{RESET}")

def print_wrong(message):
    print(f"{RED}{message}{RESET}")

def print_win(msg):
    print(f"\033[42m{msg}\033[0m{RESET}")

def print_lose(msg):
    print(f"\033[41m{msg}\033[0m{RESET}")

def print_hi_streak(msg):
    print(f"\033[34;43m{msg}\033[0m{RESET}")
def print_purple(msg):
    print(f"{PURPLE}{msg}{RESET}")

#==================== Auxiliary functions:
def fatalInputHandling_Integer(currentVar,loValue,hiValue):
    try:
        currentVar = int(currentVar)
        if ((currentVar >hiValue) or (currentVar<loValue)) == False: #if any criteria = false, then it returns true
            return True
        else:
            print(("="*30)+ "Range error" + ("="*30))
            return False
    except ValueError:
        print(("="*30)+ "Value error" + ("="*30))
        return False
#Code: 

def streakUpload(shiftScenario):
    global currentUser, streak
    cursor.execute("SELECT Hi_streak FROM users WHERE userID = ?",(currentUser,))
    streak2compare = cursor.fetchone()[0]
    streak2compare = int(streak2compare)
    if streak > streak2compare:
        cursor.execute("UPDATE users SET Hi_streak = ? WHERE userID = ?",(streak,currentUser,))
        conn.commit()
        print_hi_streak(f"{shiftScenario} Congrats for acing this streak as your highest streak in your lifetime!")


def InclRangeCheck(questionPrompt,hi,lo,TolerantBlank):
    proceed1 = False
    proceed2 = False
    while (not proceed1) or (not proceed2):
        val = input(questionPrompt)
        if (TolerantBlank == True) and (val == ''): #return the blank value instantly, useful for editWords()
            break
        else:
            proceed1 = ctype(val,'int')
            if not proceed1:
                print_lose("It is not an integer! Input that again.")
                continue
            val = int(val)
            proceed2 = boundary(hi,lo,val,'incl')
            if not proceed2:
                print_lose(f"The value, {val}, is not between {lo} and {hi}! Please input that again.")
    return val



#=============================

#Doolhickeys toolchain Functions section
#This function is to print nth wildcard, like *. For example, the word Soulmate has 8 letters, therefore it prints ******** (8 stars).
def initlinedwd():
    global rannum, wordlen, singleSlotted, singleSlotted__WildCard
    wordlen = len(word)
    singleSlotted = list(word)
    singleSlotted__WildCard = '*'*wordlen
    print(singleSlotted__WildCard)
    singleSlotted__WildCard = list(singleSlotted__WildCard)
 

def PrintmoddedLinedWd():
    temp = 0
    global letter_to_be_replaced_index, singleSlotted__WildCard,word
    while (letter_to_be_replaced_index != []):
        temp = letter_to_be_replaced_index[0]
        singleSlotted__WildCard[temp] = guess
        letter_to_be_replaced_index.pop(0)
    print(''.join(singleSlotted__WildCard))


def letterPosit():
    global letter_to_be_replaced_index, guess, word
    #startPos is a local var
    startPos = 0
    #This while loop ensures all of the positions of the letter that the word contains are included
    while guess in word[startPos:]:
        startPos = singleSlotted.index(guess, startPos)
        letter_to_be_replaced_index.append(startPos)
        startPos += 1

def revealALetter():
    global singleSlotted__WildCard, word, guess
    wildcardIndex = singleSlotted__WildCard.index('*')
    guess = word[wildcardIndex]
    letterPosit()
    PrintmoddedLinedWd()

def nomination(reqDifficultyLo, reqDifficultyHi):#nomination() is to select a word that meets the criteria of (difficulty set by the player & not yet played by the player)
    global currentUser, availableWordsPool,difficultyHi,difficultyLo
    availableWordsPool = []
    reqDifficulty = list(range(reqDifficultyLo, reqDifficultyHi + 1))
    
    for i in reqDifficulty:
        cursor.execute(f"SELECT word FROM wordbank WHERE playedByUser{currentUser} = 0 AND difficulty = ?", (i,))

        results = cursor.fetchall()
        for j in results:
            availableWordsPool.append(j[0])  # Append the word itself, not the tuple
    
    if availableWordsPool:
        return random.choice(availableWordsPool)
    else:
        return None  # or handle the case when no words are available

def StreakHiScoreTotalScore():
    global currentUser, score
    score2compare = ''
    #total score
    currentUser = str(currentUser)
    conn.execute('UPDATE users SET Total_score = (SELECT Total_score FROM wordbank WHERE userID = ?) + ? WHERE userID = ?',(currentUser,score,currentUser,))
    conn.commit()
    cursor.execute('SELECT Hi_score FROM users WHERE userID = ?',(currentUser,))
    score2compare = cursor.fetchone()[0]
    score2compare = int(score2compare)
    if score > score2compare:#highest score
        conn.execute('UPDATE users SET Hi_score = ? WHERE userID = ?',(score,currentUser,))
        conn.commit()

def streakHandling():
    global lives, streak, score, currentUser, youLost
    congratWord = 'Fabulous Marvelous Wonderful Amazing Splendid Spectecular' #random congrats wordings to make the player happier
    if lives == 0:
        #Upload streak results if applicable
        print_tip(youLost)
        print_lose(f"Unfortunately, your streak is broken and reset to 0 as a result of losing the game. Your streak was {streak}.")
        streakUpload('However,')
        streak = 0
        print('')
        input("Press enter to continue.")

        gameMenu()
    else:
        streak += 1
        if score > 0:
            print(f"{random.choice(congratWord.split())} work! Your streak has been grown to {streak}!")
        else:
            print(f"Fair work, your streak is now {streak}.")
        input("Press enter to continue.")
        mainGame()
        
        

#///////////////////////////////////////////////        
#SQL retrival functions hub

def unpack_and_deliver(): #tbh, cursor.fetchone is soooo good for single data item, at least it doesn't include some branches
    results = cursor.fetchall()
    entreport = []
    for row in results:
        row = str(row)
        #The slice function used is to remove unnecessary symbols that are fetched from the SQL
        row = row[2:]
        row = row[:(len(row) - 3)]
        entreport.append(row)
    return entreport

def shiftRecords(startingPoint):
    wordbankItemCount = wordbankItemCountFun()
    if startingPoint != wordbankItemCount + 1:
        for i in range(startingPoint + 1, wordbankItemCount + 1):
            cursor.execute("UPDATE wordbank SET ID = ? WHERE ID = ?", (i - 1, i))

def wordbankItemCountFun():
    cursor.execute("SELECT COUNT (*) FROM wordbank")
    count = cursor.fetchone()[0]
    return count
    





#====================================================================
#Main programs section

def mainGame():
    global guessed, word, wordlen, singleSlotted, lives, usedHint, correctGuess, guess, singleSlotted__WildCard, str_temp1, score, currentUser, wordId, difficultyLo,difficultyHi, streakMode, streak, doYouKnowThat, youWin
    wrongLetters = []
    lives = 5
    score = 0
    usedHint = 0
    #Main game section
    word = nomination(difficultyLo,difficultyHi)
    plot_twist = f"plot twist: {doYouKnowThat[random.randint(0,4)]}"
    print_tip(plot_twist)
    if not word: #word = null
        print_win(f"Congratulations! You have gone through all of the words between level {difficultyLo} to {difficultyHi}. Consider adding your own words in the customize section or adjust the difficulty?")
        input("Press enter to continue.")
        gameMenu()
    else:
        print("Let's start the hangman game! Input 1 for a description of the word and 2 for revealing a letter in the word. Input 0 to exit to menu.")
        temp100 = (f"The difficulty of the words are in between {difficultyLo} and {difficultyHi}.")
        print_tip(temp100)
        cursor.execute("SELECT id FROM wordbank WHERE word = ?",(word,))
        wordId = cursor.fetchone()[0]
        initlinedwd()

        
        print(hangman_stages[5])
        while lives > 0:
            guess = str(input("Input one letter: "))
            guess = guess.lower()
            if len(guess) != 1:
                print("I apologize but you can merely input 1 letter or at least try to input a letter instead of leaving it blank. Try again. UwO")
            else:
                

                if guess not in singleSlotted: 
                    if guess == '2':
                        #Tip to show description
                        usedHint += 17
                        cursor.execute(f"SELECT tip FROM wordbank WHERE ID = {wordId} ")
                        str_temp1 = unpack_and_deliver()
                        print_tip(f"As per your request for a tip, it is {str_temp1[0]}. Mark has been deducted 17 for the cost of the tip." )
                    elif guess == '1':
                        #reveal a letter
                        usedHint += 11
                        print_tip(f"As per your request for a hint to reveal a letter, the letter {guess} has been inputted. Marks has been deducted for 11 for the tip.")
                        revealALetter()
                    elif guess == '0':
                        if streakMode == 1:
                            print_hi_streak(f"Your streak was {streak}.")
                            streakUpload('')

                        gameMenu()
                    elif guess in wrongLetters:
                        print_wrong(f"You have already guessed {guess}. Input another letter.")
                    elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
                        print_wrong(f"{guess} is not a valid english letter. Input a valid one.")
                    elif lives > 1: #This implies wrong guess
                        if guess not in wrongLetters:
                            wrongLetters.append(guess)
                        lives -= 1
                        print(hangman_stages[lives])
                        PrintmoddedLinedWd()
                        print_wrong(f"You have inputted, {guess}, but this is not a correct letter. Lives has been deducted for 1. You have {lives} lives now. Try again")

                        print_purple(f"The letters that you have wrongly guessed are {wrongLetters}.")
                    else: #Lost the game
                        lives = 0
                        print(hangman_stages[0])
                        print(f'I am sorry but you lost the Hangman game as a result of you have 0 lives now. The word you are trying to guess is {word}. Your score is {correctGuess}. Better luck next time!')
                        if streakMode == 1:
                            streakHandling()    
                        gameMenu()
                else: #This implies good guess
                    if guess in guessed:
                        print_wrong(f"You have already guessed this letter of {guess}, try another.")
                    else:
                        guessed += guess
                        correctGuess += 1
                        print_correct("Correct!")
                        letterPosit()
                        PrintmoddedLinedWd()
            if ''.join(singleSlotted__WildCard) == word: #Won the game
                conn.execute(f"UPDATE wordbank SET playedByUser{currentUser} = 1 WHERE id = ?",(wordId,))
                conn.commit()
                score = (lives * 17) - usedHint + correctGuess

                if score > 0:
                    print_win(youWin)
                    print_win(f"Congratulations, you nailed the word! The word '{word}' is correct! Your score is {score}.")
                    print_correct('you win!')
                    #Since it's discouraging to deduct players' marks if they failed to guess the word, the total score only acculmulates if they win with positive marks
                    StreakHiScoreTotalScore()
                    if streakMode == 1:
                        
                        streakHandling()
                    else:
                        break
                else: #Guessed the word successfully but negative/0 marks
                    print_correct(f"You get the word, {word}, right. However, your score is {score}. Don't use too much hints or tips next time!")
                    if streakMode == 1:
                        streakHandling()
                    else:
                        gameMenu()

def leaderboard():
    print('Here is the leaderboard of the players who played on this device, as well as the results of the creator')
    
    # Fetch data for registered users only, sorted by Hi_score in descending order
    cursor.execute("""
        SELECT name, Hi_score, Total_score, Hi_streak
        FROM users
        WHERE registered = 1
        ORDER BY Hi_score DESC
    """)
    
    results = cursor.fetchall()

    
    if not results:
        print("\nNo registered users found. The leaderboard is empty.")
        gameMenu()
        return

    # Print the leaderboard header
    print("\n" + "=" * 61)
    print(f"{'Rank:':<5}{'Name':<15}{'Highest Score':<15}{'Total Score':<15}{'Highest Streak':<10}")
    print("=" * 60)
    
    # Print each user's data in classy table form
    for rank, (name, hi_score, total_score, hi_streak) in enumerate(results, start=1):
        print(f"{rank:<5}{name:<15}{hi_score:<15}{total_score:<15}{hi_streak:<10}")
    
    print("=" * 60 + "\n")
    
       # Provide options after displaying the leaderboard
    print("Options:")
    print("1. Return to main menu")
    print("2. Reset leaderboard") #this causes gamer rage, you will be lashed by others if you ever dare to do this.
    
    choice = input("Enter your choice (1or2): ")
    
    if choice == '1':
        gameMenu()
    elif choice == '2':
        reset_leaderboard()
    else:
        print_wrong("Invalid command.")

def reset_leaderboard():
    confirm = input("Are you sure you want to reset the leaderboard? This action cannot be undone. (y/n): ")
    if confirm.lower() == 'y':
        cursor.execute("""
            UPDATE users
            SET Hi_score = 0, Total_score = 0, Hi_streak = 0
        """)
        conn.commit()
        print_lose("Leaderboard has been reset.")
    else:
        print("Leaderboard reset cancelled.")
    gameMenu()
    #Include highest score, streak, and sort the results



#.................................Customizing-Words subprograms zone.........................
def addWords():
    proceed1 = False #to check if can be converted into int
    proceed2 = False #to check if in range
    ownWord = ''
    ownTip = ''
    ownDifficulty = 0
    cursor.execute("SELECT word FROM wordbank")
    availableWords = (item[0] for item in cursor.fetchall())

    while (ownWord == '') or (ownWord in availableWords):
        ownWord = str(input("Input your own word: "))
        if ownWord in availableWords:
            print_wrong(f"The word {ownWord} is duplicated!")
            ownWord = '' #initialize the var before the next loop
        if ownWord == '0':
            print_hi_streak("Returning to game menu...")
            gameMenu()
            break
    while ownTip == '':
        ownTip = str(input(f"Input your own tip for the word {ownWord}: "))
    while not proceed1 or not proceed2: #if use and, if it's int, but out of range, the term disagrees with "and" or!!!!!
        ownDifficulty = input(f"Input your own difficulty for the word {ownWord}. It has to be an integer between 1 to 5: ")
        proceed1 = ctype(ownDifficulty,'int')
        if not proceed1: #cuz the program crashes if insist
            print_lose("It is not a valid integer that is between 1 & 5!") 
            continue
        proceed2 = boundary(5,1,int(ownDifficulty),'incl')
    
    cursor.execute("INSERT INTO wordbank (word, tip, difficulty, custom_word, playedByUser1, playedByUser2, playedByUser3, playedByUser4, playedByUser5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(ownWord, ownTip, ownDifficulty, True, False, False, False, False, False))
    conn.commit()
    print_correct(f"Adding the word {ownWord} done sucessfully!")
    gameMenu()

 
def deleteWords():
    ID2del = 0
    graveyard = ''
    existingID = []
    proceed1 = False
    showWordBank()
    cursor.execute("SELECT id FROM wordbank")
    existingID = [row[0] for row in cursor.fetchall()]

    while not proceed1: #if use and, if it's int, but out of range, the term disagrees with "and" or!!!!!
        ID2del = input("Input the word's ID in order to delete the entire record of the word.")
        proceed1 = ctype(ID2del,'int')
        if not proceed1: #cuz the program crashes if insists
            print_wrong("The ID provided is not a valid Integer ID.")
            continue
    ID2del = int(ID2del)
    if ID2del not in existingID:
        if ID2del != '0':
            print_hi_streak("The ID doesn't exist!")
            gameMenu()
        else:
            print("Returning to game menu...")
            gameMenu()
            

    cursor.execute("SELECT word FROM wordbank WHERE ID = ?", (ID2del,))
    graveyard = unpack_and_deliver()
    cursor.execute(f"DELETE FROM wordbank WHERE ID = {ID2del}")
    conn.commit()
    print_correct(f"The word {graveyard} has been deleted sucessfully")
    shiftRecords(ID2del)
    gameMenu()

def showWordBank():
    cursor.execute("SELECT id,word,tip,difficulty FROM wordbank ORDER BY difficulty ASC")
    print("The following is a table of the word bank.")
    print("[ID]=====[Word]=====[Tip]======[difficulty]")
    results = cursor.fetchall()
    for row in results:
        print(row)
    print('')
    
def editWords():
    showWordBank()
    difficulty2change = '0'
    id2change = 0
    proceed1 = False
    proceed2 = False
    print_tip("Keep the input, (word/tip/difficulty) below blank if you don't want to do any modification to them.")
    
    while (not proceed1) or (not proceed2):
        id2change = input("Input the ID of the word that is to be changed. ")
        proceed1 = ctype(id2change,'int')
        if not proceed1:
            if id2change != '0':
                print_lose("The id is not an integer! Input that again.")
                continue
            else:
                print("Returning to game menu...")
                gameMenu()
        id2change = int(id2change)
        proceed2 = boundary(wordbankItemCountFun(),1,id2change,'incl')
        if not proceed2:
            print_lose(f"The ID, {id2change} doesn't exist!")
    cursor.execute("SELECT word, tip, difficulty FROM wordbank WHERE id = ?", (id2change,) )
    originalRecord = cursor.fetchone()

    word2change = str(input("Input the word that you want to replace it. "))
    if word2change == '':
        word2change = originalRecord[0]
    tip2change = str(input("Input the new tip for the word"))
    if tip2change == '':
        tip2change = originalRecord[1]

    difficulty2change = InclRangeCheck("Input its new difficulty. The value must be inbetween 1 and 5. ",5,1,True)    
    if difficulty2change == '':
        difficulty2change = originalRecord[2]
        difficulty2change = int(difficulty2change)
    difficulty2change = int(difficulty2change)    
    
    cursor.execute("UPDATE wordbank SET (word,tip,difficulty,custom_word) = (?,?,?,?) WHERE id = ?",(word2change,tip2change,difficulty2change,True,id2change,))
    conn.commit()
    cursor.execute("SELECT word,tip,difficulty FROM wordbank WHERE id = ?", (id2change,))
    display = cursor.fetchone()
    print_correct(f"The record has been changed and customized sucessfully. The new record for the word, tip and difficulty are {display} respectfully.")
    gameMenu()

#=============================Accounts System Subprograms=============================#
def loginScreen():
    global str_temp1, currentUser, logreg, hm_adv
    detcurrentUser = 0
    availableSlots = []
    currentUser = 0
    i = 0
    print_hi_streak("Hangman Game Login Menu")
    print_correct(hm_adv)

    print_tip(logreg)
    cursor.execute('SELECT name FROM users ORDER BY userid ASC')
    print('=' * 45)
    print("Players List:")
    results = cursor.fetchall() 
    for row in results:
        i += 1
        row = ''.join(row)
        print_purple(f"Gameplay Saving Slot {i}: {row}")
    while True: #Fatal input handling
        currentUser = input("Input the slot code(1-5) to login or register the gameplay slot: ")
        try:
            currentUser = int(currentUser)
            if currentUser < 1 or currentUser >5:
                print_wrong("Error: It has to between 1 and 5")
            else:
                break
        except ValueError:
            print_wrong("Error: It has to be an integer, in which an ID representing your username or the unregistered slot.")



    cursor.execute("SELECT registered FROM users WHERE userid = ?", (currentUser,))
    detcurrentUser = int(cursor.fetchone()[0])
    if detcurrentUser == 0:
        Playerregister()
    else:
        Playerlogin()



def Playerlogin():
    global currentUser, currentUserName
    failCount = 0
    print_tip("Input just 0 in password slot to get back to the login menu.")
    while True:
        cursor.execute("SELECT password FROM users WHERE userid = ?",(currentUser,)) #get text to be decrypted
        text2dec = cursor.fetchone()
        text2dec = str(text2dec[0])
        cursor.execute("SELECT name FROM users WHERE userid = ?",(currentUser,))
        currentUserName = cursor.fetchone()
        Inputted_password = ''
        while len(Inputted_password) < 8:
            Inputted_password = getpass(f"Hello {currentUserName[0]}, please input your password: ")
            if len(Inputted_password) < 8:
                if Inputted_password == '0':
                    loginScreen()
                    break
                else:
                    print_wrong("Error: The password must be at least 8 letters long. Please try again.")
        Inputted_password = str(Inputted_password)
        if  "ABCdef" == decABC(Inputted_password,text2dec):
            print_win(f"Welcome {currentUserName[0]} to the hangman game!")
            gameMenu()
            break
        else:
            print_wrong("Invalid password, please try again.")
            failCount += 1
            if failCount == 5:
                print_lose("You have inputted the password wrongly for too many times, please try again it later. You are now temporaily blocked from logging in for 5 minutes.")
                time.sleep(300)
                loginScreen()
                break    

def Playerregister():
    global currentUser, currentUserName, hm_adv
    encrypted_text = ''
    desiredName = ''
    pw2ndChance = ''
    subprocess.run(["python3","encABC.py"])
    while True:
        while True:
            if len(desiredName) <5:
                desiredName = str(input("Input your desired user name for the hangman game. It should not overlap with others' name and it's length should larger than 5.."))
            else:
                break
            print_wrong("The user name is too short!")
        try:
            cursor.execute("UPDATE users SET name = ? WHERE userid = ?",(desiredName,currentUser,))
            conn.commit()
            break
        except sqlite3.IntegrityError:
            print_wrong("Invalid user name input. It MUST be unique. Try again.")
    while True:
        desiredPw = getpass("Please input your password.")
        desiredPw = str(desiredPw)
        if (len(desiredPw) > 8) or (len(desiredPw) <4):
            print_wrong("The password you are creating must be between 4 to 8 characters long. Please input again")
        else:
            while True:
                pw2ndChance = getpass("Please input the password again for password verification.")
                if not pw2ndChance == desiredPw:
                    print_lose("password doesn't match, try again.")
                else:
                    break

                print_wrong("Password doesn't match, please input again.")
            encrypted_text = enc(desiredPw)
            cursor.execute("Update users SET (password,registered) = (?,?) WHERE userid = ?",(encrypted_text,True,currentUser,))
            conn.commit()
            currentUserName = list(currentUserName)
            currentUserName = currentUserName.append(desiredName)
            print_tip(hm_adv)
            print_purple(f"Registration sucessful. Welcome {desiredName} to this hangman game and deep dive into this marvelous rabbit hole!")
            gameMenu()
            break

#...................................................................
#Start of party, aka menu
def gameMenu():
    global currentUserName, difficultyHi, difficultyLo, streak, streakMode, customization
    streakModeDisplay = ['enable','disable']
    print('=' * 61)
    print_purple("Hangman Game Game Menu:")
    print(f"What actions would you like to do now? \n P: Play Now.\n S: {streakModeDisplay[streakMode]} the Streak Gamemode now. (It is now {streakModeDisplay[abs(streakMode - 1)]}d.) \n L: Leaderboard. \n C: Customize your wordbank. \n H:Help and Instructions. \n D: Difficulty adjusting \n B:Bye Bye and logout ")
    print('=' * 61)
    action = str(input())
    action = action.lower()
    action += '0'
    action = action[0]
    print('')
    print('===========================================')
    print('')
    if action == 'p':
        mainGame()
    elif action == 's':
        if streakMode == 1:
            streakMode = 0 #disable streak mode
        elif streakMode == 0:
            streakMode = 1 #enable streak mode
    elif action == 'l':
        leaderboard()
        print('')
    elif action == 'h':
        print_tip(''' 
            The tutorial for the Hangman Advanced Game:
            In order to use a hint by revealing a random letter in the word, input the number 1. This costs you 11 marks. 
            In order to use a tip by giving you the description of the word, press 2. This costs you 17 marks. 
            In vocab levels, level 1,2,3,4,5 are designated for S1,S2,S3,S4,S5 students respectively.
            You can add, edit and delete the words in the word bank in the Customize Your Wordbank.


    ''')
        print('press enter to return to game menu.')
        input()
        gameMenu()
    elif action == 'c':
        print_tip(customization)
        print_hi_streak("Let's customize the words in the wordbank now! You can add your own new words (along with their tips, difficulty), delete the words, as well as edit all the words! ")
        print_purple("You can always return to the game menu by inputting 0 on the first question prompt if customizing anything is not your favor.")
        print('''
    What actions would you like to do now?
    A: Add your own words.
    E: Edit the words inside the wordbank
    S: Show the wordbank
    D: Delete the words inside the wordbank.
    R: Return to game menu                    
            ''' 
            )
        action = str(input())
        action = action.lower()
        action += '0'
        action = action[0]
        
        if action == 'a':
            addWords()
        elif action == 'd':
            deleteWords()
        elif action == 's':
            showWordBank()
        elif action == 'e':
            editWords()
        elif action == 'r':
            gameMenu()
        else:
            print_wrong("Invalid command,")
    elif action == 'b':
        try:
            print(f"See you soon, {currentUserName[0]}~ :3")
        except TypeError:
            print("See you soon! Bye!")
        loginScreen()
    elif action == 'd':
        #Difficulty adjusting
        print('=' * 61)
        print("Let's adjust your desired difficulty of the words in this section.")
        print(f"Currently, the word's difficulty is between {difficultyLo} and {difficultyHi}.")
        go_on = False
        while go_on == False:
            temp1 = input("What is your desired lowest difficulty? It has to between 1 and 5: ")
            go_on = fatalInputHandling_Integer(temp1,1,5)
        difficultyLo = int(temp1)
        go_on = False
        while go_on == False:
            temp1 = input("What is your desired highest difficulty? It has to between 1 and 5: ")
            go_on = fatalInputHandling_Integer(temp1,1,5)    
        difficultyHi = int(temp1)
        print_correct(f"Difficulty has been adjusted successfully! The new difficulty of the words is between {difficultyLo} and {difficultyHi}!")
        input("Press enter to return to game menu.")
        print('=' * 61)
        gameMenu()
    
    elif action == "o":
        print("Options")
    else:
        print_wrong("Invalid command.")
    gameMenu()








currentUser = 1
score = 100
StreakHiScoreTotalScore()
loginScreen()
gameMenu()


#wasted code crate
'''
#cursor.execute("SELECT COUNT (*) FROM wordbank")
    #wordbankItemCount = cursor.fetchone()[0]
    #print(wordbankItemCount)
    #rannum = random.randint(1,wordbankItemCount)
   # cursor.execute(f"SELECT word FROM wordbank WHERE ID = {rannum}")
    #word = unpack_and_deliver()

'''