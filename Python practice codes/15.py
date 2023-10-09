import math

def calculate_ladder_length(height, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    ladder_length = height / math.sin(angle_radians)
    return ladder_length

height = float(input("Enter the height to be reached (in meters): "))
angle_degrees = float(input("Enter the angle of the ladder (in degrees): "))
ladder_length = calculate_ladder_length(height, angle_degrees)
print(f"The length of the ladder required is {ladder_length:.2f} meters.")