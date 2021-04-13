###########
# SCREENS #

#screen crosshair1:
    #imagebutton:
    #    idle "hunt/crosshair_focused.png"
    #    xpos 200 ypos 50
    #    focus_mask True at q_move7
    #    action None

############ REFERENCES #################

## Code used and edited from (Code is royalty Free and in the public domain) :
## ColoradoStark. (2017, January 24). ColoradoStark/Renpy_Shooter.
## GitHub. https://github.com/ColoradoStark/Renpy_Shooter

##########
# IMAGES #


image target01:
    "hunt/crosshair_focused.png"


image target02:
    "hunt/target.png"



##############
# TRANSFORMS #


transform q_move01:
    ypos 200
    xanchor 200
    ##change
    ##this is to move (code below), moving target will be later.
    linear 1.5 xpos 900
    linear 3.0 xpos 0
    linear 1.5 xpos 350
    repeat

transform moving_target01:

    ##change target position.
    xpos 550
    ypos 200

transform mark01 (id):
    xpos 0
    ypos id * 30

##################################################
# LABELS SUPPOSED TO BE CALLED AND RETURNED FROM #

label begin_hunt01:

    ## calls this function to the main script file in label hello1
    #show screen crosshair1
    $ shots_fired01 = 0
    $ targets_hit01 = 0

    while shots_fired01 < 3:

        call hunting01
        ##(Struggled coding the gun game, got help from a discord server
        ##(made by the owners of Renpy) which helped me to debug my code.)
        ## 6.	Kong, A. K. (2021, March 31). Join the Ren’Py Discord Server!
        ## Discord. https://discord.com/invite/pZ8NuSCXmj



        # This is a special variable returned from the last call

        ## This makes a green box if you hit and a red box if you missed.
        if _return: # Good result
            $ targets_hit01 += 1
            $ renpy.show ('', at_list=[mark02(shots_fired01)], layer='master', what=Solid('#00FF00', xsize=24, ysize=24), zorder=50, tag='mark%d'%shots_fired01)

        else:       # bad result
            $ renpy.show ('', at_list=[mark02(shots_fired01)], layer='master', what=Solid('#FF0000', xsize=24, ysize=24), zorder=50, tag='mark%d'%shots_fired01)

        $ shots_fired01 += 1

    return targets_hit01

## if you shot, even if you hit or miss it will + 1, since you only have 3 turns

label hunting01:

    #show target at moving_target

    $ position00 = At('target01', q_move01)
    $ position01 = At('target02', moving_target01)
    show expression position01
    show expression position00


    pause # This waits for you to click (actually to proceed)

    hide target01
    # $ renpy.notify (position.xpos)

    ## if the position is between 640 and 740 then you hit the target.
    if position00.xpos >= 640 and position00.xpos <= 740:

        with vpunch
        $ renpy.notify ("You Hit.")
        ## gives you a message whether you hit or missed on the top left of the screen.

        return True

    with vpunch
    $ renpy.notify ("You Missed.")

    return False


####################
# Normal game flow #
