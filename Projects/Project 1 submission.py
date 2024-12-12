###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("blue flower")

q1 = codesters . Square (100, 100, 200, 'light blue')
q2 = codesters . Square ( -100, 100, 200, 'white')
q3 = codesters . Square (-100, -100, 200, 'light blue')
q4 = codesters . Square (100, -100, 200, 'white')

s1 = codesters . Sprite ("cartoon whisk" , 100, 100)
s1. set_size(0.5)
s2 = codesters . Sprite ("Orca 2" , -100, -130)
s2. set_size(0.2)
s3 = codesters . Sprite ("Ivy leaf" , 100, -100)
s3.set_size(0.2)
s4 = codesters . Sprite ("Soccer ball", -100, 100)
s4.set_size(0.1)

message1 = codesters.Text( "Ivy" ,0,220,"Dark blue")
message2 = codesters. Text("Don't talk to me" , 0,-220,"black")