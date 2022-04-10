class point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1=point()
point1.draw()
point1.x=10
print(point1.x)