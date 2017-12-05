# David Ding
# ICS3U1
# Final Summative Game

# ========================== IMPORTS
import pygame
import math
import random
from pygame import *
pygame.init()
pygame.mixer.init()

# SCREEN_SIZE is a constant that defines the screen size
# myClock is a variable that handles the frame rate
# screen is the screen
SCREEN_SIZE = (800, 600)
myClock = pygame.time.Clock()
screen = display.set_mode(SCREEN_SIZE)

# == Rectangles
# Main Menu Rectangles
MAIN_RECTS = {
    # UPPER_RECT is the rectangle for "PLAY!"
    "UPPER_RECT": Rect(100, 300, 600, 50),
    "LOWER_RECT": Rect(100, 450, 600, 50),
    "TITLE": Rect(200, 200, 400, 100),
    "TEXT ONE": Rect(150, 320, 200, 50),
    "TEXT TWO": Rect(150, 470, 200, 50)
}

# Character Selection Rectangles
CHAR_RECTS = {
    "CHAR_ONE_RECT": Rect(200, 400, 50, 50),
    "CHAR_TWO_RECT": Rect(300, 400, 50, 50),
    "CHAR_THREE_RECT": Rect(400, 400, 50, 50),
    "CHAR_FOUR_RECT": Rect(500, 400, 50, 50),
    "CONTINUE": Rect(600, 400, 75, 50)
}

# Mini-Tutorial Rectangles
TUTORIAL_RECT = {
    "W_KEY": Rect(150, 100, 50, 50),
    "S_KEY": Rect(160, 155, 50, 50),
    "A_KEY": Rect(105, 155, 50, 50),
    "D_KEY": Rect(215, 155, 50, 50),
    "Q_KEY": Rect(95, 100, 50, 50),
    "E_KEY": Rect(205, 100, 50, 50),
    "SPACE": Rect(145, 275, 250, 50)
}

# In-Game Rectangles
# UPDGRADE_RECTANGLES are the rectangles needed to upgrade abilities
# ABILITY RECTANGLES are the rectangles needed to place Ability Icons
UPGRADE_RECTANGLES = {
    "Health": Rect(20, 20, 160, 20),
    "Damage": Rect(20, 50, 160, 20),
    "Move Speed": Rect(20, 80, 160, 20),
    "Critical Chance": Rect(20, 110, 160, 20),
    "Mana": Rect(20, 140, 160, 20)
}
ABILITY_RECTANGLES = {
    "AB1": Rect(20, 525, 50, 50),
    "ab2": Rect(180, 525, 50, 50)
}

# == Colors, Fairly Self-Explanatory
# BACKGROUND_COLOR is used for the menu/character selection background
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "BULLET": (0, 255, 127)

}
BACKGROUND_COLOR = {
    "sky": (0, 47, 104),
    "black": (0, 0, 0),
    "light": (255, 255, 0),
    "green": (12, 122, 39),
    "cloud": (182, 188, 196),
    "brown": (15, 12, 3),
    "grass": (0, 79, 8),
    "grey": (94, 93, 83)
}


# == Fonts
FONTS = {
    # TITLE is used for the title
    # MENU is a smaller font used for menus and larger text
    # SMALL is another smaller text
    # TINY is the smallest text, used when SMALL is not small enough
    "TITLE": font.SysFont("courier", 40),
    "MENU": font.SysFont("courier", 30),
    "SMALL": font.SysFont("courier", 20),
    "TINY": font.SysFont("courier", 15)
}

# == Sounds
# Hit is the sound the bullet makes upon hitting an enemy
# crit is the sound that the strike makes if it crits
SOUNDS = {
    "Hit": mixer.Sound("res/hit.wav"),
    "Crit": mixer.Sound("res/crit.wav")
}
SOUNDS["Hit"].set_volume(0.25)
SOUNDS["Crit"].set_volume(0.25)


# Player Sprites to be loaded by the individual characters
PLAYER_SPRITES = {
    "Rogue": {
        "RIGHT": [image.load("res/rogue_sprites/right1.png").convert_alpha(),
                  image.load("res/rogue_sprites/right2.png").convert_alpha(),
                  image.load("res/rogue_sprites/right3.png").convert_alpha(),
                  image.load("res/rogue_sprites/right2.png").convert_alpha()],
        "LEFT": [image.load("res/rogue_sprites/left1.png").convert_alpha(),
                 image.load("res/rogue_sprites/left2.png").convert_alpha(),
                 image.load("res/rogue_sprites/left3.png").convert_alpha(),
                 image.load("res/rogue_sprites/left2.png").convert_alpha()]},
    "Archer": {
        "RIGHT": [image.load("res/archer_sprites/right1.png").convert_alpha(),
                  image.load("res/archer_sprites/right2.png").convert_alpha(),
                  image.load("res/archer_sprites/right3.png").convert_alpha(),
                  image.load("res/archer_sprites/right2.png").convert_alpha()],
        "LEFT": [image.load("res/archer_sprites/left1.png").convert_alpha(),
                 image.load("res/archer_sprites/left2.png").convert_alpha(),
                 image.load("res/archer_sprites/left3.png").convert_alpha(),
                 image.load("res/archer_sprites/left2.png").convert_alpha()]},
    "Tank": {
        "RIGHT": [image.load("res/tank_sprites/right1.png").convert_alpha(),
                  image.load("res/tank_sprites/right2.png").convert_alpha(),
                  image.load("res/tank_sprites/right3.png").convert_alpha(),
                  image.load("res/tank_sprites/right2.png").convert_alpha()],
        "LEFT": [image.load("res/tank_sprites/left1.png").convert_alpha(),
                 image.load("res/tank_sprites/left2.png").convert_alpha(),
                 image.load("res/tank_sprites/left3.png").convert_alpha(),
                 image.load("res/tank_sprites/left2.png").convert_alpha()]},
    "Cleric": {
        "RIGHT": [image.load("res/shaman_sprites/right1.png").convert_alpha(),
                  image.load("res/shaman_sprites/right2.png").convert_alpha(),
                  image.load("res/shaman_sprites/right3.png").convert_alpha(),
                  image.load("res/shaman_sprites/right2.png").convert_alpha()],
        "LEFT": [image.load( "res/shaman_sprites/left1.png").convert_alpha(),
                 image.load( "res/shaman_sprites/left2.png").convert_alpha(),
                 image.load( "res/shaman_sprites/left3.png").convert_alpha(),
                 image.load( "res/shaman_sprites/left2.png").convert_alpha()]}
}   

# Footsteps on the brick
FOOTSTEPS = [
    mixer.Sound("res/sounds/footsteps/concrete1.wav"),
    mixer.Sound("res/sounds/footsteps/concrete2.wav"),
    mixer.Sound("res/sounds/footsteps/concrete3.wav"),
    mixer.Sound("res/sounds/footsteps/concrete4.wav")
]

# Sounds for the Swords
SWORD_SOUNDS = {
    1: mixer.Sound("res/sounds/sword_sounds/1.wav"),
    2: mixer.Sound("res/sounds/sword_sounds/2.wav"),
    3: mixer.Sound("res/sounds/sword_sounds/3.wav"),
    4: mixer.Sound("res/sounds/sword_sounds/4.wav"),
    5: mixer.Sound("res/sounds/sword_sounds/5.wav"),
    6: mixer.Sound("res/sounds/sword_sounds/6.wav"),
    7: mixer.Sound("res/sounds/sword_sounds/7.wav"),
    8: mixer.Sound("res/sounds/sword_sounds/8.wav"),
}

# Background music that has to be imported
BACKGROUND_MUSIC = {
    1: mixer.Sound("res/bg_music/1.ogg"),
    2: mixer.Sound("res/bg_music/2.ogg"),
    3: mixer.Sound("res/bg_music/3.ogg"),
    4: mixer.Sound("res/bg_music/4.ogg"),
    5: mixer.Sound("res/bg_music/5.ogg"),
    6: mixer.Sound("res/bg_music/6.ogg"),
    7: mixer.Sound("res/bg_music/7.ogg"),
}
BACKGROUND_MUSIC[1].set_volume(0.25)
BACKGROUND_MUSIC[2].set_volume(0.25)
BACKGROUND_MUSIC[3].set_volume(0.25)

# This dictionary handles typing in the High-Scores class
keys_pressed = {
    "pressed_a": False,
    "pressed_b": False,
    "pressed_c": False,
    "pressed_d": False,
    "pressed_e": False,
    "pressed_f": False,
    "pressed_g": False,
    "pressed_h": False,
    "pressed_i": False,
    "pressed_j": False,
    "pressed_k": False,
    "pressed_l": False,
    "pressed_m": False,
    "pressed_n": False,
    "pressed_o": False,
    "pressed_p": False,
    "pressed_q": False,
    "pressed_r": False,
    "pressed_s": False,
    "pressed_t": False,
    "pressed_u": False,
    "pressed_v": False,
    "pressed_w": False,
    "pressed_x": False,
    "pressed_y": False,
    "pressed_z": False,
    "pressed_backspace": False,
    "pressed_space": False,
    "pressed_period": False
}


# Sprites for abilities
ABILITY_SPRITES = {
    "Rogue": [
        image.load("res/rogue_sprites/ability1.png"),
        image.load("res/rogue_sprites/ability3.png")
],
    "Archer": [
        image.load("res/archer_sprites/ability1.png"),
        image.load("res/archer_sprites/ability3.png")
    ],
    "Tank": [
        image.load("res/tank_sprites/ability1.png"),
        image.load("res/tank_sprites/ability3.png")
    ],
    "Shaman": [
        image.load("res/shaman_sprites/ability1.png"),
        image.load("res/shaman_sprites/ability3.png")
    ]
}

