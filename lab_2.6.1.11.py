hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
minraw = int(mins+dura)
hourraw = int(hour + (minraw/60))

hourfinal = int(hourraw % 24)
minfinal = int(minraw % 60)

print("end_time = ",hourfinal, ":", minfinal)