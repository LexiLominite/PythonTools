import rotatescreen
import random
import time

screen = rotatescreen.get_primary_display()

for i in range(1, 10):
    k = random.randint(1, 10)
    time.sleep(1)
    screen.rotate_to(k*90 % 360)