/*
Ваша цель в этом задании - реализовать функцию разности, которая вычитает один список из другого и возвращает результат.
Он должен удалить все значения из списка a, которые присутствуют в списке b, сохраняя их порядок.
array_diff([1,2],[1]) == [2]
Если значение присутствует в b, все его вхождения должны быть удалены из другого:
array_diff([1,2,2,2,3],[2]) == [1,3]
*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
  public static int[] ArrayDiff(int[] a, int[] b)
  {
    List<int> result = new List<int>();
    foreach (int num in a)
    {
      if (!b.Contains(num))
      {
        result.Add(num);
      }
    }
    return result.ToArray();
  }
}
