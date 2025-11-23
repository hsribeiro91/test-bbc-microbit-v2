input.onButtonPressed(Button.A, function () {
    if (x == 1) {
        basic.showIcon(IconNames.Yes)
        music.play(music.stringPlayable("C5 F A C A E C C5 ", 120), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.Square)
    }
})
input.onButtonPressed(Button.B, function () {
    if (x == 1) {
        x = 0
    } else {
        x += 1
    }
})
let x = 0
basic.clearScreen()
