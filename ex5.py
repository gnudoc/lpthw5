name = 'Nij'
age = 39
height = 167
imp_ht = round(height / 2.54)
weight = 80
imp_wt = round(weight / 2.2)
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} cms or {imp_ht} inches tall.")
print(f"He's {weight} kg or {imp_wt} pounds heavy.")
print("That's not too bad.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is apparently tricky
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
