from sturdystarter import SturdyBot
import time
import random
import ev3dev.ev3 as ev3

config = {SturdyBot.LEFT_MOTOR: 'outC',
       SturdyBot.RIGHT_MOTOR: 'outB',
       SturdyBot.SERVO_MOTOR: 'outD',
       SturdyBot.LEFT_TOUCH: 'in4',
       SturdyBot.RIGHT_TOUCH: 'in1',
       SturdyBot.COLOR_SENSOR: 'in2',
       #SturdyBot.GYRO_SENSOR: 'in1',
       SturdyBot.ULTRA_SENSOR: 'in3'}

robot = SturdyBot('Robot', config)

button = ev3.Button()

def EscapeBox():
  robot.leftPointer(.25,450)
  left = robot.readAmbient()
  print(left)
  robot.zeroPointer()
  mid = robot.readAmbient()
  print(mid)
  robot.rightPointer(.25,450)
  right = robot.readAmbient()
  print(right)
  robot.zeroPointer()

  time.sleep(.2)

  if left > mid:
    robot.turnLeft(.25,500)
    direction = 'left'
  elif right > mid:
    robot.turnRight(.25,500)
    direction = 'right'
  else:
    direction = 'straight'

  time.sleep(.2)

  if robot.readDistance() < 20 or robot.leftTouch.is_pressed or robot.rightTouch.is_pressed:
    print(robot.readDistance())
    if direction == 'left':
      robot.curve(-.5,-.25,1000)
    elif direction == 'right':
      robot.curve(-.25,-.5,1000)
    else:
      if left > right:
        robot.curve(-.5,-.25,1000)
      elif right > left:
        robot.curve(-.25,-.5,1000)

  time.sleep(.2)

  print('made it here')
  robot.forward(.25,1000)

  if left >= 3 and right >= 3 and mid >=3:
    robot.beep()
    return True

  return False





# -----------------------------------------------------
found = False
while not found or button.any():
  print('looping')
  found = EscapeBox()

