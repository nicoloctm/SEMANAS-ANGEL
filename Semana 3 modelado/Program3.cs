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
        // Usamos false para "No Dirigido" (ida y vuelta) como pide la extensión
        static bool esDirigido = false; 

        static void Main(string[] args)
        {
            grafo.Clear();
            Console.WriteLine("--- Generando Grafo Urbano Ampliado ---");

            // --- CARGA INICIAL (Mínimo 12 aristas únicas) ---
            
            // Zona Residencial
            AgregarConexion("Casa", "Parque", 5);
            AgregarConexion("Casa", "Supermercado", 10);
            AgregarConexion("Casa", "Farmacia", 7); // Nueva

            // Zona Comercial/Educativa
            AgregarConexion("Parque", "Escuela", 8);
            AgregarConexion("Parque", "Gimnasio", 6); // Nueva
            AgregarConexion("Supermercado", "Escuela", 4);
            AgregarConexion("Supermercado", "Cine", 6);
            AgregarConexion("Supermercado", "Farmacia", 3); // Nueva

            // Zona Servicios/Salud
            AgregarConexion("Escuela", "Hospital", 15);
            AgregarConexion("Escuela", "Biblioteca", 5); // Nueva
            AgregarConexion("Cine", "Gimnasio", 4); // Nueva
            AgregarConexion("Cine", "Hospital", 2);
            
            // Conexiones periféricas
            AgregarConexion("Farmacia", "Hospital", 12); // Nueva
            AgregarConexion("Gimnasio", "Biblioteca", 9); // Nueva

            // Total: 14 conexiones únicas (calles). 
            // Al ser no dirigido, generará 28 líneas en el archivo. ¡Cumple de sobra!

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
                Console.WriteLine($"Exito: Se han exportado {grafo.Count} aristas a {rutaArchivo}.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
        }
    }
}