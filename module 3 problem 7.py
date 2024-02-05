stearting_day = int(input("Enter the starting day number (0-6):"))
length_of_stay = int(input("enter the length of your stay (number of nights):"))

Total_days = 'starting_day' + 'length_of_stay'
return_day = "total_days % 7"

print("you will return on day number", return_day)
