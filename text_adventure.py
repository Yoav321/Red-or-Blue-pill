"""
Interactive test adventure where the player is in a burning house and has to choose between their best friend and revenge.
Yoav Bierkatz - September 2026
"""
def where_am_i() -> None:
    """
    Manages experience after where am I
    """
    print("""You struggle to breathe as you recall that your best friend betrayed you
and burned down your house
""")

    input("Press Enter to continue\n")

    print("""You hear crackling and whining,
and realize that the roof is going to fall any second but you can't remember anything about yourself
""")

    response: str = ""
    while response == "":
        response = input("""Who are you?
    1) Boy
    2) Girl
     """)

    # Not storing it, won't be used.

    input("What is your name? ")

    where_am_i_pt2()

def where_am_i_pt2() -> None:
    """
    Manages experience after who are you for where am I
    """
    print("""As you remember who you are and that your friend betrayed you, 
you smell the smoke all around you and hear the roof falling.
""")

    input("Press Enter to continue\n")

    print("""As you try to escape the roof completely gives out and 
just as you get one foot through the doorway the other gets trapped under the burning roof.
""")

    input("Press Enter to continue\n")

    print("""The pain shoots up your leg then stops, as you lose all feeling in your leg and realize it's on fire. 
The last thing you see is the picture of your best friend smirking at you as you black out.
""")

    input("Press Enter to continue\n")

    print("YOU DIED.")
    
def escape() -> None:
    """
    Manages experience after escape.
    """
    print("""You manage to get out of the house just in the nick of time,
as the roof collapses behind you.
""")

    input("Press Enter to continue\n")

    print("""As the roof collapses,
you realize you don't remember anything, not your name, nothing. """)

    response: str = input("""Who are you?
    1) Boy
    2) Girl 
    """)

    print("""As you stand there trying to remember more things about yourself, 
you watch your house burn to ashes as the sky around you 
turns orange and the smell of fire grows stronger and stronger.""")

    escapept2()

def escapept2() -> None:
    """
    Manages the stash and police transfer
    """
    response: str = input("""Do you 
    1) call the police, or
    2) walk away from the house to the secret stash you swore you would never touch again
    """)

    if "1" in response:
        police()

    elif "2" in response:
        stash()

    else:
        print("Invalid input")    
        main()
def police() -> None:
    """
    Manages the police response
    """
    print("""As the police arrive you recall all the terrible things that you did in your life 
and the police tackle you to the ground and put you in maximum security jail for the rest of your 
natural life
""")

    input("Press Enter to continue\n")

    print("The End.")
def stash() -> None:
    """
    Manages the stash branch
    """
    print("""As you walk away from the bonfire that your house has become and flinch as you remember 
the absolute horrors that you did and swore to your dead wife never to go back to. 
But you will NOT let your former best friend get away with this, 
even if it's the last thing that you do.
""")

    response: str = input("""How determined are you really?
1) I can't actually do this. He was my best friend. I can't do this.
2) Even if I don't get the revenge I want, I will make his life a living fiery ball of hell until my last breath
""")

    if "1" in response:
        coward()

    elif "2" in response:
        committed()

    else:
        print("Invalid input")    
        main()
def committed() -> None:
    """
    Manages the committed branch
    """
    print("""You go to your stash and empty everything from it 
and use those tools to exact your revenge on your former best friend
""")

    input("Press Enter to continue\n")

    print("As you watch their house burn, you wonder, was it really worth it?")

    input("Press Enter to continue\n")  

    print("The End.")
def coward() -> None:
    """
    Manages the coward's way branch
    """

    print("""As you reach your stash, the adrenaline washes away 
and the clarity of what you were going to do hits you hard, 
making you stumble into the wet grass and you break down crying
""")

    input("Press Enter to continue\n")   

    print("The End.")

def main() -> None:
    print("""You wake up to the smell of smoke and the cloudy air surrounding you. 
You slowly open your eyes only to see the orange air around you.""")

    response: str = input("""What do you try to do?
    1) Escape	
    2) Where am I? 
    """)

    if "1" in response:
        escape()

    elif "2" in response:
       where_am_i()
    else:
        print("Invalid input")    
        main()
        
if __name__ == "__main__":
    main()