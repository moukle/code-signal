bool[] alreadyInCell = new bool[9];

bool sudoku2(char[][] grid)
{
    // check all 3x3 cells
    for (int rOffset = 0; rOffset < 9; rOffset+=3)
    {
        for (int cOffset = 0; cOffset < 9; cOffset+=3)
        {
            for (int r = 0; r < 3; r++)
            {
                for (int c = 0; c < 3; c++)
                {
                    char number = grid[r + rOffset][c + cOffset];
                    if (charAlreadyInCellAndSet(number))
                    {
                        Console.WriteLine("cell broken");
                        return false;
                    }
                }
            }
            Array.Clear(alreadyInCell, 0, 9);
        }
    }

    // check rows
    for (int i = 0; i < 9; i++)
    {
        for(int j = 0; j < 9; j++) 
        {
            char number = grid[i][j];
            if (charAlreadyInCellAndSet(number))
            {
                Console.WriteLine("row broken");
                return false;
            }
        }
        Array.Clear(alreadyInCell, 0, 9);
    }

    // check columns
    for (int i = 0; i < 9; i++)
    {
        for(int j = 0; j < 9; j++) 
        {
            char number = grid[j][i];
            if (charAlreadyInCellAndSet(number))
            {
                Console.WriteLine("column broken");
                return false;
            }
        }
        Array.Clear(alreadyInCell, 0, 9);
    }
    return true;
}

bool charAlreadyInCellAndSet(char c) {
    int number = c - '0';

    if (number >= 1 && number <= 9)
    {
        if (alreadyInCell[number-1])
        {
            Console.WriteLine(number + " doubled");
            return true;
        }
        else
        {
            alreadyInCell[number-1] = true;
            return false;
        }
    }
    return false;
}