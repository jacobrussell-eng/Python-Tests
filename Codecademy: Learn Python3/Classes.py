""" 1: Setting up our Robot
Create a Robot class with a constructor and the three instance variables: 'Motor Speed', 'Direction', 'Sense Range'
"""
"""
class DriveBot():
    def __init__(self, motor_speed, direction, sense_range):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sense_range = sense_range

robot_1 = DriveBot(5,90,10)
"""

""" 2: Adding Robot Logic
Create a control_bot method to change speed and direction, and a method adjust_sensor to change the sensor range
"""
"""
class DriveBot():
    def __init__(self, motor_speed, direction, sense_range):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sense_range = sense_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_range):
        self.sense_range = new_range

"""
""" 3: Adding Defaults
Include default values within the constructor function in case users don't provide them
"""
"""
class DriveBot():
    def __init__(self, motor_speed=0, direction=180, sense_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sense_range = sense_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_range):
        self.sense_range = new_range

"""
""" 4: Controlling Them All
Add a new feature that allows the user to control multiple robots at once. 
The robots should be able to all have the same latitude and longitude GPS destination coordinates as well as a setting for disabling them all called all_disabled.
"""
"""
class DriveBot():
    all_disabled = False
    latitude = -999999
    longitude = -999999
    def __init__(self, motor_speed=0, direction=180, sense_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sense_range = sense_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_range):
        self.sense_range = new_range

DriveBot.longitude = -79.98553
DriveBot.latitude = 40.60793
DriveBot.all_disabled = False

"""
""" 5: Identifying Robots
In order to keep track of the robots we are creating, we want to be able to assign an ID value to each robot when it is created. 
If we create five robots in a row, we want the IDs of each robot to be 1, 2, 3, 4, and 5 respectively. 
This can be accomplished by using a class variable counter which increments and is assigned to an instance variable for the ID whenever the constructor is called.
"""
class DriveBot():
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
    def __init__(self, motor_speed=0, direction=180, sense_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sense_range = sense_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_range):
        self.sense_range = new_range
