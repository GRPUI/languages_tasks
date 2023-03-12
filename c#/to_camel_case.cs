public static string ToCamelCase(string input)
{
    string[] words = input.Split(new char[] { '-', '_' });

    for (int i = 1; i < words.Length; i++)
    {
        words[i] = char.ToUpper(words[i][0]) + words[i].Substring(1);
    }

    return string.Concat(words);
}
