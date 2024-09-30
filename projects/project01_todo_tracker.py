
with open("task_lists.txt") as file:
    user_tasks = file.readlines()
user_tasks=['']
task_list = f"Your current tasks are :{ user_tasks}"

#add_or_del =input( "would you like to add or remove  a task? :" )
while True: 
    print(task_list)
    print("____________________________________________________")
    add_or_del =input( "would you like to add or remove  a task? :" )
    while add_or_del == "add":
        new_task= input('add a task :')
        user_tasks.append(new_task +'\n')
        task_list = f"Your current tasks are :{ user_tasks[1:200]}"
        print(task_list)
        print("____________________________________________________")
        add_or_del =input( "would you like to add or remove  a task? :" ) 
    while add_or_del == "remove":
        user_tasks.remove(input('remove a task :'))
        task_list = f"Your current tasks are :{ user_tasks[1:200]}                                                                                                                      ________________________________________________________"
        print(task_list)
        print("____________________________________________________")
        add_or_del =input( "would you like to add or remove  a task? :" )
        print("____________________________________________________")
        
        
else :
with open("task_list.txt","w") as file:
file.writelines(user_tasks)
