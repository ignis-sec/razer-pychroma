
from chromasdk.ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid


import allogate as logging
import time

class RazerController():
    def __init__(self, fade_step=1, delay=0):
        logging.pprint("Creating Chroma Information.", 4)
        self.info = ChromaAppInfo()
        self.info.DeveloperName = 'Ignis'
        self.info.DeveloperContact = 'me@ignis.wtf'
        self.info.Category = 'application'
        self.info.SupportedDevices = ['keyboard', 'mouse', 'mousepad', 'headset']
        self.info.Description = 'Sync Razer device colors with other components'
        self.info.Title = '.\\.\\Ignis\'s Spotify Sync Tool'
        logging.pprint("Creating Chroma App.", 2)
        self.app = ChromaApp(self.info)
        logging.pprint("Chroma App created.", 1)
        self.fade_step = fade_step
        self.r, self.g, self.b = (255,255,255)
        self.delay=delay
        self.coef=1

    def set(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.update_color(self.r, self.g, self.b)

    def fade(self,r,g,b, step=1):
        logging.pprint(f"Fading to {r},{g},{b} from {self.r},{self.g},{self.b}", 2)
        while True:
            logging.pprint(f"Fading to {r},{g},{b} from {self.r},{self.g},{self.b}", 3)
            if(abs(self.r-r)<step): self.r=r
            if(r>self.r): self.r+=step
            elif(r<self.r): self.r-=step

            if(abs(self.r-r)<step): self.g=g
            if(g>self.g):self.g+=step
            elif(g<self.g): self.g-=step
            
            if(abs(self.r-r)<step): self.b=b
            if(b>self.b):self.b+=step
            elif(b<self.b): self.b-=step

            self.update_color(self.r, self.g, self.b)
            if(r == self.r and g == self.g and b==self.b): return

    def wave(self):
        while True:
            for i in range(0,255,1):
                c = ChromaColor(i,30,30)
                self.app.Mouse.setStatic(c)
                self.app.Headset.setStatic(c)

    def update_color(self, r, g, b):
        if(self.delay):
            time.sleep(self.delay)
        c = ChromaColor(r*self.coef,g*self.coef,b*self.coef)
        self.app.Mouse.setStatic(color=c)
        self.app.Headset.setStatic(color=c)

    def rainbow(self, step):
        r=0xff
        g=0
        b=0
        while(True):
            for g in range(0,0x1e, step):
                self.set(r=r, g=g, b=b)
            for g in range(0x1e, 0x50, step):
                self.set(r=r, g=g, b=b)
            for r in range(0xff, 0x00, -1*step):
                self.set(r=r, g=g, b=b)
            for b in range(0x00, 0x50, step):
                self.set(r=r, g=g-b, b=b)
            g=0
            for r in range(0x00, 0xff, step):
                self.set(r=r, g=g, b=b)
            for b in range(0x50, 0x00, -1*step):
                self.set(r=r, g=g, b=b)

    def adjust_brightness(self, coef):
        self.coef = coef

if(__name__=="__main__"):
    import argparse

    parser = argparse.ArgumentParser(description='RGB Keyboard CLI')
    parser.add_argument("-v","--verbose", action="count", help="Set verbosity level")
    parser.add_argument("-c","--color", help="Lighting Mode")
    args = parser.parse_args() 

    logging.VERBOSITY=0
    if args.verbose:
        logging.VERBOSITY=int(args.verbose)
    
    controller = RazerController(delay=0.01)

    logging.pprint("Setting device colors.", 1)
    
    controller.fade(0,0,0, 5)
    controller.fade(255,255,0, 5)
    controller.fade(0,255,255, 5)
    controller.fade(255,0,0, 5)
    controller.rainbow(step=15)