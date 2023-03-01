/*
Завершите метод, который принимает логическое значение и возвращает строку "Yes" для true или строку "No" для false.
*/

package kata

func BoolToWord(word bool) string {
  if word {
    return "Yes"
  } else {
    return "No"
  }
}
