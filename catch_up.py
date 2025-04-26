from pygame import *
#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Китайку учат матеше')
#задай фон сцены
background = transform.scale(image.load('kalk.jpg'),(700,500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('kitau.png'),(100,100))
sprite2 = transform.scale(image.load('ymnichel.png'),(100,100))
x1 = 100
y1 = 100
x2 = 150
y2 = 50
speed = 10
clock = time.Clock()
game = True
while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))

    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if key_pressed[K_RIGHT] and x1 < 650:
        x1 += speed
    if key_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if key_pressed[K_DOWN] and y1 < 450:
        y1 += speed

    if key_pressed[K_a] and x2 > 5:
        x2 -= speed
    if key_pressed[K_d] and x2 < 650:
        x2 += speed
    if key_pressed[K_w] and y2 > 5:
        y2 -= speed
    if key_pressed[K_s] and y2 < 450:
        y2 += speed



    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()
