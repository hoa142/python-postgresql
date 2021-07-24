day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's tuesday.")
else:
    print("Full speed ahead!")

print("This always runs.")


"""The order of keywords is important. Remember that the if comes first,
then any elif, if you want them, and finally the else.
the elif and else keywords are optional if you want to add those branches to your if statement.
"""