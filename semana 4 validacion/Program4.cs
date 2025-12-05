using System;
using System.Collections.Generic;
using System.IO;

namespace GrafoActividad
{
    public class Arista
    {
        public string Origen { get; set; }
        public string Destino { get; set; }
        public int Peso { get; set; }

        public Arista(string origen, string destino, int peso)
        {
            Origen = origen;
            Destino = destino;
            Peso = peso;
        }
    }

    class Program
    {
        static List<Arista> grafo = new List<Arista>();
        static bool esDirigido = false; // Importante: false para grafo no dirigido

        static void Main(string[] args)
        {
            grafo.Clear();
            Console.WriteLine("--- Generando Grafo Urbano (Semana 4) ---");

            // Carga de conexiones (Mapa Urbano)
            AgregarConexion("Casa", "Parque", 5);
            AgregarConexion("Casa", "Supermercado", 10);
            AgregarConexion("Casa", "Farmacia", 7);
            AgregarConexion("Parque", "Escuela", 8);
            AgregarConexion("Parque", "Gimnasio", 6);
            AgregarConexion("Supermercado", "Escuela", 4);
            AgregarConexion("Supermercado", "Cine", 6);
            AgregarConexion("Supermercado", "Farmacia", 3);
            AgregarConexion("Escuela", "Hospital", 15);
            AgregarConexion("Escuela", "Biblioteca", 5);
            AgregarConexion("Cine", "Gimnasio", 4);
            AgregarConexion("Cine", "Hospital", 2);
            AgregarConexion("Farmacia", "Hospital", 12);
            AgregarConexion("Gimnasio", "Biblioteca", 9);

            GenerarArchivo();
        }

        static void AgregarConexion(string origen, string destino, int peso)
        {
            grafo.Add(new Arista(origen, destino, peso));
            if (!esDirigido)
            {
                grafo.Add(new Arista(destino, origen, peso));
            }
        }

        static void GenerarArchivo()
        {
            string rutaArchivo = "edges.txt";
            try 
            {
                using (StreamWriter sw = new StreamWriter(rutaArchivo))
                {
                    foreach (var arista in grafo)
                    {
                        sw.WriteLine($"{arista.Origen},{arista.Destino},{arista.Peso}");
                    }
                }
                Console.WriteLine($"Exito: {grafo.Count} aristas exportadas a {rutaArchivo}.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
        }
    }
}