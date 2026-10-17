# Dynamic Flight Telemetry Log
# Introduction to Python - Unit: Lists


# Create a list of 8 initial altitude readings in ft
flight_log = [1000, 2500, 4200, 6000, 7800, 9500, 11000, 12500]
print("Initial log:", flight_log)


# Simulate the sensor receiving 2 new readings as the flight continues using .append() dot append important
flight_log.append(14000)
print("After first append:", flight_log)

flight_log.append(15200)
print("After second append:", flight_log)

# Remove the first two corrupted sensor noise readings using explicit index positions
removed_first = flight_log.pop(0)
print(f"Removed corrupted reading ({removed_first} ft). After first pop:", flight_log)

removed_second = flight_log.pop(0)
print(f"Removed corrupted reading ({removed_second} ft). After second pop:", flight_log)

# Step 4: Insert a missing mid-flight reading# Insert a reasonable altitude value (8650 ft) at index 2 so it fits fine between 7800 and 9500
flight_log.insert(2, 8650)
print("After insert:", flight_log)


print(f"Reading at index 3: {flight_log[3]} ft")
print("Final flight log:", flight_log)

# efficient code go brrr

