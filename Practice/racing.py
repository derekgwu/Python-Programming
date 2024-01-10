import math
import random

class Car():
    def __init__(self, name, speed, control, weight):
        self.name = name
        self.speed = speed
        self.control = control
        self.weight = weight
    
    def compute_time(this):
        total_time = 0
        for lap in range(0,50):
            lap_time = (this.weight * 0.9) - (this.speed *0.8)
            rand_control = 100 - this.control
            lap_time += (random.randrange(1, rand_control))
            total_time += lap_time
            this.convert_time(total_time)

    def convert_time(this, total_time):
        totalmin = math.floor(total_time/60)
        totalmin_str = str(totalmin)
        if totalmin < 10:
            totalmin_str = "0" + totalmin_str
        totalsec = math.floor(total_time - (totalmin*60))
        totalsec_str = str(totalsec)
        if totalsec < 10:
            totalsec_str = "0" + totalsec_str

        print("CURRENT TIME: " + totalmin_str + ":" + totalsec_str)
    
    def set_name():
        None


class Bullet(Car):
    def __init__(self, name):
        super().__init__(name, 70, 30, 50)

    
class Precision(Car):
    def __init__(self, name):
        super().__init__(name, 50, 70, 70)
        #good control
        #ok speed
        #bad weight
        
class Feather(Car):
    def __init__(self, name):
        super().__init__(name, 30, 50, 30)

def play():
    input2 = input("Please Name Your Car: ")
    input1 = input("Please Select Your Car: ")
    user_car = None
    if input1 == "Bullet":
        user_car = Bullet(input2)
    elif input1 == "Feather":
        user_car = Feather(input2)
    elif input1 == "Precision":
        user_car = Precision(input2)
    print("Racing your car: ")
    user_car.compute_time()

        



play()
