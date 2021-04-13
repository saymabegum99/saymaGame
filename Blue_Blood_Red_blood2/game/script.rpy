# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character. ##in Variables section

##Reference for Text animation. (Blinking Text): 3.	Donmai. (2017, June 11).
##text animations - Lemma Soft Forums. Lemmasoft.Renai.Us/.
##https://lemmasoft.renai.us/forums/viewtopic.php?t=44371

## this makes the text bigger and hover a little up and downwards on the screen.
transform text_effect:
    parallel:
        block:

            ##position in the dialogue box.
            xpos 500
            ypos 600
            linear 0.3 xoffset -6 yoffset 5
            linear 0.2 xoffset 4 yoffset -6
            linear 0.4 xoffset 6 yoffset -5
            linear 0.2 xoffset -5 yoffset 3
            linear 0.3 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha 0.1
            linear 1.0 alpha 0.9
            linear 1.0 alpha 0.2
            repeat




# The game starts here.
#Chapter 1: Where it began and where it ended.
#Kolya's flashback.
label start:

    play music "<loop 6.333>sounds/Warfare_despair_mp3.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene background_logo1
    with Fade(2, 1, 6)


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #play music "sounds/battle_sound.mp3"

    # These display lines of dialogue


    scene black_bg
    with Fade(2, 1, 6)

    kolya "The row of nearly-headless men slumped down the trench in the darkest
    hour of the night. It was a blood bath out here, brother killing brother."

    kolya "Some even as young as 16— no younger. They didn’t have a clue."

    scene battlefield_101
    with Fade(2, 1, 6)



    kolya "Of course, none of us knew what we were getting ourselves into.
    It was foolish—everything was foolish! The king, the country, the damned army.
    We were all in it, no turning back now."

    kolya "Nowhere to run and nowhere to hide. Those who fled?"

    kolya "Dead."

    kolya "Froze to death or shot in the head if they were lucky enough and
    those who remained begged for the end,
    for the angel to take us away sooner."

    kolya "Men plagued with gritted teeth and bayonets were left.
    We were freezing, withering away to the bitter depth of winter."

    kolya "You know, I’d never dreamt of winter sneaking
    in to our mother country so quickly, you would never know it was August."

    kolya "Our half-starved bodies barely provided us a coat of warmth,
     the rags that we held on us festered with lice, God damn the lice!
     God damn leeches they were!"

    kolya "We were all leeches, sucking on the edge of life and death itself
    and the three-pound firing canon would not bloody stop.
    I was so sure I’d be a deaf man before I would become a dead one."

    kolya "What were we thinking?"

    show soldier1

    kolya "There he was, the man who I had been waiting for all my life.
    The angel had come to take me away; I was so sure of it."

    kolya "Blond and beautiful, singing strange songs in a strange voice."

    kolya "The gate to the world above is so near.
    I can almost hear it’s hymns in the tunnel of light."

    kolya "Louder, Louder!"

    kolya "Argh!"

    kolya "‘Do it now!’ I screamed at the German."

    kolya "‘Kill me!’"

    kolya "‘Kill me now!’"

    label hello1:
        ## this calls the function of Hunt, from the hunt folder. It's a game where you have
        ##to shoot the soldier.  If you shoot him more than once then it takes you to the next stage.
        ##other wise you have to repeat the game.

        scene battlefield_101
        call begin_hunt01
        if _return > 0: # This is a special variable returned from the last call

            kolya "Crap! I got him."
            hide expression position01
            kolya "God...my head."
            scene black with dissolve

        else:

            kolya "Ah"
            scene dead_scene with Fade (2,1,5)
            jump hello1


    scene hospital_bed
    play music "<loop 6.333>sounds/Ambient_Joy_mp3.mp3"
    with Fade(2, 1, 6)

    # click on the gun three times to shoot, small spinning gun mini game.

    #Flashabck ended, Kolya wakes up at the hospital.
    #Kolya and a strange man are talking, seperated by a hospital curtain.
    kolya "So that's the story."

    kolya "A man begging for his own end."

    kolya "Would you call me a coward? Would you say I'm weak?"

    stranger pic "Why did you want it to bad?"

    kolya "Who wouldn't!?"

    kolya "You say yourself you were there. Isn't Death the ultimate
    equaliser?"

    kolya "What's so wrong in wanting the inevitable?"

    stranger pic "No that isn't what I meann."

    stranger pic "I'm not calling you a coward for anything you went through."

    kolya "No, but you asked why I wanted it."

    stranger pic "Well yes b—"

    kolya "And I answered didn't I?"

    stranger pic "Yes, you answered."

    stranger pic "You are alive now aren't you? Do you still want it?
    Your death I mean?"

    kolya "Yes, I do. Even now..."

    stranger pic "And why is that—?"

    kolya "I just told you, they'll make us go back there soon enough."

    stranger pic "Surely you don't mean that?"

    kolya "Of course I meant it. Don't make me repeat
    myself again for christ's sake."

    stranger pic "No, I'm sorry."

    stranger pic "Don't you have anyone to return to? Surely everyone has someone."

    stranger pic "Son or daughter? A wife? Mother or father? Even siblings?"

    kolya "There's no one—"

    stranger pic "Surely you can't be serious. People like to think emotionally
    ,thinking they're the only one in the world who feels like they do."

    stranger pic "Oh grow up will you? You don't."

    kolya "What did you say!? Have you any idea!?"

    #click to open the curtain..
    show patient
    with Fade(2,1,6)

    kolya "Oh my God..."

    kolya "Kiril."

    show black_bg
    with irisin


    scene chapter1
    with Fade(2,1,6)
    scene kiril_house
    with Fade(2, 1, 6)
    #flashback to the pre war years.
    show kiril_body_talk
    kiril talk "so what's it going to be today?"

    kolya "And good morning to you too!"

    kolya "You haven't told me what's on offer yet."

    kiril talk "Yes, yes morning."

    kiril talk "Well... we have Kasha or
    I can whip up a good Blini if you'd prefer it."

    hide kiril_body_talk
   #first choice that user will make is between foods!
   ##multiple choice, there are two choices a user can pick.
    menu:

        "Kasha please":
            show kiril_body_talk
            kiril talk "Goodness, you've gone so boring Kolya!"
            kolya "Call it a bodily investment haha."
            scene kasha
            #image of kasha
            hide kiril_body_talk
        "I've been on savoury foods for far too long, Blini.":
            show kiril_body_talk
            kiril talk "Ah yeah! Now were talking!"
            kolya "Need to compensate the lack of sweetness in our lives
            some how right?"
            scene blini

            hide kiril_body_talk
            #image of blini/pancake

    label after_menu:
    kolya "Thanks Kiril, I really mean it."

    kolya "I don't want to be a burden or anything. Just give me the world
    and I'll leave. You wont even notice I'm gone."

    kiril talk "Relax will you Kolya, it's all right. Just help me pay the
    rent and we'll make it work."

    kolya "I'd never thought everything would result into this... you know?"

    kolya "Anyway rent? That's easy. I just need a job."

    kiril smile "Of course! Everything is easy for a {i}clever{/i} man like you.
    You're all brains!"

    kolya "What about you?"

    kolya "All fun and games, no work and no study."

    kiril smile "Well I like to say I excel in practical knowledge and
    common sense!"

    kolya "So then, I take it you didn't have enough commen sense
    regarding the fact I'm squatting in your house."

    kiril smile "Well at least it's not both of us squatting. I am practically
    the owner you know."

    kolya "No you're not."

    kolya "It's your father who owns these four walls, not you."

    kiril talk "Well yes, but they did leave it under my care."

    kolya "They did, did they? And where are they now?"

    kiril talk "Relax, there on a business trip and won't be back for a few
    weeks."

    kolya "And they don't know I'm here do they?"

    kiril smile "I said relax, good grief. No they don't but I don't see why
    they won't approve. We've known each other for years!"

    kolya "Almost two decades, on and off actually. God I can't stay here, what
    was I thinking?"

    kiril "No don't say that."

    kolya "But it's true! My parents! You! How can I be so clueless?"

    kiril talk "God will you just learn to do as I say!"

    kiril "I have a plan."

    kolya "And what is that? This is not the time for one of your rubbish
    plans. Were not in high school anymore! You just don't understand!"

    kiril angry "Eat your breakfast and listen will you!?"

    kiril "I've decided to join the army and I think you should too..."

    kolya "You've gone insane! Have you gone mad? That's the very reason why
    I left them!"

    kiril talk "Come on, you're in the capital! Out of everything you could've
    picked, you've picked the one place where they're bound to conscript you."

    kiril smile "Lacking in common sense and practicality or what? Haha."

    kolya "I had no choice, it's where you live!"

    kiril smile "So you left because of me? How sweet!"

    kolya "Don't get it twisted! I don't know anyone else."

    kolya "Would you want to live your entire life knowing you were born to pay back the very
    people who used to own you and your ancestors?"

    kiril "Course not, I'm not sure of a single person in the world who would."

    kolya "I don't even know if I even have a single friend left on this planet
    to tell you the truth, did I even have one to start with? I can't recall."

    kiril "Look, come to the registration office with me today, it's still
    bright and early. You'll feel different about it, I promise you."

    kolya "I already told you— No."

    kolya "I'll get a job in a factory or whatever else. My uncle Lev did that,
    I suppose I could too. It's worth a try. I think I'm good with a—"

    kiril "No, Kolya stop."

    kiril "You'd rather rot in hell than work there, trust me. Don't you think
    I'd try that?"

    kolya "You? What were you doing in a factory? I've always imagined you in
    one of your father's offices."

    kiril "Since when has this conversation been about me? You're better
    off being a lousy farmer and someone else's dog than working in a factory!"

    kolya "So that's what you thought of me?"

    kiril "No—"

    kolya "They did everything they could to make me join, what makes you think
    I'd join after suffering that."

    kiril "That's easy, they're your parents and not me! So stop this whining."

    kiril "Call your parents tomorrow, I'm sure they'll be thrilled. You'll be
    free of them the moment you join."

    kolya "Ah, great. Now I really can't join."

    kiril talk "Better join sooner rather than later. Don't want to get
    classed as the poor farmer boy who never held a weapon in his life, do you?"

    kolya "I don't care for these things, I've already had enough of it
    from my family and I do not need it from you. Take it in long enough and
    it becomes meaningless."

    kolya "The world's gone meaningless. The last thing I wanted is to become
    as slave!"

    kolya "It's all the same, my parents, the army, factories. I wonder when humans will
    learn to cherish each other rather than rule over one another."

    kiril talk "Okay, I guess we talked about it for long enough now. You
    haven't eaten a bite yet. Come on, you look like you haven't eaten in days!"

    kiril smile "Eat up now and save the worries for another time."

    kolya "Right, I'm sorry. I've gone off on one haven't I?
    I will eat."

    kiril smile "No problem. Don't worry about it."

    ##FACT CARD 1905 revolution - back drop.
    ## this allows the user to see a newspaper fact card which will pop up on screen.
    label start3:
    screen fact1():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/farmers_discontent.png"
            hover "images/newspaper_facts/farmers_discontent_hover.png"
            focus_mask True
            action None
## this button takes you to the next stage.
        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("fact1_5")

    label callfact1():
    call screen fact1
## calls the labour discontent fact card to pop up.
    label fact1_5:
        screen fact1_5():
            modal True
            imagebutton:
                xpos 300
                ypos 130
                idle "images/newspaper_facts/labourers_discontent.png"
                focus_mask True
                action None

            imagebutton:
                xpos 800
                ypos 570
                idle "images/ok.png"
                hover "images/ok_hover.png"
                focus_mask True
                action Jump("afterFact1")

        label callfact1_5():
        call screen fact1_5
