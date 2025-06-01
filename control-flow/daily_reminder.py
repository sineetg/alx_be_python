task = input('Engter the task you want to be reminded of: ')
priority = (input('Enter the priority of the task - (low/medium/high): ')).lower()
time_bound = input('Is the task time bound? (yes/no): ').lower()

match priority:
    case 'high':
        # time_bound == 'yes'
        print(f"{task} is a high priority task that requires immediate attention today!")
    case 'medium':
        time_bound == 'yes'
        print(f"{task} is a medium priority task that should be completed soon.")
    case 'low':
        # time_bound == 'no'
        print(f"{task} is a low priority task. Consider completing it when you have free time.")
