# ======================================================================================================
#  Farmer Harvest Calcuator
# ======================================================================================================
# --- Assignment Operator (=) ---
# Store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 100

#   --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average harvest
total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest: ", total, "kg")
print("Average per field: ", average, "kg" )

# Price per kg is 15 dollars - calculate total earnings
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings : $. ", earnings)

# -- Floor Division (//) and Modulus (%) --
# Pack the harvest into bags of 25 kg each 
bags      = total // 25
leftovers = total %25

print("Full bags packed: ", bags)
print("Leftover grain :", leftovers, "kg")

# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Better than last year? :", total > last_year)
print("Same as this year? :", total == last_year)
print("At least its good? :", total >= last_year)

# --- Assignment Operators ---
# A bonus field adds 30 kg to the total
total += 30
print("After bonus crop  :", total, "kg")
