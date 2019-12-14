import pygame as pg

RED = (255,0,0)
WHITE = (255,255,255)


def text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,color)
    s.blit(msgobj,(x,y))


def reverse1(s):
    g = list(s)
    g.reverse()
    b = ''.join(g)
    print (b)

def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = WHITE
    color_active = RED
    color = color_inactive
    active = False
    text = ''
    done = False
    pg.draw.rect(screen,WHITE,(100,100,100,50))
    text ("FLIP!",100,100,RED)
    if event.type == pg.MOUSEBUTTONDOWN:
        if x in range(165,315) and y in range(310,460):
            reversal(text)
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pg.draw.rect(screen, color, input_box, 2)
        pg.display.flip()
        clock.tick(30)

    






if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
