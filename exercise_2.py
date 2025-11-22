'''Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
додає всі його символи до двосторонньої черги (deque з модуля collections
в Python), а потім порівнює символи з обох кінців черги, щоб визначити,
чи є рядок паліндромом. Програма повинна правильно враховувати як рядки
з парною, так і з непарною кількістю символів, а також бути нечутливою
до регістру та пробілів.'''

from collections import deque

def is_palindrome(text: str) -> bool:
    '''TODO: порівняти символи з обох боків черги'''
    parse_text = text.replace(' ', '').lower()
    deq: deque = deque(list(parse_text))

    if len(parse_text) % 2 == 0:
        while deq:
            if deq.popleft() != deq.pop():
                return False
        return True
    return False
