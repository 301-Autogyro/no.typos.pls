'''Модуль генерации очереди процессов'''

# Временные метки и unix
import time
# Модуль рандомизации
import random
# Создание красивой таблицы
from prettytable import PrettyTable

class Process():
    '''Класс процесса'''
    def __init__(self, id, priority, work_time) -> None:
        self.id = id
        self.priority = priority
        self.work_time = work_time

class Generator():
    '''Классс генерации процессов'''
    def generate(proc_count: int = 5, last_id_proc: int = 0) -> list[Process]:
        processes = []
        for i in range(proc_count):
            processes.append(Process(last_id_proc+i,
                                random.randint(0, 10),
                                float(str(random.randint(0, 59)) + '.' + str(random.randint(1, 999)))
                                )
                            )
        return processes