
from .chromasdk.ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid
from .aud_razer import RazerAudioVisualizer
import asyncio

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
        """ Instantly set color
        """
        self.r = r
        self.g = g
        self.b = b
        self.update_color(self.r, self.g, self.b)

    def fade(self,r,g,b, step=1):
        """ Fade from current color to target, gradually
        """
        logging.pprint(f"Fading to {r},{g},{b} from {self.r},{self.g},{self.b}", 5)
        while True:
            logging.pprint(f"Fading to {r},{g},{b} from {self.r},{self.g},{self.b}", 5)
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
        """ Simple wave effect
        """
        while True:
            for i in range(0,255,1):
                c = ChromaColor(i,30,30)
                self.app.Mouse.setStatic(c)
                self.app.Headset.setStatic(c)

    def update_color(self, r, g, b):
        
        """ Update and render colors
        """
        logging.pprint(f"setting color to {r},{g},{b}", 5)
        if(self.delay):
            time.sleep(self.delay)
        r= int(r*self.coef)
        g= int(g*self.coef)
        b= int(b*self.coef)


        if(r>255): r=255
        if(g>255): g=255
        if(b>255): b=255

        if(r<0): r=0
        if(g<0): g=0
        if(b<0): b=0
        c = ChromaColor(r,g,b)
        self.app.Mouse.setStatic(color=c)
        self.app.Headset.setStatic(color=c)

    def rainbow(self, step):
        """ Loop on a rainbow effect
        """
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

