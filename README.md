# Awesome Scripts 🚀

Welcome to **Awesome Scripts**! This repository is your go-to hub for a collection of useful scripts designed for a variety of tasks, from system administration to network management. Whether you’re a developer, sysadmin, or someone who loves automating tasks, there's something useful for you here! 🛠️

## Scripts Overview

### 1. Build Go Multi-OS
**Description:** This script allows you to build Go applications for multiple operating systems and architectures (Linux and Windows, both 64-bit).

**Files:**
- `main.ps1` (PowerShell script for Windows)
- `main.sh` (Bash script for Linux)

**Usage:**

**Linux:**
```bash
bash <(curl -s https://raw.githubusercontent.com/imafaz/awesome-scripts/main/build-go-multi-os/main.sh)
```

**Windows:**
1. First, download the `main.ps1` script using curl:
   ```powershell
   curl -o main.ps1 https://raw.githubusercontent.com/imafaz/awesome-scripts/main/build-go-multi-os/main.ps1
   ```
2. Run the script in PowerShell:
   ```powershell
   .\main.ps1
   ```

---

### 2. Extract IPs from File for MikroTik
**Description:** This Go script extracts IP addresses from a given file and generates a MikroTik-compatible address list in `.rsc` format.

**Usage:**

**Linux (amd64):**
```bash
curl -o extract-ips https://raw.githubusercontent.com/imafaz/awesome-scripts/main/extract-ips-from-file-for-mikrotik/linux-amd64
chmod +x extract-ips
./extract-ips
```

**Windows (amd64):**
```powershell
curl -o extract-ips.exe https://raw.githubusercontent.com/imafaz/awesome-scripts/main/extract-ips-from-file-for-mikrotik/windows-amd64.exe
.\extract-ips.exe
```

---

### 3. Find String in Directory Files
**Description:** This Go script searches for a specific string within all files in a given directory.

**Usage:**

**Linux (amd64):**
```bash
curl -o find-str https://raw.githubusercontent.com/imafaz/awesome-scripts/main/find-str-in-directory-files/linux-amd64
chmod +x find-str
./find-str
```

**Windows (amd64):**
```powershell
curl -o find-str.exe https://raw.githubusercontent.com/imafaz/awesome-scripts/main/find-str-in-directory-files/windows-amd64.exe
.\find-str.exe
```

---

### 4. Fix CentOS 7 Repository
**Description:** This Bash script replaces the default CentOS 7 repository configuration with a functioning one.

**Usage:**
```bash
bash <(curl -s https://raw.githubusercontent.com/imafaz/awesome-scripts/main/fix-centos7-repository/main.sh)
```

---

### 5. MikroTik User Manager User & Password Creator
**Description:** This Go script generates user accounts and passwords for MikroTik's User Manager and exports them in `.rsc` format.

**Usage:**

**Linux (amd64):**
```bash
curl -o mikrotik-user https://raw.githubusercontent.com/imafaz/awesome-scripts/main/mikrotik-um-user-pass-creator/linux-amd64
chmod +x mikrotik-user
./mikrotik-user
```

**Windows (amd64):**
```powershell
curl -o mikrotik-user.exe https://raw.githubusercontent.com/imafaz/awesome-scripts/main/mikrotik-um-user-pass-creator/windows-amd64.exe
.\mikrotik-user.exe
```

---

### 6. Replace String in Directory Files
**Description:** This Go script replaces a specific string with another string in all files within a given directory.

**Usage:**

**Linux (amd64):**
```bash
curl -o replace-str https://raw.githubusercontent.com/imafaz/awesome-scripts/main/replace-str-in-directory-files/linux-amd64
chmod +x replace-str
./replace-str
```

**Windows (amd64):**
```powershell
curl -o replace-str.exe https://raw.githubusercontent.com/imafaz/awesome-scripts/main/replace-str-in-directory-files/windows-amd64.exe
.\replace-str.exe
```

---

### 7. Set Proxy
**Description:** This Bash script sets up proxy settings for your environment.

**Usage:**
```bash
bash <(curl -s https://raw.githubusercontent.com/imafaz/awesome-scripts/main/set-proxy/main.sh) http://username:password@ip:port/
```
*Example:*
```bash
bash <(curl -s https://raw.githubusercontent.com/imafaz/awesome-scripts/main/set-proxy/main.sh) http://user:pass@192.168.1.1:8080/
```

---

### 8. Convert Linux to MikroTik
**Description:** This Bash script converts a Linux machine into a MikroTik CHR (Cloud Hosted Router) by downloading the MikroTik CHR image, writing it to the disk, and rebooting the system.


**Usage:**

```bash
bash <(curl -s https://raw.githubusercontent.com/imafaz/awesome-scripts/main/convert-linux-to-mikrotik/main.sh)
```
**Note:** This script will overwrite the disk content, so use it with caution!


---

## Contributing 🤝
Feel free to contribute to this repository by submitting pull requests or opening issues. Your contributions are always welcome!

## License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

Enjoy using these scripts to simplify your tasks! If you find them helpful, don’t forget to star the repository and share it with others! 🌟

