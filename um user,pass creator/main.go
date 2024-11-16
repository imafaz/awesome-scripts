package main

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"strings"
)

func RandomPassword(charset string, length int) string {
	password := make([]byte, length)

	for i := range password {
		password[i] = charset[rand.Intn(len(charset))]
	}

	return string(password)
}

func main() {
	var userCount int
	var profileName string
	var sharedUser int
	var usernameStartWith string
	var passwordCharCount int
	var rscFileContent strings.Builder
	var userPassFileContents strings.Builder

	fmt.Print("pliase inter user count: ")
	fmt.Scan(&userCount)
	fmt.Print("pliase inter profile name: ")
	fmt.Scan(&profileName)
	fmt.Print("pliase inter shared users: ")
	fmt.Scan(&sharedUser)
	fmt.Print("pliase inter username start with: ")
	fmt.Scan(&usernameStartWith)
	fmt.Print("pliase inter password character count: ")
	fmt.Scan(&passwordCharCount)
	for i := 0; i < userCount; i++ {
		username := usernameStartWith + strconv.Itoa(i)
		password := RandomPassword("0123456789", passwordCharCount)
		rscFileContent.WriteString(fmt.Sprintf("/user-manager/user/add name=%s password=%s shared-users=%d\n", username, password, sharedUser))
		rscFileContent.WriteString(fmt.Sprintf("/user-manager/user-profile/add profile=%s user=%s\n", profileName, username))
		userPassFileContents.WriteString(fmt.Sprintf("User: %s   --->  Password: %s\n", username, password))
	}
	if err := os.WriteFile("mikrotik.rsc", []byte(rscFileContent.String()), 0644); err != nil {
		log.Fatalf("Error writing to file: %v", err)
	}
	if err := os.WriteFile("users.txt", []byte(userPassFileContents.String()), 0644); err != nil {
		log.Fatalf("Error writing to file: %v", err)
	}
	fmt.Println("Your rsc file for mikrotik save to file: mikrotik.rsc")
	fmt.Println("Your user,pass file for users save to file: users.txt")

}
