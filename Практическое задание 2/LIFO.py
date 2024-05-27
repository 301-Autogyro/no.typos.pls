'''Файл реализации алгоритма LIFO для очереди процессов'''
# Импорт модуля генератора процессов
from ProcessGenerator import Process, Generator
# Создание таблицы
from prettytable import PrettyTable

process_count = input('Введите кол-во процессов: ')
process_count = int(process_count)
proc_generate_count = input('Введите кол-во генерируемых процессов: ')
proc_generate_count = int(proc_generate_count)

# Стек процессов
processes: list = Generator.generate(process_count)


for i in range(proc_generate_count):
    # --- #
    # Указываем заголовки страницы
    head = ['ID', 'Приоритет', 'Время выполнения']
    # Создаём объект таблицы
    table = PrettyTable(head)
    # Сборка таблицы
    for process in processes:
        table.add_row([process.id, process.priority, process.work_time])
    print(table)
    # --- #
    # Генерируем новый процесс для добавления
    proc_for_add: Process = Generator.generate(1, processes[len(processes)-1].id + 1)[0]

    # Удаляем первый элемент стека
    # TODO: Добавить расчёт пиздюлей
    processes.pop(0) # непосредственное удаление элемента стека

    # Добавляем новый элемент в стек
    processes.append(proc_for_add)