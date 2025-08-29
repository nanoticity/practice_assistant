import pygame as pg
import pygame.mixer as mixer
import asyncio

SIZE = [1600, 900]
FPS = 60
screen = pg.display.set_mode(SIZE)
pg.init()
mixer.init()
pg.display.set_caption("Yunchan Practice Assistant")

# Initialize sounds dictionary with all files from sounds directory
if __name__ == "__main__":
        sounds = {
        "done_next_phrase": mixer.Sound("docs/sounds/done_next_phrase.ogg"),
        "learn_it": mixer.Sound("docs/sounds/learn_it.ogg"),
        "half_speed": mixer.Sound("docs/sounds/half_speed.ogg"),
        "negative_1": mixer.Sound("docs/sounds/negative_1.ogg"),
        "negative_2": mixer.Sound("docs/sounds/negative_2.ogg"),
        "negative_3": mixer.Sound("docs/sounds/negative_3.ogg"),
        "negative_4": mixer.Sound("docs/sounds/negative_4.ogg"),
        "negative_5": mixer.Sound("docs/sounds/negative_5.ogg"),
        "0": mixer.Sound("docs/sounds/0.ogg"),
        "1": mixer.Sound("docs/sounds/1.ogg"),
        "2": mixer.Sound("docs/sounds/2.ogg"),
        "3": mixer.Sound("docs/sounds/3.ogg"),
        "reset": mixer.Sound("docs/sounds/reset.ogg"),
        "forget": mixer.Sound("docs/sounds/are_you_forgetting_about_me?.ogg")
    }
else:
        sounds = {
        "done_next_phrase": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/done_next_phrase.ogg"),
        "half_speed": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/half_speed.ogg"),
        "negative_1": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/negative_1.ogg"),
        "negative_2": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/negative_2.ogg"),
        "negative_3": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/negative_3.ogg"),
        "negative_4": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/negative_4.ogg"),
        "negative_5": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/negative_5.ogg"),
        "0": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/0.ogg"),
        "1": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/1.ogg"),
        "2": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/2.ogg"),
        "3": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/3.ogg"),
        "reset": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/reset.ogg"),
        "forget": mixer.Sound("/lib/python3.12/site-packages/assistant/docs/sounds/are_you_forgetting_about_me?.ogg")
    }


async def play_sound(sound_name):
    """Play a sound from the sounds dictionary and wait for it to finish."""
    if sound_name in sounds:
        sounds[sound_name].play()
        # Wait until the sound finishes playing
        while mixer.get_busy():
            await asyncio.sleep(0.1)  # Wait for 100ms to avoid excessive CPU usage
            
        return 1
    return 0

def text(text, pos, size, color):
    font = pg.font.Font(None, size)
    text = font.render(text, True,  color)
    textpos = text.get_rect(x=0, y=0)
    textpos.center = pos
    screen.blit(text, textpos) 
    
async def main():
    run = True
    count = 0
    c0 = pg.time.get_ticks()

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    count += 1
                    if count >= 0:
                        await play_sound(str(count))
                    else:
                        await play_sound(f"negative_{abs(count)}")
                if event.key == pg.K_SPACE:
                    if count > 0:
                        count = 0
                        await play_sound("reset")
                    else:
                        count -= 1
                    if count < 0:
                        if count == -1:
                            await play_sound("half_speed")
                            await play_sound(f"negative_{abs(count)}")
                        else:
                            await play_sound(f"negative_{abs(count)}")
                    else:
                        await play_sound(str(count))

        screen.fill((255, 255, 255))  
        text("Yunchan Practice Assistant", (800, 100), 150, (0, 0, 0))
        if count < 0 and count != -5:
            text("HALF SPEED!", (800, 300), 200, (255, 0, 0))
        if count == 3:
            text("Done!", (800, 300), 200, (0, 255, 0))
        if count == -5:
            await play_sound("learn_it")
            text("Learn it.", (800, 300), 200, (255, 0, 0))
        text(f"Count: {count}", (800, 650), 400, (0, 0, 0))
        pg.display.flip()  
        await asyncio.sleep(0.06) 
        if count == 3:
            await play_sound("done_next_phrase")
            count = 0
        if count == -5:
            count = 0
            await asyncio.sleep(1)
        c1 = pg.time.get_ticks()
        if c1 - c0 >= 300_000:
            await play_sound("forget")
            c0 = c1

    pg.quit()

if __name__ == "__main__":
    asyncio.run(main())