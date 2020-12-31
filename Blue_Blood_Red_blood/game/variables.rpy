# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#global variables
#for Kolya
define kolya = Character("Kolya")

#for kiril & Kiril's full pictures
define kiril_full = Character("Kiril")
define stranger= Character("Stranger")

#variable for Vladimir full
define vladimir_full = Character("Vladimir")


#side image for kiril.
define kiril = Character("Kiril", image="kiril")
image side kiril normal = "Side_Kiril_Normal.png"
image side kiril smile = "Side_Kiril_Smile.png"
image side kiril talk = "Side_Kiril_Talk.png"
image side kiril angry = "Side_Kiril_Angry.png"

#side images for vladimir
define vladimir = Character("Vladimir", image="vladimir")
image side vladimir normal = "Vladimir_side_normal.png"
image side vladimir smile = "Vladimir_side_smile.png"
image side vladimir talk = "Vladimir_side_talk.png"
image side vladimir angry = "Vladimir_side_angry.png"
