Opp_points = 0
Bestie_points = 0


answer = input ("Do you glaze JJ crawford A yes) or B no)")
if answer == "A":
    Opp_points += 1
elif answer == "B":
    Bestie_points += 1


answer = input ("Do you smack when you eat?) A yes ) or B no)")
if answer == "A":
    Opp_points += 1
elif answer == "B":
    Bestie_points += 1


answer = input ("You don't talk bad about you freinds) A yes) or B no)")
if answer == "A":
    Bestie_points += 1
elif answer == "B":
    Opp_points += 1


answer = input ("Do you aggressively play fight with your freinds at school?) A yes) or B no)")
if answer == "A":
    Opp_points += 1
elif answer == "B":
    Bestie_points += 1


answer = input ("You always want compliments) A yes) or B no)")
if answer == "A":
    Opp_points += 1
elif answer == "B":
    Bestie_points += 1

if Opp_points > Bestie_points:
    print ("You are an Opp")
elif Bestie_points > Opp_points:
    print ("You are a new Bestie")
elif Opp_points == Bestie_points:
    print ("Im not sure of you")