# Sprites for Elementalist
AA = [
    image.load("res/shaman_sprites/Attack0/sprite_00.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_01.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_02.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_03.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_04.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_05.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_06.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_07.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_08.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_09.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_10.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_11.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_12.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack0/sprite_13.png").convert_alpha()

]
THUNDER = [
    image.load("res/shaman_sprites/Attack1/sprite_0.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack1/sprite_1.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack1/sprite_2.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack1/sprite_3.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack1/sprite_4.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack1/sprite_5.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack1/sprite_6.png").convert_alpha()
]
FIRE = [
    image.load("res/shaman_sprites/Attack2/sprite_0.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack2/sprite_1.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack2/sprite_2.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack2/sprite_3.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack2/sprite_4.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack2/sprite_5.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack2/sprite_6.png").convert_alpha(),
    image.load("res/shaman_sprites/Attack2/sprite_7.png").convert_alpha()
]

# Sprites for Tank
TANK_AA = [
    image.load("res/tank_sprites/AA/sprite_0.png").convert_alpha(),
    image.load("res/tank_sprites/AA/sprite_1.png").convert_alpha(),
    image.load("res/tank_sprites/AA/sprite_2.png").convert_alpha(),
    image.load("res/tank_sprites/AA/sprite_3.png").convert_alpha()
]

# Full Body Sprites:
FULL_BODY = {
    1: image.load("res/face029.png").convert_alpha(),
    2: image.load("res/face022.png").convert_alpha(),
    3: image.load("res/face032.png").convert_alpha(),
    4: image.load("res/face038.png").convert_alpha()
}


# Level text files to be parsed
LEVELS = {
    1: "res/levels/2.txt",
    2: "res/levels/2.txt",
    3: "res/levels/3.txt",
    4: "res/levels/4.txt",
    5: "res/levels/5.txt"
}


# ============================ CLASSES
# This is the object for spawning enemies, Spawn points, denoted by the point on the .txt file at E
class SpawnPoint(object):
    # This function initializes the spawn point at x and y points
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This spawns enemies and appends them to the enemies list
    def spawn(self, entity):
        if entity == 1:
            enemies.append(Grunt(self.x, self.y))
        if entity == 2:
            enemies.append(Flier(self.x, self.y))


