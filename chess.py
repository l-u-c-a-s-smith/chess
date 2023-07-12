# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:07:21 2023

@author: Lucas
"""
print('chess game :) ')
print('to get setarted, input "play()" !!!!')

#contructing blank board

dict={}
for i in ['a','b','c','d','e','f','g','h']:
    #for j in range(8):
    dict[i]={'1':'_','2':'_','3':'_','4':'_','5':'_','6':'_','7':'_','8':'_'}

board = dict

def board_setter():
    
    #capital name peices
    board['a']['1'] = 'R'
    board['h']['1'] = 'R'
    board['b']['1'] = 'H'
    board['g']['1'] = 'H'
    board['c']['1'] = 'B'
    board['f']['1'] = 'B'
    board['d']['1'] = 'Q'
    board['e']['1'] = 'K'
    
    #capital pawns
    board['a']['2'] = 'P'
    board['h']['2'] = 'P'
    board['b']['2'] = 'P'
    board['g']['2'] = 'P'
    board['c']['2'] = 'P'
    board['f']['2'] = 'P'
    board['d']['2'] = 'P'
    board['e']['2'] = 'P'
    
    #lowercase name peices
    board['a']['8'] = 'r'
    board['h']['8'] = 'r'
    board['b']['8'] = 'h'
    board['g']['8'] = 'h'
    board['c']['8'] = 'b'
    board['f']['8'] = 'b'
    board['d']['8'] = 'k'
    board['e']['8'] = 'q'

    #lowercase pwns
    board['a']['7'] = 'p'
    board['h']['7'] = 'p'
    board['b']['7'] = 'p'
    board['g']['7'] = 'p'
    board['c']['7'] = 'p'
    board['f']['7'] = 'p'
    board['d']['7'] = 'p'
    board['e']['7'] = 'p'
    
    return board
board_setter()
    

def play():
    print('Your are playing now :) capitals go first.')
    
    game_cont = True
    
    while game_cont:
        input1 = int(input('input "1" for a regular move or "2" for special: '))
        
        if input1 == 1:
            letter1 = input('what is your initial file/horizontal/letter? ')
            number1 = input('what is your initial rank/vertical/number? ')
            letter2 = input('what is your final file/horizontal/letter? ')
            number2 = input('what is your final rank/vertical/number? ')
        

            print(f"{board.get(letter1,{}).get(number1)} to {letter2 + number2}")
            
            #oppertunity to check case here so that peices cannot take same colour
            
            if board.get(letter1,{}).get(number1) != '_':
                print(f"{board.get(letter1,{}).get(number1)} takes {board.get(letter2,{}).get(number2)}!!!!!")
                
            board[letter2][number2] = board[letter1][number1]
            board[letter1][letter2] = '_'
        if input1 == 2:
            input2 = int(input('enter "1" to resest the board, enter "2" to exit the game, enter "3" for manual square edit: '))
            
            if input2 == 1:
                
                board_setter()
            if input2 == 2:
                game_cont = False
            if input2 == 3:
                a = 0
                while a == 0:
                    manual_let = input('file/horizontal/letter of changed square? ')
                    manual_num = input('rank/vertical/number of changed square? ')
                    maunual_pc = input('what piece are you changing this square to? "_" for an empty square: ')
                    
                    board[manual_let][manual_num] = maunual_pc
                    
                    y_n = input('are there more manual square edits? y/n: ')
                    
                    if y_n == 'n':
                     a = 1
                    
                    
        
                
        
            