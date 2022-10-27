def on_button_pressed_a():
    global myMessage
    myMessage = "New Msg"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("Stop shaking me!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

myMessage = ""
myMessage = "Msg1"
basic.show_icon(IconNames.HEART)
basic.pause(2000)

def on_forever():
    basic.show_string(myMessage)
    basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
