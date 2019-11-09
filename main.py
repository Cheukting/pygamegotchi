WIDTH = 500
HEIGHT = 500

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pet_image = "snake"

pet = Actor(pet_image)
pet.pos = WIDTH / 2, HEIGHT / 2


def draw():
    screen.clear()
    screen.fill(BLACK)
    pet.draw()
