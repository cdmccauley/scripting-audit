# demonstrates: declare variable, assign variable, get input, convert data type
grade = float(raw_input("Enter a grade between 0 and 100: "))

# demonstrates: if..elif..else, comparison operators, blocks, print, string literals
if (grade > 89):
    print "You earned an A!"
elif (grade > 79):
    print "You earned a B!"
elif (grade > 69):
    print "You earned a C!"
elif (grade > 59):
    print "You earned a D!"
else:
    print "Yipes!, you failed this course"