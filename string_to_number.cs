/*
Нам нужна функция, которая может преобразовать строку в число. Какие способы достижения этого вы знаете?

Примечание: Не волнуйтесь, все входные данные будут строками, и каждая строка является абсолютно корректным представлением целого числа.
*/

Console.WriteLine(Kata.StringToNumber("14241"));
//ожидаемый вывод: 14241

using System;
  public class Kata
  {
    public static int StringToNumber(String str) {
        return Convert.ToInt32(str);
  }
}
