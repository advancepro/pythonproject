import pygame
from tkinter import *
from RoomCall import Room
from WallOfTheRoom import Wall
import unittest
from tkinter import ttk
from tkinter import filedialog

def click(textentry=0):
    entered_text = textentry.get()

def say_hello():
    name_of_user = entry_1.get()
    string_to_display = "Hello" + name_of_user
    label_2 = Label(my_window)
    label_2["text"] = string_to_display
    label_2.grid(row=1, column=1)


my_window = Tk()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NAVYBLUE = (0, 0, 128)
ORANGERED = (255, 69, 0)
LIGHTCORAL = (240, 128, 128)
YELLOW = (255, 255, 0)
RED = (255, 0, 1)
TURQUOISE = (64, 224, 208)
LAWNGREEN = (124, 252, 0)
KHAKI = (240, 230, 140)

label_1 = Label(my_window, text="Please enter your name: \n")

entry_1 = Entry(my_window)
button_1 = Button(my_window, text="Click me to enter name", command=say_hello)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)

my_window.mainloop()


class Player(pygame.sprite.Sprite):
    change_x = 0  # speed
    change_y = 0

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(YELLOW)  # THE PLAYER

        self.rect = self.image.get_rect()  # location of the player
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        self.rect.x += self.change_x  # hareket halinde

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left  # geri gittiğinde odaları dolaşır 0dan 1 1den 0 a
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room1(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, YELLOW],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, YELLOW],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, YELLOW],
                 [390, 50, 20, 500, KHAKI]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, NAVYBLUE],
                 [0, 350, 20, 250, ORANGERED],
                 [780, 0, 20, 250, NAVYBLUE],
                 [780, 350, 20, 250, ORANGERED],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, ORANGERED],
                 [190, 50, 20, 500, NAVYBLUE],
                 [590, 50, 20, 500, ORANGERED]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, LIGHTCORAL],
                 [0, 350, 20, 250, LIGHTCORAL],
                 [780, 0, 20, 250, LIGHTCORAL],
                 [780, 350, 20, 250, LIGHTCORAL],
                 [20, 0, 760, 20, LIGHTCORAL],
                 [20, 580, 760, 20, LIGHTCORAL]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):#beyazlar(son oda)
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, TURQUOISE)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):#maviler(son oda)
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


def main():
    pygame.init()

    screen = pygame.display.set_mode([800, 600])#ekran büyüklüğü

    pygame.display.set_caption('Room to Room')

    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 901: #diğer odaya girme süresi
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)#karenin hızı(oyuncu)

    pygame.quit()


if __name__ == "__main__":
    main()
