# Charecters & background
player = codesters.Sprite("gum packet")

object = codesters.Sprite("gum")
object = codesters.Sprite("hand")

stage = StageClass()
set_background("school")



# Controls 

player.event_key("Up arrow", up)
player.event_key("Down arrow", down)
player.event_key("Right arrow", right)
player.event_key("Left arrow", left)