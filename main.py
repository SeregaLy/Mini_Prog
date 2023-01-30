import tkinter
from timeit import default_timer as timer
import random


def speed_test():
    speed_test_sentences = [
        'Карлсон - хороший друг',
        'Собака друг человека'
    ]

    sentence = random.choice(speed_test_sentences)
    start = timer()
    main_window = tkinter.Tk()
    main_window.geometry('600x400')

    label_1 = tkinter.Label(main_window, text=f'Контрольный текст: {sentence}',
                            font='times 20')
    label_1.place(x=10, y=10)

    label_2 = tkinter.Label(main_window, text='Начинайте печатать',
                            font='times 20')
    label_2.place(x=10, y=50)

    entry = tkinter.Entry(main_window)
    entry.place(x=280, y=55)

    def check_result():
        if entry.get() == sentence:
            end = timer()
            label_3.configure(
                text=f'Ваше время: {round((end - start), 4)} сек')
        else:
            label_3.configure(text='Есть ошибка')

    button_1 = tkinter.Button(main_window, text='Проверить',
                              command=check_result, width=12, bg='grey')
    button_1.place(x=150, y=100)

    button_2 = tkinter.Button(main_window, text='Начать заново',
                              command=speed_test, width=12, bg='grey')
    button_2.place(x=300, y=100)

    label_3 = tkinter.Label(main_window, text='', font='times 20')
    label_3.place(x=10, y=300)

    main_window.mainloop()


if __name__ == '__main__':
    speed_test()
