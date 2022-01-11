#прога крестики-нолики
#список функций
#Глобальные константы
X="X"
O="O"
EMPTY=" "
TIE="Ничья"
NUM_SQUARES=9
#display_instruct функция выводит дисплей для игрока
def display_instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
        """Чтобы сделать ход,введи число от 0 до 8. Числа соответствуют полям доски -так, как на рисунке
        0|1|2
        -----
        3|4|5
        -----
        6|7|8 \n"""
    )
#функция ask_yes_no()
def ask_yes_no(question):
    """Задаёт вопрос с ответом "Да" или "Нет"."""
    response=None
    while response not in ('y','n'):
        response=input(question).lower()
    return response
#Функция ask_number() 
# можно ещё шаг задать,но по умолчанию он 1, чтоб задать 
# step=int(input("Введите с каким шагом будет ваш ход или вызывайте функцию без step параметра,чтоб 1?"))
def ask_number(question,low,high,step=1):
    """Просит ввести число из диапазона."""
    response=None
    while response not in range(low,high,step):
        response=int(input(question))
    return response
#функция pieces()
def pieces():
    """Определяет принадлежность первого хода."""
    go_first=ask_yes_no("Хочешь оставить за собой право ходить первым? (y/n):")
    if go_first=="y":
        print("Ну чтож даю тебе фору: играй крестиками.")
        human=X
        computer=O
    else:
        print("Очень зря, так можешь легко проиграть.Буду начинать я")
        human=O
        computer=X
    return computer,human
#функция new_board()
def new_board():
    """Создаёт новую игровую доску, где все 9 элементов равны EMPTY"""
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
#Функция display_board()
def display_board(board):
    """Отображает игровую доску на экране."""
    print('\n\t',board[0],'|',board[1],'|',board[2])
    print('\t','---------')
    print('\n\t',board[3],'|',board[4],'|',board[5])
    print('\t','---------')
    print('\n\t',board[6],'|',board[7],'|',board[8],'\n')
#функция legal_moves()
def legal_moves(board):
    """Создаёт список доступных ходов, перебирает список и составляет новый из тех где пробелы"""
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square]==EMPTY:
            moves.append(square)
    return moves
#функция winner()
def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN=((0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            winner=board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None
#Функция human_move()
def human_move(board,human):
    "Получает ход человека."
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move=ask_number('Твой ход.Выбери одно из полей (0-8):',0,NUM_SQUARES)
        if move not in legal:
            print('\nЭто поле уже занято.Выбери другое.\n')
    print('Ладно...')
    return move
#Функция computer_move()
def computer_move(board, computer, human):
    """Делает ход за компьютерного противника."""
    #Создадим рабочую копию доски, потому что функция будет менять некоторые значения в списке
    board=board[:]
    #Стратегия действий для компьютерного противника: 1)Сделать ход если есть возможность выиграть 2)Если есть ход, после которого противние выиграет, то надо предупредить этот ход 3)Выбор лучшего из доступных ходов
    #Поля от лучшего к худшему
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print('Я выберу поле номер',end=' ')
    for move in legal_moves(board):
        board[move]=computer
        #Если следующим ходом может победить компьютер,выберем этот метод
        if winner(board)==computer:
            print(move)
            return(move)
    #Выполнив проверку, отменим внесённые изменения
        board[move]=EMPTY
#Если дошло до этого места значит комп не может выиграть следующим ходом и переходим к пункту 2
    for move in legal_moves(board):
        board[move]=human
        #Если следующим ходом может победить человек,блокируем этот ход
        if winner(board)==human:
            print(move)
            return(move)
    #Выполнив проверку, отменим внесённые изменения
        board[move]=EMPTY
#Если программа дошла до этого места,значит ниодна из команд не выиграет следующим ходом
        #Выберем лучшее из достойных
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
#Функция next_turn()
def next_turn(turn):
    """Осуществляется переход хода."""
    if turn==X:
        return O
    else:
        return X
#Функция congrat_winner()
def congrat_winner(the_winner,computer,human):
    """Поздравляет победителя игры"""
    if the_winner!=TIE:
        print("Три",the_winner,"в ряд\n")
    else:
        print("Ничья!\n")
    if the_winner==computer:
        print("Победа за мной\n")
    elif the_winner==human:
        print('Ты выиграл,но это не значит что ты умней!')
    elif the_winner==TIE:
        print("Дружеская ничья")
#Функция main()
def main():
    display_instruct()
    computer,human=pieces()
    turn=X
    board=new_board()
    display_board(board)
    while not winner(board):
        if turn==human:
            move=human_move(board,human)
            board[move]=human
        else:
            print("сейчас ход противника")
            move=computer_move(board,computer,human)
            board[move]=computer
        display_board(board)
        turn=next_turn(turn)
    the_winner=winner(board)
    congrat_winner(the_winner,computer,human)
    #запуск программы
main()






input("\n\nНажмите Enter, чтобы выйти")
