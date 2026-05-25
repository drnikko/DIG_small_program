# ------------------------------------------------------------------------------------------
#       Title: Experimenting with To Do List for DIG
#       Name: Kiersten Conley
# ------------------------------------------------------------------------------------------

# THINGS I NEED TO FIGURE OUT 
# capitalization
# differences in time (12am, verses 24:00, verses midnight, etc)
# organizing things in order of time

def createToDo(day: str, time: str, category: str, description: str) -> dict: 
    """ This function takes the information of day, time, category, and description (all as strings) and makes a dictionary with the following keys: 'day', 'time', 
    'category', and 'description'. 
    :param day: (str) Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    :param time: (str) Time of day 
    :param category: (str) Category of a task (ex: User might put a homework task into a catgory called 'school')
    :param description: (str) User's description of the to do task 
    :return: (dict) Returns a dictonary holding the information of the to do list 
    >>> createToDoList("Monday", "12pm", "Yardwork", "Water the garden")
    {'day': 'Monday', 'time': '12pm', 'category': 'Yardwork', 'description': 'Water the garden'}
    """
    todo_dictionary:dict = {} # creating dictionary that stores the to do list 
    # creating keys for values that the user will input
    todo_dictionary["day"] = day 
    todo_dictionary["time"] = time 
    todo_dictionary["category"] = category 
    todo_dictionary["description"] = description
    return todo_dictionary # returns the to do list

def addTask(todo_list: list, task: dict) -> None: 
    """ This function adds a task to the to do list 
    :param todo_list: (list) List of to do tasks 
    :param task: (dict) An individual task 
    >>> myToDo = [{'day': 'Monday', 'time': '12pm', 'category': 'Yardwork', 'description': 'Water the garden'}, {'day': 'Wednesday', 'time': '11:59pm', 'category':
    'School', 'description': 'SDS assignment due'}]
    >>> newTask = {'day': 'Sunday', 'time': '10am', 'category': 'Family', 'description': 'Brunch with Mom'}
    >>> addTask(myToDo, newTask)
    [{'day': 'Monday', 'time': '12pm', 'category': 'Yardwork', 'description': 'Water the garden'}, {'day': 'Wednesday', 'time': '11:59pm', 'category': 'School', 
    'description': 'SDS assignment due'}, {'day': 'Sunday', 'time': '10am', 'category': 'Family', 'description': 'Brunch with Mom'}]
    """
    todo_list.append(task)

def removeTask(todo_list: list, index: int) -> None: 
    """ This function removes a task from the to do list 

    """
    if index in range (1, len(todo_list) - 1): # Checks if the task exists while translating from the user input to index notation
        remove_this_task = todo_list[index -1 ] # Picks the task that is getting removed
        todo_list.remove(remove_this_task) # Removes the task from the to do list
    else: 
        print("This task does not exist.") # If the task does not exist

def viewList(todo_list: list) -> list: 
    """ This function shows the user to do list 
    :param todo_list: (list) A list of to do tasks
    :return: (list) List of specific tasks
    >>> myToDo = [{'day': 'Monday', 'time': '12pm', 'category': 'Yardwork', 'description': 'Water the garden'}, {'day': 'Wednesday', 'time': '11:59pm', 'category':
    'School', 'description': 'SDS assignment due'}]
    >>> viewList(myToDo)
    [{'day': 'Monday', 'time': '12pm', 'category': 'Yardwork', 'description': 'Water the garden'}, {'day': 'Wednesday', 'time': '11:59pm', 'category':
    'School', 'description': 'SDS assignment due'}]
    """
    return(todo_list) # I want them to be sorted by day and time

def main() ->  None: 
    """ This function handles user inputs and operations for the to do list 
    """
    option = ""
    todo_list = []
    
    initial = str(input("Do you want to use your to do list?:")).upper
    if initial != "YES":
       option = "QUIT"
    else:
        # the set up of the to do list is incorrect but idk why atm
        todo_list = createToDoList() # figure this out (related to red scribbles under if statement) 
    
    while option != "QUIT":
        option = input("Select an option (ADD, REMOVE, SHOW LIST: ").upper()        

        if option == "ADD":
            todo_list["day"] = day 
            todo_list["time"] = time 
            todo_list["category"] = category 
            todo_list["description"] = description
            task_entry = createToDo(day, time, category, description)
            addTask(todo_list,task_entry)

    # everything below this is from Alicia's HW 7 
    
    elif option == "REMOVE":
      index = int(input("Which # would you like to remove? "))
      removeBook(library, index)
        
    elif option == "PRINT":
      printLibrary(library)
        
    elif option == "TITLES":
      titles = getTitles(library)
      for item in titles:
          print(item, end="; ")
      print("END")

    elif option == "RECOMMEND":
      print("I recommend you read", getRandomCitation(library))
    
    elif option == "SAVE":
      save_option = input("Select an option (TITLES, ALL): ").upper()
      file_name = input("Enter the files name to save the library (without an extension): ")
      if save_option == "TITLES" and file_name:
        saveToFile(library, False, file_name + ".txt")
      elif save_option == "ALL":
        saveToFile(library, True, file_name + ".txt")
      else:
        print("Invalid Input")

  print("Goodbye!")

# does this change show? 