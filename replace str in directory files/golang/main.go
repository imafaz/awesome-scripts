package main

import (
	"fmt"
	"io/fs"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func replaceWordInFile(filePath, strToReplace, strReplace string) error {
	fileContent, err := os.ReadFile(filePath)
	if err != nil {
		return err
	}

	if strings.Contains(string(fileContent), strToReplace) {
		replaced := strings.ReplaceAll(string(fileContent), strToReplace, strReplace)
		if err := os.WriteFile(filePath, []byte(replaced), 0644); err != nil {
			return err
		}
		fmt.Printf("String replaced in: %s\n", filePath)
	}
	return nil
}

func main() {
	var folderPath, oldString, newString string

	fmt.Print("Please enter folder path: ")
	if _, err := fmt.Scanln(&folderPath); err != nil {
		log.Fatal(err)
	}

	fmt.Print("Please enter old string: ")
	if _, err := fmt.Scanln(&oldString); err != nil {
		log.Fatal(err)
	}

	fmt.Print("Please enter new string: ")
	if _, err := fmt.Scanln(&newString); err != nil {
		log.Fatal(err)
	}

	if err := filepath.Walk(folderPath, func(path string, info fs.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			return replaceWordInFile(path, oldString, newString)
		}
		return nil
	}); err != nil {
		log.Fatal(err)
	}
}
