class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
       print("hihi",self.name)

john=Person("Mridula")
john.talk()
bob=Person("bob")
bob.talk()