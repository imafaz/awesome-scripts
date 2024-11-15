package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func searchInFile(str string, filePath string) bool {
	fileContents, err := os.ReadFile(filePath)
	if err != nil {
		log.Fatal("cant read file %s, error: %v", filePath, err)
	}
	return strings.Contains(string(fileContents), str)
}
func main() {
	var dirName string
	var strToSearch string
	fmt.Println("pliase inter directory name:")
	_, err := fmt.Scanln(&dirName)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("pliase inter word to search:")
	_, err = fmt.Scanln(&strToSearch)
	if err != nil {
		log.Fatal(err)
	}
	filepath.Walk(dirName, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			log.Fatal(err)
		}
		if !info.IsDir() {
			if searchInFile(strToSearch, path) {
				fmt.Println("found in ", path)
			}

		}
		return nil
	})
}
