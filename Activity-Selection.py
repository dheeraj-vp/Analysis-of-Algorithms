def activity_selection(activities):
    # Sort activities based on their finish times
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_finish_time = 0
    
    for i, (start, finish) in enumerate(activities):
        if start >= last_finish_time:
            selected.append(i)
            last_finish_time = finish
    
    print("Selected activities:", selected)

# Input
n = int(input("Enter number of activities: "))
activities = []
for i in range(n):
    start, finish = map(int, input(f"Activity {i}: ").split())
    activities.append((start, finish))

activity_selection(activities)
