    # Section 1:Setup
import random
import codesters
from codesters import StageClass
stage = StageClass()
stage.disable_all_walls()

stage.set_background("school")
player = codesters.Sprite("gum packet",0, -160)
player.set_size(0.5)

object_speed = 3
points = 0

# Section 2: Objects 

def falling_object():
    global object_speed, object1
    if points >= 0: # the game is NOT over
    
        x = random.randint(-200, 200)
        
        object = codesters.Sprite("gum", x,500)
        object.set_size(0.3)
        object. go_to(x,250)
        object.set_y_speed(-object_speed) 

stage.event_interval (falling_object, 5)

# Section 3: Collision

def collision(player, object) :
    global points
    
    if object.get_image_name() == "gum":
        stage.remove_sprite(object)
        points+=1
        if points >= 0:
            player.say(f"{points} points",0.5)
        else:
            player.say(f"Out of gum - You lose!",5)
player.event_collision(collision)

# object_speed +=0.5


# Section 4: Controls

def go_right():
    player.move_right(4)

player.event_key("right", go_right)

def go_left():
    player.move_left(4)

player.event_key("left", go_left)

def go_up():
    player.move_up(4)

player.event_key("up", go_up)

def go_down():
    player.move_down(4)

player.event_key("down", go_down)

# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play") 