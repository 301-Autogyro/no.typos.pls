'''Файл реализации алгоритма First in, First Out (FIFO) для очереди процессов'''
# Импорт модуля генератора процессов
from queue_generator import QueueGenerator

while True:
    process_count = input('Введите кол-во процессов: ')
    try: 
        process_count = int(process_count)
        break
    except: print('Введите кол-во процессов, как целое число типа int: ')

while True:
    process_max_time = input('Введите максимальное время работы процесса в секундах: ')
    try: 
        process_max_time = float(process_max_time)
        break
    except: print('Введите максимальное время работы процесса в секундах, как число с плавающей запятой типа float (либо целое типа int): ')


genr = QueueGenerator(process_count=process_count, process_max_time=process_max_time) # Создаём объект класса очереди процессов
queue = genr.generate_queue() # Создание очереди процессов

# Визуальный декор 
print('ЭВМ запущено...')
print('Текущая очередь процессов после запуска:')
print(genr.table_creator(queue)) # вывод таблички процессов

# Заранее созданные переменные
proc_bans_fifo = proc_bans_lifo = 0 # Сумма шрафов всех процессов
proc_ban_cnt = 0 # Кол-во шрафов всех процессов

for proc in queue:
    print(f'Исключаем процесс ID {proc["id"]}...')

    # Рассчёт шрафа для процесса из штрафа за приоритет и шрафа за время работы

    # Создаём переменные памяти
    step_id_fifo = step_id_lifo = proc['id'] # ID рассчитываемого процесса
    proc_work_time_fifo = proc_work_time_lifo = 0 # время работы процесса (время процесса + всех процессов до)
    step_count_fifo = step_count_lifo = 1 # кол-во процессов до, включая текущий

    # Рассчёт времени для FIFO
    while queue:
        proc_work_time_fifo += queue[step_id_fifo]['work_time']
        step_id_fifo -= 1
        if step_id_fifo < 0: break
        step_count_fifo += 1

    # Рассчёт времени для LIFO
    while queue:
        proc_work_time_lifo += queue[step_id_lifo]['work_time']
        step_id_lifo += 1
        if step_id_lifo > len(queue)-1: break
        step_count_lifo += 1

    # Расчёт штрафов для алгоритмов
    proc_ban_fifo = (proc['priority']*100)/10 + (100 - ((proc_work_time_fifo*100)/(process_max_time*step_count_fifo)))
    proc_ban_lifo = (proc['priority']*100)/10 + (100 - ((proc_work_time_lifo*100)/(process_max_time*step_count_lifo)))

    # Перевод из 200% систему в 100% систему
    proc_usr_fifo = round((proc_ban_fifo*100)/200, 1)
    proc_usr_lifo = round((proc_ban_lifo*100)/200, 1)
    print(f'Штраф за данный процесс в процентах:\nFIFO - {proc_usr_fifo}%\nLIFO - {proc_usr_lifo}%')
    
    # Счётчики (см. выше)
    proc_bans_fifo += proc_usr_fifo
    proc_bans_lifo += proc_usr_lifo
    proc_ban_cnt += 1

    # Небольшое UI для пошаговости
    cmd = input('')
    if cmd == '': continue
    else:
        print('Завершаю работу терминала...')
        break

print('Общий (усреднённый) штраф алгоритма FIFO: ' + str(round(proc_bans_fifo/proc_ban_cnt, 1)) + '%')
print('Общий (усреднённый) штраф алгоритма LIFO: ' + str(round(proc_bans_lifo/proc_ban_cnt, 1)) + '%')
