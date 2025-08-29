# Question1
# Smartphone Class 
class Smartphone:
    color = "Black"  # Class attribute 
    size = "6.1 inches"  # Class attribute 
#method
    def smartphone_info(self):
        print("The phone is a smartphone.")
        #constructor
    def __init__(self, brand, model, storage, battery_capacity, is_water_resistant=False):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_capacity = battery_capacity  # in mAh
        self.is_water_resistant = is_water_resistant
        self._battery_level = 100  # Encapsulated attribute (private)
        self.is_powered_on = False
    
    def power_on(self):
        if not self.is_powered_on:
            self.is_powered_on = True
            return f"{self.brand} {self.model} is now powered on!"
        return "Phone is already on."
    
    def power_off(self):
        if self.is_powered_on:
            self.is_powered_on = False
            return f"{self.brand} {self.model} is now powered off."
        return "Phone is already off."
    
    def check_battery(self):
        return f"Battery level: {self._battery_level}%"
    
    def use_battery(self, amount):
        if self._battery_level - amount >= 0:
            self._battery_level -= amount
            return f"Used {amount}% battery. {self.check_battery()}"
        else:
            self._battery_level = 0
            self.is_powered_on = False
            return "Battery depleted! Phone has powered off."
    
    def charge(self, amount):
        if self._battery_level + amount <= 100:
            self._battery_level += amount
            return f"Charged {amount}%. {self.check_battery()}"
        else:
            self._battery_level = 100
            return "Fully charged!"
    
    def make_call(self, number):
        if self.is_powered_on:
            battery_used = 5
            return f"Calling {number}... {self.use_battery(battery_used)}"
        return "Cannot make call. Phone is powered off."
    
    def __str__(self):
        water_resistant = "Yes" if self.is_water_resistant else "No"
        return (f"{self.brand} {self.model} | {self.storage}GB | "
                f"{self.battery_capacity}mAh | Water Resistant: {water_resistant}")


# GamingPhone Class (Inherits from Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, gpu_model, refresh_rate, is_water_resistant=False):
        super().__init__(brand, model, storage, battery_capacity, is_water_resistant)
        self.gpu_model = gpu_model
        self.refresh_rate = refresh_rate  # in Hz
        self.is_gaming_mode = False
    
    def enable_gaming_mode(self):
        if not self.is_gaming_mode:
            self.is_gaming_mode = True
            return "Gaming mode enabled! Performance boosted."
        return "Gaming mode is already enabled."
    
    def disable_gaming_mode(self):
        if self.is_gaming_mode:
            self.is_gaming_mode = False
            return "Gaming mode disabled."
        return "Gaming mode is not active."
    
    def play_game(self, game_name):
        if self.is_powered_on:
            if self.is_gaming_mode:
                battery_used = 15
                return (f"Playing {game_name} in gaming mode... "
                        f"{self.use_battery(battery_used)}")
            else:
                battery_used = 10
                return (f"Playing {game_name}... "
                        f"{self.use_battery(battery_used)}")
        return "Cannot play game. Phone is powered off."
    
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} | GPU: {self.gpu_model} | {self.refresh_rate}Hz"


# Demonstration
print("=== Assignment 1: Smartphone Class Demonstration ===")

# Create a regular smartphone
iphone = Smartphone("Apple", "iPhone 14", 128, 3200, True)
print(iphone)
print(iphone.power_on())
print(iphone.make_call("555-1234"))
print(iphone.check_battery())
print(iphone.charge(20))
print(iphone.power_off())
print()

# Create a gaming phone
gaming_phone = GamingPhone("ASUS", "ROG Phone 6", 256, 6000, "Adreno 730", 165, True)
print(gaming_phone)
print(gaming_phone.power_on())
print(gaming_phone.enable_gaming_mode())
print(gaming_phone.play_game("Genshin Impact"))
print(gaming_phone.check_battery())
print(gaming_phone.disable_gaming_mode())
print(gaming_phone.power_off())


#question2
# Animal Class
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def move(self):
        return "I move in some way"
    
    def speak(self):
        return "I make some sound"
    
    def __str__(self):
        return f"I am a {self.name} and I live in {self.habitat}"


# Bird Class (inherits from Animal)
class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan
    
    def move(self):  # Polymorphic implementation
        return "Flying 🕊️"
    
    def speak(self):
        return "Chirp chirp!"
    
    def build_nest(self):
        return "Building a nest for my eggs"


# Fish Class (inherits from Animal)
class Fish(Animal):
    def __init__(self, name, habitat, fin_count):
        super().__init__(name, habitat)
        self.fin_count = fin_count
    
    def move(self):  # Polymorphic implementation
        return "Swimming 🐟"
    
    def speak(self):
        return "Blub blub (fish don't really speak)"
    
    def blow_bubbles(self):
        return "Blowing bubbles in the water"


# Snake Class (inherits from Animal)
class Snake(Animal):
    def __init__(self, name, habitat, is_venomous):
        super().__init__(name, habitat)
        self.is_venomous = is_venomous
    
    def move(self):  # Polymorphic implementation
        return "Slithering 🐍"
    
    def speak(self):
        return "Hiss hiss!"
    
    def shed_skin(self):
        return "Shedding my skin as I grow"


# Kangaroo Class (inherits from Animal)
class Kangaroo(Animal):
    def __init__(self, name, habitat, jump_height):
        super().__init__(name, habitat)
        self.jump_height = jump_height
    
    def move(self):  # Polymorphic implementation
        return "Hopping 🦘"
    
    def speak(self):
        return "Chortle chortle!"
    
    def carry_joey(self):
        return "Carrying my baby in my pouch"


# Function to demonstrate polymorphism
def demonstrate_movement(animals):
    print("\n=== Animal Movement Demonstration ===")
    for animal in animals:
        print(f"{animal.name}: {animal.move()}")


# Create instances of different animals
eagle = Bird("Bald Eagle", "Mountains", 2.3)
salmon = Fish("Salmon", "Rivers", 7)
cobra = Snake("King Cobra", "Jungles", True)
kangaroo = Kangaroo("Red Kangaroo", "Outback", 3)



