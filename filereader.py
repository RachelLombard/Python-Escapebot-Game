from random import randint

#Rachel Lombard
#Student ID: 121705031

'''
code to focus on inheritance allows to define a class that inherits all its methods
and properties from another class
'''
#In this case, the parent class is Filereader
#The child class, question file reader inherits the parents methods

#Parent class
class FileReader:

    def __init__(self, filename):
        self.__filename = filename #private instance variable
        print("instance of FileReader class created!")
    
    def read_all(self):
        try:
            file_1 = open(self.__filename)
            lines = file_1.readlines()
            file_1.close()
            return lines
        except:
            print("file not opened. Terminating method")
            return False


    def line_count(self):
        lines = self.read_all()
        line_amount = len(lines)
        return line_amount   


    def get_filename(self):
        return self.__filename

    def set_filename(self, new_filename):
        self.__filename = new_filename 

    file = property(get_filename, set_filename)


'''
Creating questionfilereader class which reads contents from a file and converts it
into a specified dictionary format. It extends upton the Filereader class. 
Returns a set of questions in a format that will be readable by the Escapebot class
'''
#created child class 
#added super() to method override 
#self.__filename is a private instance variable
class QuestionFileReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)
        self.__filename = filename 
        print("Instance of QuestionFileReader class created!")

    
