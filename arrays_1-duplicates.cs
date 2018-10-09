using System;
public class fuuu
{
    public static void main() {
        int[] a = new int[1, 2, 3, 4, 5, 1, 2];
        Console.WriteLine(firstDuplicate(a));
    }
    public int firstDuplicate(int[] a)
    {
        consoleWriteLine();
        bool[] found = new bool[a.Length];

        for (int i = 0; i < a.Length; i++)
        {
            if (found[a[i]] == false)
            {
                found[a[i]] = true;
            }
            else
            {
                return a[i];
            }
        }
        return -1;
    }
}