/*
Нам нужна функция, которая может преобразовать строку в число. Какие способы достижения этого вы знаете?

Примечание: Не волнуйтесь, все входные данные будут строками, и каждая строка является абсолютно корректным представлением целого числа.
*/

package main

import (
	"fmt"
	"strconv"
)

func string_to_int_parseint(num string) int64 {
	x, err := strconv.ParseInt(num, 10, 64)
	if err != nil {
		panic(err)
	}
	return x
}

func string_to_int_atoi(num string) int {
	x, err := strconv.Atoi(num)
	if err != nil {
		panic(err)
	}
	return x
}

func main() {
	fmt.Println(string_to_int_parseint("1231"))
	fmt.Println(string_to_int_atoi("2314"))
}
