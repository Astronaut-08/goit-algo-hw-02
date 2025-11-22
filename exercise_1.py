'''Потрібно розробити програму, яка імітує приймання й обробку заявок:
програма має автоматично генерувати нові заявки (ідентифіковані унікальним
номером або іншими даними), додавати їх до черги, а потім послідовно
видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.'''

import time
from queue import Queue

queue = Queue()

def generate_request(cou):
    '''TODO: Створити нову заявку
    Додати заявку до черги'''
    print(f'Заявка {cou} створена!\n')
    queue.put(cou)

def process_request():
    '''TODO: Обробити заявку
    Видалити заявку з черги'''
    if not queue.empty():
        work = queue.get()
        print(f'Заявка {work} в обробці!')
        time.sleep(1)
        print(f'Заявку {work} успішно опрацьовано!\n')
    else:
        print('Черга пуста')


print('Щоб запустити обробку ввведи "operate", щоб вийти "exit"')
while True:
    req = input('Введи запит який треба обробити: ')
    if req.casefold() == 'operate':
        while not queue.empty():
            process_request()

        process_request() # Повідомлення про пусту чергу
        continue
    elif req.casefold() == 'exit':
        print('Бувай!')
        break

    generate_request(req) # додаємо реквест
