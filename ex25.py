def print_num(x):
    print("Num is", x)

rename_print = print_num
rename_print(100)
print_num(100)

color = "Red"

corvette = {
    "color": color
    }

print("LITTLE", corvette["color"], "CORVETTE")

def run():
    print("VROOM")

corvette = {
    "color": "Red",
    "run": run
    }

print("My", corvette["color"], "can go")
corvette["run"]()
