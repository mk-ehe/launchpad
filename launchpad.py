from tkinter import *
import pygame
from random import randint
from os import getcwd

print(getcwd())
pygame.mixer.init()
pygame.mixer.music.set_volume(0.36)


window = Tk()
bg_png = PhotoImage(file='daszi.png')
icon = PhotoImage(file='daszi_icon.png')
window.geometry('750x790')
window.title('Launchpad')
window.resizable(False,False)
window.iconphoto(True,icon)
bg = Label(window, image=bg_png)
bg.pack()


sound1 = pygame.mixer.Sound("bg.mp3")
channel_2 = pygame.mixer.Channel(1)
channel_2.set_volume(0.24)
    

def hex_color():
    kolor = f'#{randint(0,255):02X}{randint(0,255):02X}{randint(0,255):02X}'
    return kolor


def my_callback(event): # When any key is pressed
    for widget in window.winfo_children():  # Collect all classes of the widgets 
        if isinstance(widget, Button):  # If it belongs to button class 
            if widget['text']==event.char or widget['text'].lower()==event.char:
                widget['relief']='sunken'   # Update relief option to pressed 
                widget.config(background=hex_color())
            
            if event.char == '0':
                channel_2.play(sound1,loops=0)
                

            elif event.char == '1':
                pygame.mixer.music.load('1.wav')
                pygame.mixer.music.play(loops=0)

            elif event.char == '2':
                pygame.mixer.music.load('2.wav')
                pygame.mixer.music.play(loops=0)


            elif event.char == '3':
                pygame.mixer.music.load('3.wav')
                pygame.mixer.music.play(loops=0)

            elif event.char == '4':
                pygame.mixer.music.load('4.wav')
                pygame.mixer.music.play(loops=0)

            elif event.char == '5':
                pygame.mixer.music.load('5.wav')
                pygame.mixer.music.play(loops=0)
            
            elif event.char == '6':
                pygame.mixer.music.load('6.wav')
                pygame.mixer.music.play(loops=0)

            elif event.char == '7':
                pygame.mixer.music.load('7.wav')
                pygame.mixer.music.play(loops=0)

            elif event.char == '8':
                pygame.mixer.music.load('8.wav')
                pygame.mixer.music.play(loops=0)

            elif event.char == '9':
                pygame.mixer.music.load('9.wav')
                pygame.mixer.music.play(loops=0)
            

def release(event):
    for widget in window.winfo_children():
        if isinstance(widget, Button):
            widget['relief'] = 'raised'


tile_0 = Button(window, background=hex_color(), text='0',font=('Arial',20,'bold'),padx=150,pady=20)
tile_0.place(x=208,y=670)

tile_1 = Button(window, background=hex_color(), text='1',font=('Arial',30,'bold'),padx=55,pady=45)
tile_1.place(x=65,y=480)

tile_2 = Button(window, background=hex_color(),text='2',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_2.place(x=294,y=480)

tile_3 = Button(window, background=hex_color(),text='3',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_3.place(x=520,y=480)

tile_4 = Button(window,background=hex_color(),text='4',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_4.place(x=65,y=270)

tile_5 = Button(window,background=hex_color(),text='5',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_5.place(x=294,y=270)

tile_6 = Button(window,background=hex_color(),text='6',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_6.place(x=520,y=270)

tile_7 = Button(window,background=hex_color(),text='7',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_7.place(x=65,y=60)

tile_8 = Button(window,background=hex_color(),text='8',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_8.place(x=294,y=60)

tile_9 = Button(window,background=hex_color(),text='9',font=('Arial',30,'bold') ,padx=55,pady=45)
tile_9.place(x=520,y=60)

window.bind('<Key>',my_callback)
window.bind('<KeyRelease>',release)
window.mainloop()