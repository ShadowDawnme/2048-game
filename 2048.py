import random
import copy

screen_format = '''
 ___________________________
|      |      |      |      |
| {0:4} | {1:4} | {2:4} | {3:4} |
|      |      |      |      |
|------|------|------|------|
|      |      |      |      |
| {4:4} | {5:4} | {6:4} | {7:4} |
|      |      |      |      |
|------|------|------|------|
|      |      |      |      |
| {8:4} | {9:4} | {10:4} | {11:4} |
|      |      |      |      |
|------|------|------|------|
|      |      |      |      |
| {12:4} | {13:4} | {14:4} | {15:4} |
|______|______|______|______|
'''
# for testing
record = [[0,2,0,0],\
          [2,0,2,0],\
          [0,0,0,2],\
          [0,0,0,0]]

title ='''

=============================

.---------------------------.
|                           |
|         ZETNIEN           |
|      --------------       |
|                           |
|       It is a game        |
|      so called 2048.      |
|                           |
|     /\/\/\/\/\/\/\/\      |
|                           |
|                           |
'---------------------------'

|| Best score: {0}
|| Trial: {1}

=============================
'''


def GetPlayerInfo(): # content: [best score, trial]
    f = open('2048PlayerInfo.txt','r')
    content = f.read().splitlines()
    f.close()
    for i in content:
        content[content.index(i)] = int((i.split())[1])
    return content


def WriteInfo(inli):  # inli-playrt information list
    f = open('2048PlayerInfo.txt','w')
    f.write('BestScore {0}\nTrail {1}'. format (inli[0], inli[1]))
    f.close()

    
def combine_r(re): # r-right, re-record, li-list
    for li in re:
        if (li[3] == li[0]) and (li[1] == li[2] == ''):
            li[0] = ''
            li[3] *= 2
        elif (li[3] == li[2]) and (li[2] != ''):
            li[2] = ''
            li[3] *= 2
            if (li[1] == li[0]) and (li[1] != ''):
                li[0] = ''
                li[1] *= 2
        elif (li[3] == li[1]) and (li[2] == ''):
            li[1] = ''
            li[3] *= 2
        elif (li[2] == li[1]) and (li[1] != ''):
            li[1] = ''
            li[2] *= 2
        elif (li[2] == li[0]) and (li[1] == ''):
            li[0] = ''
            li[2] *= 2
        elif (li[1] == li[0]) and (li[0] != ''):
            li[0] = ''
            li[1] *= 2
    return re


def combine_l(re): # l-left, re-record, li-list
    for li in re:
        if (li[3] == li[0]) and (li[1] == li[2] == ''):
            li[3] = ''
            li[0] *= 2
        elif (li[1] == li[0]) and (li[1] != ''):
            li[1] = ''
            li[0] *= 2
            if (li[3] == li[2]) and (li[2] != ''):
                li[3] = ''
                li[2] *= 2
        elif (li[2] == li[0]) and (li[1] == ''):
            li[2] = ''
            li[0] *= 2
        elif (li[2] == li[1]) and (li[1] != ''):
            li[2] = ''
            li[1] *= 2
        elif (li[3] == li[1]) and (li[2] == ''):
            li[3] = ''
            li[1] *= 2
        elif (li[3] == li[2]) and (li[2] != ''):
            li[3] = ''
            li[2] *= 2
    return re


def combine_d(re): # d-down, re-record, li-list
    for a in range(0,4):
        if (re[3][a] == re[0][a]) and (re[1][a] == re[2][a] == ''):
            re[0][a] = ''
            re[3][a] *= 2
        elif (re[3][a] == re[2][a]) and (re[2][a] != ''):
            re[2][a] = ''
            re[3][a] *= 2
            if (re[1][a] == re[0][a]) and (re[1][a] != ''):
                re[0][a] = ''
                re[1][a] *= 2
        elif (re[3][a] == re[1][a]) and (re[2][a] == ''):
            re[1][a] = ''
            re[3][a] *= 2
        elif (re[2][a] == re[1][a]) and (re[1][a] != ''):
            re[1][a] = ''
            re[2][a] *= 2
        elif (re[2][a] == re[0][a]) and (re[1][a] == ''):
            re[0][a] = ''
            re[2][a] *= 2
        elif (re[1][a] == re[0][a]) and (re[0][a] != ''):
            re[0][a] = ''
            re[1][a] *= 2
    return re


