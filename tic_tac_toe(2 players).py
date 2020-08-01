#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def call_clear():
    from IPython.display import clear_output
    clear_output()


# In[ ]:


def print_tic():
    print("\t"+'|'+"\t"+'|'+"\t")
    print('   '+t[7]+'    '+'|'+'   '+t[8]+'   '+'|'+'   '+t[9])
    print("\t"+'|'+"\t"+'|'+"\t")
    print('-------------------------')
    print("\t"+'|'+"\t"+'|'+"\t")
    print('   '+t[4]+'    '+'|'+'   '+t[5]+'   '+'|'+'   '+t[6])
    print("\t"+'|'+"\t"+'|'+"\t")
    print('-------------------------')
    print("\t"+'|'+"\t"+'|'+"\t")
    print('   '+t[1]+'    '+'|'+'   '+t[2]+'   '+'|'+'   '+t[3])
    print("\t"+'|'+"\t"+'|'+"\t")


# In[ ]:


def choose_mark():
    choice='WRONG'
    acceptable_range=['X','O','x','o']
    while choice not in acceptable_range:
        choice= input('Please choose your mark("X" or "O") for Player 1:')
        if choice not in acceptable_range:
            print('The entered value is unacceptable. please choose either X or O')
            
        else:
            pass
    global player1_mark
    global player2_mark
    player1_mark=choice.upper() 
    if player1_mark=='X':
        
        player2_mark='O'
    else:
        player2_mark='X'
    print(f'player 1 mark: {player1_mark}, player 2 mark: {player2_mark}')
    return (player1_mark,player2_mark)


# In[ ]:


def place_marker(pos1,player):
    if player==1:
        t[pos1]=player1_mark
    else:
        t[pos1]=player2_mark
    print_tic()


# In[ ]:


def win_condition():
    if t[1]=='X' and t[2]=='X' and t[3]=='X':
        return True
    elif t[4]=='X' and t[5]=='X' and t[6]=='X':
        return True
    elif t[7]=='X' and t[8]=='X' and t[9]=='X':
        return True
    elif t[1]=='O' and t[2]=='O' and t[3]=='O':
        return True
    elif t[4]=='O' and t[5]=='O' and t[6]=='O':
        return True
    elif t[7]=='O' and t[8]=='O' and t[9]=='O':
        return True
    elif t[1]=='X' and t[4]=='X' and t[7]=='X':
        return True
    elif t[2]=='X' and t[5]=='X' and t[8]=='X':
        return True
    elif t[3]=='X' and t[6]=='X' and t[9]=='X':
        return True
    elif t[1]=='O' and t[4]=='O' and t[7]=='O':
        return True
    elif t[2]=='O' and t[5]=='O' and t[8]=='O':
        return True
    elif t[3]=='O' and t[6]=='O' and t[9]=='O':
        return True
    elif t[7]=='X' and t[5]=='X' and t[3]=='X':
        return True
    elif t[1]=='X' and t[5]=='X' and t[9]=='X':
        return True
    elif t[7]=='O' and t[5]=='O' and t[3]=='O':
        return True
    elif t[1]=='O' and t[5]=='O' and t[9]=='O':
        return True
    else:
        return False


# In[ ]:


def entry_value():
    global playerno
    result= False
    pos=0
    i=1
    while result==False:
        acceptable_range=[1,2,3,4,5,6,7,8,9]
        sol=['X','O']
        pos='WRONG'
        if i%2==0:
            playerno=2
            while pos not in acceptable_range:
                pos= input(f'Player {playerno} enter your mark {player2_mark} at postion(1-9): ')
                pos=int(pos)
                if pos not in acceptable_range:
                    print('Player 2 please enter the numerical value from 1-9 as your mark position.')
                elif t[pos] in sol:
                    print('A mark already exists at this position. Please choose other position.')
                elif pos==0:
                    break
                else:
                    pass
            
            i+=1
            place_marker(pos,playerno)
            result=win_condition()
        else:
            playerno=1
            while pos not in acceptable_range:
                pos= input(f'Player {playerno} enter your mark {player1_mark} at postion(1-9): ')
                pos=int(pos)
                if pos not in acceptable_range:
                    print('Player 1 please enter the numerical value from 1-9 as your mark position.')
                elif t[pos] in sol:
                    print('A mark already exists at this position. Please choose other position.')
                else:
                    pass
            
            i+=1
            place_marker(pos,playerno)
            result=win_condition()
    print(f'congratultion! {playerno}, you won.')
    
    
   


# In[ ]:


global t
t=['X',' ',' ',' ',' ',' ',' ',' ',' ',' ']

call_clear()

choose_mark()

entry_value()


# 
