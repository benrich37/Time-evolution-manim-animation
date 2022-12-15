from manimlib import Scene, ValueTracker


class ReImMod(Scene):
    rePart = ValueTracker(0)
    imPart = ValueTracker(0)
    modPart = ValueTracker(0)

    def __init__(self, rePart, imPart, modPart):
        self.rePart = rePart
        self.imPart = imPart
        self.modPart = modPart

    def set_parts(self, re, im, mod):
        self.rePart.set_value(re)
        self.imPart.set_value(im)
        self.modPart.set_value(mod)
