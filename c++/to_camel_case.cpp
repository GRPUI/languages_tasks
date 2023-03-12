#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string toCamelCase(string input)
{
    vector<string> words;
    string currentWord = "";

    for (char c : input)
    {
        if (c == '-' || c == '_')
        {
            words.push_back(currentWord);
            currentWord = "";
        }
        else
        {
            currentWord += c;
        }
    }

    words.push_back(currentWord);

    for (int i = 1; i < words.size(); i++)
    {
        words[i][0] = toupper(words[i][0]);
    }

    string result = "";

    for (string word : words)
    {
        result += word;
    }

    return result;
}

int main()
{
    string input = "the-stealth-warrior";
    string output = toCamelCase(input);
    cout << output << endl;

    return 0;
}
