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

# Main program
if __name__ == "__main__":
    # Create a new car
    new_car = Car(registration_number="ABC-123", max_speed=142)

    # Accelerate the car
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)

    # Print out the current speed of the car
    print("Current Speed:", new_car.current_speed, "km/h")

    # Use the emergency brake
    new_car.accelerate(-200)

    # Print out the final speed of the car
    print("Final Speed:", new_car.current_speed, "km/h")
