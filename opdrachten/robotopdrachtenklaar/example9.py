from RobotArm import RobotArm
import random
robotArm = RobotArm('exercise 9')
robotArm.speed = 2
for y in range(10):
    for i in range(random.randrange(0, 4)):
        robotArm.moveRight()
    robotArm.grab()
    for x in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(9):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:

