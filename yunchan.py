import pygame as pg
import pyttsx3
import datetime as dt

SIZE = [1800, 1097]
FPS = 60
screen = pg.display.set_mode(SIZE)
pg.init()
pg.display.set_caption("Yunchan Practice Assistant")

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def text(text, pos, size, color):
    font = pg.font.Font(None, size)
    text = font.render(text, True,  color)
    textpos = text.get_rect(x=0, y=0)
    textpos.center = pos
    screen.blit(text, textpos) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    clock = pg.time.Clock()
    run = True
    count = 0

    start_time = dt.datetime.now()
    start_time = start_time.strftime("%H:%M")
    changed = False

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    count += 1
                    if count >= 0:
                        changed = f"{count}"
                    else:
                        changed = f"negative {abs(count)}"
                if event.key == pg.K_SPACE:
                    if count > 0:
                        count = 0
                        changed = "reset"
                    else:
                        count -= 1
                    if count < 0:
                        if count == -1:
                            changed = "negative 1 half speed"
                        else:
                            changed = f"negative {abs(count)}"
                    else:
                        changed = f"{count}"

        screen.fill((255, 255, 255))  
        text("Yunchan Practice Assistant", (900, 100), 175, (0, 0, 0))
        text(f"Start Time: {start_time}", (900, 925), 100, (0, 0, 0))
        if count < 0:
            text("HALF SPEED!", (900, 300), 200, (255, 0, 0))
        if count == 3:
            text("Done!", (900, 300), 200, (0, 255, 0))
        text(f"Count: {count}", (900, 650), 400, (0, 0, 0))
        pg.display.flip()  
        clock.tick(FPS) 
        if changed != False:
            speak(changed)
            changed = False 
        if count == 3:
            speak("Done, next phrase")
            count = 0

    pg.quit()
    
if __name__ == "__main__":
    main()