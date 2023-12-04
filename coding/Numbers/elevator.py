class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1

    def move_to_floor(self, target_floor):
        if 1 <= target_floor <= self.num_floors:
            if target_floor == self.current_floor:
                print(f"Elevator is already on floor {self.current_floor}")
            else:
                if target_floor > self.current_floor:
                    self.move_up(target_floor)
                else:
                    self.move_down(target_floor)
        else:
            print("Invalid floor request. Please select a valid floor.")

    def move_up(self, target_floor):
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Moving up... Now on floor {self.current_floor}")

    def move_down(self, target_floor):
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Moving down... Now on floor {self.current_floor}")

# Usage example:
elevator = Elevator(10)
elevator.move_to_floor(5)
elevator.move_to_floor(8)
elevator.move_to_floor(2)

#In this code, we create an Elevator class with methods to move to a target floor, move up, and move down.
# The elevator starts on the first floor, and you can call the move_to_floor method to move it to the desired floor.
# The elevator will print the current floor while moving.