/*
Ваша цель в этом задании - реализовать функцию разности, которая вычитает один список из другого и возвращает результат.
Он должен удалить все значения из списка a, которые присутствуют в списке b, сохраняя их порядок.
array_diff([1,2],[1]) == [2]
Если значение присутствует в b, все его вхождения должны быть удалены из другого:
array_diff([1,2,2,2,3],[2]) == [1,3]
*/

package kata

func ArrayDiff(a, b []int) []int {
  result := []int{}
  for _, num := range a {
    if !contains(b, num) {
      result = append(result, num)
    }
  }
  return result
}

func contains(arr []int, num int) bool {
  for _, val := range arr {
    if val == num {
      return true
    }
  }
  return false
}
