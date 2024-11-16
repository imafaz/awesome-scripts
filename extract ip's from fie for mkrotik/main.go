package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"
	"regexp"
	"strings"
)

func removeDuplicates(slice []string) []string {
	seen := make(map[string]bool)
	result := []string{}

	for _, val := range slice {
		if !seen[val] {
			seen[val] = true
			result = append(result, val)
		}
	}
	return result
}

func extractIPsFromFile(filepath string) []string {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatalf("Error opening file: %v", err)
	}
	defer file.Close()

	re := regexp.MustCompile(`(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,2})?)`)
	var ips []string
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		ips = append(ips, re.FindAllString(line, -1)...)
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	return ips
}

func main() {
	var listName string
	var fileName string
	var addressList strings.Builder
	var ips []string

	fmt.Print("Please enter file name: ")
	fmt.Scan(&fileName)
	fmt.Print("Please enter address list name: ")
	fmt.Scan(&listName)

	ips = extractIPsFromFile(fileName)
	addressList.WriteString("/ip/firewall/address-list\n")

	for _, value := range removeDuplicates(ips) {
		if _, _, err := net.ParseCIDR(value); err == nil || net.ParseIP(value) != nil {
			addressList.WriteString(fmt.Sprintf("add address=%s disabled=no list=%s\n", value, listName))
		}
	}

	outputFileName := listName + ".rsc"
	if err := os.WriteFile(outputFileName, []byte(addressList.String()), 0644); err != nil {
		log.Fatalf("Error writing to file: %v", err)
	}

	fmt.Printf("Your address list exported to file: %s\n", outputFileName)
}
