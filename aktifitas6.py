class student:
    def __init__(self,n,a,k):
        self.name=n
        self.age=a
        self.kelas=k
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_kelas(self):
        return self.kelas
f = student("Esa Noer Fadhila", 21, "4ASISTEL")
print(f.get_name())
print(f.get_age())
print(f.get_kelas())