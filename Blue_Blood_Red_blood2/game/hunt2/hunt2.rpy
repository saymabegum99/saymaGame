###########
# SCREENS #

#screen crosshair1:
    #imagebutton:
    #    idle "hunt/crosshair_focused.png"
    #    xpos 200 ypos 50
    #    focus_mask True at q_move7
    #    action None


##########
# IMAGES #


image target05:
    "hunt/crosshair_focused.png"


image target06:
    "hunt/target_board.png"



##############
# TRANSFORMS #


transform q_move03:
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
transform moving_target03:

    ##change target position.
    xpos 0
    ypos 50

transform mark03 (id):
    xpos 0
    ypos id * 30

##################################################
# LABELS SUPPOSED TO BE CALLED AND RETURNED FROM #

label begin_hunt03:
    ## calls this function to the main script file in label hello3
    #show screen crosshair1
    $ shots_fired03 = 0
    $ targets_hit03 = 0

    while shots_fired03 < 1:

        call hunting03

        # This is a special variable returned from the last call

            ##(Struggled coding the gun game, got help from a discord server
            ##(made by the owners of Renpy) which helped me to debug my code.)
            ## 6.	Kong, A. K. (2021, March 31). Join the Ren’Py Discord Server!
            ## Discord. https://discord.com/invite/pZ8NuSCXmj
            ## This makes a green box if you hit and a red box if you missed.

            # This is a special variable returned from the last call
            ## This makes a green box if you hit and a red box if you missed.
        if _return: # Good result
            $ targets_hit03 += 1
            $ renpy.show ('', at_list=[mark03(shots_fired03)], layer='master', what=Solid('#00FF00', xsize=24, ysize=24), zorder=50, tag='mark%d'%shots_fired03)

        else:       # bad result
            $ renpy.show ('', at_list=[mark03(shots_fired03)], layer='master', what=Solid('#FF0000', xsize=24, ysize=24), zorder=50, tag='mark%d'%shots_fired03)

        $ shots_fired03 += 1

    return targets_hit03


label hunting03:

    #show target at moving_target

    $ position05 = At('target05', q_move03)
    $ position06 = At('target06', moving_target03)
    show expression position06
    show expression position05

    #show screen crosshair1   # I don't get this part. You'd probably want to
    #show expression position # just change your mouse pointer picture here

    pause # This waits for you to click (actually to proceed)

    hide target05
    # $ renpy.notify (position.xpos)

    ## if the position is between 640 and 740 then you hit the target.
    if position05.xpos >= 640 and position05.xpos <= 740:

        with vpunch
        $ renpy.notify ("You Hit.")

        return True

    with vpunch
    $ renpy.notify ("You Missed.")

    return False


####################
# Normal game flow #
