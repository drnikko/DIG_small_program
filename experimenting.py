# ------------------------------------------------------------------------------------------
#       Title: Experimenting with To Do List for DIG
#       Name: Kiersten Conley
# ------------------------------------------------------------------------------------------

# creating variables for the numbers associated with each day
day_order = {"MONDAY": 0, 
             "TUESDAY": 1, 
             "WEDNESDAY": 2, 
             "THURSDAY": 3, 
             "FRIDAY": 4, 
             "SATURDAY": 5, 
             "SUNDAY": 6}

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
    todo_dictionary:dict = {} # creating dictionary that stores a task
    # creating keys for values that the user will input
    todo_dictionary["day"] = day 
    todo_dictionary["time"] = time 
    todo_dictionary["category"] = category 
    todo_dictionary["description"] = description
    return todo_dictionary # returns the task

def convertTime(time_str: str) -> int: 
   """
   Converts times (such as 12pm and 1:30pm) into an integer value for the number of minutes after midnight
   :param time_str: (str) User inputed time 
   :return: (int) Number of minutes after midnight
   >>> convertTime(2pm)
   840
   """
   time_str = time_str.strip().lower() # breaks down the characters and makes everything lower case (if not already)

   # spliting am and pm
   if "am" in time_str: # if it's a morning time
      period = "am"
      time_str = time_str.replace("am", "") # takes out am
   else: # if it's an afternoon time
       period = "pm"
       time_str = time_str.replace("pm", "") # takes out pm
       
   # hour/minute handling
   if ":" in time_str: # if theres a colon
      hour, minute = time_str.split(":") # splits minutes and hours
   else: # when there's no minutes
      hour = time_str
      minute = "0"

   hour = int(hour)
   minute = int(minute)

   if period == "pm" and hour != 12: # for pm times
      hour += 12
   elif period == "am" and hour == 12: # for am times
      hour = 0

   return (hour * 60 + minute) # number of hours * 60 minutes + number of minutes

def sortTasks(task: dict) -> tuple[int, int]: 
   """
   Gives Python a sorting key for day and time 
   :param task: (dict)
   :return: 
   :return: 
   >>> myToDo = {'day': 'Wednesday', 'time': '11:59pm', 'category': 'School', 'description': 'SDS assignment}
   >>> sortTasks(myToDo)
   2 
   2359
   """
   day_value = day_order[task["day"].upper()] # sorts days in order Mon-Sun. uses .upper() so 'Monday' and 'monday' aren't viewed differently.
   time_value = convertTime(task["time"]) # sorts tasks by their military time
   return (day_value, time_value)

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
    todo_list.append(task) # adds task to list
    todo_list.sort(key=sortTasks) # sorts the task by day and time using the sortTasks function

def removeTask(todo_list: list, index: int) -> None: 
    """ This function removes a task from the to do list 
    :param todo_list: (list) User inputed list of to do tasks
    :param index: (int) User inputed integer value, indicated the dictionary within the list
    >>> myToDo = [{'day': 'Monday', 'time': '12pm', 'category': 'Yardwork', 'description': 'Water the garden'}, {'day': 'Wednesday', 'time': '11:59pm', 'category':
    'School', 'description': 'SDS assignment due'}]
    >>> removeTask(myToDo, 2)
    [{'day': 'Monday', 'time': '12pm', 'category': 'Yardwork', 'description': 'Water the garden'}]
    """
    if index in range(1, len(todo_list) + 1): # Checks if the task exists while translating from the user input to index notation
        remove_this_task = todo_list[index -1 ] # Picks the task that is getting removed
        todo_list.remove(remove_this_task) # Removes the task from the to do list
    else: 
        print("This task does not exist.") # If the task does not exist

def main() ->  None: 
    """ This function handles user inputs and operations for the to do list 
    """
    todo_list = [] # creating to do list

    while True: 
        print("\nTO DO LIST")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Choose an option: ") # user is prompted to pick a number that matches what they want to do

        if choice == "1": # adding task

            day = input("Day: ")
            time = input("Time (ex: 2pm, 1:30pm): ")
            category = input("Category: ")
            description = input("Description: ")

            task = createToDo(day, time, category, description)
            addTask(todo_list, task)

            print("Task added.")
        
        elif choice == "2": # removing task

            if len(todo_list) == 0: # in case there's nothing in the list
                print("Your to do list is empty. There is nothing to remove.")
            else: 
                # print's tasks in numerical order for user to select which number they want to remove
                print("/nCurrent Tasks:")
                for i, task in enumerate(todo_list, start=1):
                    # f is a "formatted string literal" or "f-string" 
                    print(f"{i}. {task['day']} {task['time']} - "
                          f"{task['category']} - {task['description']}")
                
                index = int(input("Enter task number to remove: ")) # user selects which number to delete
                
                removeTask(todo_list, index) # removing task
        
        elif choice == "3": # viewing tasks

            if len(todo_list) == 0: # in case there's northing in the list
                print("Your to do list is empty.")
            else: 
                # same as above under choice 2
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task['day']} {task['time']} - "
                          f"{task['category']} - {task['description']}")
        
        elif choice == "4": # quits the loop
            print("Goodbye!")
            break
        
        else: # in case user inputs something else
            print("Invalid option. Please try again.")
    
if __name__ == "__main__":
    main()