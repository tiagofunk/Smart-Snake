# remove pygame welcome message
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from UI import UI

if __name__ == '__main__':
    ui = UI()
    ui.run()