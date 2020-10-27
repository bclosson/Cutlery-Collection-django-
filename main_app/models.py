from django.db import models

# Create your models here.
class Cutlery:
    def __init__(self, maker, style, use, steel, price):
        self.maker = maker
        self.style = style
        self.use = use 
        self.steel = steel
        self.price = price

blades = [
    Cutlery('Shun', 'Meat-Cleaver', 'Meat/Bone', 'AUS 8 Stainless Steel', 159.95),
    Cutlery('Asai Enji', 'Fruit/Utility', 'Fruit/Vegetables', 'damascus san mai VG-10 core', 196.00),
    Cutlery('Yoshikazu Ikeda', 'Sushi', 'Sashimi', 'mizu-honyaki shirogami 3 carbon steel', 3500.00)
]