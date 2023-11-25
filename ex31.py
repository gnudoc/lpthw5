from dis import dis

#dis('''
people = 30
cars = 40
trucks = 15


if cars > people:
    print("we should take the cars.")
elif cars < people:
    print("we shouldn't take the cars.")
else:
    print("we can't decide")

if trucks > cars:
    print("too many trucks.")
elif trucks < cars:
    print("maybe take the trucks?")
else:
    print("still can't decide.")

if people > trucks:
    print("alright, we'll take the trucks.")
else:
    print("fine, we'll just stay at home.")
#''')
