input.onButtonPressed(Button.A, function () {
    positie_player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    positie_player.change(LedSpriteProperty.X, 1)
})
let score = 0
let positie_player: game.LedSprite = null
positie_player = game.createSprite(2, 5)
let vallend_blok = game.createSprite(randint(0, 5), 0)
vallend_blok.delete()
basic.forever(function () {
    if (vallend_blok.isDeleted()) {
        vallend_blok = game.createSprite(randint(0, 5), 0)
    }
    for (let index = 0; index < 4; index++) {
        basic.pause(500)
        vallend_blok.change(LedSpriteProperty.Y, 1)
    }
    if (vallend_blok.isTouching(positie_player)) {
        score += 1
        basic.showIcon(IconNames.Yes)
        basic.pause(500)
        vallend_blok.delete()
    } else {
        basic.showIcon(IconNames.No)
        basic.pause(500)
        basic.clearScreen()
        basic.showNumber(score)
        basic.pause(500)
        basic.clearScreen()
        score = 0
        vallend_blok.delete()
    }
})
