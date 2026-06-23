while True:
    
    # gets user input and strips space chars from it
    user_action = input("Type Add, Show, Delete, Edit or Exit:")
    user_action = user_action.strip()
 

        # check if user action is "add "Add a todo""
    if 'add' in user_action:
        todo = user_action[4:]
        
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)


    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
        
        
    elif 'edit' in user_action:
        number = user_action[5:]
        number = number - 1

        with open('todos.txt', 'r') as file:
            file.readlines()
        
        new_todo = user_action[5:]
        todos[number] = new_todo

        print('Here is how it will be ', todos)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'delete' in user_action:
        number = user_action[6:]
        
        with open('todos.txt', 'r') as file:
            file.readlines()
        index = number - 1
        to_remove = todos[index].strip()
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo '{to_remove}' has been deleted."
        print(message)
        
    elif 'exit' in user_action:
        break

print("Bye!")