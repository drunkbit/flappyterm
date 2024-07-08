import keyboard
import os
import random
import sys
import time

done = False
dead = False
score = 0
hz = 0.05
d0 = 0
t0 = time.time()
t1 = time.time()


class flappyterm:
    def __init__(self, width, height, yx):
        self.width = width
        self.height = height
        self.yx = yx = [[" " for y in range(self.width)] for x in range(self.height)]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_yx(self):
        return self.yx

    def clear(self):
        os.system("clear")

    def erase(self):
        self.yx = [[" " for y in range(self.width)] for x in range(self.height)]

    def draw(self):
        flappyterm.clear()
        for y in range(self.height):
            for x in range(self.width):
                sys.stdout.write(self.yx[y][x])
            sys.stdout.write("\n")
        sys.stdout.write("<ESC> -> Exit / <Backspace> -> Restart / <Space> -> Jump: ")
        sys.stdout.flush()

    def recommendations(self):
        print(
            "\nRecommendations:\n - Console size at least 80 rows and 24 columns\n - Using Monospace or similar\n - No zoom\n - Using fullscreen (F11 mostly)\n"
        )
        input("Press <Enter> to continue... ")

    def lost(self):
        tmp = "You Lost! Score:     "
        center_height = int(flappyterm.get_height() / 2) - 1
        center_width = int(flappyterm.get_width() / 2) - 11
        n = 0
        self.yx[center_height][center_width] = "┌"
        for a in range(22):
            self.yx[center_height][center_width + 1 + a] = "─"
        self.yx[center_height][center_width + 23] = "┐"
        self.yx[center_height + 1][center_width] = "│"
        self.yx[center_height + 1][center_width + 23] = "│"
        self.yx[center_height + 2][center_width] = "└"
        for a in range(22):
            self.yx[center_height + 2][center_width + 1 + a] = "─"
        self.yx[center_height + 2][center_width + 23] = "┘"
        for a in tmp:
            self.yx[center_height + 1][center_width + 2 + n] = a
            n = n + 1
        if score < 10:
            self.yx[center_height + 1][center_width + 19] = "0"
            self.yx[center_height + 1][center_width + 20] = "0"
            self.yx[center_height + 1][center_width + 21] = str(score)[0]
        elif score > 9 and score < 1000:
            self.yx[center_height + 1][center_width + 19] = "0"
            self.yx[center_height + 1][center_width + 20] = str(score)[0]
            self.yx[center_height + 1][center_width + 21] = str(score)[1]
        else:
            self.yx[center_height + 1][center_width + 19] = str(score)[0]
            self.yx[center_height + 1][center_width + 20] = str(score)[1]
            self.yx[center_height + 1][center_width + 21] = str(score)[2]

    def play(self):
        global score
        global d0
        score = 0
        while dead == False:
            flappyterm.erase()
            if "pipe0" in locals():
                if pipe0.get_x() == 0:
                    del pipe0
                    score = score + 1
                else:
                    pipe0.update()
                    d0 = d0 + 1
            if "pipe1" in locals():
                if pipe1.get_x() == 0:
                    del pipe1
                    score = score + 1
                else:
                    pipe1.update()
            if "pipe0" not in locals():
                pipe0 = pipe("#", random.randint(5, flappyterm.get_height() - 6), 80)
                pipe0.update()
            if d0 > 40:
                if "pipe1" not in locals():
                    pipe1 = pipe(
                        "#", random.randint(5, flappyterm.get_height() - 6), 80
                    )
                    pipe1.update()
                    d0 = 0
            bird.update()
            flappyterm.draw()
            time.sleep(hz)


