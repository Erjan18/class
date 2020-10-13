class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = 0
    def decription(self):
        return f'{self.make} {self.model} {self.year}'

    def update_odometer_reading(self,km):
       if km >=self.odmeter_reading:
           self.odmeter_reading = km
       else:
           print('не шути шуточки')
    def increment_odometer(self,km):
        self.odmeter_reading += km

    def odometer_response(self):
        return f'Пробег вашего автомабиля {self.odmeter_reading}'

class Battery:
    def __init__(self,battery=100):
        self.battary = Battery

    def battery_desription(self):
        print(f'У вашего автомабиля аккамулятор  {self.battary} % заряд аккумулятора')

class ElectronicslCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = 100
    def battery_desription(self):
        print(f'У вашего автомабиля аккамулятор на {self.battery} процентов')

    def desription(self):
        print(f'{self.model} {self.year}')

    def power(self,km):
        result = km // 10
        self.battery -= result
        return self.battery_desription()
tesla = ElectronicslCar('Tesl','X','2019')
tesla.battery = 25
tesla.power(240)