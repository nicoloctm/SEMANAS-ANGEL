using System;
using System.Diagnostics;
using System.Collections.Generic;

class Program
{
    static long FibMemo(int n, Dictionary<int, long> memo)
    {
        if (memo.ContainsKey(n)) return memo[n];
        if (n <= 1) return n;
        memo[n] = FibMemo(n - 1, memo) + FibMemo(n - 2, memo);
        return memo[n];
    }

    static long FibTab(int n)
    {
        if (n <= 1) return n;
        long[] dp = new long[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++)
            dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }

    static void Main()
    {
        int n = 40;
        Stopwatch sw = new Stopwatch();

        sw.Restart();
        var memo = new Dictionary<int, long>();
        long r1 = FibMemo(n, memo);
        sw.Stop();
        double t1 = sw.Elapsed.TotalMilliseconds;

        sw.Restart();
        long r2 = FibTab(n);
        sw.Stop();
        double t2 = sw.Elapsed.TotalMilliseconds;

        Console.WriteLine($"Fibonacci({n}) = {r1}");
        Console.WriteLine();
        Console.WriteLine("Top-Down (Memoización): " + t1.ToString("F4") + " ms");
        Console.WriteLine("Bottom-Up (Tabulación): " + t2.ToString("F4") + " ms");
    }
}