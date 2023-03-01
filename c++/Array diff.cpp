/*
Ваша цель в этом задании - реализовать функцию разности, которая вычитает один список из другого и возвращает результат.
Он должен удалить все значения из списка a, которые присутствуют в списке b, сохраняя их порядок.
array_diff([1,2],[1]) == [2]
Если значение присутствует в b, все его вхождения должны быть удалены из другого:
array_diff([1,2,2,2,3],[2]) == [1,3]
*/
  
#include <vector>
#include <algorithm>

std::vector<int> array_diff(std::vector<int> a, std::vector<int> b)
{
  std::vector<int> result;
  for (int num : a)
  {
    if (std::find(b.begin(), b.end(), num) == b.end())
    {
      result.push_back(num);
    }
  }
  return result;
}
