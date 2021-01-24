
from .razer_chroma import *

if(__name__=="__main__"):
    """ This package is not meant to be used directly, so this part is only for testing purpose
    """
    import argparse

    parser = argparse.ArgumentParser(description='RGB Keyboard CLI')
    parser.add_argument("-v", "--verbose", action="count", help="Set verbosity level")
    parser.add_argument("-c", "--color", help="Lighting Mode")
    parser.add_argument("-a", "--audio", action="store_true", help="Audio mode")
    args = parser.parse_args() 

    logging.VERBOSITY=0
    if args.verbose:
        logging.VERBOSITY=int(args.verbose)
    
    controller = RazerController(delay=None)

    logging.pprint("Setting device colors.", 1)
    
    if(args.audio):
        controller.set(255,255,0)
        visualizer = RazerAudioVisualizer(controller)
        asyncio.run(visualizer.visualize())

    




    controller.fade(0,0,0, 5)
    controller.fade(255,255,0, 5)
    controller.fade(0,255,255, 5)
    controller.fade(255,0,0, 5)
    controller.rainbow(step=15)