
import math
import asyncio
from .audio_loopback.audio_loopback import AudioController
import allogate as logging

class AudioVisualizer:
    """ Audio visualizer class for keyboard.
        convert audio data to Keyboard Matrix
    """
    def __init__(self, chroma_app, threshold=1000, fade=0.8, delay=0.05, dampen=2400, ceiling=2700, ambient_brightness_coef=0.1):
        """
        @param threshold - Threshold to clamp audio data when reached. Maximum audio level from input.
        @param fade - fade constant, higher the value, longer the fade effect will last. Between 0-1
        @param delay - how long to wait between each read from audio
        """

        self.chroma_app = chroma_app
        self.audio = AudioController()

        self.r=0
        self.g=0
        self.b=0

        self.threshold = threshold
        self.fade = fade
        self.delay = delay
        self.dampen = dampen
        self.ceiling = ceiling
        self.ambient_brightness_coef = ambient_brightness_coef

    def visualizeOnce(self, falloff=0.8):
        """ Visualize current levels of audio on the razer devices, and render it
        """
        
        r = self.chroma_app.r * falloff
        g = self.chroma_app.g * falloff
        b = self.chroma_app.b * falloff

        #audio data from stream (after fft)
        data = self.audio.readOnce(5,50)

        logging.pprint(data[4], 5)
        #render colors
        self.chroma_app.coef = (data[4]-self.dampen)/(self.ceiling - self.dampen)
        if(self.chroma_app.coef<self.ambient_brightness_coef): self.chroma_app.coef=self.ambient_brightness_coef
        self.chroma_app.update_color(self.chroma_app.r,self.chroma_app.g,self.chroma_app.b)

    async def change_color(self, r,g,b):
        self.chroma_app.fade(r,g,b)
        
    async def visualize(self, falloff=0.8):
        """ Loop visualizeOnce infinitely
        """
        while True:
            self.visualizeOnce()
            await asyncio.sleep(self.delay)

        


