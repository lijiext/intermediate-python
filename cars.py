# import importlib
# importlib.reload(cars)

class Car:
    runs = True
    number_of_wheels = 4

    # 构造方法
    def __init__(self, name):
        self.name = name
        print(f"Does Run? {self.runs}")

    def __str__(self):
        return f"My Car the {self.name} currently {self.runs}"

    def __repr__(self):
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f"Car {self.name} is started")
        else:
            print(f"Car {self.name} is broken")

    # 类型的方法，无需实例调用
    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels
