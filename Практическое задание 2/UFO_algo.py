'''Файл реализации алгоритма First in, First Out (FIFO) для очереди процессов'''
# Импорт модуля генератора процессов
from queue_generator import QueueGenerator

genr = QueueGenerator() # Создаём объект класса очереди процессов
queue = genr.generate_queue() # Создание очереди процессов

# Визуальный декор 
print('ЭВМ запущено...')
print('Текущая очередь процессов после запуска:')
print(genr.table_creator(queue)) # вывод таблички процессов

# Заранее созданные переменные
proc_bans = 0 # Сумма шрафов всех процессов
proc_ban_cnt = 0 # Кол-во шрафов всех процессов

for proc in queue:
    print(f'Исключаем процесс ID {proc["id"]}...')
    # Рассчёт шрафа для процесса из штрафа за приоритет и шрафа за время работы
    # Детальнее см. ABOUT.md
    proc_ban = (proc['priority']*100)/10 + (100 - (proc['work_time']*100)/60)

    # Перевод из 200% систему в 100% систему
    proc_usr = round((proc_ban*100)/200, 1)
    print(f'Штраф за данный процесс в процентах: {proc_usr}%')
    
    # Счётчики (см. выше)
    proc_bans += proc_usr
    proc_ban_cnt += 1

    # Небольшое UI для пошаговости
    cmd = input('')
    if cmd == '': continue
    else:
        print('Завершаю работу терминала...')
        break

print('Общий (усреднённый) штраф алгоритма FIFO: ' + str(round(proc_bans/proc_ban_cnt, 1)) + '%')