using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine(Fib(40)); // 102334155
        Console.WriteLine(Fib(50)); // 12586269025
    }

    static int FibMemo(int n, Dictionary<int, int> memo)
    {
        if (n <= 1) return n;
        if (memo.TryGetValue(n, out int v)) return v;
        v = FibMemo(n - 1, memo) + FibMemo(n - 2, memo);
        memo[n] = v;
        return v;
    }

    static int Fib(int n) => FibMemo(n, new Dictionary<int, int>());
}