# This is the basic grunt enemy, quite dumb
class Grunt(sprite.Sprite):
    # Initialization of the Grunt
    def __init__(self, x, y):
        # self.yvel holds the y-velocity of the grunt
        # self.xvel holds the x-velicity of the grunt
        # self.x holds the x position of the grunt
        # self.y holds the y position of the grunt
        # self.dmg is the damage inflicted to the player if they collide with the grunt
        # self.hp is the health of the enemy, increases (scales) with time
        # self.vel is the movement speed of the grunt
        # self.grounded is a boolean that sees if the grunt is on the ground
        # self.jump is the boolean to see if the grunt should jump or not
        # self.image is the sprite used for the enemy
        # self.rect is the rectangle used for the enemy's hitbos
        # self.xp is the amount of xp to be given to the player for defeating the enemy
        sprite.Sprite.__init__(self)
        self.yvel = 0
        self.xvel = 0
        self.x = x
        self.y = y
        self.dmg = 5 + difficulty // 60
        self.hp = 100 + difficulty // 80
        self.vel = 8
        self.grounded = False
        self.jump = False
        self.image = image.load("res/poop.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.xp = 10
        self.lifetimer = 0

    # Called every frame, this updates the position of the enemy
    def update(self):
        self.lifetimer += 1
        if self.lifetimer > 1500:
            enemies.remove(self)
        # This checks the position of the enemy and checks it with the relative position to the center of the screen
        # If it is on either side, then move to either side
        if relative_view(self, camera)[0] > 400:
            self.xvel = -self.vel
        if relative_view(self, camera)[0] < 400:
            self.xvel = self.vel

        # If the enemy is under the enemy and at least half a screen away, they will jump up and try to reach the player
        if relative_view(self, camera)[1] > 300 and (relative_view(self, camera)[0] < 600 or relative_view(self, camera)[0] > 200):
            # Only allow the enemy to jump if it contacting the floor
            if self.grounded:
                self.jump = True
                self.yvel -= 20

        # Update positions and see if the enemy will fall through the ground
        self.rect.right += self.xvel
        self.collide(self.xvel, 0, world)

        # If the enemy does not touch the ground, then that means it is in freefall
        if not self.grounded:
            self.yvel += 2
            # Limit the velocity to avoid the enemy accelerating endlessly towards the center of the earth (o.O)
            if self.yvel > 10:
                self.yvel = 10
            self.rect.top += self.yvel

        # If the enemy is jumping, then allow it to jump
        if self.jump:
            self.yvel += 2
            self.rect.top += self.yvel
            if self.grounded:
                self.jump = False
        self.grounded = False
        self.collide(0, self.yvel, world)

    # Function checks if the enemy is touching anything in the world that is a "block"
    def collide(self, xvel, yvel, world):
        # Assume that it is not touching anything to begin with
        self.grounded = False

        # Check through every single element in the world (kinda inefficient)
        for ele in world:
            # If the enemy collides with the world, then...
            if self.rect.colliderect(ele):
                if xvel > 0:
                    self.rect.right = ele.rect.left
                if xvel < 0:
                    self.rect.left = ele.rect.right
                if yvel > 0:
                    self.rect.bottom = ele.rect.top
                    self.yvel = 0
                    self.grounded = True
                if yvel < 0:
                    self.rect.top = ele.rect.bottom
                    self.yvel = 0


# Other type of enemy, flies towards the player
class Flier(sprite.Sprite):
    def __init__(self, x, y):
        # x is the x-coordinate that it is initialized at
        # y is the y-coordinate that it is initialized at
        # xvel is the current xvelocity of the enemy
        # yvel is the current yvelocity of the enemy
        # dmg is the dmg that it will do once it comes into contact with the player, scales with time
        # hp is the hp of the enemy, scales with time
        # vel is the velocity in either areas of the enemy
        # image is the sprite of the flying enemy
        # rect is the hitbox of the flying enemy
        # xp is the amount of xp that the player will get from killing the enemy
        self.lifetimer = 0
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.dmg = 5 + difficulty // 80
        self.hp = 10 + difficulty // 60
        self.vel = 8
        self.image = image.load("res/fly.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.xp = 15

    def update(self):
        self.lifetimer += 1
        if self.lifetimer > 1500:
            enemies.remove(self)
        # If the flying enemy is on either side of the player, move the fly so that it isnt on that side of the player
        if relative_view(self, camera)[0] > 400:
            self.xvel = -self.vel
        if relative_view(self, camera)[0] < 400:
            self.xvel = self.vel
        if relative_view(self, camera)[1] > 300:
            self.yvel = -self.vel
        if relative_view(self, camera)[1] < 300:
            self.yvel = self.vel

        # Updates coordinates of the flying enemy
        self.rect.right += self.xvel
        self.rect.top += self.yvel


# Camera method
class Camera(object):
    def __init__(self, screen, player, level_width, level_height):
        # player is the player class
        # rect is the hitbox of the camera, size of the screen in a rectangle form
        # world_rect is the total size of the map
        self.player = player
        self.rect = screen.get_rect()
        self.rect.center = self.player.center
        self.world_rect = Rect(0, 0, level_width, level_height)

    # Updates the camera based on the coordinates of the player
    def update(self):
        if self.player.centerx > self.rect.centerx:
            self.rect.centerx = self.player.centerx
        if self.player.centerx < self.rect.centerx:
            self.rect.centerx = self.player.centerx
        if self.player.centery > self.rect.centery:
            self.rect.centery = self.player.centery
        if self.player.centery < self.rect.centery:
            self.rect.centery = self.player.centery

    # Draws all the sprites (player, enemies, block) onto the screen. This includes anything that needs to be relative
    # of another thing
    def draw_sprites(self, surf, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                surf.blit(s.image, relative_view(s, self))


# Bullets, this is the stuff that the Archer class shoots
class Bullet(object):
    def __init__(self, x, y, tox, toy, player):
        # x is the x position of the bullet
        # y is the y position of the bullet
        # originalx is the original x position of the bullet, used to calculate trajectory
        # originaly is the original y position of the bullet, used to calculate trajectory
        # tox is where the bullet is going to (x), used to calculate trajectory
        # toy is the where the bullet is going to (y), used to calculate trajectory
        # vel is the velocity that the bullet moves at
        # rnge is the range of the bullet, in frames
        # prog is the progress of the bullet, in frames
        # dmg is the damage that the bullet will do upon impact
        # color is the color of the bullet
        # rect is the rectangle (hitbox) of the bullet
        self.x = x
        self.y = y
        self.originalx = x
        self.originaly = y
        self.tox = tox
        self.toy = toy
        self.vel = 20
        self.rnge = 15
        self.prog = 0
        self.dmg = player.dmg
        self.color = COLORS["BULLET"]
        self.rect = Rect(self.x, self.y, 5, 5)

    def update(self):
        # not sure why I need to import math here, but the code will crash otherwise...
        import math

        # Increases Progress of the bullet
        self.prog += 1

        # Updates Coordinate values
        self.x += int(self.vel * (self.tox - self.originalx) /
                      (math.sqrt((self.tox - self.originalx) ** 2 +
                                 (self.toy - self.originaly) ** 2)))
        self.y += int(self.vel * (self.toy - self.originaly) /
                      (math.sqrt((self.tox - self.originalx) ** 2 +
                                 (self.toy - self.originaly) ** 2)))
        self.rect.center = [self.x, self.y]

        # Checks if the bullet is out of range, then deletes it, if it is
        if self.prog >= self.rnge:
            bullets.remove(self)


# This object handles the rogue's basic auto attacks
class SwordHit(object):
    def __init__(self, mx, my):
        # x is the position of the mouse (x)
        # y is the y-position of the mouse
        # time is the time that the sword animation is active for
        # passed is the time that has already passed since the played clicked the mouse
        # dmg is the damage of the sword (scales with player's damage)
        # left are all the images for swords on the left of the player
        # right are all the images for swords on the right of the player
        self.x = mx
        self.y = my
        self.time = 2
        self.passed = 0
        self.dmg = player.dmg * 2
        self.left = [
            image.load("res/rogue_sprites/sword/left1.png").convert_alpha(),
            image.load("res/rogue_sprites/sword/left2.png").convert_alpha(),
            image.load("res/rogue_sprites/sword/left3.png").convert_alpha()
        ]
        self.right = [
            image.load("res/rogue_sprites/sword/right1.png").convert_alpha(),
            image.load("res/rogue_sprites/sword/right2.png").convert_alpha(),
            image.load("res/rogue_sprites/sword/right3.png").convert_alpha()
        ]

        # This checks if the user wants to hit on their right side, or their left side
        if self.x > 400:
            self.image = self.right[random.randint(0, 2)]
            self.rect = self.image.get_rect()
            self.rect.left = 400
            self.rect.top = 280
        else:
            self.image = self.left[random.randint(0, 2)]
            self.rect = self.image.get_rect()
            self.rect.right = 390
            self.rect.top = 280

    def update(self):
        # Checks how long the sword swing has been active for
        self.passed += 1
        if self.passed > self.time:
            blades.remove(self)


# This handles the Cleric's Elemental Attacks (Auto Attack, Q Ability and E ability)
class ElementalHit(object):
    def __init__(self, mx, my, type):
        # x is the x position (initially center of the screen)
        # y is the y position (initially center of the screen)
        # originalx is the original x position (center of the screen), this is used to calculate the hit's trajectory
        # originaly is the original y positon
        # tox is the x position of the mouse, used to calculate the hit's trajectory
        # toy is the y position of the mouse, used to calculate the hit's trajectory
        # vel is the hit's velocity
        # prog is the progress of the hit, in frames. This is used to determine when the hit becomes out of range
        # dmg is the blasts' damage. It scales off of the player's damage
        # type is the type of bullet, normal, lightning, or fire
        # rect is the hitbox of the blast. Anything in the hitbox will be damaged
        # rnge is the range of the shot, in frames
        # icons is the number of frames to be rotated through in the animation
        self.x = 400
        self.y = 300
        self.originalx = 400
        self.originaly = 300
        self.tox = mx
        self.toy = my
        self.vel = 20
        self.prog = 0
        self.dmg = player.dmg // 2
        self.type = type
        if type == 1:
            self.icons = AA
            self.rect = AA[0].get_rect()
            self.rect.center = [self.x, self.y]
        if type == 2:
            self.icons = THUNDER
            self.rect = AA[0].get_rect()
            self.rect.center = [self.x, self.y]
            self.dmg = player.dmg
        if type == 3:
            self.icons = FIRE
            self.rect = AA[0].get_rect()
            self.rect.center = [self.x, self.y]
        self.rnge = len(self.icons) * 2

    def update(self):
        # Imports .. Still no idea why I have to do this
        import math

        # Increases progress and variables in the hit
        self.prog += 1
        self.x += int(self.vel * (self.tox - self.originalx) /
                      (math.sqrt((self.tox - self.originalx) ** 2 +
                                 (self.toy - self.originaly) ** 2)))
        self.y += int(self.vel * (self.toy - self.originaly) /
                      (math.sqrt((self.tox - self.originalx) ** 2 +
                                 (self.toy - self.originaly) ** 2)))
        self.rect.center = [self.x, self.y]

        # Checks if the element should be out of range or not
        if self.prog > self.rnge:
            elementalists.remove(self)


# This handles the "attack" of the Tank Class
class Bubble(object):
    def __init__(self):
        # Imports
        import math

        # x is the center of the screen, because that is where the player is
        # y is the center of the screen, because that is where the player is
        # prog is an index variable that cycles through the bubbles animations
        # dmg is the damage that the bubble will do to the players
        # rect is the hitbox of the bubble, damaging enemies that walk through it 
        self.x = 400
        self.y = 300
        self.prog = 0
        self.dmg = math.sqrt(player.dmg)
        self.icon = TANK_AA[self.prog]
        self.rect = self.icon.get_rect()
        self.rect.center = [self.x, self.y]

    def update(self):
        # This updates variables and also sets the current icon, following the rotation
        self.prog += 1
        if self.prog == 4:
            self.prog = 0
        self.icon = TANK_AA[self.prog]
        self.rect = self.icon.get_rect()
        self.rect.center = [self.x, self.y]


class Level(object):
    def __init__(self, open_level):
        # player is the player class of the level/game
        # level_lines is the number of lines in the open_level text document
        # world is the position of the items in the array
        # sprite refers to the sprite for the basic block
        # all_sprites is a Sprite Group that collects all the sprites in the game (objects, player, enemies)
        # level is the file for the text document, opens it in read mode
        # spawn is the array for all enemy spawn points that exist in the map
        self.player = None
        self.level_lines = []
        self.world = []
        self.sprite = image.load("res/block.png").convert_alpha()
        self.all_sprite = sprite.Group()
        self.level = open(open_level, "r")
        self.spawn = []

    # Creates the level
    def create_level(self, x, y):
        # Parses the file
        for l in self.level:
            self.level_lines.append(l)

        for row in self.level_lines:
            for col in row:
                # If the digit is an #, then it is a block object
                if col == "#":
                    obstacle = Obstacle(x, y)
                    self.world.append(obstacle)
                    self.all_sprite.add(self.world)
                # If the digit is a P, then that indicates player spawn
                if col == "P":
                    self.player = Player(x, y, character)
                    self.all_sprite.add(self.player)
                # If the digit is an E, then it indicates an enemy spawn point
                if col == "E":
                    self.spawn.append(SpawnPoint(x, y))
                x += block
            y += block
            x = 0

    # Gets the size of the world, this is used with character/camera movement
    def get_size(self):
        lines = self.level_lines
        line = max(lines, key=len)
        self.width = (len(line)) * block
        self.height = (len(lines)) * block
        return (self.width, self.height)


# Obstacle class, handles all obstacles
class Obstacle(sprite.Sprite):
    def __init__(self, x, y):
        # x is the x-coordinate of the block (top left)
        # y is the y-coordinate of the block (top right)
        # image is the image of the block
        # rect is the hitbox of the rectangle, checks to see if anything hits it
        self.x = x
        self.y = y
        sprite.Sprite.__init__(self)
        self.image = image.load("res/block.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]


# Player class, handles player movement, etc
class Player(sprite.Sprite):
    def __init__(self, x, y, type):
        # yvel is the current yvelocity of the player
        # xvel is the current xvelocity of the player
        # x is the x coordinate of the player (this is relative to the map, not to the camera)
        # y is the y coordinate of the player (this is relative to the map, not to the camera)
        # grounded is a variable that indicates if the character is grounded or not
        # Credits to Palmer Insull for the idea
        # jump is a variable that handles whether or not the character is going to jump
        # money is the amount of money the player gas
        # levels are the players' levels 
        # dmg is the players' damage
        # maxhp is the maximum hp that the player can have
        # hp is the current hp value that the player has
        # mana is the amount of mana that the player has
        # maxmana is the maximum mana that the player can have
        # move_speed determines the xvelocity when the respective buttons are pressed
        # crit_chance is the probability that a shot or point of damage will do double damage
        # temp is a temporary variable used for temporary assignment when a player has a buffing ability active 
        # image is the sprite that is currently displayed to the screen
        # cd1 is the timer for the first ability's cooldown
        # cd2 is the timer for the ultimate ability's cooldown
        # ab1timer is the duration of the first ability
        # ab2timer is the duration of the second ability 
        # fullab1cd is the total cooldown for the first ability's cooldown
        # fullcd2cd is the total cooldown for the ultimate ability's cooldown
        # ab1manacost is the mana cost of the first ability
        # ab2manacost is the mana cost of the second ability
        # rect is the rectangle of the player
        # run_left is the array that stores the animations for running left
        # run_right is the array that stores the animations for running right
        # frame is the progress in the running animation
        # direction handles the player's direction, 0 is left, 1 is center, 2 is right
        # regen_timer is the variable that holds how long it would take for the player to regenerate health
        # ab1 is a boolean variable that stores if the first ability is active or not
        # ab2 is a boolean variable that stores if the second ability is active or not 
        # idle is the idle icon, used for when the player is just stationary 
        sprite.Sprite.__init__(self)
        self.yvel = 0
        self.xvel = 0
        self.x = 0
        self.y = y
        self.grounded = False
        self.jump = False
        self.money = 0
        self.levels = {
            "Health": 0,
            "Dmg": 0,
            "Movement Speed": 0,
            "Crit": 0,
            "Regen": 0,
            "Mana": 0,
        }
        self.dmg = 0
        self.maxhp = 0
        self.hp = 0
        self.mana = 0
        self.maxmana = 0
        self.move_speed = 0
        self.crit_chance = 0
        self.temp = 0
        self.image = image.load("res/rogue_sprites/idle.png")
        self.cd1 = 0
        self.cd2 = 0
        self.ab1timer = 0
        self.ab2timer = 0
        self.fullab1cd = 0
        self.fullab2cd = 0
        self.ab1manacost = 0
        self.ab2manacost = 0
        self.rect = None
        self.run_left = None
        self.run_right = None
        self.frame = 0
        self.direction = 1
        self.regen_timer = 0
        self.ab1 = False
        self.ab2 = False
        self.idle = None
        
        # If the player wants to be the Rogue class
        if type == 1:
            self.move_speed = 10
            self.maxhp = 800
            self.hp = 800
            self.mana = 200
            self.maxmana = 200
            self.dmg = 10
            self.image = image.load("res/rogue_sprites/idle.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = [x, y]
            self.idle = image.load("res/rogue_sprites/idle.png")
            self.run_right = PLAYER_SPRITES["Rogue"]["RIGHT"]
            self.run_left = PLAYER_SPRITES["Rogue"]["LEFT"]
            self.icon = image.load("res/rogue_sprites/face.png").convert_alpha()
            self.fullab1cd = 150
            self.fullab2cd = 900
            self.ab1manacost = 40
            self.ab2manacost = 100
        
        # If the player wants to be the Archer class
        elif type == 2:
            self.move_speed = 15
            self.maxhp = 500
            self.hp = 500
            self.mana = 350
            self.maxmana = 350
            self.dmg = 20
            self.crit_chance = 15
            self.image = image.load("res/archer_sprites/idle.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = [x, y]
            self.idle = image.load("res/archer_sprites/idle.png")
            self.run_right = PLAYER_SPRITES["Archer"]["RIGHT"]
            self.run_left = PLAYER_SPRITES["Archer"]["LEFT"]
            self.icon = image.load("res/archer_sprites/face.png").convert_alpha()
            self.fullab1cd = 150
            self.fullab2cd = 700
            self.ab1manacost = 40
            self.ab2manacost = 70
        
        # If the player wants to be the Tank class
        elif type == 3:
            self.move_speed = 8
            self.maxhp = 1800
            self.hp = 1800
            self.mana = 100
            self.maxmana = 100
            self.dmg = 5
            self.image = image.load("res/tank_sprites/idle.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = [x, y]
            self.idle = image.load("res/tank_sprites/idle.png")
            self.run_right = PLAYER_SPRITES["Tank"]["RIGHT"]
            self.run_left = PLAYER_SPRITES["Tank"]["LEFT"]
            self.icon = image.load("res/tank_sprites/face.png").convert_alpha()
            self.fullab1cd = 120
            self.fullab2cd = 600
            self.ab1manacost = 40
            self.ab2manacost = 80

        # If the player wants to be the Cleric class
        elif type == 4:
            self.move_speed = 10
            self.maxhp = 600
            self.hp = 600
            self.mana = 250
            self.maxmana = 250
            self.dmg = 20
            self.rect = self.image.get_rect()
            self.rect.topleft = [x, y]
            self.idle = image.load("res/shaman_sprites/idle.png")
            self.run_right = PLAYER_SPRITES["Cleric"]["RIGHT"]
            self.run_left = PLAYER_SPRITES["Cleric"]["LEFT"]
            self.icon = image.load("res/shaman_sprites/face.png").convert_alpha()
            self.fullab1cd = 120
            self.fullab2cd = 150
            self.ab1manacost = 40
            self.ab2manacost = 50

    # Updates the player's positions, called every frame
    def update(self, jump, left, right):
        # If the player wants to jump
        if jump:
            if self.grounded:
                self.jump = True
                self.yvel -= 25
        # If the player wants to move left
        if left:
            self.xvel = -self.move_speed
            self.direction = 0
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.run_left[self.frame]
            if self.grounded:
                run.play(FOOTSTEPS[random.randint(0, 3)])
        # If the player wants to move right
        if right:
            self.xvel = self.move_speed
            self.direction = 0
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.run_right[self.frame]
            if self.grounded:
                run.play(FOOTSTEPS[random.randint(0, 3)])

        # If the player is stationary, not moving at all
        if not (left or right):
            self.xvel = 0
            self.direction = 1
            self.image = self.idle

        # Update horizontal coordinates then see if the thing player hits with objects or not
        self.rect.right += self.xvel
        self.collide(self.xvel, 0, world)

        # If the player is not on the ground, then it must be in freefall,
        if not self.grounded:
            self.yvel += 2
            if self.yvel > 10:
                self.yvel = 10
        # If the player wants to jump, then allow them to jump
        if self.jump:
            self.yvel += 2
            if self.grounded:
                self.jump = False

        # Updates y-values
        self.rect.top += self.yvel
        self.grounded = False
        self.collide(0, self.yvel, world)

    # Checks if the player collides with any elements in the world
    def collide(self, xvel, yvel, world):
        # In each element in the world array, check if the player collides with it, relative to the entire scene
        for ele in world:
            if self.rect.colliderect(ele):
                if xvel > 0:
                    self.rect.right = ele.rect.left
                if xvel < 0:
                    self.rect.left = ele.rect.right
                if yvel > 0:
                    self.rect.bottom = ele.rect.top
                    self.yvel = 0
                    self.grounded = True
                if yvel < 0:
                    self.rect.top = ele.rect.bottom
                    self.yvel = 0


# Used for drawing in the main screen
class Cloud(object):
    def __init__(self, x, y, size):
        # circles is an array that holds the grey circles as part of a cloud
        # x is the x-coordinate. This is increased every time to give the effect that the cloud is moving
        # y is the y-coordinate. This is remained constant for each cloud particle
        self.circles = []
        self.x = x - 120
        self.y = y
        for i in range(size):
            self.circles.append([screen, BACKGROUND_COLOR["cloud"], (self.x, self.y), random.randint(10, 25)])
            self.x += 10
            self.y += random.randint(-10, 10)

    # Updates all circles in the array
    def update(self):
        # If the circle is out of bounds, then remove it from the array
        for circle in self.circles:
            if circle[2][0] > 825:
                self.circles.remove(circle)
            else:
                self.circles[self.circles.index(circle)] = ((screen, BACKGROUND_COLOR["cloud"],
                                                             (circle[2][0] + 1, circle[2][1]), circle[3]))


# ------------------- DEFINITIONS
# Gets mouse and returns, mouse x position, mouse y position, and whether or not the button has been clicked
def get_mouse():
    mx, my = mouse.get_pos()
    mb, mr = mouse.get_pressed()[0], mouse.get_pressed()[1]
    return mx, my, mb


# Draws the Heads up Display
def heads_up_display():
    # UPGRADE_TEXTS show the levels and stats of the player
    UPGRADE_TEXTS = {
        "Health": FONTS["TINY"].render("HP: %i" % player.maxhp, 1, COLORS["BLACK"]),
        "Damage": FONTS["TINY"].render("Damage: %i" % player.dmg, 1, COLORS["BLACK"]),
        "Move Speed": FONTS["TINY"].render("Move Speed: %i" % player.move_speed, 1, COLORS["BLACK"]),
        "Critical Chance": FONTS["TINY"].render("Luck: %i%%" % player.crit_chance, 1, COLORS["BLACK"]),
        "Mana": FONTS["TINY"].render("Mana: %i" % player.maxmana, 1, COLORS["BLACK"])}

    # Health Bar
    draw.rect(screen, (140, 0, 0), Rect(500, 500, 250, 25))
    draw.rect(screen, (0, 200, 0), Rect(500, 500, (250 * player.hp / player.maxhp), 25))

    # Mana Bar
    draw.rect(screen, (0, 0, 0), Rect(500, 550, 250, 25))
    draw.rect(screen, (0, 0, 150), Rect(500, 550, (250 * player.mana / player.maxmana), 25))

    # Indiators on the health bar
    health = FONTS["TINY"].render("%i / %i" % (player.hp, player.maxhp), 1, COLORS["WHITE"])
    mana = FONTS["TINY"].render("%i / %i" % (player.mana, player.maxmana), 1, COLORS["WHITE"])
    screen.blit(health, Rect(600, 505, 100, 100))
    screen.blit(mana, Rect(600, 555, 100, 100))

    # Character Icon
    screen.blit(player.icon, (390, 490))

    # Draws Buttons to Upgrade
    for rect in UPGRADE_RECTANGLES:
        draw.rect(screen, COLORS["WHITE"], UPGRADE_RECTANGLES[rect])

    # Draws ability icons for each player
    if character == 1:
        screen.blit(ABILITY_SPRITES["Rogue"][0], ABILITY_RECTANGLES["AB1"])
        screen.blit(ABILITY_SPRITES["Rogue"][1], ABILITY_RECTANGLES["ab2"])
    elif character == 2:
            screen.blit(ABILITY_SPRITES["Archer"][0], ABILITY_RECTANGLES["AB1"])
            screen.blit(ABILITY_SPRITES["Archer"][1], ABILITY_RECTANGLES["ab2"])
    elif character == 3:
        screen.blit(ABILITY_SPRITES["Tank"][0], ABILITY_RECTANGLES["AB1"])
        screen.blit(ABILITY_SPRITES["Tank"][1], ABILITY_RECTANGLES["ab2"])
    elif character == 4:
        screen.blit(ABILITY_SPRITES["Shaman"][0], ABILITY_RECTANGLES["AB1"])
        screen.blit(ABILITY_SPRITES["Shaman"][1], ABILITY_RECTANGLES["ab2"])

    # Draws black/green boxes to show if abilities are active or on cooldown
    if player.ab1timer > 0:
        draw.rect(screen, COLORS["BLACK"], ABILITY_RECTANGLES["AB1"])
    elif player.cd1 > 0:
        draw.rect(screen, COLORS["GREEN"], Rect(20, 525, 50 * (player.cd1 / player.fullab1cd), 50))
    if player.ab2timer > 0:
        draw.rect(screen, COLORS["BLACK"], ABILITY_RECTANGLES["ab2"])
    elif player.cd2 > 0:
        draw.rect(screen, COLORS["GREEN"], Rect(180, 525, 50 * (player.cd2 / player.fullab2cd), 50))

    # Draws Text inside the Ability Boxes
    for text in UPGRADE_TEXTS:
        screen.blit(UPGRADE_TEXTS[text], UPGRADE_RECTANGLES[text])

    # Handles the money output on the corner of the screen (other side)
    draw.rect(screen, COLORS["WHITE"], Rect(620, 20, 200, 40))
    money_text = FONTS["SMALL"].render("Money: %i" % player.money, 1, COLORS["BLACK"])
    screen.blit(money_text, Rect(640, 30, 50, 25))


# Method for relative rectangles
def relative_view(actor, camera):
    return Rect(actor.rect.x - camera.rect.x, actor.rect.y - camera.rect.y, actor.rect.w, actor.rect.h)


# Handles the menu
def menu():
    # Variable Declaration and Initialization
    # run_menu states whether or not the menu should be run
    # scene is to handle which scene within the menu to display
    # myClock is the clock variable
    # Time is the variable to keep track of the frames passed for the background animations
    run_menu = True
    scene = 0
    selected = 0
    myClock = time.Clock()
    Time = 0

    while run_menu:
        # Handles Back ground music
        if not bgm.get_busy():
            bgm.play(BACKGROUND_MUSIC[random.randint(1, 7)], 0)

        # Getting User Input
        mx, my, mb = get_mouse()

        # Sees if the player wants to quit
        for evnt in pygame.event.get():
            if evnt.type == QUIT:
                run_menu = False
                pygame.quit()
                break

        # If the scene is set to 0, then the player is at the main menu
        # If the scene is set to 1, then the player is at the character selection screen
        # If the scene is set to 3, then the player has chosen a character and is wanting to start the game
        if scene == 0:
            scene = draw_menu(mx, my, mb, Time)
        elif scene == 1:
            scene, selected = char_select(selected, mx, my, mb, Time)
        elif scene == 3:
            return selected

        display.flip()
        myClock.tick(30)


# This draws the character selection screen
def char_select(selected, mx, my, mb, time):

        # draws and updates the background
        menu_background(time)
        for cloud in clouds:
            for c in cloud.circles:
                pygame.draw.circle(c[0], c[1], c[2], c[3])
            cloud.update()

        #  Draws the four classes in the character selection screen
        draw.rect(screen, COLORS["WHITE"], CHAR_RECTS["CHAR_ONE_RECT"], 1)
        draw.rect(screen, COLORS["RED"], CHAR_RECTS["CHAR_TWO_RECT"], 1)
        draw.rect(screen, COLORS["GREEN"], CHAR_RECTS["CHAR_THREE_RECT"], 1)
        draw.rect(screen, COLORS["BLUE"], CHAR_RECTS["CHAR_FOUR_RECT"], 1)
        draw.rect(screen, COLORS["WHITE"], CHAR_RECTS["CONTINUE"], 1)
        screen.blit(FONTS["SMALL"].render("START!", 1, COLORS["RED"]), Rect(602, 415, 75, 50))

        # Checks for mouse collision/character selection (highlighted or clicked)
        if mb == 0:
            if CHAR_RECTS["CHAR_ONE_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["WHITE"], CHAR_RECTS["CHAR_ONE_RECT"])
            elif CHAR_RECTS["CHAR_TWO_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["RED"], CHAR_RECTS["CHAR_TWO_RECT"])
            elif CHAR_RECTS["CHAR_THREE_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["GREEN"], CHAR_RECTS["CHAR_THREE_RECT"])
            elif CHAR_RECTS["CHAR_FOUR_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["BLUE"], CHAR_RECTS["CHAR_FOUR_RECT"])
        elif mb == 1:
            if CHAR_RECTS["CHAR_ONE_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["WHITE"], CHAR_RECTS["CHAR_ONE_RECT"])
                selected = 1
            elif CHAR_RECTS["CHAR_TWO_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["RED"], CHAR_RECTS["CHAR_TWO_RECT"])
                selected = 2
            elif CHAR_RECTS["CHAR_THREE_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["GREEN"], CHAR_RECTS["CHAR_THREE_RECT"])
                selected = 3
            elif CHAR_RECTS["CHAR_FOUR_RECT"].collidepoint(mx, my):
                draw.rect(screen, COLORS["BLUE"], CHAR_RECTS["CHAR_FOUR_RECT"])
                selected = 4
            elif CHAR_RECTS["CONTINUE"].collidepoint(mx, my):
                if selected != 0:
                    return 3, selected

        # If the player has not selected a class yet, then display the mini-tutorial
        # if the player has chosen the first class, then display information about that class
        # Same goes for the other classes
        if selected == 0:
            # SHOW THE CONTROLS
            Q = FONTS["SMALL"].render("Q", 1, COLORS["WHITE"])
            R = FONTS["SMALL"].render("R", 1, COLORS["WHITE"])
            A = FONTS["SMALL"].render("A", 1, COLORS["WHITE"])
            D = FONTS["SMALL"].render("D", 1, COLORS["WHITE"])
            SPACE = FONTS["SMALL"].render("SPACE", 1, COLORS["WHITE"])
            MB = FONTS["SMALL"].render("MB", 1, COLORS["WHITE"])

            draw.rect(screen, COLORS["WHITE"], TUTORIAL_RECT["A_KEY"], 2)
            draw.rect(screen, COLORS["WHITE"], TUTORIAL_RECT["S_KEY"], 2)
            draw.rect(screen, COLORS["WHITE"], TUTORIAL_RECT["D_KEY"], 2)
            draw.rect(screen, COLORS["WHITE"], TUTORIAL_RECT["Q_KEY"], 2)
            draw.rect(screen, COLORS["WHITE"], TUTORIAL_RECT["W_KEY"], 2)
            draw.rect(screen, COLORS["WHITE"], TUTORIAL_RECT["E_KEY"], 2)
            draw.rect(screen, COLORS["WHITE"], TUTORIAL_RECT["SPACE"], 2)

            SUBTITLE = FONTS["SMALL"].render("Instructions: Please pick a class by picking a square below!", 1, COLORS["RED"])
            Q = FONTS["SMALL"].render("Q ------> ABILITY 1", 1, COLORS["WHITE"])
            R = FONTS["SMALL"].render("R ------> ABILITY 2", 1, COLORS["WHITE"])
            A = FONTS["SMALL"].render("A ------> LEFT", 1, COLORS["WHITE"])
            D = FONTS["SMALL"].render("D ------> RIGHT", 1, COLORS["WHITE"])
            SPACE = FONTS["SMALL"].render("SPACE --> JUMP", 1, COLORS["WHITE"])
            UPGRADES = FONTS["SMALL"].render("Click the Stats in the Top Left to Upgrade!", 1, COLORS["WHITE"])
            PAUSE = FONTS["SMALL"].render("Press ESC to Pause", 1, COLORS["WHITE"])

            screen.blit(SUBTITLE, Rect(50, 50, 600, 50))
            screen.blit(Q, Rect(400, 100, 50, 50))
            screen.blit(R, Rect(400, 130, 50, 50))
            screen.blit(A, Rect(400, 160, 50, 50))
            screen.blit(D, Rect(400, 190, 50, 50))
            screen.blit(SPACE, Rect(400, 210, 50, 50))
            screen.blit(UPGRADES, Rect(250, 240, 50, 50))
            screen.blit(PAUSE, Rect(400, 270, 50, 50))
        elif selected == 1:
            title = FONTS["MENU"].render("ROGUE", 1, COLORS["WHITE"])
            screen.blit(title, Rect(100, 100, 100, 100))
            screen.blit(FONTS["SMALL"].render("CLICK --> Short Range Melee Attack", 1, COLORS["WHITE"]),
                        Rect(100, 150, 100, 100))
            screen.blit(FONTS["SMALL"].render("Q --> Increases Luck to 80%", 1, COLORS["WHITE"]),
                        Rect(100, 200, 100, 100))
            screen.blit(FONTS["SMALL"].render("E --> Instantly kills all enemies", 1, COLORS["WHITE"]),
                        Rect(100, 250, 100, 100))
            screen.blit(FULL_BODY[1], Rect(-50, 310, 100, 100))
        elif selected == 2:
            title = FONTS["MENU"].render("ARCHER", 1, COLORS["WHITE"])
            screen.blit(title, Rect(100, 100, 100, 100))
            screen.blit(FONTS["SMALL"].render("CLICK --> Shoots a Medium Range Bullet", 1, COLORS["WHITE"]),
                        Rect(100, 150, 100, 100))
            screen.blit(FONTS["SMALL"].render("W --> Temporarily Increases Damages", 1, COLORS["WHITE"]),
                        Rect(100, 200, 100, 100))
            screen.blit(FONTS["SMALL"].render("E --> Creates a Triple-Shot Barrage", 1, COLORS["WHITE"]),
                        Rect(100, 250, 100, 100))
            screen.blit(FULL_BODY[2], Rect(-50, 310, 100, 100))
        elif selected == 3:
            title = FONTS["MENU"].render("TANK", 1, COLORS["WHITE"])
            screen.blit(title, Rect(100, 100, 100, 100))
            screen.blit(FONTS["SMALL"].render("CLICK --> No Effect, Permanent Bubble Around Character", 1, COLORS["WHITE"]),
                        Rect(100, 150, 100, 100))
            screen.blit(FONTS["SMALL"].render("Q --> Increases Movement Speed", 1, COLORS["WHITE"]),
                        Rect(100, 200, 100, 100))
            screen.blit(FONTS["SMALL"].render("R --> Grants Temporary Invincibility", 1, COLORS["WHITE"]),
                        Rect(100, 250, 100, 100))
            screen.blit(FULL_BODY[3], Rect(-50, 310, 100, 100))
        elif selected == 4:
            title = FONTS["MENU"].render("CLERIC", 1, COLORS["WHITE"])
            screen.blit(title, Rect(100, 100, 100, 100))
            screen.blit(FONTS["SMALL"].render("CLICK --> Long Range Spell That Deals Damage", 1, COLORS["WHITE"]),
                        Rect(100, 150, 100, 100))
            screen.blit(
                FONTS["SMALL"].render("Q --> Next Spell is Shorter Range but deals Double Damage", 1,
                                      COLORS["WHITE"]), Rect(100, 200, 100, 100))
            screen.blit(FONTS["SMALL"].render("R --> Next Spell Grants Lifesteal and Manasteal", 1, COLORS["WHITE"]),
                        Rect(100, 250, 100, 100))
            screen.blit(FULL_BODY[4], Rect(-50, 310, 100, 100))
        return 1, selected


# Draws the main menu
def draw_menu(mx, my, mb, time):
    # Draws and updates background every frame
    menu_background(time)
    for cloud in clouds:
        for c in cloud.circles:
            pygame.draw.circle(c[0], c[1], c[2], c[3])
        cloud.update()

    # ------------------- Local Variables for the drawing of the menu
    # title is the title
    # play is the text of the play button
    # play_highlighted is the highlighted version of the play button
    # highscore draws a menu of the highscores
    # highscores_highlighted shows the highscores menu whilst highlighted
    title = FONTS["TITLE"].render("TRASH-GUARD", 1, COLORS["RED"])
    play = FONTS["MENU"].render("PLAY", 1, COLORS["RED"])
    play_highlighted = FONTS["MENU"].render("PLAY", 1, COLORS["WHITE"])
    highscore = FONTS["MENU"].render("HIGHSCORES", 1, COLORS["RED"])
    highscores_highlighted = FONTS["MENU"].render("HIGHSCORES", 1, COLORS["WHITE"])

    # Displays the above texts and rectangles for hitboxes
    screen.blit(title, MAIN_RECTS["TITLE"])
    screen.blit(play, MAIN_RECTS["TEXT ONE"])
    screen.blit(highscore, MAIN_RECTS["TEXT TWO"])
    draw.rect(screen, COLORS["RED"], MAIN_RECTS["UPPER_RECT"], 1)
    draw.rect(screen, COLORS["RED"], MAIN_RECTS["LOWER_RECT"], 1)

    # Check if anything is highlighted
    if mb == 0:
        if MAIN_RECTS["UPPER_RECT"].collidepoint(mx, my):
            draw.rect(screen, COLORS["RED"], MAIN_RECTS["UPPER_RECT"], 0)
            screen.blit(play_highlighted, MAIN_RECTS["TEXT ONE"])
        if MAIN_RECTS["LOWER_RECT"].collidepoint(mx, my):
            draw.rect(screen, COLORS["RED"], MAIN_RECTS["LOWER_RECT"], 0)
            screen.blit(highscores_highlighted, MAIN_RECTS["TEXT TWO"])
    elif mb == 1:
        if MAIN_RECTS["UPPER_RECT"].collidepoint(mx, my):
            return 1
        elif MAIN_RECTS["LOWER_RECT"].collidepoint(mx, my):
            highscores()
    return 0


# Draws the menu's background
def menu_background(time):
    Time = int(time)
    screen.fill(BACKGROUND_COLOR["sky"])
    draw.rect(screen, BACKGROUND_COLOR["grass"], Rect(0, 600, 350, -200))
    draw.rect(screen, BACKGROUND_COLOR["grass"], Rect(350, 600, 175, -130))
    draw.rect(screen, BACKGROUND_COLOR["grass"], Rect(525, 600, 275, -160))
    draw.rect(screen, BACKGROUND_COLOR["brown"], Rect(0, 600, 330, -180))
    draw.rect(screen, BACKGROUND_COLOR["brown"], Rect(300, 600, 300, -110))
    draw.rect(screen, BACKGROUND_COLOR["brown"], Rect(545, 600, 275, -140))
    if Time % 100 == 0:
        clouds.append(Cloud(0, random.randint(0, 300), random.randint(5, 10)))


# Draws the death screen
def you_died(time, character):
    # myClock is the clock variable
    # highscores is the text file for the highscores
    # died is running while you are dead
    # curr_word is the current word they are entering to be placed into the highscores sheet
    # ENTER_RECT is the rectangle that sees if the player wants to submit and go back to the main meny
    myClock = pygame.time.Clock()
    highscores = open("highscores.txt", "a")
    died = True
    curr_word = ""
    ENTER_RECT = Rect(100, 400, 600, 75)

    # While the player is dead and on the "you died" menu
    while died:

        # Draws the death background
        dead_background()

        # Gets user input
        for evnt in pygame.event.get():
            if evnt.type == QUIT:
                pygame.quit()

        mx, my, mb = get_mouse()
        keys = pygame.key.get_pressed()

        # Displays information onto the screen, entering name, and score
        font_out = FONTS["MENU"].render("Please Enter Your Name for High-scores: ", 1, COLORS["WHITE"])
        current = FONTS["MENU"].render("%s" % curr_word, 1, COLORS["WHITE"])
        your_score = FONTS["MENU"].render("Your Score is %i " % time, 1, COLORS["WHITE"])

        # Cycles through all the keys and sees if the user wants to press them
        if keys[pygame.K_q]:
            keys_pressed["pressed_q"] = True
        elif keys[pygame.K_w]:
            keys_pressed["pressed_w"] = True
        elif keys[pygame.K_e]:
            keys_pressed["pressed_e"] = True
        elif keys[pygame.K_r]:
            keys_pressed["pressed_r"] = True
        elif keys[pygame.K_t]:
            keys_pressed["pressed_t"] = True
        elif keys[pygame.K_y]:
            keys_pressed["pressed_y"] = True
        elif keys[pygame.K_u]:
            keys_pressed["pressed_u"] = True
        elif keys[pygame.K_i]:
            keys_pressed["pressed_i"] = True
        elif keys[pygame.K_o]:
            keys_pressed["pressed_o"] = True
        elif keys[pygame.K_p]:
            keys_pressed["pressed_p"] = True
        elif keys[pygame.K_a]:
           keys_pressed["pressed_a"] = True
        elif keys[pygame.K_s]:
            keys_pressed["pressed_s"] = True
        elif keys[pygame.K_d]:
            keys_pressed["pressed_d"] = True
        elif keys[pygame.K_f]:
            keys_pressed["pressed_f"] = True
        elif keys[pygame.K_g]:
            keys_pressed["pressed_g"] = True
        elif keys[pygame.K_h]:
            keys_pressed["pressed_h"] = True
        elif keys[pygame.K_j]:
            keys_pressed["pressed_j"] = True
        elif keys[pygame.K_k]:
            keys_pressed["pressed_k"] = True
        elif keys[pygame.K_l]:
            keys_pressed["pressed_l"] = True
        elif keys[pygame.K_z]:
            keys_pressed["pressed_z"] = True
        elif keys[pygame.K_x]:
            keys_pressed["pressed_x"] = True
        elif keys[pygame.K_c]:
            keys_pressed["pressed_c"] = True
        elif keys[pygame.K_v]:
            keys_pressed["pressed_v"] = True
        elif keys[pygame.K_b]:
            keys_pressed["pressed_b"] = True
        elif keys[pygame.K_n]:
            keys_pressed["pressed_n"] = True
        elif keys[pygame.K_m]:
            keys_pressed["pressed_m"] = True
        elif keys[pygame.K_PERIOD]:
            keys_pressed["pressed_period"] = True
        elif keys[pygame.K_BACKSPACE]:
            keys_pressed["pressed_backspace"] = True
        elif keys[pygame.K_SPACE]:
            keys_pressed["pressed_space"] = True

        # If the length of the word is less than 16 (maximum length) and the player has let go of the key, then add it
        # to their current name
        if len(curr_word) < 16:
            if keys_pressed["pressed_q"] and not keys[pygame.K_q]:
                curr_word += "q"
                keys_pressed["pressed_q"] = False
            elif keys_pressed["pressed_w"] and not keys[pygame.K_w]:
                curr_word += "w"
                keys_pressed["pressed_w"] = False
            elif keys_pressed["pressed_e"] and not keys[pygame.K_e]:
                curr_word += "e"
                keys_pressed["pressed_e"] = False
            elif keys_pressed["pressed_r"] and not keys[pygame.K_r]:
                curr_word += "r"
                keys_pressed["pressed_r"] = False
            elif keys_pressed["pressed_t"] and not keys[pygame.K_t]:
                curr_word += "t"
                keys_pressed["pressed_t"] = False
            elif keys_pressed["pressed_y"] and not keys[pygame.K_y]:
                curr_word += "y"
                keys_pressed["pressed_y"] = False
            elif keys_pressed["pressed_u"] and not keys[pygame.K_u]:
                curr_word += "jump"
                keys_pressed["pressed_u"] = False
            elif keys_pressed["pressed_i"] and not keys[pygame.K_i]:
                curr_word += "i"
                keys_pressed["pressed_i"] = False
            elif keys_pressed["pressed_o"] and not keys[pygame.K_o]:
                curr_word += "o"
                keys_pressed["pressed_o"] = False
            elif keys_pressed["pressed_p"] and not keys[pygame.K_p]:
                curr_word += "p"
                keys_pressed["pressed_p"] = False
            elif keys_pressed["pressed_a"] and not keys[pygame.K_a]:
                curr_word += "a"
                keys_pressed["pressed_a"] = False
            elif keys_pressed["pressed_s"] and not keys[pygame.K_s]:
                curr_word += "s"
                keys_pressed["pressed_s"] = False
            elif keys_pressed["pressed_d"] and not keys[pygame.K_d]:
                curr_word += "d"
                keys_pressed["pressed_d"] = False
            elif keys_pressed["pressed_f"] and not keys[pygame.K_f]:
                curr_word += "f"
                keys_pressed["pressed_f"] = False
            elif keys_pressed["pressed_g"] and not keys[pygame.K_g]:
                curr_word += "g"
                keys_pressed["pressed_g"] = False
            elif keys_pressed["pressed_h"] and not keys[pygame.K_h]:
                curr_word += "h"
                keys_pressed["pressed_h"] = False
            elif keys_pressed["pressed_j"] and not keys[pygame.K_j]:
                curr_word += "j"
                keys_pressed["pressed_j"] = False
            elif keys_pressed["pressed_k"] and not keys[pygame.K_k]:
                curr_word += "k"
                keys_pressed["pressed_k"] = False
            elif keys_pressed["pressed_l"] and not keys[pygame.K_l]:
                curr_word += "l"
                keys_pressed["pressed_l"] = False
            elif keys_pressed["pressed_z"] and not keys[pygame.K_z]:
                curr_word += "z"
                keys_pressed["pressed_z"] = False
            elif keys_pressed["pressed_x"] and not keys[pygame.K_x]:
                curr_word += "x"
                keys_pressed["pressed_x"] = False
            elif keys_pressed["pressed_c"] and not keys[pygame.K_c]:
                curr_word += "c"
                keys_pressed["pressed_c"] = False
            elif keys_pressed["pressed_v"] and not keys[pygame.K_v]:
                curr_word += "v"
                keys_pressed["pressed_v"] = False
            elif keys_pressed["pressed_b"] and not keys[pygame.K_b]:
                curr_word += "b"
                keys_pressed["pressed_b"] = False
            elif keys_pressed["pressed_n"] and not keys[pygame.K_n]:
                curr_word += "n"
                keys_pressed["pressed_n"] = False
            elif keys_pressed["pressed_m"] and not keys[pygame.K_m]:
                curr_word += "m"
                keys_pressed["pressed_m"] = False
            elif keys_pressed["pressed_backspace"] and not keys[pygame.K_BACKSPACE]:
                if curr_word != "":
                    curr_word = curr_word[0:len(curr_word) - 1]
                else:
                    curr_word = ""
                keys_pressed["pressed_backspace"] = False
            elif keys_pressed["pressed_space"] and not keys[pygame.K_SPACE]:
                curr_word += " "
                keys_pressed["pressed_space"] = False
            elif keys_pressed["pressed_period"] and not keys[pygame.K_PERIOD]:
                curr_word += "."
                keys_pressed["pressed_period"] = False
        else:
            if keys_pressed["pressed_backspace"] and not keys[pygame.K_BACKSPACE]:
                if curr_word != "":
                    curr_word = curr_word[0:len(curr_word) - 1]
                else:
                    curr_word = ""
                keys_pressed["pressed_backspace"] = False

        # Displays the relevant information
        screen.blit(font_out, Rect(50, 100, 500, 50))
        screen.blit(current, Rect(100, 150, 500, 50))
        screen.blit(your_score, Rect(100, 250, 500, 50))

        # Draws the rectangle to quit
        draw.rect(screen, COLORS["BULLET"], ENTER_RECT, 2)
        screen.blit(FONTS["MENU"].render("BACK TO MAIN MENU", 1, COLORS["WHITE"]), Rect(175, 410, 150, 150))

        # If the player has quit the death screen, then add their data to the highscores text file
        if ENTER_RECT.collidepoint(mx, my):
            if mb == 1:
                if curr_word == "":
                    curr_word = "Anonymous Sensei"
                if character == 1:
                    highscores.write("%s#%s!%i\n" % (curr_word, "Rogue", time))
                elif character == 2:
                    highscores.write("%s#%s!%i\n" % (curr_word, "Archer", time))
                elif character == 3:
                    highscores.write("%s#%s!%i\n" % (curr_word, "Tank", time))
                elif character == 4:
                    highscores.write("%s#%s!%i\n" % (curr_word, "Cleric", time))
                highscores.close()
                break
            if mb == 0:
                draw.rect(screen, COLORS["BULLET"], ENTER_RECT)
                screen.blit(FONTS["MENU"].render("BACK TO MAIN MENU", 1, COLORS["WHITE"]), Rect(175, 410, 150, 150))

        display.flip()
        myClock.tick(30)


# Draws the background for the death screen
def dead_background():
    screen.fill(COLORS["BLACK"])


# Draws the highscores page
def highscores():
    # file is the highscores text document that is opened
    # data is all the lines, unparsed
    # names are the names that are to be entered
    # classes are the classes of people that are entered
    # scores are all the scores of people that are entered
    # highscores is whether or not the player still wants to be on the highscores page
    # highscore is a list of the top ten scores
    # myClock is the clock variable
    file = open("highscores.txt", "r")
    data = []
    names = ["NO ENTRIES"] * 10
    classes = ["NO ENTRIES"] * 10
    scores = [-1] * 10
    highscores = True
    highscore = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None
    }
    myClock = time.Clock()
    # Getting input from text file
    while True:
        line = file.readline()
        if line != "":
            data.append(line)
        else:
            break

    # Parsing the data
    for line in data:
        names.append(line[0:line.index("#")])
        classes.append(line[line.index("#") + 1: line.index("!")])
        scores.append(int(line[line.index("!") + 1:len(line) - 1]))
    # Sorting the arrays
    for num in range(len(scores) - 1, 0, -1):
        for i in range(num):
            if scores[i] < scores[i + 1]:
                temp1 = scores[i]
                temp2 = names[i]
                temp3 = classes[i]

                scores[i] = scores[i + 1]
                names[i] = names[i + 1]
                classes[i] = classes[i + 1]

                scores[i + 1] = temp1
                names[i + 1] = temp2
                classes[i + 1] = temp3

    # Sets highscores into the highscores dictionary
    for i in range(1, 11):
        highscore[i] = FONTS["SMALL"].render("%i. %s --- %s --- %i" % (int(i), names[i - 1], classes[i - 1], int(scores[i - 1])),
                                             1, COLORS["WHITE"])

    while highscores:

        # Draw the background
        dead_background()

        # Getting user input
        for evnt in pygame.event.get():
            if evnt.type == QUIT:
                highscores = False
                break
        mx, my, mb = get_mouse()

        # Display the highscores
        for i in range(1, 11):
            screen.blit(highscore[i], Rect(100, 125 + (35 * i), 450, 35))

        # Draws a square that lets the player go back
        draw.rect(screen, COLORS["WHITE"], Rect(50, 525, 700, 50), 2)
        screen.blit(FONTS["MENU"].render("GO BACK", 1, COLORS["WHITE"]), Rect(150, 535, 700, 50))
        if Rect(50, 525, 700, 50).collidepoint(mx, my):
            if mb == 1:
                file.close()
                break
            else:
                draw.rect(screen, COLORS["WHITE"], Rect(50, 525, 700, 50))
                screen.blit(FONTS["MENU"].render("GO BACK", 1, COLORS["RED"]), Rect(150, 535, 700, 50))
        display.flip()
        myClock.tick(30)


def pause():
    # pause is to see if the player is still paused
    # pause_game is the toggle variable to see if the person has let go of the escape key
    pause = True
    pause_game = False
    while pause:

        # Getting user input
        for evnt in pygame.event.get():
            if evnt.type == QUIT:
                pause = False
                pygame.quit()
                break

        keys = pygame.key.get_pressed()

        # Drawing to screen
        screen.fill((255, 255, 255))
        text = FONTS["TITLE"].render("GAME IS PAUSED", 1, COLORS["BLACK"])
        back = FONTS["TITLE"].render("PRESS ESCAPE TO UNPAUSE", 1, COLORS["BLUE"])
        screen.blit(text, MAIN_RECTS["UPPER_RECT"])
        screen.blit(back, MAIN_RECTS["LOWER_RECT"])

        # Checks if the user wants to go back into the game
        if keys[K_ESCAPE]:
            pause_game = True
        if pause_game and not keys[K_ESCAPE]:
            return False

        display.flip()
        myClock.tick(30)


# MAIN GAME ============================= Variable Declaration and Initialization
# SCREEN_SIZE is a constant tuple that defines the screen size
# myClock is the clock variable
# running is for the main game loop
# block is the size of each block in pixels
# size is the size of the map
# bullets stores all the bullets in the archer class
# enemies stores all the enemies in the game
# blades stores all sword hits from the rogue
# elementalists stores all elemental hits from the cleric
# clouds stores all the clouds in the menu
# UPGRADE_POSSIBLE stores if attributes can be upgraded (Max levels)
# pause_game stores if the player wants to pause the game
running = True
block = 20
size = []
bullets = []
enemies = []
blades = []
elementalists = []
clouds = []
UPGRADE_POSSIBLE = {
    1: False,
    2: False,
    3: False,
    4: False,
    5: False
}
pause_game = False


# ----------- Sounds Channels
# bgm is the background music channel
# run is the footsteps channel
# sword is the sword fx channel
# bullet_sound is the channel for bullet sounds
# crit_sound is the channel for critical hits
bgm = mixer.Channel(0)
run = mixer.Channel(1)
sword = mixer.Channel(2)
bullet_sound = mixer.Channel(3)
crit_sound = mixer.Channel(4)

# Starts the background music
bgm.play(BACKGROUND_MUSIC[random.randint(1, 7)], 0)

# ====== GAME LOOP
while running:

    # Getting user input
    for evnt in pygame.event.get():
        if evnt.type == QUIT:
            running = False

    # Draws the menu and allows player to choose a character
    character = menu()

    # Variables
    # game is whether or not the main game is running
    # enemies is reset to empty
    # screen_rect is the screen size (for side scrolling)
    # background is the background image
    # background_rect is the rectangle for the background
    # level is the level class
    # bubble is the array for bubbles (for the tank class)
    # world array shows the number of blocks in the world
    # player is the player class
    # spawn_points is the number of enemy spawn point classes
    # difficulty scales the enemy stats
    # camera is the main camera object
    # MAXENEMIES is the maximum number of enemies there are
    # all_sprite is a Sprite Group of all the sprites
    # score is reset to 0
    # timer is reset to 0
    # upgradecost is the array of upgrade costs, per level upgrade
    game = True
    enemies = []
    screen_rect = screen.get_rect()
    background = image.load("res/background.png").convert_alpha()
    background_rect = background.get_rect()
    level = Level(LEVELS[random.randint(1, 5)])
    level.create_level(0, 0)
    bubble = []
    world = level.world
    player = level.player
    spawn_points = level.spawn
    difficulty = 0
    camera = Camera(screen, player.rect, level.get_size()[0], level.get_size()[1])
    MAXENEMIES = 10 + difficulty // 100
    if character == 3:
        bubble.append(Bubble())
    else:
        bubble = []
    all_sprite = level.all_sprite
    score = 0
    timer = 0
    upgradecost = [200, 1000, 1500, 2000, 2500, 3000, 4000, 5000]

    # Main game
    while game:

        # Handles Back ground music
        if not bgm.get_busy():
            bgm.play(BACKGROUND_MUSIC[random.randint(1, 7)], 0)

        # handles regen
        if player.regen_timer > 180 and player.hp < player.maxhp:
            player.hp += 1

        # Resets controls before getting input
        up = left = right = False

        # Sees if user wants to quit
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                running = False
                game = False

        # Gets user input
        keys = key.get_pressed()
        mx, my, mb = get_mouse()

        # Parsing user input
        if keys[K_SPACE]:
            up = True
        if keys[K_a]:
            left = True
        if keys[K_d]:
            right = True
        if keys[K_q] and player.cd1 <= 0 and player.ab1timer <= 0 and player.mana >= player.ab1manacost and not player.ab1:
            player.mana -= player.ab1manacost
            player.ab1 = True
        if keys[K_r] and player.cd2 <= 0 and player.ab2timer <= 0 and player.mana >= player.ab2manacost and not player.ab2:
            player.mana -= player.ab2manacost
            player.ab2 = True
        if keys[K_ESCAPE]:
            pause_game = True
        if pause_game and not keys[K_ESCAPE]:
            pause_game = pause()

        # Handles all first abilities, separated by character
        if player.ab1:
            if character == 1:
                player.temp = player.crit_chance
                player.crit_chance = 80
                player.ab1 = False
                player.ab1timer = 150

            if character == 2:
                player.temp = player.dmg
                player.dmg += 50
                player.ab1 = False
                player.ab1timer = 150

            if character == 3:
                player.temp = player.move_speed
                player.move_speed += 10
                player.ab1 = False
                player.ab1timer = 150

        # Handles all second abilities, separated by character
        if player.ab2:
            if character == 1:
                player.ab2timer = 15
                enemies = []
                player.ab2 = False
            if character == 2:
                player.ab2timer = 150
                player.ab2 = False
            if character == 3:
                player.ab2timer = 150
                player.ab2 = False

        # Resets all player fist ability (buffs) back to original values upon resetting the
        # cooldown on the active portion
        if player.ab1timer == 1:
            player.cd1 = player.fullab1cd
            if character == 1:
                player.crit_chance = player.temp
            if character == 2:
                player.dmg = player.temp
            if character == 3:
                player.move_speed = player.temp

        # If the active portion runs out, put the ability on cooldown
        if player.ab2timer == 1:
            player.cd2 = player.fullab2cd

        # If the player clicked something
        if mb == 1:
            # If its the first character, then append swords to swords
            if character == 1:
                if len(blades) < 3:
                    blades.append(SwordHit(mx, my))
                    if not sword.get_busy():
                        sword.play(SWORD_SOUNDS[random.randint(1, 8)])
            # If its the second character, append bullets to bullets
            if character == 2:
                bullets.append(
                    Bullet(relative_view(player, camera)[0] + 10, relative_view(player, camera)[1] + 15, mx,
                           my, player))
                if player.ab2timer > 0:
                    bullets.append(
                        Bullet(relative_view(player, camera)[0] + 10, relative_view(player, camera)[1] + 15, mx,
                               my - 100, player))
                    bullets.append(
                        Bullet(relative_view(player, camera)[0] + 10, relative_view(player, camera)[1] + 15, mx,
                               my + 100, player))
            # 3rd character doesn't have an attack, so fourth: append elemental shots to elementalists, only if empty
            if character == 4:
                if len(elementalists) == 0:
                    if player.ab1:
                        typ = 2
                        player.ab1 = False
                        player.ab1timer = 2
                    elif player.ab2:
                        typ = 3
                        player.ab2 = False
                        player.ab2timer = 2
                    else:
                        typ = 1
                    elementalists.append(ElementalHit(mx, my, typ))

            # Checks if the player can upgrade
            if UPGRADE_RECTANGLES["Health"].collidepoint(mx, my) and player.money >= upgradecost[player.levels["Health"]] and player.levels["Health"] < 7:
                UPGRADE_POSSIBLE[1] = True
            if UPGRADE_RECTANGLES["Damage"].collidepoint(mx, my) and player.money >= upgradecost[player.levels["Dmg"]] and player.levels["Dmg"] < 7:
                UPGRADE_POSSIBLE[2] = True
            if UPGRADE_RECTANGLES["Move Speed"].collidepoint(mx, my) and player.money >= upgradecost[player.levels["Movement Speed"]] and player.levels["Movement Speed"] < 7:
                UPGRADE_POSSIBLE[3] = True
            if UPGRADE_RECTANGLES["Critical Chance"].collidepoint(mx, my) and player.money >= upgradecost[player.levels["Crit"]] and player.levels["Crit"] < 7:
                UPGRADE_POSSIBLE[4] = True
            if UPGRADE_RECTANGLES["Mana"].collidepoint(mx, my) and player.money > upgradecost[player.levels["Mana"]] and player.levels["Mana"] < 7:
                UPGRADE_POSSIBLE[5] = True

        # UPGRADING ABILITIES
        if UPGRADE_POSSIBLE[1] and mb == 0:
            hpupgrade = player.maxhp * 0.15
            player.maxhp += hpupgrade
            player.hp += hpupgrade
            player.money -= upgradecost[player.levels["Health"]]
            player.levels["Health"] += 1
            UPGRADE_POSSIBLE[1] = False
            print("HEALTH ++")
        if UPGRADE_POSSIBLE[2] and mb == 0:
            dmgupgrade = player.dmg * 0.5
            player.dmg += dmgupgrade
            player.money -= upgradecost[player.levels["Dmg"]]
            player.levels["Dmg"] += 1
            UPGRADE_POSSIBLE[2] = False
            print("DAMAGE ++")
        if UPGRADE_POSSIBLE[3] and mb == 0:
            player.move_speed += 1
            player.money -= upgradecost[player.levels["Movement Speed"]]
            player.levels["Movement Speed"] += 1
            UPGRADE_POSSIBLE[3] = False
            print("MOVE SPEED ++")
        if UPGRADE_POSSIBLE[4] and mb == 0:
            player.crit_chance += 5
            player.money -= upgradecost[player.levels["Crit"]]
            player.levels["Crit"] += 1
            UPGRADE_POSSIBLE[4] = False
            print("CRIT ++")
        if UPGRADE_POSSIBLE[5] and mb == 0:
            player.mana += 50
            player.maxmana += 50
            player.money -= upgradecost[player.levels["Mana"]]
            player.levels["Mana"] += 1
            UPGRADE_POSSIBLE[5] = False
            print("MANA ++")

        # Spawns enemies
        for spawn in spawn_points:
            s = random.randint(1, 1000)
            if s > 995 and len(enemies) <= MAXENEMIES:
                spawn.spawn(random.randint(1, 2))
            else:
                sp = False

        # Updates player variables
        player.update(up, left, right)
        player.regen_timer += 1
        difficulty += 1

        # Updates Cool down related Variables
        if player.ab1timer > 0:
            player.ab1timer -= 1
        if player.ab2timer > 0:
            player.ab2timer -= 1
        if player.cd1 > 0:
            player.cd1 -= 1
        if player.cd2 > 0:
            player.cd2 -= 1
        score += 0.1

        # Updates Mana
        if player.mana < player.maxmana:
            player.mana += 0.05

        # Checks if the player is dead or not
        if player.hp <= 0:
            you_died(score, character)
            game = False

        # Draw the background
        size = ((screen_rect.w // background_rect.w + 1) * background_rect.w,
                (screen_rect.h // background_rect.h + 1) * background_rect.h)
        bg = Surface(size)
        for x in range(0, size[0], background_rect.w):
            for y in range(0, size[1], background_rect.h):
                screen.blit(background, (x, y))

        # Draws sprites onto the screen
        camera.draw_sprites(screen, all_sprite)

        # Draws Attack Animations
        for bullet in bullets:
            draw.rect(screen, bullet.color, bullet.rect)
            bullet.update()
        for blade in blades:
            screen.blit(blade.image, blade.rect)
            blade.update()
        for element in elementalists:
            screen.blit(element.icons[(element.prog // 2) - 1], element.rect)
            element.update()

        # Checks if enemies collide with attacks and draws enemies
        for enemy in enemies:
            enemy.update()
            screen.blit(enemy.image, relative_view(enemy, camera))

            # Check Bullet collision and critical chance
            for bullet in bullets:
                if relative_view(enemy, camera).colliderect(bullet):
                    crit = random.randint(0, 100)
                    if crit < player.crit_chance:
                        enemy.hp -= 2 * bullet.dmg
                        if not crit_sound.get_busy():
                            SOUNDS["Crit"].play()
                    else:
                        enemy.hp -= bullet.dmg
                        if not bullet_sound.get_busy():
                            SOUNDS["Hit"].play()
                    bullets.remove(bullet)

            # Check Blade hits
            for blade in blades:
                if relative_view(enemy, camera).colliderect(blade.rect):
                    crit = random.randint(0, 100)
                    if crit < player.crit_chance:
                        enemy.hp -= player.dmg * 2
                        SOUNDS["Crit"].play()
                    else:
                        enemy.hp -= player.dmg

            # Check elemental hits
            for element in elementalists:
                if relative_view(enemy, camera).colliderect(element.rect):
                    if element.type == 3:
                        if player.hp < player.maxhp:
                            player.hp += player.dmg // 2
                        if player.mana < player.maxmana:
                            player.mana += player.dmg // 2
                    crit = random.randint(1, 100)
                    if crit < player.crit_chance:
                        enemy.hp -= element.dmg * 2
                        SOUNDS["Crit"].play()
                    else:
                        enemy.hp -= player.dmg

            # Check tank hits
            for bub in bubble:
                if relative_view(enemy, camera).colliderect(bub.rect):
                    crit = random.randint(1, 100)
                    if crit < player.crit_chance:
                        enemy.hp -= player.dmg * 2
                        SOUNDS["Crit"].play()
                    else:
                        enemy.hp -= player.dmg
            if enemy.hp <= 0:
                player.money += enemy.xp + difficulty // 20
                score += (enemy.xp * 10)
                enemies.remove(enemy)
            if enemy.rect.colliderect(player.rect):
                if character == 3 and player.ab2timer > 0:
                    player.regen_timer = 0
                else:
                    player.hp -= enemy.dmg
                    player.regen_timer = 0

        # Draws the protective block onto the screen
        for bub in bubble:
            screen.blit(bub.icon, bub.rect)
            bub.update()

        # Checks for errors
        if player.hp > player.maxhp:
            player.hp = player.maxhp
        if player.mana > player.maxmana:
            player.mana = player.maxmana

        # Final updates
        heads_up_display()
        camera.update()
        myClock.tick(30)
        display.flip()

pygame.quit()
