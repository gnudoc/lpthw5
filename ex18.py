# this bit is like the script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok so *args is a bit pointless? we can just do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this bit just takes one argument
def print_1(arg1):
    print(f"arg1: {arg1}")

# this one has no args
def print_none():
    print("I got nothin'.")

print_two("nij", "pij")
print_two_again("nijjy","pijjy")
print_1("This!")
print_none()
