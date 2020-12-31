# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
#Chapter 1: Where it began and where it ended.
#Kolya's flashback.
label start:
    play music "<loop 6.333>sounds/warfare_despair01.mp3"

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

    scene battlefield
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
     the rags that we held on us festered with lice, god damn the lice!
     God damn leeches they were!"

    kolya "We were all leeches, sucking on the edge of life and death itself
    and the three-pound firing canon would not bloody stop.
    I was so sure I’d be a deaf man before I would become a dead one."

    kolya "What were we thinking?"

    kolya "There he was, the man who I had been waiting for all my life.
    The angel had come to take me away; I was so sure of it."

    kolya "Blond and beautiful, singing strange songs in a strange voice."

    kolya "There we go, come closer. You are ever so close aren’t you?"

    kolya "Aren’t I also? The gate to the world above is ever so near.
    I can almost hear it’s hymns in the tunnel of light."

    kolya "Louder, Louder!"

    kolya "Argh!"
    kolya "I can feel my fingertips crawling ever so close to the
    ‘monster machine’ I’d called it so often."

    kolya "‘Do it now!’ I screamed at the German."

    kolya "‘Kill me!’"

    kolya "‘Kill me now!’"

    play music "<loop 6.333>sounds/Ambient_hope.wav"

    scene hospital_bed
    with Fade(2, 1, 6)

    # click on the gun three times to shoot, small spinning gun mini game.

    #Flashabck ended, Kolya wakes up at the hospital.
    #Kolya and a strange man are talking, seperated by a hospital curtain.
    kolya "So that's the story."

    kolya "A man begging for his own end."

    kolya "Would you call me a coward? Would you call say I'm weak?"

    stranger "Why did you want it to bad?"

    kolya "Who wouldn't!?"

    kolya "You say yourself you were there. Isn't Death the ultimate
    equaliser?"

    kolya "What's so wrong in wanting the inevitable?"

    stranger "No that isn't what I meann."

    stranger "I'm not calling you a coward for anything you went through."

    kolya "No, but you asked why I wanted it."

    stranger "Well yes b—"

    kolya "And I answered didn't I?"

    stranger "Yes, you answered."

    stranger "You are alive now aren't you? Do you still want it?
    Your death I mean?"

    kolya "Yes, I do. Even now..."

    stranger "And why is that—?"

    kolya "I just told you, they'll make us go back there soon enough."

    stranger "Surely you don't mean that?"

    kolya "Of course I meant it. Don't make me repeat
    myself again for christ's sake."

    stranger "No, I'm sorry."

    stranger "Don't you have anyone to return to? Surely everyone has someone."

    stranger "Son or daughter? A wife? Mother or father? Even siblings?"

    kolya "There's no one—"

    stranger "Surely you can't be serious. People like to think emotionally
    ,thinking they're the only one in the world who feels like they do."

    stranger "Oh grow up will you? You don't."

    kolya "What did you say!? Have you any idea!?"

    #click to open the curtain..
    show patient
    with dissolve

    kolya "Oh my god..."

    kolya "Kiril."

    show black_bg
    with irisin

    scene kiril_house
    with Fade(2, 1, 6)
    #flashback to the pre war years.
    show kiril_body_talk
    kiril_full "so what's it going to be today?"

    kolya "And good morning to you too!"

    kolya "You haven't told me what's on offer yet."

    kiril_full "Yes, yes morning."

    kiril_full "Well... we have Kasha or
    I can whip up a good Blini if you'd prefer it."

    hide kiril_body_talk
   #first choice that user will make is between foods!
    menu:

        "Kasha please":
            show kiril_body_talk
            kiril_full "Goodness, you've gone so boring Kolya!"
            kolya "Call it a bodily investment haha."
            scene kasha
            #image of kasha
            hide kiril_body_talk
        "I've been on savoury foods for far too long, Blini.":
            show kiril_body_talk
            kiril_full "Ah yeah! Now were talking!"
            kolya "Need to compensate the lack of sweetness in our lives
            some how right?"
            scene blini

            hide kiril_body_talk
            #image of blini/pancake

    label after_menu:
    kolya "Thanks Kiril, I really mean it."

    kolya "I don't want to be a burden or anything. Just give me the world
    and I'll leave. You wont even notice I'm gone."

    kiril talk "Relax will you Kolya, it's alright. Just help me pay the
    rent and we'll make it work."

    kolya "I'd never thought I'd result into this... you know?"

    kolya "Anyway rent? That's easy. I just need a job."

    kiril smile "Of course! Everything is easy for {i}clever{/i} man like you.
    You're all brains!"

    kolya "What about you?"

    kolya "All fun and games, no work and no study."

    kiril smile "Well I like to say I excel in practical knowledge and
    common sense!"

    kolya "So then, I take it that you didn't have enough comment sense
    regarding the fact I'm squatting in your house."

    kiril smile "Well at least it's not both of us squatting. I am practically
    the owner you know."

    kolya "No you're not."

    kolya "It's your Father who owns these four walls, not you."

    kiril talk "Well yes, but they did leave it under my care."

    kolya "They did, did they? And where are they now?"

    kiril talk "Relax, there on a business trip and won't be back for a few
    weeks."

    kolya "And they don't know I'm here do they?"

    kiril smile "I said relax, good grief. No they don't but I don't see why
    they won't approve. We've known each other for years!"

    kolya "Almost 2 decades, on and off actually. God I can't stay here, what
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

    kolya "I don't even know if I even have a single friend left on this planet
    to tell you the truth, did I even have one to start with? I can't recall."

    kiril "Look, come to the registration office with me today, it's still
    bright and early. You'll feel different about it, I promise you."

    kolya "I already told you— No."

    kolya "They did everything they could to make me join, what makes you think
    I'd join after suffering that."

    kiril "That's easy, they're your parents and not me! So stop crying."

    kiril "Call your parents tomorrow, I'm sure they'll be thrilled. You'll be
    free of them the moment you join."

    kolya "Ah, great. Now I really can't join."

    kiril talk "Better join sooner rather than later. Don't want to get
    classed as the poor farmer boy who never held a weapon in his life, do you?"

    kolya "I don't care for these things, I've already had enough of it
    from my family and I do not need it from you. Take it in long enough and
    it becomes meaningless."

    kolya "The world's gone meaningless. The last thing I wanted is to becomes
    as slave!"

    kolya "It's all the same, my parents, the army. I wonder when will
    humans learn to listen rather than yell."

    kiril talk "Okay, I guess we talked about it for long enough now. You
    haven't eaten a bite yet. Come on, you look like you haven't eaten in days!"

    kiril smile "Eat up now and save the worries for another time."

    kolya "Right, I'm sorry. I've gone off on one haven't I?
    I will eat."

    kiril smile "No problem. Don't worry about it."



#street scene, goes to registration office, pub.

    scene Street_path

    return
