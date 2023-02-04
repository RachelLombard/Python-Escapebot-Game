from filereader import QuestionFileReader
from bot import EscapeBot

#Rachel Lombard
#Student ID: 121705031

#Methods are being called in the main.py

#first feature - 
#asks the user when they get a question wrong if they would like to change their questions, 
#if yes, a menu will appear with different options for the user to choose from
#(note - these options are methods that were from filereader.py)
#they must enter in a number which correlates with the option
#they will then recieve a question
#amount of lives will stay the same 
#if they choose no, the current question that they were currently on will be asked again 

#second feature - 
#when the user has one life remaining, a question will be asked if they would like to answer another question and gain back a life
#will gain back a life if they get the answer correct
#if they get the answer wrong, they will lose the game as they were currently at 1 life remaining 
#added some new methods for both features but also inherited other methods from bot.py and filereader.py


#String representation information here
Name_of_file = QuestionFileReader("Instance of QuestionFileReader class, this class is used to read contents from python game text file and convert into a dictionary format")
print("Information about object:", Name_of_file.get_filename()) #changed this to call all parent methods


#First added feature
#Method to call an interactive menu for users to change their nested dictionary of choice
def dict_menu():
    #asks the user do they want to change their group of questions
    dict_choice = input("Would you like to change your questions?(y/n) \n")
    #while the choice is not = "n" or "N", then the menu loops
    #if N is entered then loop is broken and game continues where it left off
    while dict_choice.lower() != "n":
        print("Choose below how you would like to generate your questions. ")
        print("1. Specific question indicated by line number")
        print("2. Range of questions")
        print("3. Randomly generated questions")
        print("4. Exclude specific question indicated by line number")
        print("5. Exclude a range of questions")
        choice = input("Please choose which option you want for generating your questions (1-5): \n")
        #checks to see what choice is = to and changes nested dictionary of question based on choice
        #if choice is not equal to 1 - 5, then the user is asked to input a correct answer
        #n or N will break the loop and game will continue
        if choice == "1":
            input_list = []
            input_list = [int(item) for item in input("Enter the list items: ").split()] 
            EscapeBot("Zoey", 3, question_file_reader.lines_as_dictionary(input_list))
            break
        elif choice == "2":
            input_list = []
            input_list = [int(item) for item in input("Enter the 2 item list: ").split()]
            EscapeBot("Zoey", 3, question_file_reader.get_dictionary_range(input_list))
            break
        elif choice == "3":
            EscapeBot("Zoey", 3, question_file_reader.random_dictionary_questions())
            break
        elif choice == "4":
            input_list = []
            input_list = [int(item) for item in input("Enter the item list: ").split()]
            EscapeBot("Zoey", 3, question_file_reader.exclude_dictionary_questions(input_list))
            break
        elif choice == "5":
            input_list = []
            input_list = [int(item) for item in input("Enter the 2 item list: ").split()]
            EscapeBot("Zoey", 3, question_file_reader.exclude_dictionary_range(input_list))
            break
        else:
            print("%s is not an option. Please choose an option between 1-5 to continue..." % choice)
            dict_menu()
            break
        

#Created an object instantiation
question_file_reader = QuestionFileReader("python-game-file.txt")
escape_bot = EscapeBot("Zoey", 3, question_file_reader.all_dictionary_questions()) 


#Parent methods
#print(question_file_reader.read_all())
#print(question_file_reader.line_count())
#print(question_file_reader.get_filename())



print("Information about object:", escape_bot) 
escape_bot.draw("Bot") #calling the previous method above to display the robot in the console
escape_bot.display_name() 

in_play = False
user_in = input("Press Y to continue. Any other key quits the game!\n")

if user_in.lower() == "y":
    in_play = True

#using object variables to call its methods while game is in process 
while in_play:
    escape_bot.display_lives()
    escape_bot.display_position()
    escape_bot.current_question()
    user_input = input("What is your guess? Type the answer here\n")

    if escape_bot.check_answer(user_input) == True:
        no_questions_left = escape_bot.increment_position()
        if no_questions_left == True:
            in_play = False
    else:
        no_lives_left = escape_bot.decrement_lives() #take a life and reveal the answer if the gamer gets a question wrong 
        escape_bot.reveal_answer()
        #First added feature continued
        #checking if the lives remaining are = 2 
        #if they are then the interactive menu is called
        if escape_bot.get_lives() == 2:
            dict_menu()
        #second feature here
        #getting user input, checking if its equal to y
        #calling display extra function, question asks to gain a life 
        #asking user to enter answer to the question
        #checking to see if check answer function 
        #checking if whats being returned is true, if it is, return a life
        #if not, removing a life and game over 
        elif escape_bot.get_lives() == 1:
            gamba_choice = input("Would you like to try answer another question to gain back a life?(y/n) \n")
            if gamba_choice.lower() == 'y':
                extra_question = question_file_reader.single_question()
                escape_bot.display_extra_question(extra_question)
                user_input = input("What is your guess? Type the answer here\n")

                if escape_bot.check_extra_answer(extra_question, user_input) == True:
                    escape_bot.set_lives(1)
                    
                else:
                    no_lives_left = escape_bot.decrement_lives()
                    if no_lives_left == False:
                        in_play = False
        else:
            in_play = False
     
    
print("\n"*4)
escape_bot.draw("Bot")
escape_bot.terminate_message()

