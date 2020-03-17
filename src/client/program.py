from os import path
from _thread import *
from client import Network
from pynput import keyboard

class Game():
    def __init__(self,ip):
        # SETUP pygame environment
        #SETUP CONNECTION TO SERVER

        self.network = Network(ip)
        self.reply = ""

        print("So far so good!")

        # Get initializing data from server
        self.start = self.network.getInit()
        if not self.start:
            self.quit()
        else:
            print(self.start)

        print("now running!")
        self.run()
    
    def on_press(self,key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            self.reply = key.char
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            self.reply = str(key)
            print("reply : ", self.reply)

    def on_release(self,key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

        def inputloop(self):
            print("ran!")
            while True:
                self.reply = input("Send : ")

    def update(self):
        rep = "dummy" 
        if not self.reply == "":
            rep = self.reply
            self.reply = ""

        self.data = self.network.send(rep)
    
    def get_my_tank(self,tanks):
        for tank in tanks:
            if tank.id == self.playerid:
                return tank
        return None
    
    def listen(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


    def run(self):
        self.run = True
        start_new_thread(self.listen,())

        while self.run:
            #self.dt = self.clock.tick(60) / 1000
            self.update()


game = Game('192.168.0.75')
