def get_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Error: enter positive number")
        except ValueError:
            print("Error: enter whole number")
days = get_positive_int("days:")
period = get_positive_int("periods:")
n = get_positive_int("number of subject:")
subjects = {}
for i in range(n):
    name = input("Subject name:")
    count = get_positive_int("Periods for " + name + ":")
    subjects[name] = count

total = sum(subjects.values())
slots = days * period

if total != slots:
    print(f"Error: Total weekly periods ({total}) must equal available slots ({slots}).")
    exit()

for name in subjects:
    if subjects[name] > 2 * days:
        print(f"Timetable cannot be generated: {name} needs {subjects[name]} periods in {days} day, but the limit is 2 per day.")
        exit()
timetable = []
for d in range(days):
    today = {}
    day_list = []
    for slot in range(period):
        best = None
        for name in subjects:
            if subjects[name] > 0 and today.get(name, 0) < 2:
                if best is None or subjects[name] > subjects[best]:
                    best = name
        if best is None:
            print("Timetable cannot be generated")
            exit()
        subjects[best] -= 1
        today[best] = today.get(best, 0) + 1
        day_list.append(best)
    timetable.append(day_list)
print(timetable)
day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

for i in range(days):
    print(day_names[i] + ": " + ", ".join(timetable[i]))
