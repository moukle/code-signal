char firstNotRepeatingCharacter(string s) {
    List<char> charIndex = new List<char>();
    int[] counter = new int[26];

    foreach(char c in s){
        if(!charIndex.Contains(c)) {
            charIndex.Add(c);
        }
        counter[charIndex.IndexOf(c)]++;
    }

    for (int i = 0; i < charIndex.Count; i++)
    {
        if(counter[i] == 1)
        {
            Console.WriteLine(charIndex[i]);
            return charIndex[i];
        }
    }
    return '_';
}