#Header
# display a welcome message
print("The crop cover calculator")
print("It's pretty easy to use. Insert your data and the calculator will provide you with the data you need!")

# get input from the user
area_length = float(input(" Please type in the are length(.ft): \t"))
area_width = float(input("Please type in the area width(.ft):\t"))

# calculate miles per gallon
acerage = (area_length * area_width) / 43560
seeding_rate = float(input("Please type in the seeding rate (lbs):\t"))
cover_crop_needed = float(acerage * seeding_rate)

print(cover_crop_needed)

print(f"The data you inserted for length was: {area_length}.")
print(f"The data you inserted for width was: {area_width}")
print(f"The data you inserted for seeding rate was: {seeding_rate}.")

print(f"The coverage you need is: {cover_crop_needed}.")
print("Thank you for making use of our calculator!")

print("Designed by Amy Jacobus")

