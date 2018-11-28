import simplegui


time = 0
a = 0
b = 0


def format(time):
    seconds = time // 10
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(time // 600) + ":" + str(seconds) + "." + str(time % 10)
pass


def start_handler():
    timer.start()


def stop_handler():
    global a, b
    if (timer.is_running()):
        if time % 10 == 0 and time != 0:
            a += 1
        elif time != 0:
            b += 1
    timer.stop()


def reset_handler():
    global time, a, b
    timer.stop()
    time = 0
    a = 0
    b = 0


def timer_handler():
    global time
    time += 1


def draw_handler(canvas):
    canvas.draw_text(format(time), (140, 200), 60, "Red")
    canvas.draw_text(str(a), (290, 60), 35, "Black")
    canvas.draw_text("/", (330, 60), 35, "Black")
    canvas.draw_text(str(b), (360, 60), 35, "Black")


frame = simplegui.create_frame("Stop: Game", 420, 420)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.set_canvas_background('Green')
frame.add_button("Start", start_handler, 150)
frame.add_button("Stop", stop_handler, 150)
frame.add_button("Reset", reset_handler, 150)

frame.start()
