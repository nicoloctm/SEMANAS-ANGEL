using System;
using System.Collections.Generic;

public class Program
{
    public static List<string> HanoiRecursivo(int n, char origen, char destino, char auxiliar)
    {
        var moves = new List<string>();

        void Solve(int k, char from, char to, char aux)
        {
            // Caso base: si no hay discos, no hacer nada
            if (k == 0) return;

            // Paso 1: Mover k-1 discos al auxiliar
            Solve(k - 1, from, aux, to);

            // Paso 2: Mover el disco grande al destino
            moves.Add($"{from} -> {to}");

            // Paso 3: Mover k-1 discos del auxiliar al destino
            Solve(k - 1, aux, to, from);
        }

        Solve(n, origen, destino, auxiliar);
        return moves;
    }

    // Prueba
    public static void Main()
    {
        Console.Write("¿Cuántos discos? ");
        int n = int.Parse(Console.ReadLine()!);

        var resultado = HanoiRecursivo(n, 'A', 'C', 'B');

        Console.WriteLine($"\nSe necesitan {resultado.Count} movimientos:\n");
        foreach (var m in resultado)
            Console.WriteLine(m);
    }
}