import random
import tkinter

from fontTools.subset import timer


def speed_test():
    speed_test_sentences = [
        " ",
        " "
    ]

    sentence = random.choice(speed_test_sentences)
    start = timer()
    main_window = tkinter.Tk()
    main_window.geometry('600x400')

if __name__ == '__main__':
    speed_test()
