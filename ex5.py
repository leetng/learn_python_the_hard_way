my_name = 'leetng'
my_age = 28
my_height = 160 # cm
my_weight = 50 # kg
my_eyes_color = 'Black'
my_teeth_color = 'White'
my_hair_color = 'Black'

# fixed, must be version 3.6 or newer
# something is wrong below

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cms tall.")
print(f"He's {my_weight} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes_color} eyes and {my_hair_color} hair.")
print(f"His teeth are usually {my_teeth_color} depending on the drinks.")

# this line is tricky, try to get it exactly right

total = my_age + my_weight + my_height
print(f"If I add {my_age}, {my_weight}, and {my_height} I get {total}.")
