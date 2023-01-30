import random
import tkinter
import timer


def speed_test():
    speed_test_sentences = [
        " ",
        " "
    ]

    sentence = random.choice(speed_test_sentences)
    start = timer()
    main_window = tkinter.Tk()
    main_window.geometry('600x400')

    label_1 = tkinter.Label(main_window, text=sentence, font='times 20')
    label_1.place(x=150, y=10)

    label_2 = tkinter.Label(main_window, text='Start Typing', font='times 20')
    label_2.place(x=10 , y = 50)

    entry = tkinter.Entry(main_window)
    entry.place(x=280, y = 55)


if __name__ == '__main__':
    speed_test()
