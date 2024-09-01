def main():
    tasks = []

    while True:
        print("***** To do list *****")
        print("1.Add task")
        print("2.Show tasks")
        print("4.Mark as done")
        print("5.Exit")

        choice = input("Enter the choice : ")

        if choice == '1':
           print()
           n_tasks = int(input("How many tasks yow want to add:"))

           for i in range(n_tasks):
               task = input("Enter the task:")
               tasks.append({"task":task,"done": False})
               print("Task added:")
        elif choice == '2':        
            print("\n Tasks:")
            for index,tasks in enumerate(tasks):
                status = "Done" if task ["done"] else "Not done"
                print(f"{index + 1}. {task['task']} - {status}")
        elif choice == '3':
            task_index = int(input("Enter the task number to be done:"))
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done")
            else:
                print("Invalid task number")

        elif choice == '4':
            print("Exiting to do list")
            break
        else:
            print("Invalid choice.Please try again.")

if __name__ == "__main__":
    main()