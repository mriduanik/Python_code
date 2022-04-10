try:
    age=int(input("age"))
    print(age)
    income=2000
    risk=income/age
except ValueError:
    print("invalid error")
except ZeroDivisionError:
    print("age cannot by zieo")