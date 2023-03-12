package main

import (
    "fmt"
    "strings"
)

func toCamelCase(input string) string {
    words := strings.Split(input, "-")
    words = append(words, strings.Split(input, "_")...)
    result := ""

    for i, word := range words {
        if i == 0 {
            result += word
        } else {
            result += strings.Title(word)
        }
    }

    return result
}

func main() {
    input := "the-stealth-warrior"
    output := toCamelCase(input)
    fmt.Println(output)
}


