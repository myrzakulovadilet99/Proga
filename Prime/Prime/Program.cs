using System;

namespace Prime
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = Console.ReadLine();
            args = s.Split(); // каждое число написать отдельно
            foreach (string k in args)
            {
                int a = int.Parse(k); // переводим стринг на число инт
                int c = 0;
                for (int i = 2; i < a; i++)
                {
                    if (a % i == 0)
                        c++;
                }
                if (c == 0)
                    if (c != 1)
                        Console.WriteLine(a);

            }
            Console.ReadKey();
        }
    }
}

        