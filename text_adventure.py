"""
Describe your text adventure experience.
Yoav Bierkatz - September 2026
"""
def where_am_i() -> None:
    """
    Manage experience after where am I
    """
    print("""You struggle to breathe as you recall that your best friend betrayed you
     and burned down your house""")

    input("Press Enter to continue")

    print("""You hear crackling and whining,
     and realize that the roof is going to fall any second but you cant remember anything about yourself""")

    response: str = input("""Who are you?
    1) Boy
    2) Girl """)

    input("What is your name? ")
def where_am_i_pt2() -> None:
    """
    Manage experience after who are you for where am I
    """
    print("""As you remember who you are and that your friend betrayed you, 
    you smell the smoke all around you and hear the roof falling.""")

    input("Press Enter to continue")

    print("""As you try to escape the roof completely gives out and 
    just as you get one foot through the doorway the other gets trapped under the burning roof.""")

    input("Press Enter to continue")

    print("""The pain shoots up your leg then stops, as you lose all feeling in your leg and realize its on fire. 
    The last thing you see is the picture of your best friend smirking at you as you black out.""")

    input("Press Enter to continue")

    print("YOU DIED.")
    
def escape() -> None:
    """
    Manage experience after escape.
    """
    print("""You manage to get out of the house just in the nick of time,
    as the roof collapses behind you""")

    input("Press Enter to continue")

    print("""As the roof collapses,
    you realize you don't remember anything, not your name nothing. """)

    response: str = input("""Who are you?
    1) Boy
    2) Girl """)

    input("What is your name? ")




def main() -> None:
    print("""You wake up to the smell of smoke and the cloudy air surrounding you. 
    You slowly open your eyes only to see the orange air around  you.""")

    response: str = input("""What do you try to do.
    1) Escape	
    2) Where am I? 
    """)

    if "1" in response:
        escape()

    elif response == "2":
        print("")
    else:
        print("Invalid input")    
        main()
if __name__ == "__main__":
    main()