def combine_u(re): # u-up, re-record, li-list
    for a in range(0,4):
        if (re[3][a] == re[0][a]) and (re[1][a] == re[2][a] == ''):
            re[3][a] = ''
            re[0][a] *= 2
        elif (re[1][a] == re[0][a]) and (re[1][a] != ''):
            re[1][a] = ''
            re[0][a] *= 2
            if (re[3][a] == re[2][a]) and (re[2][a] != ''):
                re[3][a] = ''
                re[2][a] *= 2
        elif (re[2][a] == re[0][a]) and (re[1][a] == ''):
            re[2][a] = ''
            re[0][a] *= 2
        elif (re[2][a] == re[1][a]) and (re[1][a] != ''):
            re[2][a] = ''
            re[1][a] *= 2
        elif (re[3][a] == re[1][a]) and (re[2][a] == ''):
            re[3][a] = ''
            re[1][a] *= 2
        elif (re[3][a] == re[2][a]) and (re[2][a] != ''):
            re[3][a] = ''
            re[2][a] *= 2
    return re


def replace(a, b):
    c = a
    a = b
    b = c
    return a, b


def move_r(re):  # r-right, re-record, li-list
    for li in re:
        for num in range(0,3):
            for i in range(-3,0):
                if (li[-i] == '') and (li[-(i+1)] != ''):
                    li[-i], li[-(i+1)] = replace(li[-i], li[-(i+1)])
    return re


def move_l(re):  # l-left, re-record, li-list
    for li in re:
        for num in range(0,3):
            for i in range(0,3):
                if (li[i] == '') and (li[i+1] != ''):
                    li[i], li[i+1] = replace(li[i], li[i+1])
    return re


def move_d(re):  # d-down, re-record, li-list
    for a in range(0,4):
        for num in range(0,3):
            for i in range(-3,0):
                if (re[-i][a] == '') and (re[-(i+1)][a] != ''):
                    re[-i][a], re[-(i+1)][a] = replace(re[-i][a], re[-(i+1)][a])
    return re


def move_u(re):  # u-up, re-record, li-list
    for a in range(0,4):
        for num in range(0,3):
            for i in range(0,3):
                if (re[i][a] == '') and (re[i+1][a] != ''):
                    re[i][a], re[i+1][a] = replace(re[i][a], re[i+1][a])
    return re


def init():
    origin_record = [['','','',''],\
          ['','','',''],\
          ['','','',''],\
          ['','','','']]
    a = random.randint(0,3)
    b = random.randint(0,3)
    
    c = random.randint(0,3)
    while c == a:
        c = random.randint(0,3)
        
    d = random.randint(0,3)
    while d == b:
        d = random.randint(0,3)    # to ensure (a,b) != (c,d)
        
    #print(a,b,c,d)
    origin_record[a][b] = 2
    origin_record[c][d] = 2
    
    return origin_record


def show_record(re, screen_format, step, sc):
    print(f'\n\n\n|| Total step: {step}')
    if sum(sc[:2]) > sc[2]:
        sc[2] = sum(sc[:2])
    print(f'|| Scores: {sc[0]} + {sc[1]} = {sum(sc[:2])} / {sc[2]}')
    #re2 = re.copy()
    '''
    for a in re:
        for b in a:
            if b != '':
                re[re.index(a)][a.index(b)] = f' {re[re.index(a)][a.index(b)]}  '
    '''
               
    #print(re2)
    print(screen_format. format (re[0][0],re[0][1],re[0][2],re[0][3],\
                                 re[1][0],re[1][1],re[1][2],re[1][3],\
                                 re[2][0],re[2][1],re[2][2],re[2][3],\
                                 re[3][0],re[3][1],re[3][2],re[3][3]))
    return


