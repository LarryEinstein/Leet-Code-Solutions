# python/dunder_examples.py

class PhoneNumber:
    def __init__(self, digits: str):
        """This runs automatically when creating a new PhoneNumber object"""
        self.digits = digits
        print(f"Creating new phone number with digits: {digits}")
    
    def __str__(self) -> str:
        """This defines how the object is printed"""
        return f"Phone number: {self.digits}"
    
    def __len__(self) -> int:
        """This defines how to get the length of the object"""
        return len(self.digits)

if __name__ == "__main__":
    # Create a new phone number
    phone = PhoneNumber("23")
    
    # __str__ example
    print(phone)  # This will print "Phone number: 23"
    
    # __len__ example
    print(f"Length of phone number: {len(phone)}")  # This will print "Length of phone number: 2" 