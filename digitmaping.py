phone=input("Phone: ")
digit_maping={
    "1": "One",
    "2": "Two",
    "3": "three",
    "4": "four"

}
output=""
for ch in phone:
    output+=digit_maping.get(ch, "!")+" "
print(output)