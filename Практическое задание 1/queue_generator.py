'''Модуль генерации очереди процессов'''

# Временные метки и unix
import time
# Модуль рандомизации
import random

class QueueGenerator():
    '''Генератор очереди процессов'''
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
        '''Генерирует очередь процессов'''
        queue = []
        for i in range(self.process_count):
            process = {'id': i,
                       'priority': random.randint(self.minimum_priority_level, 10),
                       'work_time': float(str(random.randint(self.minimum_work_time, 60)) + '.' + str(random.randint(0, 999)))}
            queue.append(process)
        
        return queue
    
    def generate_one_process(self, pid: int = 0) -> dict:
        '''Генерирует один процесс очереди.
        
        :param plid: ID процесса в очереди
        :type plid: :obj:`int`'''

        return {'id': pid + 1,
                'priority': random.randint(self.minimum_priority_level, 10),
                'work_time': float(str(random.randint(self.minimum_work_time, 60)) + '.' + str(random.randint(0, 999)))}

            
            
