import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Ensure speed doesn't go below 0
        self.current_speed = max(0, self.current_speed + speed_change)
        # Ensure speed doesn't exceed the maximum
        self.current_speed = min(self.current_speed, self.max_speed)

    def drive(self, hours):
        # Calculate the distance traveled based on constant speed
        distance_traveled = self.current_speed * hours
        # Update the travelled distance
        self.travelled_distance += distance_traveled

# Function to create a random speed between 100 km/h and 200 km/h
def generate_random_speed():
    return random.randint(100, 200)

# Main program
if __name__ == "__main__":
    # Create a list of 10 car objects
    cars = [Car(registration_number=f"ABC-{i}", max_speed=generate_random_speed()) for i in range(1, 11)]

    # Race until one car has advanced at least 10,000 kilometers
    while all(car.travell
