number=5
guess_counta=0
guess_limit=3
while guess_counta<guess_limit:
    guss=int(input("guess number"))
    guess_counta+=1
    if  number==guss:
        print("won")
        break
else:
    print("you loos")

