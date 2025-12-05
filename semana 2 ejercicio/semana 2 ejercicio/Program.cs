using System;
using System.Collections.Generic;

class Program
{
    static (int, List<int>) Mochila01(int[] pesos, int[] valores, int capacidad)
    {
        int n = pesos.Length;
        int W = capacidad;
        int[] dp = new int[W + 1];
        bool[][] tomar = new bool[n][];
        for (int i = 0; i < n; i++)
            tomar[i] = new bool[W + 1];

        for (int i = 0; i < n; i++)
        {
            for (int w = W; w >= pesos[i]; w--)
            {
                int sinTomar = dp[w];
                int conTomar = valores[i] + dp[w - pesos[i]];
                if (conTomar > sinTomar)
                {
                    dp[w] = conTomar;
                    tomar[i][w] = true;
                }
            }
        }

        List<int> objetos = new List<int>();
        int cap = W;
        for (int i = n - 1; i >= 0; i--)
        {
            if (cap >= pesos[i] && tomar[i][cap])
            {
                objetos.Add(i);
                cap -= pesos[i];
            }
        }
        objetos.Reverse();
        return (dp[W], objetos);
    }

    static void Main()
    {
        int[] pesos = { 2, 3, 4, 5 };
        int[] valores = { 3, 4, 5, 6 };
        int capacidad = 10;

        var (valor, items) = Mochila01(pesos, valores, capacidad);
        Console.WriteLine(valor);
        Console.WriteLine(string.Join(" ", items));

        int[] pesos2 = { 1, 3, 4, 5 };
        int[] valores2 = { 1, 4, 5, 7 };
        int capacidad2 = 7;

        var (valor2, items2) = Mochila01(pesos2, valores2, capacidad2);
        Console.WriteLine(valor2);
        Console.WriteLine(string.Join(" ", items2));
    }
}