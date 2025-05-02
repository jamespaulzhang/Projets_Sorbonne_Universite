
from robot import * 

nb_robots = 0
debug = True

class Robot_player(Robot):

    team_name = "HateBot"
    robot_id = -1
    iteration = 0

    def __init__(self, x_0, y_0, theta_0, name="n/a", team="n/a"):
        global nb_robots
        self.robot_id = nb_robots
        nb_robots+=1
        super().__init__(x_0, y_0, theta_0, name=name, team=team)

    def step(self, sensors, sensor_view=None, sensor_robot=None, sensor_team=None):
        print(sensors)
        sensor_to_wall = []
        sensor_to_robot = []
        for i in range (0,8):
            if  sensor_view[i] == 1:
                sensor_to_wall.append( sensors[i] )
                sensor_to_robot.append(1.0)
            elif  sensor_view[i] == 2:
                sensor_to_wall.append( 1.0 )
                sensor_to_robot.append( sensors[i] )
            else:
                sensor_to_wall.append(1.0)
                sensor_to_robot.append(1.0)

        if debug == True:
            if self.iteration % 100 == 0:
                print ("Robot",self.robot_id," (team "+str(self.team_name)+")","at step",self.iteration,":")
                print ("\tsensors (distance, max is 1.0)  =",sensors)
                print ("\t\tsensors to wall  =",sensor_to_wall)
                print ("\t\tsensors to robot =",sensor_to_robot)
                print ("\ttype (0:empty, 1:wall, 2:robot) =",sensor_view)
                print ("\trobot's name (if relevant)      =",sensor_robot)
                print ("\trobot's team (if relevant)      =",sensor_team)


        translation = sensor_to_robot[sensor_front]

        rotation = (
            sensor_to_robot[sensor_front_right] * (-1) +  
            sensor_to_robot[sensor_right] * (-1) +        
            sensor_to_robot[sensor_rear_right] * (-1) + 
            
            sensor_to_robot[sensor_front_left] * (1) +    
            sensor_to_robot[sensor_left] * (1) +         
            sensor_to_robot[sensor_rear_left] * (1) +

            sensor_to_robot[sensor_front] * (-1) +
            sensor_to_robot[sensor_rear] * (1)
        )

        
        translation = max(-1,min(translation,1))
        rotation = max(-1, min(rotation, 1))

        self.iteration = self.iteration + 1        
        return translation, rotation, False