#created string representation to give information about object in a user friendly way
    def __str__(self):
        desc = "File Name: %s" % (self.__filename) 
        return desc



    '''
    method to read entire comments from file specified apart from line number 0
    converts content to nested dictionary format
    '''
    #for loop for data list 
    #gets length of data
    #once done, split into another list 
    #removed the \n as it was appearing from text file 
    #storing each data into question, stimulus and answers
    #adding to another dictionary and storing in key values question, stimulus, answers
    #data_as_list has value of 0-7 indexes within the list, gets all of the possible answers 
    #stores within the inner dictionary, each are then assigned to question, stim, ans
    #question dict i = question 1, creates the key value and would store inner_dict within the key value
    #if i is equal to 0 then break 

    def all_dictionary_questions(self):

        question_dict = {}
        data = self.read_all() #inherited this method 

        for i in range(len(data)): 
            if i == 0:
                continue
            else:
                data_as_list = data[i].rstrip("\n").split(",")

                question = data_as_list[0]
                stimulus = data_as_list[1]
                answer = data_as_list[2:len(data_as_list)] #changed this from previous feedback, so it is not hardcoded

                inner_dict = {}
                inner_dict["question"] = question #changed to lower case
                inner_dict["stimulus"] = stimulus
                inner_dict["answers"] = answer

                question_dict[i] = inner_dict

        return question_dict


    '''
    method to return questions, stimuli and answers in dictionary format at the line numbers 
    specified in the list 
    '''
    #getting input value of line_nums_list,
    #checking for values within the list, 
    #assigning to data 
    #continuing format as above
    def lines_as_dictionary(self, line_nums_list): 

        question_dict = {}
        data = self.read_all()
        
        index_num = 1

        for i in line_nums_list:
            
            data_as_list = data[i].rstrip("\n").split(",")
            
            question = data_as_list[0]
            stimulus = data_as_list[1]
            answer = data_as_list[2:len(data_as_list)] #changed thisso that it is not hardcoded
            
            inner_dict = {}
            inner_dict["question"] = question
            inner_dict["stimulus"] = stimulus
            inner_dict["answers"] = answer
        
            question_dict[index_num] = inner_dict #changed this so that the questions start from 1 and move incrementally by 1 
            index_num += 1
            
        return question_dict



    '''
    method to read from a range of values from the file from a given line range
    returns questions, stimuli and answers in dictionary format
    '''
    #passing in the range, e.g between 1-6, would give values between 1,2,3,4,5
    #looping through range, i is taking value
    #putting data in the list
    #again removed the \n
    def get_dictionary_range(self, ran):
        
        question_dict = {}
        data =self.read_all()
        
        index_num = 1 #added this


        for i in range(ran[0], ran[1]):

            data_as_list = data[i].rstrip("\n").split(",")

            question = data_as_list[0]
            stimulus = data_as_list[1]
            answer = data_as_list[2:len(data_as_list)] #changed this from previous feedback
            
            inner_dict = {}
            inner_dict["question"] = question
            inner_dict["stimulus"] = stimulus
            inner_dict["answers"] = answer
        
            question_dict[index_num] = inner_dict
            index_num += 1 #increments by one, into the value

        return question_dict
        

    '''
    method to read lines from the file from a random line range 
    converts content to nested dictionary format and its contents
    '''   
    #looping while true
    #if start value is less than stop, then it will keep going back in
    #using start stop value for ranges
    #again removed the \n
    def random_dictionary_questions(self): #changed this code in this method per feedback given, seperated while loop from the for loop
        question_dict = {}
        data =self.read_all()
        index_num = 1
        start = 0
        stop = 0

        while True:

            start = randint(0, len(data))
            stop = randint(0, len(data))

            if start < stop:
                break

        for i in range(start, stop):
            if i == 0:
                continue
            else:
                data_as_list = data[i].rstrip("\n").split(",")

                question = data_as_list[0]
                stimulus = data_as_list[1]
                answer = data_as_list[2:len(data_as_list)] #changed this from previous feedback

                inner_dict = {}
                inner_dict["question"] = question
                inner_dict["stimulus"] = stimulus
                inner_dict["answers"] = answer

                question_dict[index_num] = inner_dict #changed this from previous feedback
                index_num += 1

        return question_dict


    '''
    method to return the text in the file in dictionary format, excluding specific question locations
    '''
    #similar to if i == 0 contine, above 
    #if i is in line_nums_list then skip, and goes onto the next number
    #wont go into loop
    #following same format as above
    def exclude_dictionary_questions(self, line_nums_list):
        question_dict = {}
        data =self.read_all()
        
        index_num = 1

        for i in range(len(data)):
            if i == 0 or i in line_nums_list:
                continue
            else:
                data_as_list = data[i].rstrip("\n").split(",")
   
                question = data_as_list[0]
                stimulus = data_as_list[1]
                answer = data_as_list[2:len(data_as_list)] #changed this 
                
                inner_dict = {}
                inner_dict["question"] = question
                inner_dict["stimulus"] = stimulus
                inner_dict["answers"] = answer
            
                question_dict[index_num] = inner_dict #changed this 
                index_num += 1
        
        
        return question_dict

    
    '''
    method to return text and associated answers in the file, excluding the range
    specified in the list
    '''
    #similar to code above but just with question range
    #did error exception
    def exclude_dictionary_range(self, questions_range):
        try: 
            question_dict = {}
            data = self.read_all()
            
            index_num = 1 #added this 

            for i in range(len(data)):
                if i == 0 or i in range(questions_range[0], questions_range[1]+1): #doesnt account for the last value 
                    continue
                else:
                    
                    data_as_list = data[i].rstrip("\n").split(",")

                    question = data_as_list[0]
                    stimulus = data_as_list[1]
                    answer = data_as_list[2:len(data_as_list)] #changed
                    
                    inner_dict = {}
                    inner_dict["question"] = question
                    inner_dict["stimulus"] = stimulus
                    inner_dict["answers"] = answer
                
                    question_dict[index_num] = inner_dict       
                    index_num += 1 
            
            return question_dict
        except: 
            return "Oops, error"


    #method added for the second feature 
    #getting a random question from the dictionary 
    #used to ask the user a question to gain an extra life 
    def single_question(self):
        data = self.read_all() #using inheritance to call the read_all method f

        data_as_list = data[randint(1, len(data)-1)].rstrip("\n").split(",")

        question = data_as_list[0]
        stimulus = data_as_list[1]
        answer = data_as_list[2:len(data_as_list)]

        inner_dict = {}
        inner_dict["question"] = question
        inner_dict["stimulus"] = stimulus
        inner_dict["answers"] = answer

        return inner_dict

        



