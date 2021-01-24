
from chromasdk.ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid


import allogate as logging
import time

class RazerController():
    def __init__(self, fade_step=1):
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

        self.color = (255,255,255)
        #change razer colors
        logging.pprint("Setting device colors.", 1)
        c = ChromaColor(123,123,123)
        self.app.Mouse.setStatic(c)
        self.app.Headset.setStatic(c)
        #self.wave()

    def fade_to_color(self,r,g,b):
        pass

    def wave(self):
        while True:
            for i in range(0,255,5):
                c = ChromaColor(i,30,30)
                self.app.Mouse.setStatic(c)
                self.app.Headset.setStatic(c)



if(__name__=="__main__"):
    import argparse
    from time import sleep

    parser = argparse.ArgumentParser(description='RGB Keyboard CLI')
    parser.add_argument("-v","--verbose", action="count", help="Set verbosity level")
    parser.add_argument("-c","--color", help="Lighting Mode")
    args = parser.parse_args() 

    logging.VERBOSITY=0
    if args.verbose:
        logging.VERBOSITY=int(args.verbose)
    
    controller = RazerController()
    sleep(100)
