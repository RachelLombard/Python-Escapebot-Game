#Name: Rachel Lombard
#Student ID: 121705031

import random 

class EscapeBot:

    #constructor to allow creation of objects and making objects ready to use 
    #below are instance variables which are unique to each object 
    #instance variables refer to the object that is instantiated 
    def __init__(self, name, lives, questions):
        self.name = name #changed this to 'name' to support reusability
        self.position = 1 #decided to keep position as 1 as it is easy to follow and is simple to understand
        #1 is a good starting number and is a good place to begin if a player makes a mistake
        self.goodbye = "Thank you for playing the Escape Room Game!"
        self.lives = lives #changed lives amount to allow resuability as future coders may not want 3 lives to be hardcoded
        self.questions = questions

    #creating setter and getter
    #getter is a method that gets values
    #setter is a method that sets values 
    #setting and getting the bots name 
    #creating properties, can now access the get_name and set_name method using the name variable
    def get_name(self): 
        return self.name 

    def set_name(self, new_name):
        if type(new_name) == str: 
            self.name = new_name

    names = property(get_name, set_name)


    #setting and getting the goodbye message 
    #creating properties, can now access the get_goodbye and set_goodbye method using the message variable
    def get_goodbye_message(self): 
        return self.goodbye 

    def set_goodbye_message(self, new_goodbye):
        if type(new_goodbye) == str: 
            self.goodbye = new_goodbye

    message = property(get_goodbye_message, set_goodbye_message)


    #string representation to give information about the object in the output 
    #this can be changed in future code, allows flexibility and reusability
    #created local variable desc as it is declared inside of the function 
    def __str__(self): 
        desc = "Robot. Name: %s, Position: %s, Total lives: %s" % (self.name, self.position, self.lives)
        return desc 
        

    #added draw method and format to display within the console 
    #In this code, "Bot" will be displayed when it is recalled 
    #can add more pictures and name it something else to make it more resusable for future coding 
    #this method is called to the display the bot picture in different sections
    #for example, it is called at the beginning and end of the game so that there is a friendly face when the gamer starts and finishes!
    def draw(self, display):
        if display == "Bot": 
            print("\n") 
            print("     %s      " % (self.name)) 
            print("||----------||")
            print("||  ^     ^ ||")
            print("||     *    ||")
            print("||  \/\/\/  ||")
            print("||----------||")
            print("\n")

           

    #method to display name and instructions 
    #made the name reusable so that any other coder can rename the Robot, recalling self.name
    #added instuctions to this method as just having one line of code to display only the name seemed counter intuitive 
    def display_name(self):
        print("Hi, my name is %s the Robot! Welcome and enjoy the game..\n""I am on a mission.\nI must retrieve the key to open this safe in front of me!\nBut only you can help me...\nYou must help me get the answers to these questions correct before I run out of lives.\nOnly then will I be able to retrieve the key to open the safe!\n" % self.name)
    
    #method to show how many lives are remaining, this can be changed it is not hardcoded
    def display_lives(self):
        print("You have %s lives remaining..." % self.lives)


    #Getter and setter for self.lives
    #creating property to allow inheritance access to getter and setter across files
    #needed to create setter and getter to access self.lives in main 
    def get_lives(self):
        return self.lives
    
    def set_lives(self, extra_life):
        # if type(new_lives) == int:
        #     self.lives = new_lives
        #     new_lives += i
        self.lives += extra_life
    
    #lives2 = property(get_lives, set_lives)


    #method added for the second feature
    #displays extra question for the user to answer, to gain back a life 
    def display_extra_question(self, extra_question):
        questions_at_pos = extra_question["question"] #getting position and question
        stimulus_at_pos = extra_question["stimulus"] #getting position and stimulus
        answers_at_pos = extra_question["answers"] #getting position and answers 
        random.shuffle(answers_at_pos)
        answer_str = ", ".join(answers_at_pos)
        return print("The next question is...\n\n%s\n\n>>> %s\n\nChoose one of the possible answers:\n\n%s\n" % (questions_at_pos, stimulus_at_pos, answer_str), sep="")


    #method added for the second feature 
    #checks answer of the question that was asked to gain back a life 
    def check_extra_answer(self, extra_question, response):
        response = response.lower().strip(" ")

        if str(response) == extra_question['answers'][0]:
            print("That answer is correct! Well done!")
            return True
        else:
            print("That answer is incorrect! Try again...")
            return False


    #function to increment questions by 1, getting the amount of total questions inside the dictionary
    #checking to see if it is greater than amount of questions, if it is, 
    #code is pushing it back so that the questions position will only ever be equal to the bigger number
    def increment_position(self):
        self.position = self.position + 1
        total_questions = len(self.questions) #added to class to make sure it can be reused as questions can be more or less than 5 
        if self.position > int(total_questions):
            self.position = self.position - 1
            return True
        else:
            return False


    #method to reveal the answer to the user when the gamer gets the answer wrong, the correct answer will show 
    #added some formatting when showing the correct answer. It will show the correct answer that correlates with its question thats in the dictionary
    #just a note that the answer amounts are not set, there can be multiple answers 
    def reveal_answer(self):
        correct_answer = "Q%s: %s" % (self.position, self.questions[self.position]["answers"][0])
        print("The correct answer for: %s\n" % correct_answer)
    

    #function to display position, inside of the method there is self.position which is being called
    #from the constructor, this again can be changed depending on the games position to promote reusability 
    #i.e not hardcoded 
    def display_position(self):
        print("you are now at position %s " % self.position)



    #method to show the questions, stimulus and answers to the console
    #getting position in the list and printing out nested list from the questions dictionary
    #going to each key and storing it into a variable 
    def current_question(self): 
        questions_at_pos = self.questions[self.position] ["question"] #getting position and question
        stimulus_at_pos = self.questions[self.position] ["stimulus"] #getting position and stimulus
        answers_at_pos = random.sample(self.questions[self.position] ["answers"], len(self.questions[self.position] ["answers"])) #getting position and answers 
        #had to create a copy of the list for answers, to be able to show the correct answer to question layout, for example, 'the correct answer for Q1: 3' 
        #randomizing answers below with random shuffle, used the import random 
        #there will be a different answer layout each time a question is asked 
        random.shuffle(answers_at_pos)
        #turning the answers from a list to a string to have user friendly interface/format 
        answer_str = ", ".join(answers_at_pos)
        #printing and formatting to the console 
        return print("The next question is...\n\n%s\n\n>>> %s\n\nChoose one of the possible answers:\n\n%s\n" % (questions_at_pos, stimulus_at_pos, answer_str), sep="") 
       

    
    #method to check the user inputs answer taken from the console
    def check_answer(self, response):
        #making sure that responses that have capitalisation and spaces in them doesn't matter
        #will take user input  
        response = response.lower().strip(" ")
        #checking the first question which is at position 0, 
        #if it equals the right answer then return the correct message
        #if not, then print the wrong answer message
        #code is checking if the answers that are given are true or false
        #this is not hardcoded to allow for resusability as the number of questions or answers can be changed
        for key in self.questions:
            if self.position == key:
                if str(response) == self.questions[key]['answers'][0]:
                    print("That answer is correct! Well done!")
                    return True
                else:
                  print("That answer is incorrect. Try again.")
                  return False
        

    #method to check that the nested dictionary is in the correct format
    def set_questions(self, new_questions):
        #str1 and str2 local variables created to make code more resusable and flexible
        #added str1 and str2 so that they can be called in the code further down 
        #Changed this as sentence structure was too long for the lines of code 
        str1 = "Questions must be of type dictionary (nested). Questions not reset."
        str2 = "Questions are not in the correct format. Questions not reset"

        #checking to see if questions are in the correct format before it asks the question
        #making sure its a nested dictionary 
        if type(new_questions) != dict:
            print(str1)
            return
        #checking to see if position is a digit, if it is an int, continue
        #if not, return not in the correct format message 
        for key in new_questions:
            if str(key).isdigit() == False:
                print(str2)
                return
        #examining each questions, checking the keys inside
        #if not a nested dict, incorrect format message will show 
            else:
                keys = new_questions[key]
                if type(keys) != dict:
                    print(str1)
                    return
                if len(keys) != 3:
                    print(str2)
                    return -1
        #checking that question in the correct format before it is asked 
                if "question" not in keys and "answers" not in keys and "stimulus" not in keys:
                    print(str2)
                    return
        print("questions reset!")    
        self.questions = new_questions

    #resetting the position of the gamer, starts at the first position which is 1
    def reset(self): 
        reset_pos = self.position = 1
        return reset_pos


    #method to take away a life every time the gamer gets a question wrong
    #if answer is incorrect, decrement lives and stay at question
    #if correct, move onto the next question 
    #used self lives to call how many lives are left 
    #two formats, if the gamer loses all lives then game is over
    #if they get a question wrong then reduce a life 
    def decrement_lives(self): 
        if self.lives == 1:
            self.lives = self.lives - 1
            print("You have lost a life. You have %s lives left, Game Over!" % (self.lives))
            return False
        else:
            self.lives = self.lives - 1
            print("You have lost a life. You have %s lives left!" % (self.lives))
            return True

    def increment_lives(self): 
        if self.lives == 1:
            self.lives = self.lives + 1
            print("You have lost a life. You have %s lives left" % (self.lives))
            return True
    

    #added terminate message to inform user at the end, combined three methods as one, into the terminate_message. added in terminate and finished_game
    #goodbye message is being recalled from __init__ 
    def terminate_message(self): 
        print("All questions have now been played!\nThe escape room game is now being terminated! %s\n" % (self.goodbye))

