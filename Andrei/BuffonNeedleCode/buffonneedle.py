import random
import math

# Function to simulate Buffon's Needle experiment
def buffons_needle_experiment(num_needles, needle_length, line_spacing, num_lines):
    crossings = 0

    for _ in range(num_needles):
        # Randomly generate the position and angle of the needle
        needle_x = random.uniform(0, line_spacing*4)
        needle_angle = random.uniform(0, math.pi / 2)

        # Calculate the end point of the needle
        start_y = needle_x - (needle_length/2) * math.sin(needle_angle)
        end_y = needle_x + (needle_length/2) * math.sin(needle_angle)

        # Check if the needle crosses a line
        for i in range(1, num_lines+1):
            if start_y <= line_spacing*i-1000 <= end_y:
                crossings += 1

    return crossings

# Parameters for the experiment
num_needles = 500000  # Number of needles to drop
needle_length = 1000   # Length of the needle
line_spacing = 2000     # Distance between parallel lines
num_lines = 4

# Run the experiment
sum = 0
for i in range(100):
    crossings = buffons_needle_experiment(num_needles, needle_length, line_spacing, num_lines)
    estimated_pi = (2 * needle_length * num_needles) / (line_spacing * crossings)
    sum += estimated_pi
avg = sum/100

print("There were " + str(num_needles) + " needles and " + str(crossings) + " crossed a line.")
print("Estimated value of π:", avg)
print("Actual value of π:", math.pi)