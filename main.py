def on_button_pressed_a():
    positie_player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    positie_player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

score = 0
positie_player: game.LedSprite = None
positie_player = game.create_sprite(2, 5)
vallend_blok = game.create_sprite(randint(0, 5), 0)
vallend_blok.delete()

def on_forever():
    global vallend_blok, score
    if vallend_blok.is_deleted():
        vallend_blok = game.create_sprite(randint(0, 5), 0)
    for index in range(4):
        basic.pause(500)
        vallend_blok.change(LedSpriteProperty.Y, 1)
    if vallend_blok.is_touching(positie_player):
        score += 1
        basic.show_icon(IconNames.YES)
        basic.pause(500)
        vallend_blok.delete()
    else:
        basic.show_icon(IconNames.NO)
        basic.pause(500)
        basic.clear_screen()
        basic.show_number(score)
        basic.pause(500)
        basic.clear_screen()
        score = 0
        vallend_blok.delete()
basic.forever(on_forever)
