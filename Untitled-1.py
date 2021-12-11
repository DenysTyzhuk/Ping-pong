from pygame import *
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS= 60
game = True
back = (166, 123, 223)
window.fill(back)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
