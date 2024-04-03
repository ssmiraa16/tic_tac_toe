import sys
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import *
from random import random, randint

sys.setrecursionlimit(1000)


root = Tk()
root.title('Крестики-Нолики. Игрок vs Bot')


player_turn = 1
counter = 1
player_list = []        
ai_list = []            
player_letter = ' '
ai_letter = ' '

button1 = Button(root, text=' ', command=lambda: button_click(1))
button1.grid(row=0, column=0, sticky='snew', ipadx=80, ipady=80)

button2 = Button(root, text=' ', command=lambda: button_click(2))
button2.grid(row=0, column=1, sticky='snew', ipadx=80, ipady=80)

button3 = Button(root, text=' ', command=lambda: button_click(3))
button3.grid(row=0, column=2, sticky='snew', ipadx=80, ipady=80)

button4 = Button(root, text=' ', command=lambda: button_click(4))
button4.grid(row=1, column=0, sticky='snew', ipadx=80, ipady=80)

button5 = Button(root, text=' ', command=lambda: button_click(5))
button5.grid(row=1, column=1, sticky='snew', ipadx=80, ipady=80)

button6 = Button(root, text=' ', command=lambda: button_click(6))
button6.grid(row=1, column=2, sticky='snew', ipadx=80, ipady=80)

button7 = Button(root, text=' ', command=lambda: button_click(7))
button7.grid(row=2, column=0, sticky='snew', ipadx=80, ipady=80)

button8 = Button(root, text=' ', command=lambda: button_click(8))
button8.grid(row=2, column=1, sticky='snew', ipadx=80, ipady=80)

button9 = Button(root, text=' ', command=lambda: button_click(9))
button9.grid(row=2, column=2, sticky='snew', ipadx=80, ipady=80)



def player_goes_first():
    # random() 1 / 0
    random_value = random()

    # True - ПЕРВЫМ ХОДИТ ИГРОК
    if random_value > 0.5:
        return True
    return False



def select_letter():
    global player_letter
    global ai_letter

    choice = askyesno("БОЛЬШИНСТВО ПРЕДПОЧИТАЮТ КРЕСТИК...", message="ТВОЙ ВЫБОР - X ?")
    print(choice)

    if choice == True:  # ИГРОК - Х
        player_letter = 'X'
        ai_letter = 'O'
    else:
        player_letter = 'O'
        ai_letter = 'X'



def button_click(id):
    global player_turn
    global player_letter
    global counter

    if player_turn == 1:
        set_board(id, player_letter, 'lightblue')
        player_list.append(id)
        check_winner()
        check_draw()
        player_turn = 0
        counter += 1
        print("СПИСОК ИГРОКА: {}".format(player_list))
    ai_turn()



