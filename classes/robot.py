class Robot:
    def __init__(self, name, model_num, battery_type ):
        self.name = name
        self.age = 0
        self.model_num = model_num
        self.battery_type = battery_type

    def lasers (self):
        return "PEW PEW PEW"
    
    def greeting (self):
        return f'Hi my name is {self.name}, how can I help you today'