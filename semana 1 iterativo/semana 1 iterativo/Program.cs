using System;
using System.Collections.Generic;

List<string> HanoiIterativo(int n, char A, char B, char C)
{
    var moves = new List<string>();

    // Ciclo del disco 1 según paridad de n
    var cicloImpar = new[] { (A, C), (C, B), (B, A) };
    var cicloPar = new[] { (A, B), (B, C), (C, A) };
    var ciclo = (n % 2 == 1) ? cicloImpar : cicloPar;

    // Posición actual de cada disco (1 = más pequeño, n = más grande)
    var pos = new Dictionary<int, char>();
    for (int d = 1; d <= n; d++) pos[d] = A;

    int total = (1 << n) - 1;
    int idxCiclo = 0;

    // Encuentra el disco más pequeño (superior) en una torre
    int TopDisk(char peg)
    {
        int best = int.MaxValue;
        foreach (var kv in pos)
            if (kv.Value == peg && kv.Key < best)
                best = kv.Key;
        return best == int.MaxValue ? -1 : best;
    }

    // Realiza el único movimiento legal posible entre dos torres 
    void MoverEntre(char p1, char p2)
    {
        int top1 = TopDisk(p1);
        int top2 = TopDisk(p2);

        // Si una torre está vacía, mover hacia ella
        if (top1 == -1) { pos[top2] = p1; moves.Add($"{p2} -> {p1}"); }
        else if (top2 == -1) { pos[top1] = p2; moves.Add($"{p1} -> {p2}"); }
        else if (top1 < top2) { pos[top1] = p2; moves.Add($"{p1} -> {p2}"); }
        else { pos[top2] = p1; moves.Add($"{p2} -> {p1}"); }
    }

    for (int move = 1; move <= total; move++)
    {
        if (move % 2 == 1)
        {
            // Mover el disco más pequeño según el ciclo
            var (from, to) = ciclo[idxCiclo];
            pos[1] = to;
            moves.Add($"{from} -> {to}");
            idxCiclo = (idxCiclo + 1) % 3;
        }
        else
        {
            // Mover el único disco permitido (el más pequeño que no sea el 1)
            char disco1Pos = pos[1];
            char pX = A, pY = B;
            if (disco1Pos == A) { pX = B; pY = C; }
            else if (disco1Pos == B) { pX = A; pY = C; }
            else { pX = A; pY = B; }

            MoverEntre(pX, pY);
        }
    }

    return moves;
}

int n = 3;
char origen = 'A', auxiliar = 'B', destino = 'C';

var resultado = HanoiIterativo(n, origen, auxiliar, destino);

Console.WriteLine($"Torres de Hanoi iterativo con {n} discos:");
Console.WriteLine($"Total movimientos: {resultado.Count}\n");

foreach (var mov in resultado)
    Console.WriteLine(mov);