def ai_turn():
    global ai_letter
    global player_turn
    global counter

    played = False   
    valid = False
    counter += 1
    while not valid:
        if not played:
            # ВЫИГРЫШНЫЕ СЛУЧАИ

            # СТРОКИ
            if (1 in ai_list) and (2 in ai_list) and (3 not in player_list):
                if 3 not in ai_list:
                    set_board(3, ai_letter, 'red')
                    ai_list.append(3)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 in ai_list) and (2 not in player_list) and (3 in ai_list):
                if 2 not in ai_list:
                    set_board(2, ai_letter, 'red')
                    ai_list.append(2)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 not in player_list) and (2 in ai_list) and (3 in ai_list):
                if 1 not in ai_list:
                    set_board(1, ai_letter, 'red')
                    ai_list.append(1)
                    player_turn = 1
                    valid = True
                    played = True

            elif (4 in ai_list) and (5 in ai_list) and (6 not in player_list):
                if 6 not in ai_list:
                    set_board(6, ai_letter, 'red')
                    ai_list.append(6)
                    player_turn = 1
                    valid = True
                    played = True
            elif (4 in ai_list) and (5 not in player_list) and (6 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'red')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (4 not in player_list) and (5 in ai_list) and (6 in ai_list):
                if 4 not in ai_list:
                    set_board(4, ai_letter, 'red')
                    ai_list.append(4)
                    player_turn = 1
                    valid = True
                    played = True

            elif (7 in ai_list) and (8 in ai_list) and (9 not in player_list):
                if 9 not in ai_list:
                    set_board(9, ai_letter, 'red')
                    ai_list.append(9)
                    player_turn = 1
                    valid = True
                    played = True
            elif (7 in ai_list) and (8 not in player_list) and (9 in ai_list):
                if 8 not in ai_list:
                    set_board(8, ai_letter, 'red')
                    ai_list.append(8)
                    player_turn = 1
                    valid = True
                    played = True
            elif (7 not in player_list) and (8 in ai_list) and (9 in ai_list):
                if 7 not in ai_list:
                    set_board(7, ai_letter, 'red')
                    ai_list.append(7)
                    player_turn = 1
                    valid = True
                    played = True


            # СТОЛБЦЫ
            elif (1 in ai_list) and (4 in ai_list) and (7 not in player_list):
                if 7 not in ai_list:
                    set_board(7, ai_letter, 'red')
                    ai_list.append(7)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 in ai_list) and (4 not in player_list) and (7 in ai_list):
                if 4 not in ai_list:
                    set_board(4, ai_letter, 'red')
                    ai_list.append(4)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 not in player_list) and (4 in ai_list) and (7 in ai_list):
                if 1 not in ai_list:
                    set_board(1, ai_letter, 'red')
                    ai_list.append(1)
                    player_turn = 1
                    valid = True
                    played = True

            elif (2 in ai_list) and (5 in ai_list) and (8 not in player_list):
                if 8 not in ai_list:
                    set_board(8, ai_letter, 'red')
                    ai_list.append(8)
                    player_turn = 1
                    valid = True
                    played = True
            elif (2 in ai_list) and (5 not in player_list) and (8 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'red')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (2 not in player_list) and (5 in ai_list) and (8 in ai_list):
                if 2 not in ai_list:
                    set_board(2, ai_letter, 'red')
                    ai_list.append(2)
                    player_turn = 1
                    valid = True
                    played = True

            elif (3 in ai_list) and (6 in ai_list) and (9 not in player_list):
                if 9 not in ai_list:
                    set_board(9, ai_letter, 'red')
                    ai_list.append(9)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 in ai_list) and (6 not in player_list) and (9 in ai_list):
                if 6 not in ai_list:
                    set_board(6, ai_letter, 'red')
                    ai_list.append(6)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 not in player_list) and (6 in ai_list) and (9 in ai_list):
                if 3 not in ai_list:
                    set_board(3, ai_letter, 'red')
                    ai_list.append(3)
                    player_turn = 1
                    valid = True
                    played = True


            # ДИАГОНАЛИ
            elif (1 in ai_list) and (5 in ai_list) and (9 not in player_list):
                if 9 not in ai_list:
                    set_board(9, ai_letter, 'red')
                    ai_list.append(9)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 in ai_list) and (5 not in player_list) and (9 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'red')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 not in player_list) and (5 in ai_list) and (9 in ai_list):
                if 1 not in ai_list:
                    set_board(1, ai_letter, 'red')
                    ai_list.append(1)
                    player_turn = 1
                    valid = True
                    played = True

            elif (3 in ai_list) and (5 in ai_list) and (7 not in player_list):
                if 7 not in ai_list:
                    set_board(7, ai_letter, 'red')
                    ai_list.append(7)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 in ai_list) and (5 not in player_list) and (7 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'red')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 not in player_list) and (5 in ai_list) and (7 in ai_list):
                if 3 not in ai_list:
                    set_board(3, ai_letter, 'red')
                    ai_list.append(3)
                    player_turn = 1
                    valid = True
                    played = True
            else:

                # БЛОКИРОВАНИЕ ВЫИГРЫША ИГРОКА
                # СТРОКИ
                if (1 not in ai_list) and (2 in player_list) and (3 in player_list):
                    if 1 not in player_list:
                        set_board(1, ai_letter, 'red')
                        ai_list.append(1)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (2 not in ai_list) and (3 in player_list):
                    if 2 not in player_list:
                        set_board(2, ai_letter, 'red')
                        ai_list.append(2)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (2 in player_list) and (3 not in ai_list):
                    if 3 not in player_list:
                        set_board(3, ai_letter, 'red')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True

                elif (4 not in ai_list) and (5 in player_list) and (6 in player_list):
                    if 4 not in player_list:
                        set_board(4, ai_letter, 'red')
                        ai_list.append(4)
                        player_turn = 1
                        valid = True
                        played = True
                elif (4 in player_list) and (5 not in ai_list) and (6 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'red')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (4 in player_list) and (5 in player_list) and (6 not in ai_list):
                    if 6 not in player_list:
                        set_board(3, ai_letter, 'orange')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True

                elif (7 not in ai_list) and (8 in player_list) and (9 in player_list):
                    if 7 not in player_list:
                        set_board(7, ai_letter, 'red')
                        ai_list.append(7)
                        player_turn = 1
                        valid = True
                        played = True
                elif (7 in player_list) and (8 not in ai_list) and (9 in player_list):
                    if 8 not in player_list:
                        set_board(8, ai_letter, 'red')
                        ai_list.append(8)
                        player_turn = 1
                        valid = True
                        played = True
                elif (7 in player_list) and (8 in player_list) and (9 not in ai_list):
                    if 9 not in player_list:
                        set_board(9, ai_letter, 'red')
                        ai_list.append(9)
                        player_turn = 1
                        valid = True
                        played = True



                elif (1 not in ai_list) and (4 in player_list) and (7 in player_list):
                    if 1 not in player_list:
                        set_board(1, ai_letter, 'red')
                        ai_list.append(1)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (4 not in ai_list) and (7 in player_list):
                    if 4 not in player_list:
                        set_board(4, ai_letter, 'red')
                        ai_list.append(4)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (4 in player_list) and (7 not in ai_list):
                    if 7 not in player_list:
                        set_board(7, ai_letter, 'red')
                        ai_list.append(7)
                        player_turn = 1
                        valid = True
                        played = True

                elif (2 not in ai_list) and (5 in player_list) and (8 in player_list):
                    if 2 not in player_list:
                        set_board(2, ai_letter, 'red')
                        ai_list.append(2)
                        player_turn = 1
                        valid = True
                        played = True
                elif (2 in player_list) and (5 not in ai_list) and (8 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'red')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (2 in player_list) and (5 in player_list) and (8 not in ai_list):
                    if 8 not in player_list:
                        set_board(8, ai_letter, 'orange')
                        ai_list.append(8)
                        player_turn = 1
                        valid = True
                        played = True

                elif (3 not in ai_list) and (6 in player_list) and (9 in player_list):
                    if 3 not in player_list:
                        set_board(3, ai_letter, 'red')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (6 not in ai_list) and (9 in player_list):
                    if 6 not in player_list:
                        set_board(6, ai_letter, 'red')
                        ai_list.append(6)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (6 in player_list) and (9 not in ai_list):
                    if 9 not in player_list:
                        set_board(9, ai_letter, 'red')
                        ai_list.append(9)
                        player_turn = 1
                        valid = True
                        played = True



                elif (1 not in ai_list) and (5 in player_list) and (9 in player_list):
                    if 1 not in player_list:
                        set_board(1, ai_letter, 'red')
                        ai_list.append(1)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (5 not in ai_list) and (9 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'red')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (5 in player_list) and (9 not in ai_list):
                    if 9 not in player_list:
                        set_board(9, ai_letter, 'red')
                        ai_list.append(9)
                        player_turn = 1
                        valid = True
                        played = True

                elif (3 not in ai_list) and (5 in player_list) and (7 in player_list):
                    if 3 not in player_list:
                        set_board(3, ai_letter, 'red')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (5 not in ai_list) and (7 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'red')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (5 in player_list) and (7 not in ai_list):
                    if 7 not in player_list:
                        set_board(7, ai_letter, 'red')
                        ai_list.append(7)
                        player_turn = 1
                        valid = True
                        played = True

        check_winner()
        check_draw()

        if not played:
            ai_answer = randint(1, 9)
            if (ai_answer not in player_list) and (ai_answer not in ai_list):
                set_board(ai_answer, ai_letter, 'red')
                ai_list.append(ai_answer)
                player_turn = 1
                check_winner()
                check_draw()
                print("СПИСОК ПОЗИЦИЙ Bot: {}".format(ai_list))
                return



