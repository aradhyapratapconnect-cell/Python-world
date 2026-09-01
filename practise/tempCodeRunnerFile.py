    elif user == "to do list":
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")

            choice = input("Choose an option: ")

            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                delete_task()
            else:
                print("Invalid choice ❌")