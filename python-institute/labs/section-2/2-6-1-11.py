hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# test 1 = 13:16
# hour = 12
# mins = 17
# dura = 59

# test 2 = 10:40
# hour = 23
# mins = 58
# dura = 642

# test 3 = 1:0
# hour = 0
# mins = 1
# dura = 2939

total_minutes = ((hour * 60) + (mins)) + dura
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(str(end_hour) + ":" + str(end_minute))