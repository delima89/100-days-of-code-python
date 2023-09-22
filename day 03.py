print(""""
                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------""")
print("Welcome to Treasure Island.Your mission is to find the treasure.")
s1=input("left or right?").lower()
if s1 =="right":
    print("game over").lower()
s2=input("swim or wait?")
if s2 == "swim":
    print("Attacked by trout.Game Over.")
s3=input("Which door?\nred,blue,yellow?").lower()
if s3== "red":
    print("Burned by fire.Game Over.")
elif s3=="blue":
    print("Eaten by beasts.Game Over.")
elif s3=="yellow":
    print("you win")
else:
    print("gmae over")