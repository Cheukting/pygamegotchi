import random


WIDTH = 500
HEIGHT = 500

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Pet:
    def __init__(self, img, dead_img):
        self.img = img
        self.dead_img = dead_img

        self.alive = True
        self.energy = 5

        self.actor = Actor(self.img)
        self.move(WIDTH / 2, HEIGHT / 2)

    def die(self):
        self.actor.image = self.dead_img
        self.alive = False

    def draw(self):
        self.actor.draw()

    def move(self, x, y):
        self.actor.pos = x, y

    def get_hungry(self):
        self.energy -= 1
        clock.schedule(self.get_hungry, random.randint(2, 5))

    def update(self):
        if self.energy <= 0:
            self.die()

    def start(self):
        self.get_hungry()

    def feed(self):
        self.energy += 1
        if self.energy > 10:
            self.energy = 10


pet = Pet("snake", "pet_dead")
pet.start()


feed_btn = Rect((20, 20), (100, 100))
reset_btn = Rect((20, 20), (100, 100))


def reset():
    global pet
    pet = Pet("snake", "pet_dead")
    pet.start()


def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        if pet.alive:
            if feed_btn.collidepoint(pos):
                pet.feed()
        else:
            if reset_btn.collidepoint(pos):
                reset()


def die():
    pet.die()


def update():
    pet.update()


def draw():
    screen.clear()
    screen.fill(BLACK)
    pet.draw()
    if pet.alive:
        screen.draw.textbox(f"Feed Me {pet.energy}", feed_btn, background=GREEN)
    else:
        screen.draw.textbox(f"Reset", reset_btn, background=RED)
