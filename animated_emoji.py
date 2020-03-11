from sense_hat import SenseHat

sense = SenseHat()

# display is 8x8 pixels

X = [255, 255, 255]
O = [0, 0, 0]

emoji_happy = [
    O, O, O, O, O, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, O, O, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, O, X, O, O, X, O, O,
    O, O, O, X, X, O, O, O
]

sense.set_pixels(emoji_happy)