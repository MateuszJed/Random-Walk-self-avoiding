import pygame, random
import numpy as np

pygame.init()

BLACK = (0,0,0)
WHITE = (200,200,200)
GRAY = (107,107,107)
WIDTH, HEIGHT = 500,500
blockSize = 20

moving_options =  [
{"x" : blockSize, "y" : 0}, #Right
{"x" : -blockSize, "y" : 0},#Left
{"x" : 0, "y" : blockSize}, #Down
{"x" : 0, "y" : -blockSize}]#Up

rect = pygame.Rect((WIDTH/2-blockSize/4, WIDTH/2-blockSize/4, (blockSize-2)/2, (blockSize-2)/2))
grid = np.array(np.zeros((int(WIDTH/blockSize), int(HEIGHT/blockSize))),dtype=bool,copy=True)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

FPS = 60
def draw_window():
    rect_old_x, rect_old_y = rect.centerx,rect.centery
    #drawGrid(WIDTH,HEIGHT,blockSize,GRAY) #Display grid
    pygame.draw.ellipse(WIN,WHITE,rect)
    options = []
    for i in moving_options:
        a = rect.x + moving_options[random.randint(0, 3)]["x"]
        b = rect.y + moving_options[random.randint(0, 3)]["y"]
        if is_valid(a,b):
            options.append({"x": a,"y":b})
    if len(options) > 0:
        rect.x = options[random.randint(0, len(options)-1)]["x"]
        rect.y = options[random.randint(0, len(options)-1)]["y"]
        options.clear()
    else:
        print("No another way to go")
    pygame.draw.line(WIN,WHITE,(rect.centerx,rect.centery),(rect_old_x, rect_old_y))
    grid[int(rect.x/blockSize),int(rect.y/blockSize)] = True
    
    pygame.display.update()

def is_valid(dx,dy):
    if dx < 0 or dx >= WIDTH or dy < 0 or dy >= HEIGHT:
        return False
    return not(grid[int(dx/blockSize),int(dy/blockSize)])

def drawGrid(WIDTH,HEIGH,blockSize,Color):
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGH, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(WIN, Color, rect, 1)

def main():
    clock = pygame.time.Clock()
    WIN.fill(BLACK)
    while True:
        clock.tick(FPS)
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()
        draw_window()

if __name__ == "__main__":
    main()