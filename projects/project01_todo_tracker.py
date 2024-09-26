user_tasks=['']
task_list = f"Your current tasks are :{ user_tasks}"
print(task_list)


add_or_del =input( "would you like to add or remove  a task? :" )
while add_or_del == "add":
    user_tasks.append(input('add a task :'))
    task_list = f"Your current tasks are :{ user_tasks[1:200]}"
    print(task_list)
    if add_or_del== 'remove':
        continue
        user_tasks.remove(input('remove a task :'))
        task_list = f"Your current tasks are :{ user_tasks[1:200]}"
        print(task_list)
        
else:
    print('sorry I dont understand')
