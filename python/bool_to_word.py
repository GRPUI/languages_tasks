"""
Завершите метод, который принимает логическое значение и возвращает строку "Yes" для true или строку "No" для false.
"""

def bool_to_word_simple(boolean):
  if boolean:
    return "Yes"
  return "No"

def bool_to_word_advanced(boolean):
    return "Yes" if boolean else "No"
  
  
print(bool_to_word_simple(True))
#ожидаемый вывод: "Yes"
print(bool_to_word_advanced(False))
#ожидаемый вывод: "No"