def win_judgement(re, screen_format):
    vacancy = 0
    for a in re:
        for b in a:
            if b == '':
                vacancy += 1
            else:
                if b == 2048:  # winning target ########################
                    print('\n * Congruatulations!')
                    return True
    if vacancy == 0:
        if JudegeNoCombination(re) == True: 
            print('\n * Game over!')
            return True
        else:
            return False
    else:
        return False


def JudegeNoCombination(re):  
    for a in range(0,4):
        for b in range(0,3):
            if re[b][a] == re[b+1][a]:  
                return False
    for a in range(0,4):
        for b in range(0,3):
            if re[a][b] == re[a][b+1]: 
                return False
    return True

   
def AddNumber(re):
    new_num = 2
    a = random.randint(0,3)
    b = random.randint(0,3)
    while re[a][b] != '':
        a = random.randint(0,3)
        b = random.randint(0,3)
    c = random.randint(0,9)
    if c == 9:
        new_num = 4
    re[a][b] = new_num
    return re


def CountScore(re, re2):  # sc-score[0]
    sc = 0
    no_sc = []
    li1 = list()
    li2 = list()
    for a in re:
        for b in a:
            li1.append(b)
    #print(li1)
    for c in re2:
        for d in c:
            li2.append(d)
    #print(li2)
    for i in li1:
        if i != '':
            if (i in li1) and (i in li2):
                no_sc.append(i)
                li2.remove(i)
    for i in no_sc:
            li1.remove(i)
    for num in li1:
        if num != '':
            sc += num
    return sc
            



    
def main(screen_format, title):
    info_list = GetPlayerInfo()
    print(title. format (info_list[0], info_list[1]))
    awsl = input("=== Press 'enter' to start ===")
    info_list[1] += 1  # trial + 1
    record = init()
    record2 = copy.deepcopy(record)
    #for i in record:
    #    print(i)
    step = 0
    score = [0,0,info_list[0]] 
    
    instruction_list = ['w','s','a','d','end']

    show_record(record, screen_format, step, score)  
    
    ins = input('|| Instruction: ')  
    
    while ins not in instruction_list:
        print("* Please enter 'w', 's', 'a', 'd' or 'end'.")
        ins = input('\n|| Instruction: ')
        
    while ins != 'end':   
        if ins == 'w':
            record = move_u(combine_u(record))
        elif ins == 's':
            record = move_d(combine_d(record))
        elif ins == 'a':
            record = move_l(combine_l(record))
        elif ins == 'd':
            record = move_r(combine_r(record))
            
        if record != record2:  
            score[1] = CountScore(record, record2)
            #print(score[1])
            record = AddNumber(record)  
            record2 = copy.deepcopy(record)
            step += 1
            
        show_record(record, screen_format, step, score)
        
        score[0] = sum(score[:2])
        info_list[0] = score[2]
        WriteInfo(info_list) 
            
        if win_judgement(record, screen_format) == True:
            print('\n * Press enter to restart or enter \'end\' to quit the game.')
            ins = input('\n|| Instruction: ')
            if ins == 'end':
                break  # quit game
            else:
                print('=============================\n * Game restart.\n')
                print('########### Program not finished yet ###########')
                #main(screen_format, title)  # restart
                break 
        else:
            ins = input('|| Instruction: ')  
            while ins not in instruction_list:
                print("* Please enter 'w', 's', 'a', 'd' or 'end'.")
                ins = input('\n|| Instruction: ')
                

   
    print('\n * Don\'t give up if you loose!\n')
    
main(screen_format, title)

'''
# for testing
m = move_r(combine_r(record))
for i in m:
    print(i)
'''
