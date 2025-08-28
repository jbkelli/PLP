class Smartphone:
    total_phones = 0
    
    def __init__(self, brand, model, price, storage=128):
        # Public attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        
        # Protected attribute (indicated by single underscore)
        self._price = price
        
        # Private attribute (indicated by double underscore)
        self.__serial_number = f"{brand}_{model}_{Smartphone.total_phones + 1}"
        
        # Instance attributes with default values
        self.is_on = False
        self.battery_level = 100
        self.apps_installed = []
        self.contacts = []
        
        # Increment class variable
        Smartphone.total_phones += 1
        
        print(f"{self.brand} {self.model} created successfully!")
    
    def power_on(self):
        """Turn on the smartphone"""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON")
        else:
            print(f"Phone is already ON")
    
    def power_off(self):
        """Turn off the smartphone"""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF")
        else:
            print(f"Phone is already OFF")
    
    def install_app(self, app_name):
        """
        Install an app on the phone
        
        Args:
            app_name (str): Name of the app to install
        """
        if not self.is_on:
            print("Turn on the phone first!")
            return
        
        if app_name not in self.apps_installed:
            self.apps_installed.append(app_name)
            print(f"{app_name} installed successfully!")
        else:
            print(f"{app_name} is already installed!")
    
    def add_contact(self, name, phone_number):
        """
        Add a contact to the phone
        
        Args:
            name (str): Contact name
            phone_number (str): Contact phone number
        """
        if not self.is_on:
            print("Turn on the phone first!")
            return
        
        contact = {"name": name, "phone": phone_number}
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")
    
    def make_call(self, contact_name):
        """
        Make a call to a contact
        
        Args:
            contact_name (str): Name of contact to call
        """
        if not self.is_on:
            print("Turn on the phone first!")
            return
        
        # Find contact
        contact = next((c for c in self.contacts if c["name"] == contact_name), None)
        if contact:
            self.battery_level -= 5  # Simulate battery usage
            print(f"Calling {contact['name']} at {contact['phone']}...")
        else:
            print(f"Contact '{contact_name}' not found!")
    
    def check_battery(self):
        """Check current battery level"""
        print(f"Battery: {self.battery_level}%")
        return self.battery_level
    
    def charge(self, amount=30):
        """
        Charge the phone battery
        
        Args:
            amount (int): Amount to charge (default: 30)
        """
        self.battery_level = min(100, self.battery_level + amount)
        print(f"⚡ Battery charged to {self.battery_level}%")
    
    # Encapsulation: Getter method for private attribute
    def get_serial_number(self):
        """Get the phone's serial number"""
        return self.__serial_number
    
    # Encapsulation: Getter and Setter for protected price
    def get_price(self):
        """Get the phone price"""
        return self._price
    
    def set_price(self, new_price):
        """Set a new price with validation"""
        if new_price > 0:
            self._price = new_price
            print(f"Price updated to ${new_price}")
        else:
            print("Price must be positive!")
    
    def get_phone_info(self):
        """Get comprehensive phone information"""
        return {
            "Brand": self.brand,
            "Model": self.model,
            "Price": f"${self._price}",
            "Storage": f"{self.storage}GB",
            "Power": "ON" if self.is_on else "OFF",
            "Battery": f"{self.battery_level}%",
            "Apps": len(self.apps_installed),
            "Contacts": len(self.contacts),
            "Serial": self.get_serial_number()
        }
    
    def __str__(self):
        """String representation of the smartphone"""
        return f"{self.brand} {self.model} ({self.storage}GB) - ${self._price}"
    
    @classmethod
    def get_total_phones(cls):
        """Class method to get total number of phones created"""
        return cls.total_phones
    
def main():
    """Demonstrate the Smartphone class functionality"""
    print("SMARTPHONE CLASS DEMONSTRATION")
    print("=" * 40)
    
    # Create smartphone objects with different attributes
    print("\nCreating Smartphones:")
    phone1 = Smartphone("Apple", "iPhone 15", 999.99, 256)
    phone2 = Smartphone("Samsung", "Galaxy S23", 799.99, 128)
    
    # Test basic functionality
    print("\nTesting Basic Functions:")
    phone1.power_on()
    phone1.check_battery()
    
    # Test app installation
    print("\nTesting App Installation:")
    phone1.install_app("WhatsApp")
    phone1.install_app("Instagram")
    phone1.install_app("WhatsApp")  # Try to install again
    
    # Test contacts and calling
    print("\nTesting Contacts and Calling:")
    phone1.add_contact("John Doe", "+1-234-567-8901")
    phone1.add_contact("Jane Smith", "+1-234-567-8902")
    phone1.make_call("John Doe")
    phone1.check_battery()  # Check battery after call
    
    # Test encapsulation
    print("\nTesting Encapsulation:")
    print(f"Public attribute - Brand: {phone1.brand}")
    print(f"Protected attribute - Price: {phone1.get_price()}")
    phone1.set_price(899.99)  # Update price using setter
    print(f"Private attribute - Serial: {phone1.get_serial_number()}")
    
    # Test charging
    print("\n⚡ Testing Charging:")
    phone1.charge(20)
    
    # Display phone information
    print("\nPhone Information:")
    info = phone1.get_phone_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # Test second phone
    print(f"\nSecond Phone: {phone2}")
    phone2.power_on()
    phone2.install_app("TikTok")
    
    # Show class variable
    print(f"\nTotal phones created: {Smartphone.get_total_phones()}")
    
    print("\nAll OOP concepts demonstrated:")
    print("  • Class creation with attributes and methods")
    print("  • Constructor initialization with parameters")
    print("  • Public, protected, and private attributes (encapsulation)")
    print("  • Instance methods and class methods")
    print("  • Object state management")


if __name__ == "__main__":
    main()
