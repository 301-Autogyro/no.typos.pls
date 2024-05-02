# -*- coding: utf-8 -*-
import leksem
from prettytable import PrettyTable

f = open('C:\\code\\no.typos.pls\\Лабораторная работа 1\\programm.txt', 'r', encoding='utf-8')

lks = []
str_num = 0
eyes = 0

while True:
    code_line = f.readline()
    str_num += 1
    if not code_line: break
    code_line += ' '

    akkum = ''
    akkum_of_error = 0
    for symb in code_line:
        if symb in leksem.kills:

            if akkum_of_error:
                if len(lks) > 0 and lks[len(lks)-1][0] == '=':
                    akkum = akkum.replace(' ', '')
                    num_type = 'Целочисленная константа'
                    for num in akkum:
                        if num not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if num != '.':
                                print(f'Ошибка в строке {str_num}')
                                exit()
                            else: num_type = 'Вещественная константа'
                    lks.append([akkum, num_type, akkum])
                    akkum_of_error = 0
                    akkum = ''

                if len(lks) > 0 and lks[len(lks)-1][0] == '==':
                    akkum = akkum.replace(' ', '', 1)
                    if akkum.startswith("'") and akkum.endswith("'"):
                        lks.append([akkum, 'Строковая константа', akkum])
                        akkum_of_error = 0
                        akkum = ''
                    else:
                        num_type = 'Целочисленная константа'
                        for num in akkum:
                            if num not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                if num != '.':
                                    print(f'Ошибка в строке {str_num}')
                                    exit()
                                else: num_type = 'Вещественная константа'
                        lks.append([akkum, num_type, akkum])
                        akkum_of_error = 0
                        akkum = ''
                
                if eyes and akkum[len(akkum)-1] == '👀':
                    lks.append([akkum.replace('👀', ''), 'Текст комментария', 'K☭☭'])
                    akkum = ''
                    eyes = akkum_of_error = 0

                try:  
                    if leksem.leks[akkum[len(akkum)-1]][1] in leksem.before:
                        if akkum[0] == ' ': akkum = akkum.replace(' ', '', 1)
                        for kill in leksem.kills:
                            if kill in akkum:
                                akkum = akkum.split(kill)
                                break
                        lks.append([akkum[0], 'Переменная', akkum[0]])
                        lks.append([akkum[1], leksem.leks[akkum[1]][0], leksem.leks[akkum[1]][1]])
                        akkum = ''
                        akkum_of_error = 0
                except: pass
            
            akkum = akkum.replace(' ', '', 1)
            if akkum in leksem.leks.keys():
                lks.append([akkum, leksem.leks[akkum][0], leksem.leks[akkum][1]])
                if akkum == '👀':
                    eyes = 1
                akkum = ''

            else:
                akkum_of_error = 1

        akkum += symb

# --- #

leksems = []
i = 0
lks_ids = []
for olek in lks:
    if olek[2] not in lks_ids:
        leksems.append(olek)

    lks_ids.append(olek[2])

    i+= 1

head = ['Лексема', 'Тип лексемы', 'Значение']
table = PrettyTable(head)
for row in leksems:
    table.add_row(row)
print(table)