class FirebaseClient:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = FirebaseClient("John", 36)
print(p1.name)
print(p1.age)