def set_board(id, letter, color):


    if id == 1:
        button1.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 2:
        button2.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 3:
        button3.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 4:
        button4.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 5:
        button5.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 6:
        button6.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 7:
        button7.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 8:
        button8.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 9:
        button9.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)


def check_winner():
    player_won = False
    ai_won = False

    if (1 in player_list) and (2 in player_list) and (3 in player_list):
        player_won = True
    if (1 in ai_list) and (2 in ai_list) and (3 in ai_list):
        ai_won = True

    if (4 in player_list) and (5 in player_list) and (6 in player_list):
        player_won = True
    if (4 in ai_list) and (5 in ai_list) and (6 in ai_list):
        ai_won = True

    if (7 in player_list) and (8 in player_list) and (9 in player_list):
        player_won = True
    if (7 in ai_list) and (8 in ai_list) and (9 in ai_list):
        ai_won = True

    if (1 in player_list) and (4 in player_list) and (7 in player_list):
        player_won = True
    if (1 in ai_list) and (4 in ai_list) and (7 in ai_list):
        ai_won = True

    if (2 in player_list) and (5 in player_list) and (8 in player_list):
        player_won = True
    if (2 in ai_list) and (5 in ai_list) and (8 in ai_list):
        ai_won = True

    if (3 in player_list) and (6 in player_list) and (9 in player_list):
        player_won = True
    if (3 in ai_list) and (6 in ai_list) and (9 in ai_list):
        ai_won = True

    if (1 in player_list) and (5 in player_list) and (9 in player_list):
        player_won = True
    if (1 in ai_list) and (5 in ai_list) and (9 in ai_list):
        ai_won = True

    if (3 in player_list) and (5 in player_list) and (7 in player_list):
        player_won = True
    if (3 in ai_list) and (5 in ai_list) and (7 in ai_list):
        ai_won = True

    if player_won:
        messagebox.showinfo(title="ПОЗДРАВЛЯЮ, ТЫ ПОБЕДИЛ !", message="ТЫ ПОБЕДИЛ", commad=root.quit())
    elif ai_won:
        messagebox.showinfo(title="ПОВЕЗЕТ В ДРУГОЙ РАЗ..", message="Bot ПОБЕДИЛ", command=root.quit())



def check_draw():
    global counter


    if counter == 10:
        messagebox.showinfo(title="НИЧЬЯ", message="ИГРА ЗАВЕРШИЛАСЬ НИЧЬЕЙ", command=root.quit())



def main():
    select_letter()
    if player_goes_first():
        messagebox.showinfo(title="ПЕРВЫМ ХОДИТ, СЛУЧАЙНО ВЫБРАННЫЙ ИГРОК!",
                            message="ТЫ ХОДИШЬ ПЕРВЫМ")
    else:
        messagebox.showinfo(title="ПЕРВЫМ ХОДИТ, СЛУЧАЙНО ВЫБРАННЫЙ ИГРОК!", message="Bot ХОДИТ ПЕРВЫМ, ТВОЙ ХОД СЛЕДУЮЩИЙ")
        ai_turn()


main()
root.mainloop()
