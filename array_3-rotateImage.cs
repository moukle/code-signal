int[][] rotateImage(int[][] a) {
    int[][] b = new int[a.Length][];
    
    for(int i = 0; i < a.Length; i++)
    {
        b[i] = new int[a.Length];
    }
    
    for (int i = 0; i < a.Length; i++)
    {
        for (int j = 0; j < a.Length; j++)
        {
            int columnIndex = a.Length - i - 1;
            b[j][index] = a[i][j];
        }
    }
    return b;
}

/*
    0 0 => 0 2
    0 1 => 1 2
    0 2 => 2 2

    1 0 => 0 1
    1 1 => 1 1
    1 2 => 2 1

    2 0 => 0 0
    2 1 => 1 0
    2 2 => 2 0

 */