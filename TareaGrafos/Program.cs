using System;
using System.Collections.Generic;
using System.IO;

namespace GrafoActividad
{
    // Clase simple para representar una conexión
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
        // false = Grafo No Dirigido (las calles son de doble sentido)
        static bool esDirigido = false; 

        static void Main(string[] args)
        {
            grafo.Clear();
            Console.WriteLine("--- Generando Grafo Urbano (Avance 2) ---");

            // --- CARGA DE DATOS (Mínimo 12 aristas únicas) ---
            
            // Zona Residencial
            AgregarConexion("Casa", "Parque", 5);
            AgregarConexion("Casa", "Supermercado", 10);
            AgregarConexion("Casa", "Farmacia", 7);

            // Zona Comercial y Educativa
            AgregarConexion("Parque", "Escuela", 8);
            AgregarConexion("Parque", "Gimnasio", 6);
            AgregarConexion("Supermercado", "Escuela", 4);
            AgregarConexion("Supermercado", "Cine", 6);
            AgregarConexion("Supermercado", "Farmacia", 3);

            // Zona Servicios y Salud
            AgregarConexion("Escuela", "Hospital", 15);
            AgregarConexion("Escuela", "Biblioteca", 5);
            AgregarConexion("Cine", "Gimnasio", 4);
            AgregarConexion("Cine", "Hospital", 2);
            
            // Conexiones periféricas para dar consistencia
            AgregarConexion("Farmacia", "Hospital", 12);
            AgregarConexion("Gimnasio", "Biblioteca", 9);

            GenerarArchivo();
        }

        static void AgregarConexion(string origen, string destino, int peso)
        {
            grafo.Add(new Arista(origen, destino, peso));
            
            // Si es NO dirigido, agregamos el regreso automáticamente
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
                Console.WriteLine($"Exito: Se exportaron {grafo.Count} conexiones a {rutaArchivo}.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
        }
    }
}