using System;
using System.Diagnostics;

static long HanoiRecursivo(int n, char o, char d, char a) =>
    n == 1 ? 1 : HanoiRecursivo(n - 1, o, a, d) + 1 + HanoiRecursivo(n - 1, a, d, o);

static long HanoiIterativo(int n, char o, char d, char a) =>
    (1L << n) - 1;

static void AnalisisComparativo(int n)
{
    const int Warmups = 1;
    const int Runs = 5;
    var sw = new Stopwatch();

    for (int i = 0; i < Warmups; i++)
    {
        _ = HanoiRecursivo(n, 'A', 'C', 'B');
        _ = HanoiIterativo(n, 'A', 'C', 'B');
    }

    long ticksRec = 0, ticksIte = 0;

    for (int r = 0; r < Runs; r++)
    {
        sw.Restart();
        _ = HanoiRecursivo(n, 'A', 'C', 'B');
        ticksRec += sw.ElapsedTicks;

        sw.Restart();
        _ = HanoiIterativo(n, 'A', 'C', 'B');
        ticksIte += sw.ElapsedTicks;
    }

    double msRec = (ticksRec / (double)Runs) * 1000.0 / Stopwatch.Frequency;
    double msIte = (ticksIte / (double)Runs) * 1000.0 / Stopwatch.Frequency;

    Console.WriteLine($"ANÁLISIS COMPARATIVO (n={n}):");
    Console.WriteLine($"Recursivo: {msRec:F3} ms - {(1L << n) - 1} movimientos");
    Console.WriteLine($"Iterativo: {msIte:F3} ms");
    Console.WriteLine("Complejidad temporal (ambas): O(2^n)");
    Console.WriteLine("Complejidad espacial: recursivo O(n); iterativo O(1) si es bitwise, O(n) si usa pila.");
}
AnalisisComparativo(20);