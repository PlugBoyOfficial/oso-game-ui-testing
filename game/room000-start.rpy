﻿# The game starts here.

label start:

    # setting all the flags to false (is there really no better way to do this?) (prepared to sound stupid)
    $ win_flag = False
    $ item_butterfly_package = False
    $ quest_retainer = False
    $ saw_retainerblock = False
    $ party_bs = False
    $ money = 0
    $ quest_bs = False
    $ dolly_first = False
    $ saw_museum = False
    $ saw_blue = False
    $ item_red_cash = False
    $ saw_redtile = False
    $ item_ladle_empty = False
    $ item_ladle_full = False
    $ miso_took = False
    $ quest_painting_blue = False
    $ item_painting_blue = False
    $ item_makeshift_trophy = False

    scene bg room

    show posty happy

    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    menu:

        "Start the game.":
            jump firstscene
            
        "Developer testing room.":
            jump chartest

