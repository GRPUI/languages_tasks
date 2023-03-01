/*
Завершите функцию квадратной суммы так, чтобы она возводила в квадрат каждое переданное в нее число, а затем суммировала результаты вместе.
Например, для [1, 2, 2] он должен возвращать 9, потому что 1^2 + 2^2 + 2^2 = 9.
*/

public static class Kata
{
  public static int SquareSum(int[] n)
  {
    int sum = 0;
    foreach (int num in n)
    {
      sum += num * num;
    }
    return sum;
  }
}
