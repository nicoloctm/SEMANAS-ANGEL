using System;

class P
{
    static void Main()
    {
        for (int i = 0; i <= 15; i++) Console.WriteLine("f(" + i + ") = " + f(i));
    }
    static int f(int n)
    {
        if (n <= 1) return n;
        return f(n - 1) + f(n - 2);
    }
}