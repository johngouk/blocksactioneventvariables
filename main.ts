input.onButtonPressed(Button.A, function () {
    myMessage = "New Msg"
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Stop shaking me!")
})
let myMessage = ""
myMessage = "Msg1"
basic.showIcon(IconNames.Heart)
basic.pause(2000)
basic.forever(function () {
    basic.showString(myMessage)
    basic.showIcon(IconNames.Happy)
})
