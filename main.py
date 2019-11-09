import random

WIDTH = 500
HEIGHT = 500

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pet_image = "snake"
pet_dead_image = "tombstone"

pet = Actor(pet_image)
pet.pos = WIDTH / 2, HEIGHT / 2
energy = 5

feed_btn = Rect((20, 20), (100, 100))


def on_mouse_down(pos, button):
    if button == mouse.LEFT and feed_btn.collidepoint(pos):
        print("FOOD")


def get_hungry():
    global energy
    energy -= 1
    clock.schedule(get_hungry, random.randint(2, 5))


def die():
    pet.image = pet_dead_image


def update():
    if energy <= 0:
        die()


def draw():
    screen.clear()
    screen.fill(BLACK)
    pet.draw()
    screen.draw.textbox(f"Feed Me {energy}", feed_btn, background=GREEN)


get_hungry()
