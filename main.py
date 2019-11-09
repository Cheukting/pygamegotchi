import random


WIDTH = 600
HEIGHT = 600

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
        self.mood = 5
        self.hygiene = 5

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

    def get_sad(self):
        self.mood -= 1
        clock.schedule(self.get_sad, random.randint(2, 5))

    def get_dirty(self):
        self.hygiene -= 1
        clock.schedule(self.get_dirty, random.randint(2, 5))

    def update(self):
        if self.energy <= 0 or self.mood <= 0 or self.hygiene <= 0:
            self.die()

    def start(self):
        self.get_hungry()
        self.get_sad()
        self.get_dirty()

    def feed(self):
        self.energy += 1
        if self.energy > 10:
            self.energy = 10

    def play(self):
        self.mood += 1
        if self.mood > 10:
            self.mood = 10

    def clean(self):
        self.hygiene += 1
        if self.hygiene > 10:
            self.hygiene = 10


class Btn:
    def __init__(self, pos1, pos2, text, on_click, bg_color=GREEN):
        self.rect = Rect(pos1, pos2)
        self.on_click = on_click
        self.text = text

        self.bg_color = bg_color

    def was_clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.on_click()

    def draw(self):
        screen.draw.textbox(self.text, self.rect, background=self.bg_color)


pet = Pet("snake", "pet_dead")
pet.start()


def reset():
    global pet
    pet = Pet("snake", "pet_dead")
    pet.start()


def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        if pet.alive:
            if feed_btn.was_clicked(pos):
                feed_btn.on_click()
            elif play_btn.was_clicked(pos):
                play_btn.on_click()
            elif clean_btn.was_clicked(pos):
                clean_btn.on_click()
        else:
            if reset_btn.was_clicked(pos):
                reset_btn.on_click()


def color_scale(color1, color2, amount):
    return (
        (color2[0] - color1[0]) * amount + color1[0],
        (color2[1] - color1[1]) * amount + color1[1],
        (color2[2] - color1[2]) * amount + color1[2],
    )


def die():
    pet.die()


def update():
    pet.update()
    feed_btn.bg_color = color_scale(RED, GREEN, pet.energy / 10)
    play_btn.bg_color = color_scale(RED, GREEN, pet.mood / 10)
    clean_btn.bg_color = color_scale(RED, GREEN, pet.hygiene / 10)


def draw():
    screen.clear()
    screen.fill(BLACK)
    pet.draw()
    if pet.alive:
        feed_btn.draw()
        play_btn.draw()
        clean_btn.draw()
    else:
        reset_btn.draw()


feed_btn = Btn((0, 100), (100, 100), "Feed Me", pet.feed, GREEN)
play_btn = Btn((0, 220), (100, 200), "Play With Me", pet.play, GREEN)
clean_btn = Btn((0, 440), (100, 100), "Clean Me", pet.clean, GREEN)
reset_btn = Btn((20, 20), (100, 100), "Reset", reset, RED)
