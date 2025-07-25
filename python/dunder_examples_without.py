# python/dunder_examples_without.py

class PhoneNumber:
    def set_digits(self, digits: str):
        self.digits = digits
        print(f"Setting phone number digits to: {digits}")
    
    def get_string_representation(self) -> str:
        return f"Phone number: {self.digits}"
    
    def get_length(self) -> int:
        return len(self.digits)

if __name__ == "__main__":
    # Create a new phone number
    phone = PhoneNumber()
    phone.set_digits("23")  # We have to explicitly call this instead of __init__
    
    # Print example (without __str__)
    print(phone.get_string_representation())  # We have to explicitly call this instead of print(phone)
    
    # Length example (without __len__)
    print(f"Length of phone number: {phone.get_length()}")  # We have to explicitly call this instead of len(phone)
    
    # Try to print the object directly (this will show the default Python object representation)
    print(f"Direct print of object: {phone}")  # This will print something like <__main__.PhoneNumber object at 0x...> 