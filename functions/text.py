import time

def intro():
    time = [1, 2.5, 2, 1.5, 1, 2, 1]
    text = ["Your in a maze, and you are lost",
            "Im sure there\'s evil lurking in the shadows...",
            "There\'s five swords to make it out alive.", "Be wise with them!",
            "Ready to go!"]
    print_on_a_timer(time, text)

intro()