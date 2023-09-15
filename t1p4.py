""" Traffic light program """

# Created by Jonathan Paco-Arnone and Aidan Lalonde-Novales
# Created Sept 13th 2023
# This program determines if a car can go through an intersection.

from time import sleep

def intersection(light_color, time_to_intersection):
    """Decides if a car can go through an intersection and prints"""
    if light_color == "green":
        print("\nYour car can go.")
    elif light_color == "yellow" and time_to_intersection <= 5:
        print("\nYour car can go.")
    elif light_color == "red" and time_to_intersection <= 2:
        print("\nYour car can go.")
    else:
        print("\nSTOP! Your car cannot go.")

def main():
    """Main function that starts the program"""
    # intro and input
    print("Should you go through an intersection?\n")
    light_color = input("What color is the light? ")
    distance = float(input("How far (in m) are you from the intersection? "))
    speed = float(input("How fast (in m/s) are you going? "))

    # Data validation and intersection() function
    try:
        time_to_intersection = distance / speed
        intersection(light_color, time_to_intersection)
    except Exception:
        print("\nError, make sure distance and speed are numbers.")

    sleep(1) # So the file does not instantly close when it is finished running

if __name__ == "__main__":
    main()
