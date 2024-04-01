'''Модуль генерации очереди процессов'''

# Временные метки и unix
import time
# Модуль рандомизации
import random
# Создание красивой таблицы
from prettytable import PrettyTable

class QueueGenerator():
    '''Класс генератора очереди процессов'''
    def __init__(self, process_count: int = 10, minimum_priority_level: int = 1, minimum_work_time: float = 10.0) -> None:
        '''
        Инициализация класса.

        :param process_count: количество процессов поддерживаемое очередью
        :type process_count: :obj:`int`

        :param minimum_priority_level: минимальный уровень приоритета для процессов (от 1 до 10)
        :type minimum_priority_level: :obj:`int`

        :param minimum_work_time: минимальное время работы процессов в секундах (не меньше либо равное нулю)
        :type minimum_work_time: :obj:`float`
        '''
        if minimum_priority_level not in range(1, 11):
            return 'Error'
        if minimum_work_time <= 0:
            return 'Error'
        
        self.process_count = process_count
        self.minimum_priority_level = minimum_priority_level
        self.minimum_work_time = minimum_work_time    

    def generate_queue(self) -> list[dict]:
        '''Генерирует очередь процессов
        
        list[
            dict(
                keys: id, priority, work_time;
                values: int, int, float
                )
            ]'''
        # список для объектов очереди
        queue = []
        # В цикле случайно создам данные для объекта в определённых ранее рамках
        for i in range(self.process_count):
            process = {'id': i,
                       'priority': random.randint(self.minimum_priority_level, 10),
                       'work_time': float(str(random.randint(self.minimum_work_time, 59)) + '.' + str(random.randint(0, 999)))}
            # добавляем процесс в список
            queue.append(process)
        
        return queue
    
    def generate_one_process(self, pid: int = 0) -> dict:
        '''Генерирует один процесс очереди.
        
        :param plid: ID процесса в очереди
        :type plid: :obj:`int`'''

        # Возвращаем случайно созданный словарик
        return {'id': pid + 1,
                'priority': random.randint(self.minimum_priority_level, 10),
                'work_time': float(str(random.randint(self.minimum_work_time, 60)) + '.' + str(random.randint(0, 999)))}

            
    def table_creator(self, queue: list[dict]):
        '''Собирает таблицу для вывода
        
        :param queue: Список процессов
        :type queue: :obj: `list[dict]`'''

        # Указываем заголовки страницы
        head = ['ID', 'Приоритет (важность)', 'Время выполнения']
        # Создаём объект таблицы
        table = PrettyTable(head)
        # В цикле добавляем строки в таблицу
        for row in queue:
            addrow = [row['id'], row['priority'], row['work_time']]
            table.add_row(addrow)
        # Возвращаем собранный объект страницы
        return table
