"""
Завершите метод / функцию так, чтобы она преобразовывала слова, разделенные тире/подчеркиванием, в camel case.
Первое слово в выходных данных должно быть заглавным только в том случае, если исходное слово было заглавным (часто называемый Pascal case).
Следующие слова всегда должны быть написаны с заглавной буквы.

Примеры
"the-stealth-warrior" преобразуется в "theStealthWarrior"
"The_Stealth_Warrior" преобразуется в "TheStealthWarrior"
"""

def to_camel_case(text):
    text = text.replace('-', ' ').replace('_', ' ').split(' ')
    return ''.join([text[0]] + list(map(lambda x: x.capitalize(), text[1:])))
  
  
print(to_camel_case("the_stealth_warrior"))
#ожидаемый результат: "theStealthWarrior"
print(to_camel_case("The-Stealth-Warrior"))
#ожидаемый результат: "TheStealthWarrior"
print(to_camel_case("the-Stealth_Warrior""))
#ожидаемый результат: "theStealthWarrior"
