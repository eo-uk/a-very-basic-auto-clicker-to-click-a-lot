from pynput import keyboard
import pyautogui
import time


class AutoClicker():
    def __init__(self, delay=0.001, shortcut=['a', 's', 'd']):
        self.delay = delay #delay between each click
        self.shortcut = shortcut #to start and stop clicking
        self.running = True
        self.clicking = False
        self.pressed = []

    def _on_press(self, key):
        try:
            #If ESC is pressed, stop the program
            if key == keyboard.Key.esc:
                self.listener.stop()
                self.clicking = False
                self.running = False
                print('Auto Clicker Has Stopped')
                
            #Else, add the key to the list of pressed keys
            elif key.char not in self.pressed:
                self.pressed.append(key.char)
                #Check if shortcut is complete
                if self.pressed == self.shortcut:
                    #Start/stop clicking
                    self.clicking = not self.clicking
                    print("Clicking: ", self.clicking)
                    
        #If key is not a valid char
        except AttributeError: 
            pass

    def _on_release(self, key):
        try:
            #Remove the key from the list of pressed keys
            if key.char in self.pressed:
                self.pressed.remove(key.char)
                
        #If key is not a valid char
        except AttributeError: 
            pass

    def run(self):
        #Start keyboard listener
        self.listener = keyboard.Listener(
            on_press = self._on_press,
            on_release = self._on_release,
            daemon = True
        )
        self.listener.start()

        #Start mainloop
        print("Auto Clicker Is Now Running")
        while self.running:
            if self.clicking:
                pyautogui.click()
            if self.delay:
                time.sleep(self.delay)
    

if __name__ == '__main__':
    AutoClicker().run()
