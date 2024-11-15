package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"slices"
)

func extractIpFromFile(filepath string) []string {
	fileContent, err := os.ReadFile(filepath)
	if err != nil {
		log.Fatal(err)
	}
	re, err := regexp.Compile("(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}(\\/\\d{1,2})?)")
	if err != nil {
		log.Fatal(err)
	}
	return re.FindAllString(string(fileContent), -1)

}
func main() {

	ips := extractIpFromFile("new.txt")
	slices.Sort(ips)
	for _, value := range ips {
		fmt.Println(value)
	}
}
