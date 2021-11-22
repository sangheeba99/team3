import pygame as pg
import os, time, random

TITLE = "4 Beats"       ### default setting
WIDTH = 640
HEIGHT = 480
FPS = 60
DEFAULT_FONT = "NotoSansCJKkr-Regular.otf"

WHITE = (238, 238, 238)     ### color setting
BLACK = (32, 36, 32)
RED = (246, 36, 74)
BLUE = (32, 105, 246)
ALPHA_MAX = 255

class Game:
    def __init__(self): ########################## Game Start
        pg.init()
        pg.display.set_caption(TITLE)       #title name
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))      #screen size
        self.screen_mode = 0    #screen mode (0: logo, 1: logo2, 2: main, 3: stage select, 4: play, 5: score)
        self.screen_value = [-ALPHA_MAX, 0, 0, 0]       #screen management value
        self.clock = pg.time.Clock()        #FPS timer
        self.start_tick = 0     #game timer
        self.running = True     #game initialize Boolean value
        self.song_select = 1    #select song
        self.load_date()        #data loading
        self.new()

    def load_date(self):  ########################## Data Loading
        self.dir = os.path.dirname(__file__)

            ### font
        self.fnt_dir = os.path.join(self.dir, 'font')
        self.gameFont = os.path.join(self.fnt_dir, DEFAULT_FONT)

        with open(os.path.join(self.fnt_dir, 'language.ini'), "r", encoding='UTF-8') as language_file:
            language_lists = language_file.read().split('\n')

        self.language_list = [n.split("_") for n in language_lists]


