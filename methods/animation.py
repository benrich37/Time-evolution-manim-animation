import numpy as np
from manimlib import FadeOut, FadeIn


def fade_out_all(list):
    args = []
    for i in np.arange(len(list)):
        args.append(FadeOut(list[i]))
    return args


def fade_in_all(list):
    args = []
    for i in np.arange(len(list)):
        args.append(FadeIn(list[i]))
    return args


def accelerate(t, acc=3):
    return t ** acc
