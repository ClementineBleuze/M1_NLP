from utils import check_hexacolor

class Monkey:
    """A monkey."""
    
    # Constructor
    def __init__(self, weight, size, fur_color, species = ""):
        self.species = species
        
        if check_hexacolor(fur_color):
            self.fur_color = fur_color # hexadecimal color value string
        else:
            raise ValueError("The provided fur_color isn't a valid hexadecimal color value string.")
            
        self.size = size
        self.weight = weight
    
    
    # Magic methods
    def __str__(self):
        return f"Monkey ({self.species}), {self.weight}kg, {self.size}cm, fur: {self.fur_color}"
    
    def __repr__(self):
        return __str__(self)
    
    
    # Other methods
    def compute_bmi(self)->float:
        """A method that returns the body mass index of the Monkey. BMI = weight/size²"""
        return self.weight/(self.size**2)
    
    
    
    
    
