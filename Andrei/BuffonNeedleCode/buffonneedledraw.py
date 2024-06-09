import random
import math
import pygame
import time

# Function to simulate Buffon's Needle experiment
def buffons_needle_experiment(num_needles, needle_length, line_spacing, line_color, num_lines):
    crossings = 0
    screen = pygame.display.set_mode((3*line_spacing, num_lines*line_spacing))
    screen.fill((255,255, 255))
    for i in range(1, num_lines+1):
        pygame.draw.line(screen, line_color, (0, i*line_spacing-75), (3*line_spacing, i*line_spacing-75))
    pygame.display.flip()

    for _ in range(num_needles):
        crossed = False
        #time.sleep(.03)
        # Randomly generate the position and angle of the needle
        needle_y = random.uniform(0, line_spacing*4)
        needle_x = random.uniform(0, line_spacing*3)
        needle_angle = random.uniform(0, math.pi / 2)

        # Calculate the end point of the needle
        start_y = needle_y - (needle_length/2) * math.sin(needle_angle)
        start_x = needle_x - (needle_length/2) * math.cos(needle_angle)
        end_y = needle_y + (needle_length/2) * math.sin(needle_angle)
        end_x = needle_x + (needle_length/2) * math.cos(needle_angle)

        # Check if the needle crosses a line
        for i in range(1, num_lines+1):
            if start_y <= line_spacing*i-75 <= end_y:
                crossings += 1
                crossed = True

        if crossed:
            pygame.draw.line(screen, (255, 0, 0), (start_x, start_y), (end_x, end_y))
        else:
            pygame.draw.line(screen, line_color, (start_x, start_y), (end_x, end_y))
        pygame.display.flip()

    return crossings

# Parameters for the experiment
num_needles = 10000  # Number of needles to drop
needle_length = 65   # Length of the needle
num_lines = 4
line_spacing = 150     # Distance between parallel lines
line_color = (0, 0, 0)

crossings = buffons_needle_experiment(num_needles, needle_length, line_spacing, line_color, num_lines)
if crossings == 0:
    estimated_pi = 0
else:
    estimated_pi = (2 * needle_length * num_needles) / (line_spacing * crossings)

print("There were " + str(num_needles) + " needles and " + str(crossings) + " crossed a line.")
print("Estimated value of π:", estimated_pi)
print("Actual value of π:", math.pi)