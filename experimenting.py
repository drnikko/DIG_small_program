# ------------------------------------------------------------------------------------------
#       Title: Experimenting with To Do List for DIG
#       Name: Kiersten Conley
# ------------------------------------------------------------------------------------------

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
    todo_dictionary:dict = {} # creating dictionary that stores the to do list 
    # creating keys for values that the user will input
    todo_dictionary["day"] = day 
    todo_dictionary["time"] = time 
    todo_dictionary["category"] = category 
    todo_dictionary["description"] = description
    return todo_dictionary # returns the to do list

def convertTime(time_str: str) -> int: 
   """
   Converts times such as 12pm and 1:30pm into military time integers for sorting.
   :param time_str: (str) User inputed time 
   :return: (int) Military time integer
   >>> convertTime(2pm)
   1400
   """
   time_str = time_str.strip().lower()

   # spliting am and pm
   if "am" in time_str: 
      period = "am"
      time_str = time_str.replace("am", "")
   else: 
       period = "pm"
       time_str = time_str.replace("pm", "")
       
   # hour/minute handling
   if ":" in time_str: 
      hour, minute = time_str.split(":")
   else: 
      hour = time_str
      minute = "0"

   hour = int(hour)
   minute = int(minute)

   if period == "pm" and hour != 12:
      hour += 12
   elif period == "am" and hour == 12:
      hour = 0

   return (hour * 60 + minute)

def sortTasks(task: dict): 
   """
   Gives Python a sorting key for day and time 
   :param task: (dict)
   :return: 
   :return: 
   >>>
   FINISH WRITING THIS

   """
   day_value = day_order[task["day"].upper()]
   time_value = convertTime(task["time"]) # need to make function to convert time
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
    todo_list.append(task)
    todo_list.sort(key=sortTasks)

def removeTask(todo_list: list, index: int) -> None: 
    """ This function removes a task from the to do list 

    """
    if index in range(1, len(todo_list) + 1): # Checks if the task exists while translating from the user input to index notation
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
    if len(todo_list) == 0: 
        print("Your to do list is empty.")
    else: 
        return(todo_list)

def main() ->  None: 
    """ This function handles user inputs and operations for the to do list 
    """
    todo_list = []

    while True: 
        print("\nTO DO LIST")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1": 
            day = input("Day: ")
            time = input("Time (ex: 2pm, 1:30pm): ")
            category = input("Category: ")
            description = input("Description: ")

            task = createToDo(day, time, category, description)
            addTask(todo_list, task)

            print("Task added.")
        
        elif choice == "2": 

            if len(todo_list) == 0: 
                print("Your to do list is empty. There is nothing to remove.")
            else: 
                print("/nCurrent Tasks:")

                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task['day']} {task['time']} - "
                          f"{task['category']} - {task['description']}")
                
                index = int(input("Enter task number to remove: "))
                removeTask(todo_list, index)
        
        elif choice == "3": 

            if len(todo_list) == 0: 
                print("Your to do list is empty.")
            else: 
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task['day']} {task['time']} - "
                          f"{task['category']} - {task['description']}")
        
        elif choice == "4": 
            print("Goodbye!")
            break
        
        else: 
            print("Invalid option. Please try again.")
    
if __name__ == "__main__":
    main()