##after the fact card opens, you can click on a link for further information
    label afterFact1:
    kiril smile "Information cited: BBC Bitesize. (n.d.). Russia (1881-1921) -
    Higher History Revision. Retrieved 19 January 2021,{a=https://www.bbc.co.uk/bitesize/guides/zwxv34j/revision/3}for more info!{/a}"

## Chapter 3- Joining the army.
    scene street_path

    kiril talk "You know, you still haven't told me why you're exactly here."

    kiril talk "It would be great if you did, after eating my food, sleeping on
    my sofa, using my bloody loo."

    kolya "Yes, yes I get it all right."

    kolya "I'll leave."

    kolya "First thing tomorrow morning."

    kolya "I'm sorry. I don't mean to intrude on your life, more so your
    parent's."

    kiril "No, no. I don't mean it like that."

    kiril "You're always welcome here, you should know that."

    kiril "Don't worry so much about my kin, they like you but you already knew that."

    kiril "The countless times they'd mention about those God awful nurses
    in the hospital who had swapped you out for me."

    kiril "You still won't talk about it huh?"

    kiril talk "You can't just keep living like this you know?"

    kiril talk "Look at you, so far away from home."

    kiril talk "Any man with a beard could mistake you for one of those kids
    orphaned at bloody sunday."

    kiril smile "Now cheer up. Were buying vegetables not going to a funeral."

    kolya "You don't even have a beard!"

    kiril smile "You're right, I doubt I'd look great in one either."

    kiril "But I'd doubt you'd grow one after all that frowning."

    kiril smile "You'll age faster than rotten cheese!"

    kolya "Ugh."

    kolya "I could fancy some cheese right now actually. The more aged the better!"

    kiril smile "Hah!"

    kolya "I need a strong dose of something in my life."

    kolya "I'd had nothing on the train coming here."

    kiril smile "Well then. Let's get you some food to fill that poor stomach of yours."

    kiril smile "Course mine too! I'm blood starving!"
    ##fact card of 1905 russian revolution
    screen fact2():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/father_gapon.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact2")

    label callfact2():
    call screen fact2

    label afterFact2:
    kiril smile "Information cited: BBC Bitesize. (n.d.). Russia (1881-1921) -
    Higher History Revision. Retrieved 19 January 2021,{a=https://www.bbc.co.uk/bitesize/guides/zwxv34j/revision/6}for more info!{/a}"

    scene street
    with dissolve

    kolya "Weren't we meant to go to the office?"

    kiril talk "Diddn't know you were so eager to?"

    kiril talk "Thought you hated the idea of fighting?"

    kolya "I— I do."

    kolya "Anyway, what do we need?"

    kiril talk "I don't know Kolya, what exactly do you want?"

    kolya "To eat?"

    kiril smile "Yes Kolya, to eat. What else?"

    kolya "All right. I get it."
## choice between food
    menu:

        "A biggest pot of the best beef stroganoff that money can buy!":
            show kiril_body_smile
            kiril smile "You're a wild one Smirnov."
            kiril smile"I'd be a king if I was able to afford that."
            hide kiril_body_smile
        "Soup and bread sounds good to me.":
            show kiril_body_smile
            kiril smile "That sounds great. Such a comfortable meal."
            kiril smile "You've always been so humble in your food choices Kolya
            perhaps because your a village boy at heart."
            hide Kiril_body_smile

    label after_food_Choice:

    show kiril_body_talk

    kiril talk "Well, at least I don't share a room with an
    indecisive mountain goat."

    kolya "Oh come on, you came from the mountains too, albeit long ago."
    hide kiril_body_talk
    show kiril_body_smile

    kiril smile "From Barnaul and don't you forget it!"

    hide kiril_body_smile
    show kiril_body_talk

    kiril talk "But that was my father."
    kiril "I'm from the city,not from the {i}mountains{/i}."

    kolya "What are you trying to say?"

    kolya "That we mountain folk don't belong in the empire?"

    kiril talk "That's not what I meant."

    kiril talk "You know how much I enjoyed staying with you in the summer right?"

    hide kiril_body_talk
    show kiril_body_smile

    kiril smile "I don't know why you're always
    going off on one, were not here to talk, were here to buy!"

    ##Fact card about barnaul.
    screen fact3():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/barnaul_siberia.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact3")

    label callfact3():
    call screen fact3

    label afterFact3:
    kiril smile "Wikipedia contributors. (2021, April 1). Siberia. Wikipedia
    ,{a=https://en.wikipedia.org/wiki/Siberia }for more info!{/a}"

    scene street
    with Fade(2, 1, 6)
    hide kiril_body_smile
    show kiril_body_talk

    kiril talk "Beetroot, cabbage, onions, turnips and tomatoes."

    kiril "There! Perfect for a good borsht."

    kiril talk "Kolya?"

    kiril talk "Where has that ghost boy fled to now?"

    hide kiril_body_talk
    show kiril_body_angry

    kiril angry "Kolya!"

    kolya "I'm here, I'm here!"

    kolya "Went to the bakery to get some bread."

    hide kiril_body_angry
    show kiril_body_talk

    kiril talk "I didn't know you had money on you, why didn't you tell me?"

    kolya "Well, yeah. Can't have you paying for everything now can I?"

    kiril "Perfect! Here carry these."

    kiril "To the recruitment office we go!"

    kolya "Great, while your at that, I'll run back to the house."
    hide kiril_body_talk
    show kiril_body_angry

    kiril angry "Oh no you're not!"

    kolya "Oh yes I am!"

    kiril "You'll go there with me, when we come back from the office."

    hide kiril_body_angry
    show kiril_body_talk

    kiril talk "Besides you don't even know your way back."

    kolya "No, I remember it quite nicely, thanks."

    kiril "Do you want to live with me or not?"

    kiril "Fact of the matter is, were skint."

    kiril "I can't afford things for both of us."

    kolya "Right, heck. In that case I really should be leaving."

    kolya "I don't want to be leeching off you, I've ruined this enough."

    hide kiril_body_talk
    show kiril_body_angry

    kiril angry "No!"

    kiril angry "I swear to God Kolya, if you leave I will forever be guilty."

    hide kiril_body_angry
    show kiril_body_talk

    kiril talk "I'll blame myself every night and day. My best friend, closer
    than a brother living in the streets while I sit in my arm chair sheltered!"

    kiril talk "No, I won't stand for it."

    kiril "For the love of God, please."

    kiril talk "It's for the both of us, you know it and I know it."

    scene library
    with dissolve

    show vladimirbody

    vladimir_1 "I trust you're sending the very best my way."

    vladimir_1 "I accept the best and only the best."

    vladimir_1 "We'll make these young boys into the muscle machine of that which
    sheds blood for the mother country."

    vladimir_1 "You'd be unrecognisable after were through with you."

    vladimir_1 "Ah, new comers, a fresh looking face like yours, you'd make a fine soldier."

    kiril smile "Thank you sir."

    vladimir_1 "That's Sergeant Adibov to you."

    vladimir_1 "As for you..."

    vladimir_1 "Keep sulking like that and boys half your age will learn to
    pounce all over you."

    vladimir_1 "A true soldier shows no fear."

    vladimir_1 "Remember that."

    kiril normal "Forgive him Sergant, he got off the train yesterday night."

    kiril normal "He's still feeling a little stiff."

    vladimir_1 "Well then young lad, he'd better get used to that, I'll say."

    vladimir_1 "Battle is known to be a stiff affair."

    vladimir_1 "Like an ache on ones shoulder."

    vladimir_1 "Stretch it and it cracks, weep and it's futile."

    kiril normal "Yes, of course Sergant."

    kiril talk "Well, we'll be on our way then, if that's all right."

    vladimir_1 "Very well lad, Good luck."

    scene registration
    with dissolve

    kiril smile "Now...God damn it! When is my bloody birthday?"

    kolya "You've forgotten it already?"

    kolya "You've only been born two decades."

    kiril "That's still a lot!"

    kiril talk "You're just saying that to make me feel as old as a tree."

    kolya "Right!"

    kiril "Anyway— come on, aren't you writing?"

    kolya "..."

    kolya "I can't."

    kiril "You've got to be joking!"

    kolya "No, I—"

    kiril "Ah! How could I be this blind!?"

    kolya "You always were blind, blind as a bat I'd say."

    kiril "all right, give me that!"

    kiril "7th of January 1892!"

    kolya "Wait! How'd you remember that?"

    kiril "Come on, who can ever forget that?"

    kiril smile "A birthday on Christmas day, why'd you look at that!"

    kiril "As a kid I was always kind of jealous of you."

    kiril "You know, getting twice the gifts, twice the happiness. Or so I thought."

    kolya "It was nothing like that at all—"

    kiril "Wouldn't that make your mother Mary? And your father like Joseph?"

    kolya "No, my mother's name is Viktoria."

    kiril "Come on, you know I'm only joking right?"

    kolya "No, my mother's nothing like her, absolutely nothing."

    kolya "And my father isn't like Joseph either."

    kolya "Nothing like him at all."

    kiril talk "All right, I get the picture. In that case then, the papers are done."

    kolya "And by the way, it's 189—"

    kiril "Hush! Will you Kolya?"

    kiril "You're lucky, being only a child and all."

    kiril "Hardly a peasant on a farm."

    kiril "While I have to join whether I like it or not. Seen as you're here though..."

    kolya "Yes, yes I know."

    kiril "And you still want to?"

    kolya "What else will I do? What else is there for me?"

    kiril "See?"

    kiril "Now be grateful, had you'd been a decade or so older, you'd of gone to war."

    kiril "To live at relative peace is a blessing."

    kolya "Peace?"

    kiril "Shut up Kolya. Don't make me remind you of Crimea and Japan."

    kiril "Now everythings done, let's just head home."

    ##FACT CARD FOR CONSCRIPTION.

    screen fact4():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/conscription.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact4")

    label callfact4():
    call screen fact4

    label afterFact4:
    kiril smile "Manaev, G. (2020, December 25). How soldiers were DRAFTED into the Imperial Russian Army. Russia Beyond,
    {a= https://www.rbth.com/history/333202-how-soldiers-were-drafted-into-russian-army}for more info!{/a}"

    scene pub
    with Fade(2, 1, 6)
    ##PUB SCENE FOR LATER.
    kiril smile "Wow, it's been ages since I came here. Aren't you going to order?"

    kolya "Well, what do you recomend?"

    kiril "Why am I not surprised? You've never been to one of these haven't you?"

    kolya "No, everyone drinks where they'd like."

    kiril "That explains a lot."

    kolya "Yeah, it does."

    kiril "Let's get you something then, it's on me."

    scene pub
    with vpunch

    kiril smile "Calm down Kolya, don't drink it up all at once."

    scene pub
    with hpunch
    kolya "God, my head. What the crap is this?"

    kiril smile "God look at you, I've never seen you like this before."

    kolya "You don't know a single thing about me."

    kiril "Course I do, we were practically brothers."

    kolya "You're extremely naive sometimes, did you know?"

    kolya "I did disgusting things, physical? Sexual? Disgusting things all the same."

    kiril talk "It's like your heart bursts out of you whenever you speak about that."

    kiril "The burden was forced upon you, it's not your fault, it was never your fault
    to begin with, any of it."

    kolya "What do you know about it? You know nothing."

    kiril "Let's get you home. I think you had enough of that."

    kolya "No, I think I need some more."

    kiril "No you don't. Were going home."

    ##CHAPTER 4

    scene bed
    with Fade(2, 1, 6)

    kolya "Ah. Good grief, where are my clothes?"
## the user cannot move forward until they find an image of his clothes.
    label clothes_game:
    screen char_clothes():
        modal True
        imagebutton:
            idle "find_object_game/clothes.png"
            #hover "images/kiril_Body.png"
            focus_mask True
            action Jump("after_clothes")
            xpos 1194 ypos 454

    ##GAME LOOK FOR THE CLOTHES!
    label call_clothes:
    scene bed
    with dissolve
    call screen char_clothes()
    label after_clothes:
    kolya "All right, it's all or nothing."

    kiril smile "Morning, you ready?"
    ## Kiril_points start with 0 and add up as you play through the game
    ## if you get above 4 then it unlocks a special scene.
    $ kiril_points = 0

    menu:

        "Nervous, I don't know why you forced me to do this.":
            ## add one point for this choice only
            $ kiril_points += 1;
            ## this gives the player a small notification on the top left
            ## of the screen, to indicate they have +1 point
            $ renpy.notify ("Kiril's affection +1")
            kiril smile "Come, on. Don't be like that."
            kiril "How else am I meant to keep you well fed?"

        "Pretty exited and ready as I'll ever be.":
            kiril smile "That's more like it!"
            kiril "It's great seeing a smile on your face for once!"


    label after_how_you_are:

    kiril "Now that were done, let's get going."

    kiril "Oh by the way—"

    kiril "Do you have anything else you want to say to me?"

    kolya "Not that I know of..."

    kiril "Are you sure?"

    kolya "Let's get going or we'll be late."

    kiril "It'll be fine Kolya, really. I'll look after you."

    kolya "That's all you've been doing since I set foot in St Petersburg."

    kolya "You've done nothing less whenever I'm with you."

    kolya "Thanks Kiril."

    kiril smile "You're like a brother to me Kolya, of course."

    kiril "But don't let the others hear that. They might have your head!"

    kiril "Come to think of it, they might have both our heads!"

    scene train
    with Fade(2, 1, 6)

    kiril "You know, I think you'd' make a  great soldier."

    kolya "You've got to be joking."

    kolya "Don't think I entered into this because of that, I didn't."

    kolya "I'd rather had left you're home but that didn't happen because someone
    was to afraid of letting me go."

    kiril smile "Details, details!"

    kolya "I'm not your child, you should've let me go."

    kiril "That's exactly why you'd make a great soldier, loyalty."

    kolya "You're kidding right? You've got to be joking."

    kiril talk "No, I'm not. Loyalty to those whom you care for."

    kiril "I know you don't give a pennies worth for the Tsar, you joined me
    because of me."

    kiril "Great soldiers don't follow because of obligation, it's because
    they have a sense of duty which then becomes an obligation."

    kiril "You'll be a great soldier Kolya, perhaps better than I."

    kolya "What about you?"

    kolya "You may be brash but you're also a kind person."

    kiril "What's the point in being kind? It's human decency to be kind.
    That's nothing special."

    kolya "Great soldiers aren't great because of a title, they're great because
    they sacrifice their lives for the safety and freedom of their people."

    kolya "Now that takes a large amount of kindness, on a scale which is
    hardly normal."

    kiril "I'm not so sure about that, some are extremely self righteous beings."

    kolya "I can guarantee for a fact that does not include you."

    kolya "You're genuine and behave genuinely."

    kiril "You know, I wish we didn't have to do this."

    kiril "I'd rather I escape to the village than you coming over here to
    St Petersburg."

    kolya "I never mentioned I escaped. Was it that obvious?"

    kiril "I've always known. I was just waiting for you to tell me—"

    kolya "I can't, I simply can't."

    kiril "The longer you wait, the harder it will be to get over it—"

    kolya "So you're telling me to get over what they've done to me?
    I hate them, I can't do that Kiril."

    kiril "Thank God, you're finally talking about it, a little at least."

    kiril "As a kid, I've wanted to talk about it for so long, but I couldn't
    make myself."

    kolya "I don't mean you should forgive them, I meant to get over it for
    your sake, for the sake of your future."

    kolya "I'm sorry, I can't."

    kiril "Kolya, my dear brother. I can't sit here and watch you day by day
    sitting and let your mind eat your insides out."

    kiril "You're constantly in a state of anxiety, don't think I haven't noticed."

    kiril "You're destroying yourself Kolya. Stop hating yourself."

    kiril "Promise me you'll talk about it,
    whatever it is that's really bothering you, you need to talk."

    kiril "Talk to anyone, Kolya, anyone!"

    kolya "Now is not the time for talking. Not in a place so full of violence
    and hate."

    kolya "Who exactly am I meant to talk about this too?"

    kiril "Talk to me, God Kolya."

    kiril "Promise me that one day you will."

    kolya "All right, I promise."

    kiril "Good, and just in time too, we've finally arrived."

    scene battlefield_old
    with dissolve

    show vladimir_body_talk

    vladimir_1 "Now to the left you'll see the bathroom, to the
    right the kitchen and just in front of you right here, the dorms in which
    you'll be spending these few years, let's hope."

    vladimir_1 "Unless Mother Russia calls us for war. We have no time to lose!"

    vladimir_1 "You will be properly equipt, break what you have been given and
    it will come out of your paycheck."

    vladimir_1 "Breakfast will be every 5 am sharp!"

    vladimir_1 "Lunch at 1 and dinner at 7."

    vladimir_1 "There will be no food left over, let's make that clear.
    You are either there or you're not."

    vladimir_1 "Now, I understand the hall can get a little crowded, you may
    dine outside if you wish."

    vladimir_1 "Training is on every day, accept on a sunday for obvious reasons."

    vladimir_1 "It will start after breakfast, 5:30 AM sharp. I expect every
    single one of you there, on time."

    vladimir_1 "You're names will be called out, if you're not there
    to do your duty, I'll have to file a desertion report."

    vladimir_1 "Now what time is training?"
   ## choice to see if the user was paying attention to the text
    menu:

        "10AM Sharp!":
            show vladimir_body_angry
            vladimir_1 "Think your funny?"
            vladimir_1 "I'd have your face hammered on to a desk."
            hide vladimir_body_angry
        "5.30 AM Sir!":
            show vladimirbody
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            vladimir_1 "That's Sergant to you but nevermind well done,
            you've pass my little attention span exam."
            vladimir_1 "Oh it's you. I see you've shown your brave face
            for once."
            hide vladimirbody

    label after_What_Time:

    vladimir_1 "That is all, you may leave to unpack your things."

    vladimir_1 "We will start training early morning tomorrow to find
    where you lot are in terms of wielding a weapon."

    hide vladimir_body_talk

    scene dorm
    with Fade(2, 1, 6)

    kiril smile "Right, were finally here at last."

    kolya "Right..."

    kiril talk "Don't worry too much about it Kolya."

    kolya "I'll try."

    kiril "Do you want to play a game? There isn't much to do
    now that were here, I've become a litle bored."

    kolya "Depends, what kind of game are you speaking of?"

    kiril "A beautiful lady sits inside a dungeon but her pony is outside,
    how is that so?"

    kolya "God Kiril, you're asking practically the only farmhand in the
    whole camp."

    kiril smile "Prove it! What's the answer?"

    ## choice, if the user answers the riddle correctly they have +1 point

    menu:

        "A horse! Who else has a pony tail?":
            kiril smile "Seems like you've forgotten your humble roots."
            kiril "Get it a root? It's a carrot!"

        "An orange root vegetable hidden under the soil.":
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            kolya "It's a carrot of course."
            kiril smile "So you haven't forgotten your roots!"
            kiril "Roots, get it?"

    label after_riddle1:

    kiril "Haha, your turn now! Go ahead."

    kolya "All right! Let me think, give me a minute."

    kiril "Sure, take all the time you need."

    kolya "A man dressed in a thousand coats makes grown men cry."

    kiril "You've gone too easy on my Kolya. It's an oninon of course!"

    kolya "I get the feeling you know all of these better than the back of your hand."

    kolya "A tug on your boot strap, yet you do not see..."

    kolya "A stranger in town, taking shade under your tree."

    kiril "Are you describing a weed?"

    kolya "Wait, that's not meant to—"

    kiril "I know what's it meant to be. You're quite the poet."

    kolya "You're very good."

    kiril "And since I am, I'll be the one calling it a day. We should sleep."

    kolya "Yes. A busy day ahead of us tomorrow."

    kiril "You're right. Good night then."

    kolya "Night, Kiril."

    scene battlefield_old
    with dissolve

    show vladimir_body_angry

    vladimir_1 "Well then, what are you waiting for?"

    scene battlefield_old

    show vladimir_body_angry

    ##Reference for Text animation. (Blinking Text): 3.	Donmai. (2017, June 11).
    ##text animations - Lemma Soft Forums. Lemmasoft.Renai.Us/.
    ##https://lemmasoft.renai.us/forums/viewtopic.php?t=44371

    show text '{size=50}"Run, RUN!"{/size}' at text_effect

    $ renpy.pause()

    show text '{size=50}"5 laps on the field!"{/size}' at text_effect

    $ renpy.pause()

    hide text

    show vladimirbody
    kiril smile "Come on let's race!"

    kolya "No, I've barely woken up."

    kiril "Well, that's just perfect! 1, 2, 3 ! "

    kiril "Go!!"

    kolya "Kiril!"
    hide vladimirbody
    ## Maze Race Game
    show vladimir_body_angry
    vladimir_1 "Settle down you lot."
    hide vladimir_body_angry
    scene guns_intro

    vladimir_1 "Now that were all here, each of you will pick up one of these."

    vladimir_1 "I want you to keep this as close to you as the way a mother
    is to her child."

    vladimir_1 "Targets will be set up to the front, you will practice firing until
    I examine you all one by one."

    vladimir_1 "Failure to reach a bulls eye and you will remain here until you do."

    vladimir_1 "Now go on, be off with the lot of you."

    scene gun_target_plain

    kiril smile "Hey, do you think I'll get it on the 1st?"

    kolya "You?"

    kolya "No way."

    kiril "What! No belief in your friend?"

    kolya "With your complete lack of patience, I'll prray you even make
    it on the board."

    kiril "Let's see then Mr Foreseer."

    scene gun_target_bullet

    kiril angry "God Damn it, so close!"

    kolya "See what did I tell you?"

    kiril talk "Well, I'd like to see you try, if you're so good at it."

    kolya "I didn't say I was good, but all right. It's all or nothing."

    vladimir_1 "Come on lad, here put your gun on the right side of your
    shoulder."
    ## this calls for another gun game, but the target is off centre 100% of the time
    label hello2:
        scene battlefield_old
        call begin_hunt02
        if _return > 0: # This is a special variable returned from the last call

            kolya "Bloody hell, what happened?"
            scene black with dissolve

        else:

            kolya "Ah"
            scene black with dissolve


    ##GUN GAME. BUT CROSS HAIR ALWAYS NOT LOCATED NEAR TARGET.

    scene gun_target_miss

    kiril talk "Wow! You were off by miles!"

    kolya "God, I was so sure..."

    vladimir_1 "Gracious God, do it again boy!"

    ##PLAY GAME AGAIN, CROSS HAIR STILL NOT ON TARGET.
    vladimir_1 "You'll need a lot of work. No matter, keep practicing."

    kolya "Come on...don't—"

    kolya "Kiril!"

    kiril smile "BAHAHA!"

    kiril smile "I'm sorry. It's just so funny! You were so sure of yourself!"

    kiril "It's okay I'll teach you."

    scene dorm
    with Fade(2, 1, 6)

    kiril smile "Relax, I won't leave you behind."

    kolya "Oh but you will, very soon in fact."

    kiril "How soon?"

    kolya "Tomorrow— soon."

    kiril talk "What? How? What do you mean?"

    kolya " While you were away enjoying your dinner, Sergant Adibov said everyone
    will be moving into physical combat, spare but a few."

    kolya "Well by few, I mean mean me and some others."

    kolya "Today was a simple test on natural talent."

    kiril "Why not you? Won't you join us?"

    kolya "I already told you I'm not. I clearly don't have that natural talent
    he was looking for."

    kiril "Perhaps you'll have learnt talent, that is a lot better in my
    opinion. Your hard work will pay off eventually."

    kolya "No! Don't you see? It's all a lie! He want's us gone!"

    kiril "Calm down for a second. You've only just arrived. Besides, that's
    not how training camps work, I thought you'd know that."

    kolya "You saw how I shot. A pet dog would've had a better chance."

    kiril "Oh come on it's like that old saying, without experience you'd never be able to pull a fish
    out of the pond, you know?"

    kiril "I bet you're a great fisherman."

    kolya "You still don't get it! God damn it."

    kolya "How could I be this clueless? Have you seen the way he looks at me?"

    kolya "How could I be a better archer than a shooter? I thought they Were
    the same. They require the same skills right?"

    kolya "A good eye, a steady hand. You tell me what I'm doing wrong.
    tell me Kiril."

    kiril "Steady? I don't know much, but I do know that hand of yours
    has not been steady since the day we arrived."

    kiril "You did exactly as he said right? That seemed to have worked
    for me."

    kolya "Of course, what doesn't go right for you? You were born lucky."

    kolya "Normal people have to try several times until they hit a sweet spot.
    Not like you who gets it right all in one go."

    kolya "God, I'm a fish out of water."

    kiril "Right, though I think you should listen to your own adivce."

    kolya "What do you think I've been doing all day? I haven't even had dinner
    or a lunch."

    kiril "So that's why I hadn't seen you. I was worried."

    kolya "Sure you were, why didn't you look for me?"

    kiril "The food wasn't as bad as I thought—"

    kolya "Kiril?"

    kiril smile "Let's get up extra early, we can practice out in the range if you want?"

    kolya "All right, thanks Kiril!"

    kiril "The matter is in he hat! Don't let it fall off okay?"

    kiril "If I'm going to wake up extra early, it's a good night from me then."

    kolya "Night Kiril."

    scene battlefield_night

    show target_board

    kiril talk "God Kolya, what time is it again?"

    kolya "4 AM, it was your idea, so quit complaining!"

    kiril "I'm not, I'm just asking! Jeez keep your hat on Kolya."

    kolya "Are you going to show me how it's done or not?"

    kiril "Sure, rest the gun on your right shoulder."

    ##GAME CROSS HAIR NOT ON TARGET MOVING TARGET!.

    kiril "Jeez, it's so windy!"

    kiril "They can't even afford proper boards, just look how flimsy they are!"

    kolya "God damnit, hold the boards will you Kiril?"

    kiril "You've gone mad! You want me to hold the board while you shoot at me?"

    kiril "Do you want me to die?"

    kolya "Is that a trick question?"

    kiril "You're a laugh Kolya, you won't be catching me dead doing that!
    Psht, holding that for you!"

    kolya "Come on, at least help me fix it."

    kiril "Promise you won't shoot while I do?"

    kolya "Come on, do it!"

    kiril "Fine, jeez."

    kolya "You were the one who forced me into this, remember?"

    kiril "Never thought you'd turn into a bloody monster. If I knew, I'd never
    let you—"

    ## choice, you can attempt to shoot at kiril for a joke, but that will
    ## give you - points
    menu:

        "Shoot at Kiril":
            ##+1 point for kiril
            $ kiril_points -= 1;
            $ renpy.notify ("Kiril's affection -1!")
            kiril angry "Good F***ing Lord!"
            kiril "You promised you wouldn't!"
            kolya "It was too good of an opportunity not to miss!"
            kiril talk "Thank the Lord for your terrible aim!"

        "Wait patiently.":
            ##+1 point for kiril
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            kiril "See the light of day!"
            kiril full "Thank the Lord I'm alive!"


    label after_shooting_Choice:
    kolya "I'm terrible!"

    kiril smile "No worries, keep practicing. We have until breakfast."

    kolya "Easy for you to say,an hour is all the time in the world for
    a person like you Kiril."

    kolya "What have I been doing all day yesterday?"

    kiril "All right, I get it."

    kolya "Now I'll never be able to catch up. I'll be left behind, again."

    kiril "That doesn't mean you won't catch up. Come on Kolya."

    kolya "I wish. How on earth were you able to persuade me?"

    scene bath_house_test_night1_v2
    with Fade(2, 1, 6)

    show kiril_body_bruised

    kolya "Ah, there you are."

    kolya "Wait, why on earth is there a bath tub in the kitchen?"

    kiril bruised "I don't know. You bloody tell me."

    kiril "The guys have been saying the building was owned by the Sergant's
    great aunt."

    kolya "Well, that's crazy! I'm guessing they did a half-hearted job at
    renovating the place then?"

    kiril "More like the delivery men were lazy asses."

    kolya "Jesus Kiril! What happened to your face?"

    kiril "Funny story actually..."

    kolya "Come on, spit it out."

    kiril "The Sergant had us box each other. You should've seen his face!"

    scene bath_house_test_night1_v2
    show kiril_body_bruised

    ## 3.	Donmai. (2017, June 11). text animations -
    ##Lemma Soft Forums. Lemmasoft.Renai.Us/. https://lemmasoft.renai.us/forums/viewtopic.php?t=44371
    show text '{size=50}"Bloody rage!"{/size}' at text_effect

    $ renpy.pause()

    show text '{size=50}"You will kill this mother f***ing killer!"{/size}' at text_effect

    $ renpy.pause()

    show text '{size=50}"Show me your f**ing war face!"{/size}' at text_effect

    $ renpy.pause()

    hide text

    kolya "Bloody hell, looks like you had a day."

    kolya "So you won right?"

    kolya "Didn't you?"

    kiril bruised "Of course!— Or not..."

    kiril "They're animals, f***ing animals!"

    kiril "Jesus Christ, you missed a beating."

    kolya "I suppose I did but I still can't get it though."

    kolya "At least you're not filled with utter shame. You fought with your
    dignity still in tact."

    kolya "No matter how hard I try, I'm not able to hit it. It's my hand
    I can't stop shaking it."

    kolya "I've managed to hit the board though, at least. Which is better than
    not hitting the board at all."

    kiril "Did you get to see the Serg? God the way he was yelling—"

    kiril "It could've sent me back to my mother's womb!"

    kolya "Haha! We'll get used to it."

    kolya "I hope."

    kolya "This might sound dumb or stupid but I'm glad I'm not the only one
    being told off for once!"

    kiril "I've been told off all my life, I just hid that from you."

    kolya "Anyway, let's get you cleaned up."

    kiril "Thanks man but I can do it myself."

    kolya "Yeah right."

    kiril "I'm sorry I dragged you into this. I should've bloody thought about
    it first."

    kolya "Eh, what's done is done. We can't turn back now."

    hide kiril_body_bruised

    scene dorm
    with Fade(2, 1, 6)

    show kiril_body_bruised

    kiril bruised "Hey, did you hear what's been going on lately?"

    kolya "Well, I don't really exactly have friends here, you know."

    kiril "Weren't the other crippled men with you?"

    kolya "Hey! I'm not."

    kolya "No, they all made it up a level before lunch."

    kiril "Lord..."

    kiril "Well, that's unfortunate."

    kiril "Anyway, the news..."

    kiril "The Tsar approved an increase of 500,000 men! You know what this means
    right?"

    kolya "Oh God, you don't think?"

    kiril "It seems incredibly likely Kolya."

    kiril "Better fix that aim of yours too, you won't last two seconds out
    there without it."

    kolya "It could just be for the Romanov Tercentenary.Of course,
    everything is for show."

    kiril "No that's not it. Why would you recruit that many, when you have plenty
    already?"

    kolya "You're kidding right?"

    kolya "Look at them, have you seen where they live?"

    kolya "There is no such thing as too much for the aristocracy Kiril.."

    kiril "Keep you're voice down! Look, I get what you're saying but some thing
    seems off."

    kolya "Just like your bloody nose right?"

    kolya "Damn look at you!"

    kiril "Get your hands off! That actually hurts."

    kolya "Once your done, is it all right if we sneak off for a bit?"

    kiril "Sneak off where?"

    kolya "The field, where else Kiril?"

    kiril "You've been going at it for hours, days. Don't you want a break?"

    kolya "I can't. I get the feeling the Sergant is losing his patience with me."

    kolya "Who knows, I might end up like you very soon."

    kiril "You'll end up like this if they catch us sneaking."

    kolya "Fine if you won't, I'll go myself."

    kiril "Well, hang on a minute! I didn't refuse."

    kolya "Then you'll come with me?"

    kiril "Of course. Give me a minute."

    hide kiril_body_bruised

    ##FACT CARD ABOUT ROMANOV TECENTENARY
    ##1.	Trooper6. (2015, May 28). Help with Imagebuttons
    ##(make ONLY image itself clickable). Lemma Soft Forums.
    ##https://lemmasoft.renai.us/forums/viewtopic.php?t=32324
    screen fact5():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/romanov.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact5")

    label callfact5():
    call screen fact5

    label afterFact5:

    kiril bruised "Wikipedia contributors. (2021, March 8). Romanov Tercentenary. Wikipedia,
    {a=https://en.wikipedia.org/wiki/Romanov_Tercentenary}
    for more info!{/a}"

    scene battlefield_night
    with dissolve

    show kiril_body_bruised

    kiril bruised "Still no use."

    kiril "If only there was— ah what do you call it? I bet you could hit a
    bulls eye, no sweat."

    kolya "What? Oh you mean— We can make one. The woods around here go off for miles."

    kiril "What are we waiting for? Come along."

    kolya "No, we've come here to train, not forage for wood!"

    kiril "What you need is a break. Come with me."

    kolya "Please let me stay, I need to be able to do this."

    kiril "Fine, I'll be off then. If you don't hit it by the time I return
    then you'll get a worse telling off than I had with Vlad."

    kolya "Oof, don't let Sergant hear you say that. He'll have your head."

    kiril "Right then I'm off, keep practicing Kolya."

    hide kiril_body_bruised

    scene battlefield_night
    with dissolve

    show kiril_body_bruised

    kolya "Did you find what you were looking for?"

    kiril bruised "Heck, yes! Now drop that gun and lend me a hand."

    kiril "I haven't done this since we were kids!"

    kolya "Hey, that's mine!"

    kiril "Sorry buddy, I had to get some lace from somewhere. Your boots won't
    miss them too bad, I hope."

    hide kiril_body_bruised

    ##PUZZLE GAME CREATE BOW AND ARROW
    ##7.	Renpy. (n.d.). Drag and Drop — Ren’Py Documentation.
    ##Retrieved 13 April 2021, from https://www.renpy.org/dev-doc/html/drag_drop.html
    init python:

        def puzzle_dragged(drags, drop):

            if not drop:
                return

            store.puzzle = drags[0].drag_name
            store.picture = drop.drag_name

            return True


    screen arrow_puzzle1():
        ##done button after your done with the puzzle
        modal False
        imagebutton:
            idle "images/done_.png"
            hover "images/done_hover.png"
            focus_mask True
            action Jump("arrow_puzzle")
            xpos 950 ypos 450

        # draggable items are below .
        draggroup:

            # jigsaw pieces
            drag:
                drag_name "part1"
                child "puzzle/part01.png"
                droppable False
                dragged puzzle_dragged
                xpos 500 ypos 100

            drag:
                drag_name "part2"
                child "puzzle/part02.png"
                droppable False
                dragged puzzle_dragged
                xpos 400 ypos 100

            drag:
                drag_name "part3"
                child "puzzle/part03.png"
                droppable False
                dragged puzzle_dragged
                xpos 450 ypos 100

            drag:
                drag_name "part4"
                child "puzzle/part04.png"
                droppable False
                dragged puzzle_dragged
                xpos 300 ypos 100

            drag:
                drag_name "part5"
                child "puzzle/part05.png"
                droppable False
                dragged puzzle_dragged
                xpos 600 ypos 100

            drag:
                drag_name "part6"
                child "puzzle/part06.png"
                droppable False
                dragged puzzle_dragged
                xpos 350 ypos 100

    label puzzle:

        scene battlefield_night
        with dissolve
        ##calls the puzzle game
        call screen arrow_puzzle1()

    label arrow_puzzle:

    ## this is after you click on the done button, the user has to type
    ## what they solved during the puzzle.
    $ secret_pass = renpy.random.choice (["bow and arrow"])
    $ your_try = renpy.input ("What did we make? [____ and ___](Please type 'and' ) + ( do not use punctuation )", "...")
    if your_try == secret_pass:
        ## the correct answer
        "Great! Nice work."
    else:
        ## wrong answer and returns back to the puzzle
        "I don't think that's it. Are you sure?"
        jump arrow_puzzle

    show kiril_body_bruised

    kolya "Haha! We did it!"

    kiril bruised "Nice job Kolya! What are you waiting for? Test this baby!"

    kolya "Right!"

    ##GUN GAME BUT WITH ARROW, THE TARGET IS IN THE CORRECT PLACE.

    ## gun game again, this time the target is hit correctly.

    label hello3:
        scene battlefield_night
        call begin_hunt03
        if _return > 0: # This is a special variable returned from the last call

            kolya "Yes! I knew it!"
            scene black with dissolve

        else:

            kolya "Oh Bloody hell."
            scene black with dissolve
            jump hello3

    label next:
    scene battlefield_night
    show kiril_body_bruised

    kiril bruised "And you're an amazing archer."

    kolya "If only! What's the use if I can wield a gun?"

    kiril "Let's give it another shot. Come on."

    kiril "Wait, let me fix it for you. Learn to use it with proper dexterity before
    showing off."

    kolya "God, I'm a fool. A fool!"

    kiril "Finally you agree."

    kiril "Hey you rascal, I just made that!"

    kolya "You!?"

    kiril "I froze my limbs to get you these!"

    kolya "Yes and for that, I'd never of loved you more!"

    kiril "Quiet! Two men alone in a field, what will they think of us if they heard
    you?"

    kolya "I don't care! To hell with everyone!"

    kiril "Don't tell me you actually meant it."

    kolya "What? No, Course not!"

    kolya "I mean yes, but no. Not in the way you think!"

    kolya "Enough with this, let's go back. What will you be doing tomorrow?"

    kolya "Whatever you do, meet me here after the morning run."

    kiril "A day out? We hadn't had one since the summer of 1905!"

    kolya "No. Look, I don't care if you have beg for a break. Just make it happen.
    Pretend you need to piss or something!"

    kolya "1905 though, you remember it?"

    kiril "How could I not?"

    kolya "I got a right beating almost every day that summer."

    kolya "It was well worth it though."

    kiril "Ah God, I'm sorry. I didn't know. I would've scaled it down a bit."

    kolya "Don't worry about it, it's done. Besides, were together now right?"

    kiril "Whenever you're with me, trouble is never far behind!"

    kolya "So you'll be there right?"

    kiril "Yes, and causing trouble!"

    kolya "You cause trouble and i'll make your face will look like a light injury."

    kiril "Relax Kolya, I'm joking."

    kiril "What do you want to show me then? Are you not going to tell me?"

    kolya "God bless your daft nature."

    kolya "No I lie, I'm the daftest of them all."

    kolya "I'm sorry, I've caused you all sorts of trouble, and look at how
    injured you are."

    kiril "Don't stress yourself about it. It's good to see you pull up a
    smile every now and again."

    kolya "You'll find out when you meet me there. Tomorrow, remember that, after the run!"

    kolya "What time is it again?"
## choice between times, correct answer gives you +1 point
    menu:

        "5.30 AM! Be there or be squared!":
            kolya "Close, though I never specified a time?"
            kiril "How am I meant to know when the time is right?"
            kolya "You should've heard it the first time round. Come after the morning run."

        "After that God awful run right?":
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            kolya "Yes that's it. I'm surprised you got it right!"
            kiril "Well, I seem to be full of surprised for you today."

    label after_What_Time2:

    hide kiril_body_bruised

    scene battlefield_old
    with dissolve

    show vladimir_body_talk

    vladimir_1 "It's been 3 days now and you still can't find your footing."

    vladimir_1 "Are you ready?"

    vladimir_1 "It says here you're from Siberia? What part exaclty?"

    vladimir_1 "I have a nephew living there, in Barnaul. You know it?"

    vladimir_1 "Speak up boy and go grab your gun for heavens sake."

    kolya "Barnaul? so I see you had a conversaion with Kiril then.
    I can't say you'll recognise my village though."

    kolya "It's a very small village."

    vladimir_1 "Won't you tell me? How will I ever be able to know it without
    you letting me know about it? I might pull something up my sleeve here."

    vladimir_1 "That's the trouble with village folk. Thinking us city folk as deluded and
    boastful. You're the boastful one here, thinking I lack basic geography."

    kolya "No, I'm almost certain you won't know. We hardly ever recieved
    any outside vistors unless it's family."

    vladimir_1 "Spit it out lad."

    kolya "It's near the Altaysky District."

    vladimir_1 "Ah! I know that."

    kolya "Really?"

    vladimir_1 "No, you poor soul. Living in a place so unrecognised."

    kolya "What are you trying to say?"

    vladimir_1 "See that? That's your arrogance at play. I'd have you slapped
    for takling back."

    vladimir_1 "Like your friend from yesterday. You can bet on him how much
    he enjoyed that."

    vladimir_1 "Got him wriggling like a worm. I'd hate to ruin your village face."

    vladimir_1 "You're not much of a talker are you?"

    kolya "Forgive me, I don't know what to say."

    vladimir_1 "You did just then didn't you? Anyway let's get back to your test."

    kolya "All right Sir."

    hide vladimir_body_talk

    scene battlefield_old

    show vladimir_body_talk

    ## 3.	Donmai. (2017, June 11). text animations -
    ## Lemma Soft Forums. Lemmasoft.Renai.Us/.
    ## https://lemmasoft.renai.us/forums/viewtopic.php?t=44371

    show text '{size=30}"All right Sir."{/size}' at text_effect

    $ renpy.pause()

    hide text

    vladimir_1 "You've got to start talking seriously like a man."

    vladimir_1 "Come on at least use the gun properly! You're begging for a beating
    aren't you?"

    vladimir_1 "Village folk don't belong in the army! It's a bloody waste of resources!"

    kolya "I know what I'm bloody doing old man!"

    vladimir_1 "What the F*** did you say!?"

    ##GAME STARTS. TARGET ON POINT

    label hello4:
        scene battlefield_old
        call begin_hunt04
        if _return > 0:
            kolya "Thank God!"
            scene black with dissolve

        else:
            kolya "Crap! After all this time!"
            vladimir_1 "Start again..."
            scene black with dissolve
            jump hello4

    label next2:
    scene battlefield_old
    vladimir_1 "Why you're just like Tula the blacksmith!"

    kiril smile "That was amazing Kolya! That shot almost send me straight back to high school!"

    vladimir_1 "You should be in the ring! Waltzing round here when
    your face should be black and blue! How cocky we all have become!"

    kiril talk "Right Sergant! I'll be off."

    kiril smile "Congrats though Kolya. You should be well proud."

    vladimir_1 "Mother Russia is crying to return to her global glory. {b}{i}Run along.{/i}{/b}"

    kolya "We'll talk later Kiril, it's okay."

    hide vladimir_body_talk

    scene battlefield_old
    with dissolve

    show vladimir_body_talk

    vladimir_1 "You two seem close. Are you related?"

    kolya "No Sergant, a family friend."

    vladimir_1 "Right I see."

    hide vladimir_body_talk

    #FACT CARD ABOUT BEING LEFT HANDED IN RUSSIA [OLDEN DAYS]
    ## Trooper6. (2015, May 28). Help with Imagebuttons
    ## (make ONLY image itself clickable). Lemma Soft Forums.

    screen fact6():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/left_hand.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact6")

    label callfact6():
    call screen fact6

    label afterFact6:
    kiril smile "McDonnell, S. (2017, April 6). The men who shoe fleas. BBC.
    {a=http://www.bbc.com/travel/story/20170331-where-fleas-wear-shoes}
    for more info!{/a}"

    kiril smile "For more check out: Sindelar, D. (2013, August 13).
    Remembering When Right Was Right And Left Was Wrong. RadioFreeEurope/RadioLiberty.
    {a=https://www.rferl.org/a/left-handers-day-forced-right-handedness/25074425.html}
    for more info!{/a}"

    scene bath_house_test_night1_v2
    with Fade(2, 1, 6)

    show kiril_body_smile

    kiril smile "Wow! What did he do to you?"

    kolya "Well, to my credit I bruise a lot easier than you, from what I remember."

    kiril "Yes, I remember our hiking trails especially. There had been a bruise at
    every branch you touched."

    kolya "My mother had been a right mess every night I got back home. Though she did her
    best to hide it since you had been staying over."

    kiril "You must've had a hard time when I was gone."

    kolya "Yes. well, I got these from the Sergant."

    kolya "Where are yours then?"

    kiril "In places you aren't able to see..."

    kolya "Oh God, why am I not surprised?"

    kiril "Yes, I had the upper hand for the majority of it. Vlad was furious when
    I hadn't finished him off."

    kolya "Finish the Sergant? You fought with him?"

    kolya "Wow, you are good. I take back what I said."

    kiril "No, the guy I spared—"

    kiril "Come to think of it, I don't even know the person I spared."

    kolya "So the Sergant hit you for that?"

    kiril "No, he ordered the other guy to."

    kiril "He sprang back up like he had been resurrected out from the dead."

    kiril "I was instantly knocked out and dragged out of the ring."

    hide kiril_body_smile

    show kiril_body_talk

    kiril talk "I had my hands between my knees, grunting like a bloody gorrila by the time
    I woke up!"

    kolya "Bloody hell Kiril. That must've been a site."

    kiril "I'd never let you witness that! I can barely walk now, why am I even
    bloody here?"

    kolya "It was your idea remember?"

    kiril "No, it was my idea that you come with me. I'd never asked to come,
    I was conscripted."

    kolya "You're right. I'm sorry."

    hide kiril_body_talk
    show kiril_body_smile

    kiril smile "Besides, I thought I'd left you with an estatic Vlad."

    kolya "Well yes, though you came to late to hear I had said to him a little earlier."

    kiril "Why? What did you say to him?"

    kiril "I'd never think you'd talk back to anyone. Sure you've got a temper,
    but only towards me it seems!"

    kolya "Why does it matter what I said? The result would be the same."

    kiril "Well it can't of been that bad. One of the guys got bashed in the head
    for needing to go to the toilet. He ended up going where he stood in the end."

    kiril "It was God awful. I can still smell it faintly even now."

    kiril "I wouldn't get all excited if I were you. Combat training sucks. Though
    I shouldn't of mentioned that. You'll not get a nights sleep, knowing you."

    kolya "I've never thought about it, but now you've mentioned it, I'm not sure."

    kiril "Don't worry about it. Like I said, I won't let them touch you."

    kolya "I don't think I'll get spared for this one Kiril. You weren't able
    to defend yourself either."

    kiril "There are other ways besides physical combat. Try not to think about what I said."

    kiril "Even if you end up fighting each other, that's sort of a relief. At least
    we'd know each other!"

    kolya "I'd rather be child. At least then I could ride Firefox."

    kiril "Yes, wielding wooden swords was thrilling as a child. The real thing ended
    up to be quite different."

    kiril "How is old Firefox anyway? I hope that horse isn't a sort of burden, he must
    be old now."

    kolya "He got put down shortly after you left."

    kiril "I see."

    kolya "You know, you still haven't told me why you left. I have sort of an idea
    but when you hadn't written."

    kolya "Am I that disgusting to you?"

    kiril "Kolya, I've never thought that about you my entire life. I want you to know that— at least."

    kiril "Let's get you cleaned off. You should rest."

    kolya "You should too, thought you had trouble standing?"

    kiril "Right."
    hide kiril_body_smile
    ##THE WAR YEARS ..... LAST CHAPTER
    scene brick_wall
    with dissolve

    show vladimir_body_talk

    vladimir_1 "You've come a long way since the day I met you. Though I'll say this—"

    vladimir_1 "This camp is child's play compared to the reality. I was there, in Japan."

    vladimir_1 "I'd never been so humiliated in my life. We humiliate you here so
    you'll be ready for what's to come over there."

    ##FACT CARD JAPAN- RUSSIA WAR
    ## Trooper6. (2015, May 28).
    ## Help with Imagebuttons (make ONLY image itself clickable). Lemma Soft Forums.

    screen fact7():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/japanese_war.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact7")

    label callfact7():
    call screen fact7

    label afterFact7:
    kiril smile "Britannica, T. Editors of Encyclopaedia (2021, February 1). Russo-Japanese War. Encyclopedia Britannica.
    {a=https://www.britannica.com/event/Russo-Japanese-War}
    for more info!{/a}"

    vladimir_1 "Now, I'm going to do something a little different than the usual."

    vladimir_1 "I've let the weak hide behind the fence for far too long."

    vladimir_1 "From now on I shall pull names out of a hat. Yes, that's right."

    vladimir_1 "Those of you fortunate enough to go to school will know what I mean.
    Let's have the first volunteer shall we?"

    vladimir_1 "Kiril! You've always loved a good beating. Let's give someone else the
    pleasure of it. Go on, pick a name."

    kiril talk "Oh God. Crap!"

    vladimir_1 "What? What name have you picked there boy?"

    vladimir_1 "Hah! How unfortunate indeed."

    vladimir_1 "Now let'a see, it's only fair that I pick the 2nd is it not?"

    vladimir_1 "Oh why would you look at that! Two peas in a pod. Sad, unlucky
    brethren."

    vladimir_1 "Get your pet dog and yourself up onto the ring Kiril."

    hide vladimir_body_talk
    scene brick_wall

    show vladimir_body_talk
    show text '{size=50}"MOVE IT! MOVE IT! MOVE IT!"{/size}' at text_effect

    $ renpy.pause()
    hide text
    hide vladimir_body_talk

    scene brick_wall

    show kiril_body_talk

    kiril talk "I promise, I won't hurt you okay? Not really anyway."

    kolya "I can't survive in this box what makes you think I can survive out there?"

    kolya "Please, Kiril. Don't fake with me."

    vladimir_1 "What's all that chatter?"

    hide kiril_body_talk
    scene brick_wall
    show vladimir_body_angry
    ## 3.	Donmai. (2017, June 11). text animations -
    ## Lemma Soft Forums. Lemmasoft.Renai.Us/. https://lemmasoft.renai.us/forums/viewtopic.php?t=44371
    show text '{size=50}"FIGHT, FIGHT FIGHT!"{/size}' at text_effect

    $ renpy.pause()

    hide text

    scene box
    with Fade(2, 1, 6)

    ##COMBAT CHOICE GAME

    #FACT CARD - IN COMING NEWS, FRANTZ FERDINAND KILLED!
    ##Trooper6. (2015, May 28). Help with Imagebuttons
    ## (make ONLY image itself clickable). Lemma Soft Forums.

    screen fact8():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/franz.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact8")

    label callfact8():
    call screen fact8

    label afterFact8:
    kiril smile "BBC Bitesize. (n.d.). Assassination of Archduke Franz Ferdinand (subtitled) - KS3 History. Retrieved 3 April 2021.
    {a=https://www.bbc.co.uk/bitesize/clips/zmyqhyc}
    for more info!{/a}"

    vladimir_1 "What on bloody earth!"

    vladimir_1 "Keep fighting you two! I'll be back."

    vladimir_1 "Oh heavens above! War is among us!"

    scene helping_hand
    with Fade(2, 1, 6)

    kiril smile "Come on Kolya, help me up."

    kolya "What do you suppose that was?"

    kiril "I guess you were right to not let me go easy on you. You sell yourself short,
    did you know?"

    kiril "In fact, where did you learn to fight like that?"

    kolya "The village, my cousins had a knack for things like this. They could
    toss over a sack of potatos without parting their lips."

    kiril talk "I've heard the situation is pretty bad there. I mean living in the capital
    is bad enough but living as a serf? No thanks."

    kolya "I'm not a serf. That's been dead way back in the 60s."

    kiril "Don't kid yourself. You work for your landlord— or did and your family
    still do."

    kiril "I'm surprised they aren't looking for you. They really ought to, you're a
    labour is worth a hefty amount I'd assume."

    kolya "Stop it Kiril, let's talk about something else."

    scene cafeteria

    show kiril_body_smile

    kiril smile "So, are you looking forward for today?"

    kolya "No, like every other day. Today is no different."

    kolya "My arm hurts, the amount of times I spent reloading my gun is beyond me."

    kiril "Hah!"

    kolya "It's harder than it looks. I feel like I'm reading something that's not even there."

    kolya "I always get a sickly moment of dead whenever that happens. It could be the result of
    my death, for all you know."

    kiril "You're over exaggerating. That won't happen."

    kiril "Come on let's sit over there."


    hide kiril_body_smile

    scene eating_food
    with dissolve

    kolya "You're not left handed, how would you know? I dare you and everyone else
    to try it out today in the field. Go on, use your left hand."

    kiril smile "You bet, I'll give it a go. It's only fair after the hell you've been through."

    kiril "I can't believe you were so thick. Didn't you realise you were using your weak hand?"

    kolya "You can't really tell with these things. You follow what everyone else is doing without
    a thought."

    kolya "I can hardly believe it myself."

    kiril "Well. As you said, I wouldn't know would I?"

    kolya "You're sure as hell about to find out. You're the majority you see, us left handed folks
    are so few and far between, were quite invisible."

    kiril "I guess you are right about that. Though it is strange to notice a pair of hands
    at all. Don't you think?"

    kolya "Perhaps."

    ##FACT CARD NEWS WARN GERMANY DECLARES WAR ON RUSSIA. AUSTRIA ATTACKS SERBIA ETC
    ##RUSSIAN MOBILISATION

    ##Trooper6. (2015, May 28).
    ## Help with Imagebuttons (make ONLY image itself clickable). Lemma Soft Forums.
    screen fact9():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/austria_war.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact9")

    label callfact9():
    call screen fact9

    label afterFact9:
    kiril smile "Austria - Conflict with Serbia. Encyclopedia Britannica. Retrieved 5 April 2021.
    {a=https://www.britannica.com/place/Austria/Conflict-with-Serbia}
    for more info!{/a}"
    ## Trooper6. (2015, May 28). Help with Imagebuttons
    ##(make ONLY image itself clickable). Lemma Soft Forums.
    screen fact10():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/germany.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact10")

    label callfact10():
    call screen fact10

    label afterFact10:
    kiril smile "Amt, A. (2014, July 22). The July Crisis: an ultimatum and an unexpected response. German Federal Foreign Office.
    {a=https://www.auswaertiges-amt.de/en/aamt/politiscal-archive/-/215216 }
    for more info!{/a}"

    scene bath_house_test_dusk_v2
    with Fade(2,1,5)

    show kiril_body_bruised

    kolya "You look pretty bad."

    kiril bruised "Jee thanks Kolya, like I didn't know."

    kolya "Are you okay?"

    kiril "Yes, I'll be fine. How many times have you seen me bleeding now?
    10? 20?"

    kolya "Right, though you're head looks awful though. I'll get something to cool it off."

    kiril "Cold war will be more than enough. Thanks Kolya."

    scene bath_house_test_dusk_v2
    with dissolve

    show kiril_body_bruised

    kolya "So, who was it with this time?"

    kiril bruised "F***ing Dennis. Where were you? I haven't seen you since I left the field."

    kolya "In the field."

    kiril "Right...you've been there for ages Kolya."

    kolya "The Sergant thought I'd better practice my reload speed and for once
    I don't disagree."

    kolya "Why not join me? You have a great aim. We hardly practice together."

    kiril "No, I can't. I'm out for revenge."

    kolya "I won't rest until I come for every guy who came at me."

    kiril "How else will I improve?"

    kolya "You're right. The Sergant had been so ppreoccupied lately and every
    one else for that matter."

    kiril "Of course, were going to bloody war Kolya! At any second we can all get
    called out for it."

    kolya "It kind of scares me to die out there. You're the only person I've
    ever known Kiril."

    kiril "Kolya—"

    kolya "Please let me speak. I don't think I ever told you this but you're
    my best friend and I honestly love you."

    hide kiril_body_bruised

    show vladimir_body_talk

    vladimir_1 "Why am I not surprised? What have you two boy lovers have been
    doing under this roof eh?"

    vladimir_1 "You F***ing imbeciles!"

    scene bath_house_test_dusk_v2

    show vladimir_body_angry

    ## 3.	Donmai. (2017, June 11). text animations - Lemma Soft Forums.
    ## Lemmasoft.Renai.Us/. https://lemmasoft.renai.us/forums/viewtopic.php?t=44371

    show text '{size=50}"GET OUT! MOVE IT!"{/size}' at text_effect

    $ renpy.pause()

    hide text

    kiril angry "Were friends, like brothers for goodness sake!"

    vladimir_1 "The likes of you deserve nothing but a good hanging."

    kolya "Well, wait just a minute!"

    vladimir_1 "Haven't I always said to talk seriously? Declaring love like
    that you sicken me!"

    kiril "Please, he's had a rough childhood, a village boy who doesn't know
    right from wrong."

    kolya "No, I'll gladly stand behind my words. If I should die, go on hang me,
    that tree over there looks awfully nice right!"

    kiril "Kolya, I beg you stop."

    vladimir_1 "That's it boy, I'm giving you a punishment worse than death,
    where men half your age will watch your corpse rot."

    vladimir_1 "Set upon a rock, unbeknownst to you, even to me!"

    vladimir_1 "You'll be begging for death before you're end. You'll stay
    and weep until worms decompose your body, you'll be nothing, nothing at all."

    kiril "Serg! Don't!"

    kiril "Kolya, tell him you didn't mean it! Tell him!"

    vladimir_1 "The office asked for a number of names, I think it will only
    be proper that the first will be yours."

    vladimir_1 "The first battle is always a blood bath. You'll die without
    lifting a finger."

    vladimir_1 "You're not better than one of those shitty Germans."
    vladimir_1 "You'll sleep outside for tonight, I can't have you lurking near my
    soldiers!"

    vladimir_1 "I see you're deformed in hand and heart. I almost pity you."

    kiril "If you'll just listen to me, it's nothing of the sort you're thinking of!"

    vladimir_1 "You on the other hand, I can see it on you're face. You're disgusted
    as I am."

    vladimir_1 "You are not to collaborate with him any longer. Him? She?
    I have no idea what to call that specimen."

    kiril "Wait!"

    vladimir_1 "I can barely breathe, get lost before I sentence you too!"

    ##FACT CARD ABOUT HOMOSEXUALITY IN WW1
    ## Trooper6. (2015, May 28). Help with Imagebuttons
    ## (make ONLY image itself clickable). Lemma Soft Forums.
    screen fact11():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/homosexuality_war.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact11")

    label callfact11():
    call screen fact11

    label afterFact11:
    kiril smile "Exploring Surrey’s past. (n.d.). Homosexuality and the First World War. Retrieved 3 April 2021,
    {a=https://www.exploringsurreyspast.org.uk/themes/subjects/diversity/lgbt-history/fwwhomosexuality/}
    for more info!{/a}"

    scene dark_desk

    vladimir talk "Get you're things you're leaving."

    vladimir talk "A train is bound for East Prussia, you'll be on it in a
    few minutes."

    vladimir talk "Come on then. Get up for goodness sake."

    kolya "It's not true what you said, you do know that right?"

    vladimir talk "Well, you've told me a week or two too late haven't you?"

    vladimir "It's such a waste."

    vladimir smile "You were a truly good shot, all beit on the reload."

    kolya "Wouldn't you tell your b rother you love them if you knew it was the end?"

    vladimir "No. Both my brothers and I fought in Japan, not a single farewell
    had been said, nor affection given."

    kolya "Like my father, he had died then too. I was only a child, so naive."

    vladimir talk "Well, I hope war beats that out of you boy. There is no time
    to show brotherly affection in times such as this one. It makes you weak."

    vladimir talk "Why bother establishing relationships when the very goal calls for a sacrifice
    of life?"

    kolya "I practically grew up as an orhpan growing up. Kiril's visits were always amazing for me. I'd
    always been jealous of Kiril, having blessed with loving parents."

    kolya "what does it even mean to love? I don't know."

    vladimir "You did back then."

    vladimir "You recieve visitors from family members in your village is that correct?
    Is he a cousin or something?"

    kolya "I've mentioned before, he's a family friend. His father had been close to mine during the war."

    kolya "I think he visited us only out of pity. That he had lived and my father hadn't."

    kolya "Kiril had been brought up in Barnaul though, much like your nephew."

    vladimir "You've got a good memory for such a weak heart."

    kolya "Well, he later moved to the capital and I never saw him again until a year ago."

    kolya "I'm glad I came all this way to see him. Even if that meant coming here. I'd choose this
    again and again if I could."

    kolya "After so many years of absence. I can finally put an end to this childhood nostalgia."

    vladimir "Nostalgia? Bloody hell, enough talk. Come on."

    kolya "Right."


    scene chapter2
    with Fade(2, 1, 6)
    scene train_to_war
    with Fade(2, 1, 6)


    stranger pic "You've dropped your hat young man."

    kolya "Me? Ah crap I've left my hat back there."

    kolya "Thanks, but that's not mine, it must belong to someone else. I could
    ask around for you, if you'd like?"

    kiril smile "My God kolya, won't you look at me while I'm talking to you?"

    kolya "Kiril!?"

    kiril "Hi buddy. It's been a while."

    kolya "How on earth did you get here? Don't tell me he sent you here too?"

    kiril "No, no. Nothing like that. I actually snuck in, I hope you don't mind."

    kolya "Why am I not surprised? Go back Kiril."

    kolya "Do you realise where this train is heading?"

    kiril "Course I do, Poland. I'm not daft Kolya, I can read the sign."

    kolya "That's not what I mean. Please go back, they'll file you as missing."

    kiril "What good is it when you're not there to acompany me?"

    kolya "Kiril!"

    kiril "Do you realise what I'd become? A carcass, pondering your bruised face."

    kiril talk "Do you know how guilty I'd feel? I'm not going to sit back and wait for my
    death, when I can die side by side with you."

    kiril "It's what my mother would've wanted. It's what I want for me."

    kiril "Don't you dare ask me to leave this train. I have my values too!"

    kolya "Your parents, you've hardly mentioned them since we've arrived. Do they know?"

    kolya "Do they know your walking to your death?"

    kiril "Looks like we both have very litle faith about where we are heading."

    kiril "They do, they do know. And you know what? They'd be pretty freaking glad."

    kolya "what makes you say that? You're their only son, they've got no one else!"

    kolya "They'd be heartbroken!"

    kiril "What's the difference, I'm sacrificing my life, with or without you either way."

    kolya "Have some common sense and go back. At least for them. You have time,
    spend it with them. Talk to them."

    kiril "You've not been listening to me. Were in a bloody war, a war!"

    kiril "Let me die with someone I've known and loved for all my life. Besides why'd
    you want me to go back?"

    kiril "To be beaten up until my final days? I think not!"

    kolya "I can't believe you're doing this."

    kiril "Blame yourself! Why did you not say anything when you had the chance?"

    kolya "I'm not gay!"

    kiril "Yeah right, you'd be lucky enough to love anyone at this rate Kolya,
    you don't have to tell me. I know."

    kolya "This is how it is isn't it?"

    kiril "What is?"

    kolya "My life!"

    kiril "Yes go on..."

    kolya "No I can't say it. I don't have the words right now."

    kiril "Well when will you? Upon the battle field? By the time you'd want to
    speak it might all be over for you. Don't wait, the time for talking is now."

    kiril "There's something wrong yet you won't tell me. You've always been like this,
    I couldn't fix it then but perhaps I can now. What's wrong?"

    kolya "I don't your image of me to be any different when I die."

    kiril "Image of you? Do you know what I think of you now?"

    kiril "A coward."

    kolya "You're telling me like I haven't known. Yes I am a coward, and?"

    kiril "My own hand will be my death sentence, why don't you get it? Of course
    I'm a coward. What person would love himself for that?"

    kiril "Well, every time you reload I'll be there covering for you. Don't hate
    yourself for things you can't change."

    kolya "It's every man for himself out there. Don't you dare do that Kiril."

    kiril "I guess this is it, you're a lost cause are you?"

    kiril smile "Remember that time mother came to our rescue. We got ourselves stuck  in quick sand."

    kolya "Right, I remember wanting to build the coolest A-frame ever. Our hands were
    covered in mud for days on end."

    kiril "Mother was all over us about that. She'd wash my clothes thrice to make that grass smell
    go away. It smelt like manure!"

    kolya "Gross! That den lasted for years. I'd take you there every summer but on the
    fourth I'd been too eager and fell flat on my face in quick sand."

    kiril "I didn't know what quick sand even was before that. I thought the entire earth
    was swalling you up whole."

    kolya "I'd never ventured far off from the village, only for timber with my uncles."

    kiril talk "You don't mention them often, how are they doing?"

    kolya "Well, they're alive."

    kiril "Don't you think they'd be off to war too?"

    kolya "No, they're much to old for that. My father's a baby compared to them. There was
    a day where you even mistaken them for my grandad."

    kiril "God, yes you're right."

    kolya "Let's not talk about them, not when I'm so near death."

    kiril "I'm sorry you're right. Don't worry about it so much. I don't think this
    will be the end of you just yet."

    kolya "My father had been called to Japan, and look what happeend to him. We've got it worse,
    with the germans and no one cares about the first battle either."

    kiril "You've got to fight to survive Kolya, whatever it takes or they'll have won
    before the war has even begun."

    kiril smile "Now, as the Serg always says, Show me your war face!"

    ##Facts about shell shock , mental health in WW1

    scene forest_walk
    with Fade(2, 1, 6)
    show kiril_body_talk
    kolya "When do you think we'll arrive? We've been walking for hours."

    kiril talk "Not sure which is worse, the journey to death or death itself."

    play sound "<loop 1.333>sounds/battle_sound.mp3"

    kiril "This is it. The moment we've been waiting for. Are you ready?"

    ## choice,which one gives you +1 point
    menu:

        "Good luck, I'll see you on the other side.":
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            hide kiril_body_talk
            show kiril_body_smile
            kiril smile "Heaven or the hill?"
            kolya "Feel free to choose. I'm happy either way."
            hide kiril_body_smile

        "Come on, let's get it over and done with.":
            hide kiril_body_talk
            show kiril_body_smile
            kiril smile "The battle or death?"
            kiril "Seems like both to me!"
            hide kiril_body_smile

    ##GUN GAME, MOVING TARGET.
    label hello5:
        scene forest_walk
        call begin_hunt05
        if _return > 0: # This is a special variable returned from the last call
            ## targets_hit5 counts the number of soldiers you hit with the gun
            kolya "Ah, I think I sprained my arm. Damn, well at least I got [targets_hit05]"
            scene black with dissolve

        else:

            kolya "Ah"
            scene dead_scene with Fade(2,1,5)
            jump hello5

    label after_how_you_are3:

    stop sound

    play music "<loop 1.00>sounds/Warfare_despair_mp3.mp3"
    show kiril_body_talk
    hide kiril_body_talk

    scene forest_fire

    show kiril_body_talk_war

    kiril talk_war "Kolya!?"

    kiril "Kolya! Thank God you're okay, you're not hurt are you?"

    kolya "Yes I am. Are you?"

    kiril "Yes! I'm okay as ever, quite thrilled actually!"

    kolya "That's great. Come help me carry him to the medics. I have a feeling
    he got shot under his arm."

    scene night_war
    with Fade(2, 1, 6)

    kiril smile_war "Hey, it's going to be okay. I heard they took Gumbinnen. It won't
    last for very long now, you'll see."

    kiril "Come on Kolya, with that face you'll have me crying too."

    kolya "I feel like a God damn child. We'll get you cleaned up, don't worry about it."

    kolya "Don't look at me, I wreak of piss."

    kiril "Not any less than before, I'd say!"

    kiril "Relax, this sort of thing is bound to happen. You'll dry off."

    kolya "It's like what they've always said. I'm disgusting, it's all true."

    kiril "Now blast that anger towards the Germans. I should think they'd piss their
    pants once they got a load of you."

    kiril "Now, how about we play a game? That will cheer you up for sure!"

    kolya "I don't want to play any games. We got ambushed earlier, do you want them to
    blow your bollocks off whilst you're thinking of God knows what?"

    kiril "Let's sing instead then? I know some great songs."

    kolya "No please, spare us all from your hideous voice."

    kiril "Hideous? I'll have you know I'd rather my voice burst the ears of them Germans rather
    than to put them at ease!"

    kolya "What about me? I'd have to listen to it too."

    kiril "Great, okay then. Let's get back to that game then shall we? Seen as though
    you hate my voice so much."

    kolya "You're version of {b} Dark eyes {/b} would wake half the species in very this forest."

    kiril "It's not that bad—"

    kolya "Not that bad!"

    kiril "Enough of this talk. Let's test your knowledge on historical events."

    kolya "You've got to be joking, the Germans are shelling us as we speak!"

    kiril "What better way to past the time? It's extremely patriotic if you ask me."

    kiril "So then, let's begin..."

    ##	Growlex. (2016, May 28). Specific text input...?
    ## Lemma Soft Forums. https://lemmasoft.renai.us/forums/viewtopic.php?t=12438
    label __1:
    $ secret_pass1 = ["grand duke sergei", "sergei"]   ## availible answers
    #$ secret_pass1_1 = "sergei"
    $ your_try1 = renpy.input("What was the name of the Tsar's uncle who was assassinated in 1905?") ##question
    if your_try1.lower().strip() in secret_pass1:
        kiril talk_war "Poor Sucker, if you ask me..."  ## if correct
    else:
        kiril smile_war "Good one Kolya, but no that's false." ## if wrong
        jump __1

    label __2:
    $ secret_pass2 = ["japan"] ## answer
    #$ secret_pass1_1 = "sergei"
    $ your_try2 = renpy.input("What country did Russia go to war with during 1904?") ##question
    if your_try2.lower().strip() in secret_pass2:
        kiril smile_war "We got beat pretty badly...but that's okay. We can turn things around now." ##correct
    else:
        kiril smile_war "I'd like to see that, but I'm afraid not." ##wrong
        jump __2


    label __3:
    $ secret_pass3 = ["noose", "hangman's noose"] ## answers
    #$ secret_pass1_1 = "sergei"
    $ your_try3 = renpy.input("What was the infamous Stolypin's necktie?") ##question
    if your_try3.lower().strip() in secret_pass3:
        kiril angry_war "I'd like to see him in his own tie." ##correct
    else:
        kiril smile_war "Yeah right, you wish! Guess again." ##wrong
        jump __3

    label __4:
    $ secret_pass4 = ["peasant farmer", "farmer", "peasant", "peasant farmers", "farmers", "peasants"] ##answers
   #$ secret_pass1_1 = "sergei"
    $ your_try4 = renpy.input("What was the most common job in Russia during the 1800s?") ##questions
    if your_try4.lower().strip() in secret_pass4:
        kiril smile_war "A bit like you and your family Kolya." ##correct
    else:
        kiril smile_war "That's a good laugh, imagine... but no it's not that." ##wrong
        jump __4

    label __5:
    $ secret_pass5 = ["siberia"] ##answers
    #$ secret_pass1_1 = "sergei"
    $ your_try5 = renpy.input("Where were prisoners sent in Tsarist Russia?") ##question
    if your_try5.lower().strip() in secret_pass5:
        kiril smile_war "Good thing Siberia is our true home, right Kolya?." ##correct
        kolya "That's true. You're right about that."
    else:
        kiril smile_war "That's a good laugh, imagine... but no it's not that." ##wrong
        jump __5


    kiril smile_war "That was great fun!"

    kolya "Perhaps I could quiz you next time since {b}you{/b} love our history so much."

    kiril "Course! History is a facsinating topic. If you think about it, were making history now."

    kolya "What history? Were riding towards our death."

    scene forest_trench

    kiril talk_war "Have you been hearing what people are saying?"

    kolya "No, but I hear what my legs are saying."

    kolya "And my arms too for that matter. I'm aching all over. And it's so cold, it's
    meant to be August for Christ's sake!"

    kiril smile_war "You've gone British!"
    kiril talk_war "Nevermind what the weather is! The other division, General Rennenkampf's army
    have taken a beating but I hear they've taken some land somewhere."

    kiril "Pay attention to these things Kolya, were nearly done with this. All you have to
    do is survive now."

    play music "<loop 6.33>sounds/battle_sound.mp3"

    scene forest_trench
    with hpunch

    kiril angry_war "Get down!"

    scene forest_trench
    with hpunch

    kolya "Another ambush!?"

    scene forest_trench
    with hpunch

    scene forest_war_game
    with Fade(2, 1, 4)

    ##GUN GAME MOVING TARGETS

    scene forest_trench
    with hpunch
    kolya "Kiril! Are you okay?"

    kiril bruised_war "Sure, just a mosquito bite!"

    kiril "See those trees over there?"

    kolya "What are you talking about?"

    kiril "I want you to run and never look back."

    kolya "No way!"
    kolya "There are hundreds of them out there!"

    kiril "How many can you see alive though Kolya? How many?"

    scene forest_war_game
    with vpunch

    ## gun game, there is a serious of vpunch and hpunch, this gives the effect
    ## of the screen jumping and shaking

    label hello6:
        scene forest_war_game
        call begin_hunt05
        if _return > 0:
            ##tagret_hit05 counts the hits you make
            kolya "At least I got [targets_hit05] of them, bloody hell!"
            kolya "Kiril!"
            scene black with dissolve

        else:
            kolya "Crap! After all this time!"
            vladimir_1 "Start again..."
            scene dead_scene with Fade(2,1,5)
            jump hello6

   ##GUN GAME AGAIN, MOVING Targets
    label next3:
    scene forest_trench
    with hpunch

    kiril bruised_war "Quit shooting and starting running for goodness sake!"

    kolya "Please be quiet, you'll die."

    kiril bruised_angry "I already am!"

    kolya "You're not, hold on a little longer. We'll get you a medic."

    scene forest_trench
    with Fade(2,1,4)

    kolya "Kiril? Kiril! God, wake up!"

    kolya "Good, you're awake. Rennenkampf will be here any moment with his army.
    The guys have been saying Samsanov sent a message to him!"

    kolya "He'll help us, don't worry."

    kiril bruised_war "God, I'm so cold."

    kolya "Here take my jacket. It's not for keeps though I'll need it when you're
    nice and warm again."

    scene forest_war_game
    with vpunch

    ##GAME WITH Targets repeat
    label hello7:
        scene forest_war_game
        call begin_hunt05
        if _return > 0:
            kolya "Kiril!"
            scene black with dissolve

        else:
            kolya "Crap! After all this time!"
            scene dead_scene with Fade(2,1,5)
            jump hello7

    label next4:

    scene forest_trench
    with vpunch

    kolya "Holy crap! When are they coming!?"

    kolya "They've got us encircled. Where do we go?"

    kolya "Kiril? Kiril!"

    kiril bruised_war "Sorry, I'm sorry. Don't worry about me, you go. You'll
    need to run as fast as you can."

    kolya "I'm not leaving you, don't tell me to do it."

    kiril "You'll die out here or worse take you prisoner. Please I'm commanding you
    to leave!"

    kolya "Then they'll take a free shot. Besides since when were you my Commander?
    I'm not going to take orders from you."

    kiril "Hey you don't mean that."

    ## choice whether to abandon kiril or not.
    menu:

        "Leave Kiril and go to the woods.":
            kiril bruised_war "Thank goodness!"
            kolya "I'll never forget you Kiril"
            scene forest_war_game
            with vpunch
            show soldier_target
            scene dead_scene
            with Fade(2,1,5)
            jump next4
            ##YOU DIED SCREEN

        "Choose to remain with Kiril.":
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            kiril bruised_war_angry "what are you doing!?"
            kolya "You're insane if you think I'm going to leave you here."

    label after_war_games:

    kolya "I've got an idea, though it might hurt you a bit."

    kolya "Can you walk?"

    kolya "You'll hate me for this Kiril, but I have to do it for the both of us."

    kolya "Kiril? Are you awake?"

    kiril bruised_war "What are you doing?"

    kiril "Let go of my bloody shirt!"

    kolya "Come on, you have to! We'll die out here. Is that what you want?"

    kolya "I'll cover for you."

    kiril "I don't care how pro you are with a gun, but covering for me
    will be useless. We'll both die, now is that what you want?"

    kolya "There! Those bushes, that will do. Come Kiril, we'll make it out. Come on!"

    scene bushes
    with Fade(2, 1, 6)

    kolya "Kiril? Please talk to me."

    kolya "You awake?"

    kiril bruised_war "Hey, what's up?"

    kolya "Looks like I'm going to have to carry you. I've got an idea."

    kolya "Hey? Are you there?"

    kiril bruised_war "What is it this time?"

    kolya "Okay, good you're up."

    kolya "Were need to walk back, or run for it. Depending what kind of
    energy you have."

    kiril bruised_angry "I'm not going and you can't make me. I'll slow
    you down, why can't you get that in your head."

    kolya "They won't be able to see us will they? With all the shelling."

    kiril "God Kolya— the shelling!"

    kolya "What other option do we have, you tell me Kiril?"

    kiril "I way a crap ton more than you, you can't carry me. Now
    save yourself the trouble and leave."

    kolya "If Rennenkampf won't come to us, we have no choice but to go to him."

    scene forest_war2
    with Fade(2, 1, 6)

    ## Trooper6. (2015, May 28).
    ## Help with Imagebuttons (make ONLY image itself clickable). Lemma Soft Forums.

    kiril bruised_angry "You're a wild one Kolya."
    screen fact11_5():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/tannenberg.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact11_5")

    label callfact11_5():
    call screen fact11_5

    label afterFact11_5:
    kiril smile "BBC - History. (n.d.). BBC - History - World Wars: Battle of Tannenberg: 26–30 August 1914. BBC History. Retrieved 9 April 2021,
    {a=http://www.bbc.co.uk/history/worldwars/wwone/battle_tannenberg.shtml}
    for more info!{/a}"
    ##FACT CARD SHELLING

    screen fact12():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/shelling.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact12")

    label callfact12():
    call screen fact12

    label afterFact12:
    kiril smile "Spartacus-educational. (n.d.). Shellfire in the First World War. Retrieved 3 April 2021,
    {a=https://spartacus-educational.com/FWWshellfire.htm }
    for more info!{/a}"

    scene bushes_2
    with Fade(2, 1, 6)

    kolya "Are you ready?"
    kolya "Kiril?"

    kiril bruised_war "Yes, I am."

    kiril bruised_war "I'm sorry. I should've told you sooner but I'm truly sorry."

    kolya "For what?"

    kolya "Kiril?"

    kolya "Nevermind about that, we've got to get you out of here. You let me know
    after we cross the gates."

    scene shelling_soldiers
    with Fade(2, 1, 4)
    scene shelling_soldiers
    with hpunch

    kolya "Almost there, not long now."

    kolya "You're still with me right? How's that leg?"

    kiril bruised_war "I'd rather have it sawed off, honestly Kolya. I'm not sure how
    much longer I can go on."

    kolya "Don't say that, of course you can. Come now, rest up."

    scene battlefield_101
    with Fade (2, 1, 8)

    show soldier_target

    label hello8:

        ## this is a repeat of the very first gun game.

        scene battlefield_101
        call begin_hunt01
        if _return > 0: # This is a special variable returned from the last call

            kolya "Crap! I got him."
            hide expression position01
            kolya "God...my head."
            scene black with dissolve

        else:

            kolya "Ah"
            scene dead_scene with Fade(2,1,5)
            jump hello8



    label next5:
    play music "<loop 6.333>sounds/Ambient_Joy_mp3.mp3"

    ##PRESENT DAY  HOSPITAL
    #september 1914
    scene chapter3
    with Fade(2,1,6)

    scene hospital
    with Fade(2,1,6)
    show doctor_talk

    doctor_1 "Oh good heavens. Thank God you've woken up."

    doctor_1 "You've been out for weeks did you know?"

    kolya "..."

    doctor_1 "Yes, you had a head and shoulder injury a few weeks prior and then
    you fainted upon seeing a man."
    doctor_1 "You've seemed to have quite the shock."

    doctor_1 "Do you know him?"

    kolya "What's going on? Know who?"

    doctor_1 "Kolya Smirnov is it? It's written on you're tag."

    doctor_1 "Now not to worry. The tag is on the side of the desk see?"

    doctor_1 "Can you tell us what happened? Do you recall at all?"

    kolya "No, not really. I'm sorry."

    doctor_1 "No need to apologise Kolya. You see there was this other patient
    who was taken in with you. You two know each other yes? Are you close?"

    kolya "What?"

    doctor_1 "The man who was with you when you fell. I think his name is Kiril."

    kolya "What? He's here? Where?"

    doctor_1 "He was moved rooms you see, for a precaution."

    kolya "My God! Take me to him."

    doctor_1 "Settle down, we don't want you fainting again. Is it any sort of danger at all?"

    kolya "No, no. Nothing like that. Quite the contrary."

    doctor_1 "Now, Yulianna would you please get me some water and a box of tissues would be nice."

    doctor_1 "He is well, though he seems more concerned for you."

    doctor_1 "It says here you were found just off the German territory. You're a lucky
    man did you know that?"

    kolya "How did I get here? How did {b}{i}we{/i}{/b} get here?"

    doctor_1 "A polish peasant noticed you two lying in a bush almost dead.
    He brought you here."

    doctor_1 "Though I was able to figure out Kiril's wound is much older than yours."

    kolya "Right. The Germans shelled Kiril's leg. I was shot by a soldier."

    doctor_1 "Ah, that explains it. You were both very lucky indeed. You weren't far off

    from the border. The man dragged you here to safety. God bless him."

    doctor_1 "For he has done the greatest deed of all. Both of you would have had
    seconds to go otherwise."

    kolya "Is he not here? I have to thank him. Not for me, but for my friend. Kiril."

    doctor_1 "The man left without a trace. It would be impossible to find him."

    kolya "Right, that's a shame. I owe him my life."

    doctor_1 "Indeed, you both do. Kiril's leg is in an awful shape though. Such a shame
    and so young as well!"

    doctor_1 "Ah well, he lives. That's what's most important."

    kolya "Well, will we...you know? Have to go back?"

    doctor_1 "That's something I'd like to discuss. Many patients with head injurys
    have been known to have an off fit here and there."

    doctor_1 "We'll see how you get on. The bullet hasn't ripped through any vital
    organs. I'd like to remind you, you're very fortunate indeed."

    doctor_1 "If there are any symptoms, be sure to let us know. If they're severe,
    I'll file you for a mental health defect."

    kolya "Would that mean I won't have to fight?"

    doctor_1 "Well yes, but let's not talk about that now. Let's begin you're
    recovery journey shall we?"

    doctor_1 "Though I'd like you to know that my job is not in recruitment. It's not
    my job to decide, all I can do is report the facts."

    kolya "Right, thank you sir."

    hide doctor_talk

    scene corridor
    with Fade(2, 1, 6)
    show kiril_body_smile

    kiril smile "How's your head?"

    kolya "You mean, how's {b}your{/b} leg?"

    kiril "It's getting better thanks, I can even run a bit without it stinging."

    kolya "That's great news Kiril."

    kiril "Have you head back from them?"

    hide kiril_body_smile
    show kiril_body_talk

    kiril talk "You know if you have then I have to, even I don't. I will. Since
    you saved my life and all."

    kolya "That wasn't me, that was the Polish man. I've just carried you to him,
    that's all."

    hide kiril_body_talk
    show kiril_body_smile

    kiril smile "Yeah, don't remind me. That must've been bad for your back."

    kolya "Right, you weighed a ton and a half! Stay away from those pancakes Kiril."

    kiril "You should've left me to die if you're going to be like that!"

    kiril "Besides, you sacrificed so much already, I don't want that to go to waste."

    kolya "As long as I'm fed, I'm happy I guess? Did you eat?"

    kiril "classic Kolya, you're never clued up on anything are you?"

    kolya "Spare me the nagging and tell me. I've only woken up a few days ago."

    hide kiril_body_smile
    show kiril_body_talk

    kiril talk "The price of food has skyrocketed since the start of the war. I wouldn't be able
    to buy myself a loaf of bread without selling my soul."

    kiril "There's been so many riots, I can see them from my window. Can't you?"

    kiril "In fact ,I haven't seen you outside since the day we came here."

    kolya "{i}You{/i} seem well enough to go outside."

    kiril "and you're not?"

    kolya "No, the bright lights and noise is too much. I think I need to stay inside."

    kolya "Why do you want to go out anyway?"

    hide kiril_body_talk
    show kiril_body_smile

    kiril smile "Solidarity. These things affect me too Kolya, I live here."

    kiril "I've missed being in Petrograd."

    kolya "No, you miss Saint Petersburg."

    kiril "It's only a name Kolya. The city never changes. It will always be glorious to me."

    kolya "Glorious? What kind of city conscripts children, untrained and unequipped to
    wage war on a country they do not understand, for a cause they do not understand?"

    hide kiril_body_smile
    show kiril_body_talk

    kiril talk "That wasn't the city that was you."

    kolya "ME!?"

    kiril "You know I didn't mean it like that. I meant me too, we did choose to do the
    things we did didn't we?"

    kolya "Yeah right. I may of chosen, but did you? I thought you were {i}conscripted.{/i}"

    kiril "And your point? It's not the city, it's not even me. It's the country!"

    kolya "Keep talking and we'll see what you're city has in line for you. I have
    a head ache."

    kolya "I'm going back to my bed."

    kiril "Wait, you don't have to leave!"

    ##CENCORSHIP IN RUSSIA FACT CARD

    ## Trooper6. (2015, May 28).
    ## Help with Imagebuttons (make ONLY image itself clickable). Lemma Soft Forums.
    screen fact13():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/cencorship.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact13")

    label callfact13():
    call screen fact13

    label afterFact13:
    kiril smile "BBC Bitesize. (n.d.-b). Tsarist methods of control - policies - Security of the Tsarist state before 1905 - Higher History Revision,
    {a=https://www.bbc.co.uk/bitesize/guides/z9qnsbk/revision/5}
    for more info!{/a}"
    ## NAME CHANGE OF SAINT PETERSBURG FACT
    screen fact13_5():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/name.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact13_5")

    label callfact13_5():
    call screen fact13_5

    label afterFact13_5:
    kiril smile "Schmemann, S. (1991, June 13). Leningrad, Petersburg and the Great Name Debate. The New York Times,
    {a=https://www.nytimes.com/1991/06/13/world/leningrad-petersburg-and-the-great-name-debate.html?smid=url-share}
    for more info!{/a}"

    hide kiril_body_talk
    scene hospital
    with Fade(2, 1, 6)

    show doctor_talk
    doctor_1 "What I'm about to tell you is perhaps what you won't expect. Now it's not my
    decision, you will remember that won't you?"

    doctor_1 "You've spent almost a year now recovering. I've seen you make wonderful
    progress so far and I kknow you'll be right as rain very soon—"

    kolya "Only to be crippled or dead."

    doctor_1 "so you do know what I'm trying to tell you after all."
    ## choice for actions towards the doctor
    menu:

        "Punch the doctor!":
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            show doctor_angry
            doctor_1 "You've lost it now! Perhaps I should file that lunacy report!"
            kolya "Go on, that's great for me."
            doctor_1 "I can stick you in a asylum if that's what you want."

        "Trash the room!":
            show doctor_angry
            doctor_1 "Oh you better tidy this shit up!"
            doctor_1 "What kind of crap did they teach you at that camp?"

    label after_riddle2:

    kolya "Anything is bloody better than going back there!"

    kolya "And I'd suppose I'll turn cracked in the head by the time I return!"

    kolya "I'd like to see you there, do you enjoy being here doing what you do while
    the rest of us go to our deaths?"

    doctor_1 "Without people like me you'd be dead!"

    kolya "Well in that case I'd rather I'd die sooner than later. I shall leave tomorrow morning."

    doctor_1 "A simple thank you would suffice."

    ##FACT CARD NICHOLAS IN CHARGE OF THE ARMY.
    screen fact14():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/chief.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact14")

    label callfact14():
    call screen fact14

    label afterFact14:
    kiril smile "BBC Bitesize. (n.d.). Impact of World War One - Reasons for the February Revolution, 1917 - Higher History Revision. Retrieved 6 April 2021,
    {a=https://www.bbc.co.uk/bitesize/guides/ztyk87h/revision/3 }
    for more info!{/a}"

    scene pondering_near_end_war
    with Fade(2, 1, 6)

    kiril smile "So you've gotten the news huh? I haven't seen you outside for months."

    kiril "You've spent Christmas all on your own in that lousy hospital bed. You could've visited
    me at least once. I didn't know you were that angry Kolya."

    kiril "I'm sorry about what I said. Everyone would've gotten involved in this
    sooner or later."

    kiril "It wasn't your fault and it wasn't mine either. It's no ones."

    kolya "Thanks Kiril."

    kolya "Though what's the point now? Were getting sent back until were presumed dead.
    They're churning us in and out like a machine."

    kolya "It was a terrible Christmas, and I suspect there will be more terrible
    Christmases in the future."

    kiril talk "They don't have a choice but to recruit."

    kolya "Let's leave."

    kiril "What? Leave where?"

    kolya "I mean let's escape. Russia is gone to shit, you know that."

    kiril angry "Clearly the bullet hasn't gone far enough! You're crazy!"

    kolya "Why would I sacrifice my life for a war I don't believe in? Let
    the Tsar fight his own battles."

    kiril "He is fighting! He's the Commander in chief!"

    kolya "I'd like to see him in the front lines like the rest of us. I bet he hasn't set foot there,
    not once!"

    kiril talk "We'll never know about that for sure Kolya."

    kolya "Will I live in that land they want so bad to conquer? I think not!"

    kiril "Where will you go Kolya? Finland? Siberia? Where all the other exhiles live?"

    kiril "I'd love to go. Heck I'd even go before you if I knew where to go. There's no
    way out for this one."

    kiril "I know you hate it. I hate it too, but escaping is impossible."

    kiril smile "I'm sorry."

    kolya "I'd rather have died there than come back here only to return again. I forced
    myself in this because of you."

    kolya "The moment Orlov told me you were alive, God. I had a slight
    sense of—"

    kolya "I don't know how to describe?"

    kiril "Hope?"

    kolya "Yes, hope. I had hope again, though I didn't know what for."

    kiril "I know what you mean. I would've gone beserk if I had made it out
    and you hadn't. How could I carry on?"

    kiril talk "How would I retain my dignity if that were to happen? I wouldn't."

    kiril "We've got to believe that there is something decent ahead."

    kiril smile "Green valleys and the smell of fress grass is all I need, alive or dead."

    kolya "What are you talking about now?"

    kiril "All you need is a little nudge on the shoulder and then you'll see it."

    kolya "See what?"

    kiril "The valley of our one true King."

    kolya "King?"

    kiril "Not that type of king."

    kolya "I don't think I'll make it there."

    kiril "You don't give yourself enough credit. You're a good person Kolya, remember that."

    kiril "If only you knew."

    kiril "It's funny even if you knew you'd of said the same thing."

    kolya "I guess that's why I'm terrified of leaving. "

    kiril "Terrified? I thought you were eager. Now you're all {i}'Let's escape Kiril{/i} on me!"

    kolya "I am, I'm both."

    kolya "I'm terrified of whats to come, the pain. I want it to be over and done with,
    that's what I really want."

    kiril "Okay, enough self pity. The only thing that holds you back is yourself."

    kiril "Go beyond your past Kolya. Find a new meaning, a new purpose."

    kiril talk "Promise me something."

    kiril "Please promise me you'll move on and live your life for once."

    kiril "You're not your mother or your uncle. You're simply a human being that needs love and affection."

    kolya "You're talking as if I'll make it. I've got lucky last time, you can never
    avoid your fate twice Kiril."

    kiril "Course you will! You got me out of there remember?"

    kolya "Yeah well, good luck to the both of us. We'll need all the luck we can get."

    ##FACT CARD, DISCONTENT among tsar NICHOLAS
    ## Trooper6. (2015, May 28).
    ## Help with Imagebuttons (make ONLY image itself clickable). Lemma Soft Forums.
    screen fact15():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/discontent_tsar.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact15")

    label callfact15():
    call screen fact15

    label afterFact15:
    kiril smile "BBC Bitesize. (n.d.-b). Revolution from below - Reasons for the February Revolution, 1917 - Higher History Revision. Retrieved 3 April 2021,
    {a=https://www.bbc.co.uk/bitesize/guides/ztyk87h/revision/5 }
    for more info!{/a}"
    #Train going back picture.

    scene chapter4
    with Fade(2, 1, 6)
    scene train2
    with Fade(2, 1, 6)

    scene army_war
    with Fade(2,1,4)

    kiril angry "To the left!"
    kolya "All right, cover me."
    kolya "Run!"

    scene shelter
    with Fade(2, 1, 6)
    ##year is early 1917
    kolya "So why did you leave?"

    kiril smile "What do you mean? I'm right here."

    kolya "No, not now. I mean before. Why did you leave and never came back?"

    kolya "I waited and waited every summer as a kid, yet you never came."

    kolya "So why? Aren't you going to answer?"

    kiril smile "Who would want to take a whiff of you? Not me, that's for sure."

    kolya "I—"

    kiril "Come, let's not talk about that now. You'll ruin the mood. How about a game?"

    kolya "Go on then, let's have some fun before we die."

    kiril "Don't jinx it for us now!"

    kolya "I'm not!"

    kiril "Let's play 23 truths. It's supposed to be 21, but seen as though it's you're
    birthday today and that it's Christmas. Let's do it."

    kolya "My what? Is it?"

    kolya "It's impossible to track the days now. Every day has been the same."

    kiril "We've officially been through Christmas twice since we've left the hospital and this counts as
    the third. It's quite easy to count."

    kiril "But right, every day is the same. I have no other way of calculating
    the date other than that. Let's make this day memorable then okay?"

    kolya "Today's the day we can relax, at least for a while."

    kiril "That's right Kolya. Here are the rules..."

    kiril "You can only count upwards by 2 or 3 and whoever reaches 23 they have to
    answer a question."

    kiril "I'll start, 1,2."

    ##GAME 23 TRUTHS

    menu:


     "3,4":
         kiril smile "All right, 5,6,7"

     "3,4,5":
         kiril smile "All right, 6,7"


    menu:

     "8,9":
         kiril smile "All right, 10,11,12"

     "8,9,10":
         kiril smile "All right, 11,12"

    menu:

     "13,14":
         kiril smile "All right, 15,16,17"

     "13,14,15":
         kiril smile "All right, 16,17"

    menu:

     "18,19":

         ##    KIRIL WINS
         ## lost game = true
         $ lost_23 = True
         kiril smile "all right, 20,21,22!"
         kiril "Now you have to say 23! That means I win!"
         kolya "Fine 23..."



     "19,20,21":  ##    KOLYA WINS, Kiril Lost
     ## lost game = false
         $ lost_23 = False
         kiril smile "all right, 22,23! Ah!!"
         kiril "Okay you win..."
         kolya "All right, where to begin?"
         kolya "I know..."


    ##kolya loses , kiril wins

    ## if you lose the game (lost game = true )
    if lost_23 == True:
         kiril smile "Don't worry I won't be too {i}invasive.{/i}"
         kolya "Go on then, we don't have all day."
         kiril talk "Why did you leave when you did, why not now?"
         kolya "Way to throw my question back at me..."
         kolya "It took me ages to fund myself for it. Do you know how much a train
         ticket costs if you don't have a wage?"
         kolya "I spent ages working under my uncles, they hardly suspected
         with the amount they earned."
         kiril smile "Well, I'm glad you managed to find me after all these years."
         kiril "Come to think of it, how did you find me?"
         kolya "You said only one question, remember?"
         kiril smile "I did? Since when?"

##kolya wins, kiril loses
## if you win, if lost game = false
    if lost_23 == False:
        kiril smile "Don't be invasive now..."

        menu:
         "What was your biggest screw up?":
             $ kitchen_screwup = True
             kiril smile "Really? I thought you'd go off on a self pity party."
             kolya "You said we should have some fun. Since you're already
             cracked in the head, I want to know the baddest thing you've done. Ever."
             kiril smile "Well, there was this one time when my mother was out, I
             was so cold I couldn't help myself. You know that feeling right?"
             kolya "Course, who doesnt? Get on with it, Hahah!"
             kiril smile "The bloody fire was so weak, I could barely feel my downstairs!."
             kiril "You'd think I was crazy!"
             kolya "Oh Lord, what did you do?"
             kiril "We hadn't enough logs and like the lazy ass I was back then
             I couldn't be asked to get up and go get some."
             kolya "And then?"
             kiril "I poured oil over the fire."
             kiril "Only a bit!"
             kolya "What the heck Kiril! I'd love to see you struggling in that!"
             kiril "I know! My mother was livid! absolutely livid! You should've seen her face!"
             kolya "That's one massive screw up."
             kiril talk "You can say that again. I never cooked again until—"
             kolya "I'm hungrier than ever now."
             kiril smile "Me too, but all we have is this stale piece bread."
             kiril "Here, consider it your birthday cake."
##option 2 choice, which leads to two other questions.
         "Why did you leave that summer?":
             ## if you didnt pick the first, kitchen_screwup is set to false
             $ kitchen_screwup = False

        if kitchen_screwup == False:
            ## if it's false then lead to option 1
            $ kiril_points += 1;
            $ renpy.notify ("Kiril's affection +1")
            kiril talk "You said you wouldn't be invasive!"
            kolya "How on earth is that invasive?"
            kiril talk "I'm not in the mood to talk about such sentimental questions."
            kiril talk "I thought we were playing this game so we wouldn't!"
            kolya "You thought."
            kiril "Come on, ask before I shut up for good."
            kolya "All right, all right."
            menu:
                "What was your biggest screw up?":
                    kiril smile "Really? I thought you'd go off on a self pity party."
                    kolya "You said we should have some fun. I want to know how many times
                    you F***ed the kitchen."
                    kiril smile "Well, there was this one time when my mother was out, I
                    was so cold I couldn't help myself. You know that feeling right?"
                    kolya "Course, who doesnt? Get on with it, Hahah!"
                    kiril smile "The bloody fire was so weak, I could barely feel my downstairs!."
                    kiril "You'd think I was crazy!"
                    kolya "Oh Lord, what did you do?"
                    kiril "We hadn't enough logs and like the lazy ass I was back then
                    I couldn't be asked to get up and go get some."
                    kolya "And then?"
                    kiril "I poured oil over the fire."
                    kiril "Only a bit!"
                    kolya "What the heck Kiril! I'd love to see you struggling in that!"
                    kiril "I know! My mother was livid! absolutely livid! You should've seen her face!"
                    kolya "That's one massive screw up."
                    kiril talk "You can say that again. I never cooked again until—"
                    kolya "I'm hungrier than ever now."
                    kiril smile "Me too, but all we have is this stale piece bread."
                    kiril "Here, consider it your birthday cake."

    label after_23_truths:
    #1917 - late feburary
    scene night_trench
    with Fade(2,1,6)

    kiril talk "They're saying Petrograd toppled over.You know what that
    means right?"

    kolya "No, what does it mean? We can't go back?"

    kiril "Typical. I know a few who have refused to fight for a while now."

    kolya "So you're going to desert because so and so's left the army?"
    kolya "Now you're crazy."

    kiril "Let's take your advice, let's leave."

    kiril "I know it's a suicide mission. I know."

    kiril "But it's the only way we can get away. Everyone hates it out here, hates it
    in Petrograd too."

    kolya "Then where will we go? If we can't stay here and we can't stay there?"

    kiril "I'm telling you, we have to do this. We've got to do it."

    kolya "What if they file us as a deserter? We could die out there Kiril."

    kiril angry "We'll we can die out here just as easy!"

    kolya "Don't make me run when I was just getting used to this."

    kiril "Hear yourself Kolya! I've got more flees than I'd have girlfriends!
    Now that's saying something."

    kiril talk "I know you've always thought of me as an arrogant ass."

    kolya "I never."

    kiril "I know that your worried about life after the war. That there isn't much
    for people like you even without it."

    kolya "What do you know about it? I'd like you to live a second of my life."

    kiril "Come to think of it, I'm quite lucky. I was never short of cash."

    kiril "Visiting you and the village, I felt like I had stepped back in time."

    kolya "You're living off your parents, yeah you're lucky."

    kiril "Yes, I get it. I thought the riots we met back then were bad, but I hear
    it's gone out of proportion over there in Petrograd."

    kolya "Everyone has a right to bread Kiril. What's so wrong about that?"

    kiril "No, not that. I mean even the army stopped firing their weapons. Some anyway."

    kiril "I was lucky I wasn't shot back then! Though I was kept well away from the front."

    kolya "You haven't told me about that."

    kiril "How could I? Soldiers firing at men and women for simply protesting? To say I was
    ashamed wouldn't quite cut it."

    kiril "Look, were leaving. Revolution is coming Kolya and it's calling us to it."

    kiril "I'll tell the others tomorrow."

    kolya "Others?"

    kiril "Yes! You'lll be surprised how many want to flee."

    kolya "When you put it like that, God. You make me feel ashamed."

    ##fact card 15.5
    ##	Trooper6. (2015, May 28).
    ##  Help with Imagebuttons (make ONLY image itself clickable). Lemma Soft Forums.
    screen fact15_5():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/abdication.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact15_5")

    label callfact15_5():
    call screen fact15_5

    label afterFact15_5:
    kiril smile "BBC Bitesize. (n.d.-c). The abdication of Tsar Nicholas II in 1917 - KS3 History. Retrieved 3 April 2021,
    {a=https://www.bbc.co.uk/bitesize/clips/zkt97ty}
    for more info!{/a}"

    scene escape_time
    with Fade(2,1,6)

    vladimir talk1 "Now what are you two stiff eyed boys doing still alive?"

    kiril talk "Sir!"

    vladimir talk1 "That's Sergant to you."

    vladimir talk1 "Now let me get straight to the point. I've come back from my
    side of the trench still very much wide-awake from all that Vodka I downed a minute ago."
    vladimir talk1 "I might be drunk off my ass but I overheard the word 'escape' coming
    from your mouth. That's right."

    vladimir talk1 "I'd never thought it would come from a fine soldier such as yourself
    but I guess you two really are one in the same."

    kiril talk "We were talking about the protests, it was nothing but words said by others."

    vladimir talk1 "Don't fool yourself. Now give me the real story or this won't end lightly."

    kolya "Kiril! He's innocent, I swear upon the Lord almighty."

    kiril smile "Hahha!"

    kiril "Oh God, stop Kolya I can't!"

    kolya "What? Why are you laughing? Don't you care what happens to you?"

    vladimir talk1 "Now that was amusing."

    kiril "Right! Kolya relax, he's on our side."

    kolya "what on bloody earth are you saying?"

    vladimir talk1 "Though you told a grave lie by swearing upon God, I'd have you punished for that."

    vladimir talk1 "After doing what is necessary that is."

    kolya "What's necessary? What are we even doing?"

    kiril "Let me fill you in, now listen carefully..."

    scene escape_time
    with Fade(2,1,3)

    vladimir talk1 "So you got it?"

    kolya "Wait let me replay this."

    vladimir talk1 "You didn't warn how slow he was Kiril."

    vladimir talk1 "People have been revolting since Feburary."

    kolya "Okay, but why do you need us?"

    vladimir talk1 "The situation has become dire, you need to understand this properly."

    vladimir talk1 "Now I need you both to get me to the train station."

    kolya "But you're a Sergant, why would you need permission?"

    vladimir talk1 "You thought wrong."

    kolya "Tell me why you need us?"

    vladimir talk1 "I need cover. North, south, east, west. All of it."

    kolya "{b}{i}You{/i}{/b} need cover!"

    vladimir talk1 "Be quiet, I could file you both for treason if that's what you'd like."

    vladimir talk1 "My work is much too important."

    vladimir talk1 "The Tsar will be stopped just before he reaches Petrograd,
    the Bolsheviks must have the upper hand!"

    kolya "What about the shelling? You want us to risk our lives for you and a lousy party?"

    vladimir talk1 "This party is the hope of Russia. It has set things in motion which
    cannot be undone. It's inevitable, a free Russia based on the works of Marx and Lenin."

    vladimir talk1 "We don't have a choice. Once we reach the border station, you are free to
    do as you will."

    vladimir talk1 "They'll be plenty of others who will join us, don't get it into your head that
    it's only about you, it's not."

    kiril "Anyway... the plans perfect right?"

    ## FACT CARD ABOUT febuary revolution

    screen fact16():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/feburary.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact16")

    label callfact16():
    call screen fact16

    label afterFact16:
    kiril smile "BBC Bitesize. (n.d.-b). Reasons for the failure of the Provisional Government under Kerensky -
    February Revolution - Causes, events and effects - National 5 History Revision. Retrieved 10 April 2021,
    {a=https://www.bbc.co.uk/bitesize/guides/z43tcqt/revision/7}
    for more info!{/a}"

    scene pre_bomb_scene
    with Fade(2, 1, 4)

    kiril talk "Ready?"

    kolya "No, I'll never be ready for these things. This is ludicrous!"

    vladimir talk1 "You and me both."

    kolya "Funny, we actually agree on something for once."

    vladimir talk1 "Now as I'm Sergant, Kiril will go to the left and Kolya will go to the right."

    vladimir talk1 "The rest of you will run up to the front and I'll be in the back."

    scene bombs
    with Fade(2,1,6)

    kiril bruised_angry "Shit!"

    kiril "Don't you bloody help me, run!"

    kolya "No way, I'll never do that! Give me your arm quick!"

    kiril "You'll die please go."

    kolya "If you die, I'm going whereever you are."

    kiril "Ah! Don't grab my arm like that hard!"

    kiril "God, it might fall off at this rate."

    kolya "We'll get you a medic, you'll be sent back home don't worry about it."

    kolya "It will be all right, just trust me."

    kiril "I beg you don't do this."

    kolya "Shut it and let me concentrate."

    kiril "On what!? Where's Vlad?"

    kolya "I don't know! I can't see anything with all this smoke!"

    kiril "Bloody Germans!"

    kolya "Come on, I doubt it's not that far away now. We'll get there Kiril."

    kiril bruised_war "If the guns won't take us out, the zepplins will."

    kolya "Oh Jeez, thank's for that one Kiril."

    kolya "Since when were you lost of hope? I thought that was me."

    kiril "I'm not delusional Kolya."

    kolya "Don't say that. All you have to do is stay with me, all right?"

    scene trench1
    with Fade(2, 1, 6)

    vladimir talk1 "Good, now that you're up we should get going."

    kolya "After all his been through? No way."

    kolya "They've should've gotten you instead!"

    vladimir talk1 "Please, without me you'd have no chance making it beyond the trenches.
    You tell me that huh?"

    kolya "Kiril? You're okay aren't you?"

    kiril bruised_war_dying "Look, I think you two should go on ahead."

    kolya "No, don't say that please. I'll carry you."

    kiril "I way a ton, you've done it once and now twice. Face it, it's over."

    kiril "Look at my arms and legs. I'm a gonner for sure."

    kolya "We have to get you medic. That's it, that's it!"

    kiril "Don't bother with me. The Germans won't stop firing, I'll only
    slow you down. Please you must go!"

    kolya "Don't please."

    kolya "Wake up!"

    kiril "What?"

    kolya "Look at me when I'm talking to you."

    kiril "I always told you, you were the better soldier."

    kolya "Leaving you won't make me any better, I really can carry you, to the
    border at least."

    kiril "No Kolya. Being carried by you felt like death. I don't know how many
    times I've passed out."

    kiril "I think you've forgotten about the valley."

    kolya "Don't talk about that, we can go to our valley together."

    kiril "What I'm doing, where I'm going is what everyone will do. How can something
    so common be so terrifying?"

    kolya "You're not the one to say this! Tell me you'll live, tell me you'll survive."

    kiril "There's a difference between hope and the impossible."

    kiril "Look, I'm not sure how long I can take this. I feel so cold. Can you
    check my leg?"

    kolya "Sure, anything."

    kiril "So how does it look? Red? Black?"

    kolya "It looks good."

    kiril "Don't lie to me. There's hardly anything of it left."

    kolya "There are plenty of people who are amputees Kiril, you can do this."

    kiril "I have things to tell you before I go. Will you listen?"

    kolya "When you're on a hospital bed, sure."

    kiril "Now's not the time to joke around. I mean it. If you had an ounce of
    love for me you'll listen!"

    kolya "Of course I do, an ounce and an infinity more."

    kiril "My parents, I told you they'd gone to a business trip."

    kolya "Yeah, it seems like a pretty long one at that. I'll let them know,
    if that's what you're asking."

    kiril "No, that's not it. Besides they'd probably know."

    kiril "They're dead Kolya."

    kolya "What?"

    kiril "They're dead! I lied, I wanted to tell you but I didn't know how. I
    didn't want you to pity me. Not after what they made you go through."

    kolya "What are you talking about? Your parent's are great. They're a lot like you
    actually."

    kiril "Please don't compre me with them. Though I guess I'm not different."

    kiril "I went out one day in the summer to collect some leaves for the den. I stopped
    at yours but your mother told me you were with one of your uncles."

    kolya "Kiril, please."

    kiril "I saw everything. I ran away as fast as I could. I kept it a secret since
    I was so embarassed."

    kolya "Don't—"

    kiril "One day my mother came by and told us to pack our things though she didn't say why
    until she was on her death bed."

    kolya "I don't need to know, I don't want to know."

    kiril "Oh but you do. She told me why we left, it was because of you. I want you to
    know she is so sorry about everything."

    kiril"I'm not telling you to forgive her, I have not. I was a child, but she an adult
    refused to visit the village after what had happened. That's shameful."

    kiril "I'm so sorry Kolya, truly so very sorry. I've never been so sorry in
    my entire life."

    kolya "You're the only one who has never really hurt me. It's not your fault."

    kiril "But it was. I ran when I could've saved you from that torment. I couldn't
    get that image out of my head for days on end."

    kiril "Helpless, so vulnerable."

    kiril "Kolya, say you'll forgive me?"

    kolya "Of course, there's nothing to forgive Kiril."

    kolya "Is that what you think of me now? Do you still see those images of me?"

    kiril "No, well a little. Only at times when your full of pity. I don't want you
    to think about what happend. It will get easier, I've started the conversation for you now."

    kolya "Was all this so you could say that?"

    kiril "No, for the love of all things good in this world, no. Now forgive me again,
    I'm afraid your cross with me."

    kolya "How could I ever be cross with you Kiril? I'm just tired. Of course you're forgiven."

    kolya "When I look at you all I see is the things we did together down at the village."

    kiril "You can do those things again one day I promise you."

    kolya "My childhood ended long ago Kiril."

    kiril "No, I mean with your children. "

    kolya "Kolya, how can I ever love a human being when I'm disgusting. You know me."

    kiril "I swear, if I ever hear you call yourself disgusting from above, I'll make sure
    you really—"

    kolya "What? I've lived through it all, go ahead and do your worst."

    kiril "I'm sorry. I get angry."

    kolya "I know, it's all right."

    kiril "But it's about time you heal this wound of yours."

    kolya "You're one to talk!"

    kolya "I wish it were me and not you. I'd honestly feel at peace."

    kiril "I know..."

    kolya "Kiril?"

    kiril "God, my leg."

    kolya "You've always been my best friend, even when you left. I still called you my
    best friend."

    kolya "I love you, I love you to death. Don't die, please!"

    kiril "I love you too Kolya."

    kiril "Save some love for yourself and your future. Have a family, and do the things
    we did. You'll have fun."

    kolya "You're forgetting I already have one."

    kolya "You!"

    kolya "What will I do without you? Where will I go?"

    ## all these points lead to this screen, if they collect > 4
    ## then you can open up a letter

    if kiril_points > 4:

        kiril "Take this, I was going to give it to you ages ago."
        ##TAKE KIRILS LETTER IMAGE.
        kiril "Ah crap, It's ripped."
        ## LETTER IS OPPOSITE WAY CLICK TO READ LETTER,
        screen letter():
            modal True
            imagebutton:
                xpos 300
                ypos 130
                idle "find_object_game/letter.png"
                focus_mask True
                action None

            imagebutton:
                xpos 800
                ypos 570
                idle "images/ok.png"
                hover "images/ok_hover.png"
                focus_mask True
                action Jump("afterletter")

        label callletter():
        call screen letter

        label afterletter:

        screen openletter():
            modal True
            imagebutton:
                xpos 300
                ypos 0
                idle "find_object_game/open_letter.png"
                focus_mask True
                action None

            imagebutton:
                xpos 1000
                ypos 570
                idle "images/ok.png"
                hover "images/ok_hover.png"
                focus_mask True
                action Jump("afteropenletter")

        label callopenletter():
        call screen openletter

        label afteropenletter:

        screen openletter2():
            modal True
            imagebutton:
                xpos 300
                ypos 0
                idle "find_object_game/open_letter2.png"
                focus_mask True
                action None

            imagebutton:
                xpos 1000
                ypos 570
                idle "images/ok.png"
                hover "images/ok_hover.png"
                focus_mask True
                action Jump("afteropenletter2")

        label callopenletter2():
        call screen openletter2

        label afteropenletter2:

        kolya "What's this? I can't read."

        kiril "It's the papers for the house, and a note. You know? Since my parents
        are no longer here."

        kiril "I want you to find someone in the future, someone you trust to be able to read
        that to you."

        kolya "I don't need this."

        kiril "Don't refuse, consider it a parting gift."

    kolya "I'll never forget you, Kiril."

    kiril "I know, I won't either."

    kolya "Thank you."

    kiril "I'm glad, really glad I've got to see you again."

    kolya "Me too."

    kiril "We'll see each other again."

    kiril "Now, go."

    kiril "Go!"

    vladimir talk1 "Come on, enough, we have to move."

    vladimir angry1 "Now!"

    ## SERIES OF IMAGEs
    ## KOLYA CARRYING KIRIL
    scene shelling_soldiers2
    with Fade(2,1,6)

    scene deadkiril1
    with Fade(2,1,6)

    scene left_kiril
    with Fade(10,1,6)

    ## FACT CARD ABOUT MENTAL HEALTH
    ##FACT CARD ABOUT END OF WW1 , DEATHS ETC
    ##	Trooper6. (2015, May 28).
    ##Help with Imagebuttons (make ONLY image itself clickable). Lemma Soft Forums.

    screen fact17():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/mentalhealth.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact17")

    label callfact17():
    call screen fact17

    label afterFact17:
    kolya "Experiences on the Western Front. (n.d.). Impact on Soldiers and their Families. World War 1 - Experiences on the Western Front. Retrieved 3 April 2021,
    {a=https://experiencesonthewesternfront.weebly.com/impact-on-soldiers-and-their-families.html}
    for more info!{/a}"

    screen fact18():
        modal True
        imagebutton:
            xpos 300
            ypos 130
            idle "images/newspaper_facts/end_war.png"
            focus_mask True
            action None

        imagebutton:
            xpos 800
            ypos 570
            idle "images/ok.png"
            hover "images/ok_hover.png"
            focus_mask True
            action Jump("afterFact18")

    label callfact18():
    call screen fact18

    label afterFact18:
    kolya "BBC Bitesize. (2020, January 14). How did World War One end and what happened next?
    {a=https://www.bbc.co.uk/bitesize/topics/zqhyb9q/articles/zkb86v4}
    for more info!{/a}"


    ## end game, and credit / acknowledgements
    scene credits
    with Fade(2,3,6)

    scene acknowledgements
    with Fade(2,3,6)

    scene black_bg
    with Fade (2,1,3)



    return
