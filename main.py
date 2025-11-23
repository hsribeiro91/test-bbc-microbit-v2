def on_button_pressed_a():
    if x == 1:
        basic.show_icon(IconNames.YES)
        music.play(music.string_playable("C5 F A C A E C C5 ", 120),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x
    if x == 1:
        x = 0
    else:
        x += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

x = 0
basic.clear_screen()