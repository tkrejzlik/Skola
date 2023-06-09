import pygame
import random


# Definice barev
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Velikost jedné buňky
CELL_SIZE = 15

# Velikost plánu
GRID_WIDTH = 40
GRID_HEIGHT = 40

# Inicializace pygame
pygame.init()
clock = pygame.time.Clock()

# Velikost okna
window_width = GRID_WIDTH * CELL_SIZE
window_height = GRID_HEIGHT * CELL_SIZE
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)


food_location = [random.randint(0, 40),random.randint(0, 40)]

#funkce vygeneruje novou souřadnici jídla
def generate_food_location():
    food_location.clear()
    x_loc = random.randint(0, 39)
    y_loc = random.randint(0, 39)
    food_location.append(x_loc)
    food_location.append(y_loc)

def draw_food(pos_x, pos_y):# funkce vykreslí jídlo na určené souřadnici podle parametrů
    pygame.draw.rect(screen, RED, (pos_x * CELL_SIZE, pos_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_snake(): #funkce vykreslí všechny části hada
    new_head_x = snake[-1][0] + move[0]
    new_head_y = snake[-1][1] + move[1]
    snake.append(list([new_head_x, new_head_y]))
    del snake[0]
    for i in range(len(snake)):
        pygame.draw.rect(screen, WHITE,( snake[i][0] * CELL_SIZE, snake[i][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def check_snake_food_collision():
    if snake[-1] == food_location: #hlava hada narazila na jídlo
        new_body_block = [snake[-1][0] + move[0],snake[-1][1] + move[1]]
        snake.append(new_body_block)
        generate_food_location()

def check_snake_collision_with_itself(): # hlídá, jestli po změně souřadnic hlavy nenarazila hlava do těla
    head = snake[-1]                     # vezmou se souřadnice hlavy hada a kontroluje se,
    for i in range(len(snake)-2):        # jestli není její souřadnice stejná jako nějaká souřadnice zbytku hada(=kolize)
        if i in head:
            return True

def check_snake_hits_boundaries(head_x, head_y):
    if head_x > 40 or head_y > 40 or head_x < 0 or head_y < 0:
        return True

# Hlavní smyčka hry
game_over = False
running = True
snake = [[10,15]]
move = [0,0]
direction = ""
while running:
    if game_over:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                move = [-1,0]
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                move = [1,0]
                direction = "right"
            elif event.key == pygame.K_DOWN and direction != "up":
                move = [0,1]
                direction = "down"
            elif event.key == pygame.K_UP and direction != "down":
                move = [0,-1]
                direction = "up"

    # Vykreslení plánu
    screen.fill(BLACK)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    draw_snake()
    if check_snake_hits_boundaries(snake[0][0], snake[0][1]) or check_snake_collision_with_itself():
        running = False
    draw_food(food_location[0], food_location[1])
    check_snake_food_collision()
    pygame.display.flip()
    clock.tick(15)
# Ukončení pygame
pygame.quit()