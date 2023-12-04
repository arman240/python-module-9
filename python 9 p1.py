class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Main program
if __name__ == "__main__":
    # Create a new car
    new_car = Car(registration_number="ABC-123", max_speed=142)

    # Print out all properties of the new car
    print("Registration Number:", new_car.registration_number)
    print("Maximum Speed:", new_car.max_speed, "km/h")
    print("Current Speed:", new_car.current_speed, "km/h")
    print("Travelled Distance:", new_car.travelled_distance, "km")
