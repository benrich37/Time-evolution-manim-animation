import numpy
from manimlib import Scene, Tex, GREY_B, Ellipse, WHITE, Circle, BLACK, LEFT, \
    VGroup, RIGHT

from ref.hold_constants import *
class lilGuy(Scene):
    text = Tex("\\ket{\\psi}")
    text_color = GREY_B
    scale = .7
    pup_radius = scale / 2
    eye_width = scale * 2
    eye_height = scale * 4
    char_scale = scale * 5
    look = "right"
    eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
    eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
    pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        eye_white_left.get_right() + pup_radius * LEFT)
    pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        eye_white_right.get_right() + pup_radius * LEFT)
    eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
    eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
    eyes = VGroup(eye_left, eye_right).scale(1 / 5).shift(RIGHT * .1)
    char = text.set_color(text_color).scale(char_scale)
    lilguy = VGroup(char, eyes)

    def __init__(self,text=Tex("\\ket{\\psi}"),text_color = GREY_B, scale = .7, look = "right"
                 ):
        self.text = text
        self.text_color = text_color
        self.scale = scale
        self.look = look
        self.pup_radius = self.scale / 2
        self.eye_width = self.scale * 2
        self.eye_height = self.scale * 4
        self.char_scale = self.scale * 5
        self.eye_white_left = Ellipse(width=self.eye_width, height=self.eye_height, color=WHITE, fill_opacity=1)
        self.eye_white_right = Ellipse(width=self.eye_width, height=self.eye_height, color=WHITE, fill_opacity=1)
        if self.look == "right":
            self.pupil_left = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_left.get_right() + self.pup_radius * LEFT)
            self.pupil_right = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_right.get_right() + self.pup_radius * LEFT)
        if self.look == "left":
            self.pupil_left = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_left.get_left() + self.pup_radius * RIGHT)
            self.pupil_right = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_right.get_left() + self.pup_radius * RIGHT)

        self.eye_left = VGroup(self.eye_white_left, self.pupil_left).shift(LEFT * self.eye_width)
        self.eye_right = VGroup(self.eye_white_right, self.pupil_right).shift(RIGHT * self.eye_width)
        self.eyes = VGroup(self.eye_left, self.eye_right).scale(1 / 5).shift(RIGHT * .1)
        if self.look == "right":
            self.eyes.shift(RIGHT * .1)
        if self.look == "left":
            self.eyes.shift(LEFT * .1)
        self.text.set_color(self.text_color).scale(self.char_scale)
        self.lilguy = VGroup(self.text, self.eyes)

    def shift(self,vector):
        self.lilguy.shift(vector)

    def eyes_follow(self,Point):
        for i in np.arange(2):
            self.eye_follow(Point, i)

    def eye_follow(self,Point,i):
        dir = self.get_eye_follow_dir()
        self.eyes[i][1].add_updater(
            lambda p: p.move_to()
        )


class lilGuyFromMethods(Scene):
    text = Tex("\\ket{\\psi}")
    text_color = GREY_B
    scale = .7
    pup_radius = scale / 2
    eye_width = scale * 2
    eye_height = scale * 4
    char_scale = scale * 5
    look = "right"
    eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
    eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
    pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        eye_white_left.get_right() + pup_radius * LEFT)
    pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        eye_white_right.get_right() + pup_radius * LEFT)
    eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
    eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
    eyes = VGroup(eye_left, eye_right).scale(1 / 5).shift(RIGHT * .1)
    char = text.set_color(text_color).scale(char_scale)
    lilguy = VGroup(char, eyes)

    def __init__(self,text=Tex("\\ket{\\psi}"),text_color = GREY_B, scale = .7, look = "right"
                 ):
        self.text = text
        self.text_color = text_color
        self.scale = scale
        self.look = look
        self.pup_radius = self.scale / 2
        self.eye_width = self.scale * 2
        self.eye_height = self.scale * 4
        self.char_scale = self.scale * 5
        self.eye_white_left = Ellipse(width=self.eye_width, height=self.eye_height, color=WHITE, fill_opacity=1)
        self.eye_white_right = Ellipse(width=self.eye_width, height=self.eye_height, color=WHITE, fill_opacity=1)
        if self.look == "right":
            self.pupil_left = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_left.get_right() + self.pup_radius * LEFT)
            self.pupil_right = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_right.get_right() + self.pup_radius * LEFT)
        if self.look == "left":
            self.pupil_left = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_left.get_left() + self.pup_radius * RIGHT)
            self.pupil_right = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_right.get_left() + self.pup_radius * RIGHT)

        self.eye_left = VGroup(self.eye_white_left, self.pupil_left).shift(LEFT * self.eye_width)
        self.eye_right = VGroup(self.eye_white_right, self.pupil_right).shift(RIGHT * self.eye_width)
        self.eyes = VGroup(self.eye_left, self.eye_right).scale(1 / 5).shift(RIGHT * .1)
        if self.look == "right":
            self.eyes.shift(RIGHT * .1)
        if self.look == "left":
            self.eyes.shift(LEFT * .1)
        self.text.set_color(self.text_color).scale(self.char_scale)
        self.lilguy = VGroup(self.text, self.eyes)

    def shift(self,vector):
        self.lilguy.shift(vector)

    def eyes_follow(self,Point):
        for i in np.arange(2):
            self.eye_follow(Point, i)

    def eye_follow(self,Point,i):
        dir = self.get_eye_follow_dir()
        self.eyes[i][1].add_updater(
            lambda p: p.move_to()
        )