class bird:
    def __init__(self, y, x, jump_time, fall_time):
        self.y = y
        self.x = x
        self.jump_time = jump_time
        self.fall_time = fall_time

    def set_y(self, y):
        self.y = y

    def update(self):
        global bird
        global dead
        tmp0 = 0
        if dead == False:
            bird.fall()
            if self.y >= 1 and self.y <= flappyterm.get_height() - 2:
                if bird.check_collision(self.y - 1, self.x + 1):
                    dead = True
                elif bird.check_collision(self.y - 1, self.x + 2):
                    dead = True
                elif bird.check_collision(self.y - 1, self.x + 3):
                    dead = True
                elif bird.check_collision(self.y, self.x):
                    dead = True
                elif bird.check_collision(self.y, self.x + 1):
                    dead = True
                elif bird.check_collision(self.y, self.x + 2):
                    dead = True
                elif bird.check_collision(self.y, self.x + 3):
                    dead = True
                elif bird.check_collision(self.y, self.x + 4):
                    dead = True
                elif bird.check_collision(self.y + 1, self.x + 1):
                    dead = True
                elif bird.check_collision(self.y + 1, self.x + 3):
                    dead = True
                else:
                    dead = False
                flappyterm.get_yx()[self.y - 1][self.x + 1] = "_"
                flappyterm.get_yx()[self.y - 1][self.x + 2] = "_"
                flappyterm.get_yx()[self.y - 1][self.x + 3] = "_"
                flappyterm.get_yx()[self.y][self.x] = "("
                flappyterm.get_yx()[self.y][self.x + 1] = "O"
                flappyterm.get_yx()[self.y][self.x + 2] = ","
                flappyterm.get_yx()[self.y][self.x + 3] = "O"
                flappyterm.get_yx()[self.y][self.x + 4] = ")"
                flappyterm.get_yx()[self.y + 1][self.x + 1] = '"'
                flappyterm.get_yx()[self.y + 1][self.x + 3] = '"'
            else:
                if not self.y >= 1:
                    tmp0 = 1
                if not self.y <= flappyterm.get_height() - 2:
                    tmp0 = flappyterm.get_height() - 2
                self.y = tmp0
                if bird.check_collision(self.y - 1, self.x + 1):
                    dead = True
                elif bird.check_collision(self.y - 1, self.x + 2):
                    dead = True
                elif bird.check_collision(self.y - 1, self.x + 3):
                    dead = True
                elif bird.check_collision(self.y, self.x):
                    dead = True
                elif bird.check_collision(self.y, self.x + 1):
                    dead = True
                elif bird.check_collision(self.y, self.x + 2):
                    dead = True
                elif bird.check_collision(self.y, self.x + 3):
                    dead = True
                elif bird.check_collision(self.y, self.x + 4):
                    dead = True
                elif bird.check_collision(self.y + 1, self.x + 1):
                    dead = True
                elif bird.check_collision(self.y + 1, self.x + 3):
                    dead = True
                else:
                    dead = False
                flappyterm.get_yx()[self.y - 1][self.x + 1] = "_"
                flappyterm.get_yx()[self.y - 1][self.x + 2] = "_"
                flappyterm.get_yx()[self.y - 1][self.x + 3] = "_"
                flappyterm.get_yx()[self.y][self.x] = "("
                flappyterm.get_yx()[self.y][self.x + 1] = "O"
                flappyterm.get_yx()[self.y][self.x + 2] = ","
                flappyterm.get_yx()[self.y][self.x + 3] = "O"
                flappyterm.get_yx()[self.y][self.x + 4] = ")"
                flappyterm.get_yx()[self.y + 1][self.x + 1] = '"'
                flappyterm.get_yx()[self.y + 1][self.x + 3] = '"'

    def jump(self):
        global t0
        if time.time() - t0 > self.jump_time:
            if dead == False:
                if random.randint(2, 3) == 2:
                    self.y = self.y - 2
                else:
                    self.y = self.y - 3
            t0 = time.time()

    def fall(self):
        global t1
        if time.time() - t1 > self.fall_time:
            if dead == False:
                self.y = self.y + 1
            t1 = time.time()

    def check_collision(self, i, j):
        if flappyterm.get_yx()[i][j] == "#":
            return True
        else:
            return False


class pipe:
    def __init__(self, symbol, y, x):
        self.symbol = symbol
        self.y = y
        self.x = x

    def get_x(self):
        return self.x

    def update(self):
        if self.x <= 80:
            for i in range(flappyterm.get_height()):
                for j in range(5):
                    if self.x + j < 80:
                        flappyterm.get_yx()[i][self.x + j] = self.symbol
                        if i == self.y:
                            flappyterm.get_yx()[self.y - 4][self.x + j] = " "
                            flappyterm.get_yx()[self.y - 3][self.x + j] = " "
                            flappyterm.get_yx()[self.y - 2][self.x + j] = " "
                            flappyterm.get_yx()[self.y - 1][self.x + j] = " "
                            flappyterm.get_yx()[self.y][self.x + j] = " "
                            flappyterm.get_yx()[self.y + 1][self.x + j] = " "
                            flappyterm.get_yx()[self.y + 2][self.x + j] = " "
                            flappyterm.get_yx()[self.y + 3][self.x + j] = " "
                            flappyterm.get_yx()[self.y + 4][self.x + j] = " "
                            flappyterm.get_yx()[self.y + 5][self.x + j] = " "
        self.x = self.x - 1


def on_press(event):
    global done
    global dead
    global bird
    key = event.name
    if key == "esc":
        done = True
        dead = True
        return False
    if key == "backspace":
        if dead == True:
            dead = False
    if key == "space":
        bird.jump()
        if dead == True:
            dead = False


flappyterm = flappyterm(80, 23, [[]])
bird = bird(10, 11, 0.05, hz * 3)

if __name__ == "__main__":
    keyboard.on_press(on_press)
    flappyterm.recommendations()
    while done == False:
        while dead == False:
            flappyterm.play()
        flappyterm.lost()
        flappyterm.draw()
        bird.set_y(10)
        d0 = 0
        time.sleep(hz)
    flappyterm.clear()
    exit(0)