


command=""
strted=False

while True:
    command=input(">").lower()
    if command=="start":
        if strted:
            print("Car already stared")
        else:
            strted=True
            print("Car started")
    elif command=="stop":
        if not strted:
            print("Car already Stooped")
        else:
            strted=False
            print("Car stopped")
    elif command=="help":
        print("""
start - start the car
stop  - sopt the car
quit  - quit""")
    elif command=="quit":
        print("quit")
        break

else:
    print("sorry dont know")
