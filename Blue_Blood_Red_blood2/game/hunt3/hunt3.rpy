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


image target07:
    "hunt/crosshair_focused.png"


image target08:
    "hunt/target_board.png"



##############
# TRANSFORMS #


transform q_move04:
    ypos 400
    xanchor 200
    ##change
    ##this is to move (code below), moving target will be later.
    linear 1.5 xpos 1100
    linear 3.0 xpos 0
    linear 1.5 xpos 350
    repeat
#    linear 2.0 zoom 0.5
#    linear 2.0 zoom 2
#    repeat
transform moving_target04:

    ##change target position.
    xpos 0
    ypos 50

transform mark04 (id):
    xpos 0
    ypos id * 30

##################################################
# LABELS SUPPOSED TO BE CALLED AND RETURNED FROM #

label begin_hunt04:
    ## calls this function to the main script file in label hello4
    #show screen crosshair1
    $ shots_fired04 = 0
    $ targets_hit04 = 0

    while shots_fired04 < 3:

        call hunting04

        ##(Struggled coding the gun game, got help from a discord server
        ##(made by the owners of Renpy) which helped me to debug my code.)
        ## 6.	Kong, A. K. (2021, March 31). Join the Ren’Py Discord Server!
        ## Discord. https://discord.com/invite/pZ8NuSCXmj

        # This is a special variable returned from the last call

        ## This makes a green box if you hit and a red box if you missed.

        # This is a special variable returned from the last call
        if _return: # Good result
            $ targets_hit04 += 1
            $ renpy.show ('', at_list=[mark04(shots_fired04)], layer='master', what=Solid('#00FF00', xsize=24, ysize=24), zorder=50, tag='mark%d'%shots_fired04)

        else:       # bad result
            $ renpy.show ('', at_list=[mark04(shots_fired04)], layer='master', what=Solid('#FF0000', xsize=24, ysize=24), zorder=50, tag='mark%d'%shots_fired04)

        $ shots_fired04 += 1

    return targets_hit04

## if you shot, even if you hit or miss it will + 1, since you only have 3 turns
label hunting04:

    #show target at moving_target

    $ position07 = At('target07', q_move04)
    $ position08 = At('target08', moving_target04)
    show expression position08
    show expression position07

    #show screen crosshair1   # I don't get this part. You'd probably want to
    #show expression position # just change your mouse pointer picture here

    pause # This waits for you to click (actually to proceed)

    hide target07
    # $ renpy.notify (position.xpos)

    ## if the position is between 640 and 740 then you hit the target.

    if position07.xpos >= 640 and position07.xpos <= 740:

        with vpunch
        $ renpy.notify ("You Hit.")

        return True

    with vpunch
    $ renpy.notify ("You Missed.")

    return False


####################
# Normal game flow #
