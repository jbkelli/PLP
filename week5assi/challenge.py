# Polymorphism Challenge: Animals and Vehicles with move() method
# Each class implements move() differently to demonstrate polymorphism

# Base class for Animals
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        print(f"{self.name} the {self.species} is moving")
    
    def introduce(self):
        print(f"Hi! I'm {self.name}, a {self.species}")

# Base class for Vehicles
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        print(f"The {self.year} {self.make} {self.model} is moving")
    
    def info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")

# Animal subclasses - each with unique move() implementation
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def move(self):
        print(f"{self.name} the {self.breed} is running on four paws! 🐕")
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

class Fish(Animal):
    def __init__(self, name, fish_type):
        super().__init__(name, "Fish")
        self.fish_type = fish_type
    
    def move(self):
        print(f"{self.name} the {self.fish_type} is swimming gracefully through water! 🐠")
    
    def bubble(self):
        print(f"{self.name} blows bubbles: *blub blub*")

class Bird(Animal):
    def __init__(self, name, bird_type):
        super().__init__(name, "Bird")
        self.bird_type = bird_type
    
    def move(self):
        print(f"{self.name} the {self.bird_type} is soaring through the sky! 🦅")
    
    def chirp(self):
        print(f"{self.name} chirps: Tweet tweet!")

class Snake(Animal):
    def __init__(self, name, snake_type):
        super().__init__(name, "Snake")
        self.snake_type = snake_type
    
    def move(self):
        print(f"{self.name} the {self.snake_type} is slithering on the ground! 🐍")
    
    def hiss(self):
        print(f"{self.name} hisses: Ssssss!")

# Vehicle subclasses - each with unique move() implementation
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    
    def move(self):
        print(f"The {self.year} {self.make} {self.model} is driving on the road! 🚗")
    
    def honk(self):
        print("Beep beep!")

class Plane(Vehicle):
    def __init__(self, make, model, year, max_altitude):
        super().__init__(make, model, year)
        self.max_altitude = max_altitude
    
    def move(self):
        print(f"The {self.year} {self.make} {self.model} is flying through the clouds! ✈️")
    
    def announce(self):
        print("Ladies and gentlemen, we are now cruising at altitude!")

class Boat(Vehicle):
    def __init__(self, make, model, year, boat_type):
        super().__init__(make, model, year)
        self.boat_type = boat_type
    
    def move(self):
        print(f"The {self.year} {self.make} {self.model} {self.boat_type} is sailing across the water! ⛵")
    
    def horn(self):
        print("HOOOOORN!")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count):
        super().__init__(make, model, year)
        self.gear_count = gear_count
    
    def move(self):
        print(f"The {self.year} {self.make} {self.model} bicycle is pedaling down the path! 🚲")
    
    def ring_bell(self):
        print("Ring ring!")

# Function to demonstrate polymorphism
def demonstrate_movement(creatures):
    """
    This function shows polymorphism in action.
    It can accept any object that has a move() method,
    regardless of whether it's an animal or vehicle.
    """
    print("🌟 POLYMORPHISM DEMONSTRATION 🌟")
    print("=" * 50)
    
    for creature in creatures:
        # Each object calls its own version of move()
        creature.move()
    
    print("=" * 50)

# Main demonstration
def main():
    print("🐾 ANIMALS AND VEHICLES POLYMORPHISM CHALLENGE 🚗")
    print("=" * 60)
    
    # Create animal instances
    print("\n🐾 CREATING ANIMALS:")
    dog = Dog("Buddy", "Golden Retriever")
    fish = Fish("Nemo", "Clownfish")
    bird = Bird("Eagle", "Bald Eagle")
    snake = Snake("Slither", "Python")
    
    # Create vehicle instances
    print("\n🚗 CREATING VEHICLES:")
    car = Car("Toyota", "Camry", 2023, "Gasoline")
    plane = Plane("Boeing", "747", 2020, 35000)
    boat = Boat("Sea Ray", "Sundancer", 2022, "Yacht")
    bicycle = Bicycle("Trek", "Mountain Bike", 2023, 21)
    
    # Show individual introductions
    print("\n📋 INTRODUCTIONS:")
    for animal in [dog, fish, bird, snake]:
        animal.introduce()
    
    print()
    for vehicle in [car, plane, boat, bicycle]:
        vehicle.info()
    
    # Demonstrate individual movements
    print("\n🎬 INDIVIDUAL MOVEMENTS:")
    print("\nAnimals:")
    dog.move()
    fish.move()
    bird.move()
    snake.move()
    
    print("\nVehicles:")
    car.move()
    plane.move()
    boat.move()
    bicycle.move()
    
    # Demonstrate polymorphism with mixed list
    print("\n🔥 POLYMORPHISM IN ACTION!")
    all_moving_things = [dog, car, fish, plane, bird, boat, snake, bicycle]
    demonstrate_movement(all_moving_things)
    
    # Show unique methods for each class
    print("\n🎵 UNIQUE SOUNDS AND ACTIONS:")
    dog.bark()
    fish.bubble()
    bird.chirp()
    snake.hiss()
    
    car.honk()
    plane.announce()
    boat.horn()
    bicycle.ring_bell()
    
    print("\n✨ This demonstrates polymorphism: same method name (move()),")
    print("   but different behavior for each class type!")
    print("   Each animal and vehicle moves in their own unique way! 🌟")

if __name__ == "__main__":
    main()
