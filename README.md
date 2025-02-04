# Notepad Cache Dumper

## 📜 Overview
**Notepad Cache Dumper** is a Python script that extracts text from unsaved Notepad session files stored in Windows. This tool is useful for recovering lost notes by scanning Notepad's cache folder and extracting readable text from `.bin` and `.bin.bak` files.

## 🔍 Features
- **Automated Recovery**: Finds and processes Notepad cache files.
- **Uses `strings64.exe`**: Extracts readable text from binary files.
- **Logs with Timestamp**: Provides clear logs for each step.
- **User-Friendly**: Displays progress and errors in a structured format.
- **Safe Execution**: Gracefully exits if required files or directories are missing.

## 🛠️ How It Works
1. **Identifies Notepad's cache directory** in Windows.
2. **Searches for `.bin` and `.bin.bak` files** where unsaved Notepad text might be stored.
3. **Runs `strings64.exe` on each file** to extract readable text.
4. **Saves extracted content** in a `Notepad Cache Dumps` folder.
5. **Displays progress and results** in the terminal.

## 🚀 Requirements
- Windows 10/11 with **Microsoft Store Notepad** installed.
- Python 3.x installed.
- `strings64.exe` (available in the same directory as the script).
- Administrator privileges may be required to access certain system files.

## 🔧 Installation & Usage
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Ozz961/Notepad-Cache-Dumper.git
cd Notepad-Cache-Dumper
```

### 2️⃣ Download `strings64.exe`
The `strings64.exe` is from Microsoft Sysinternals suite. Which You can get it from:
- [Microsoft Sysinternals](https://docs.microsoft.com/en-us/sysinternals/downloads/strings)

### 3️⃣ Run the Script
```sh
python notepad_cache_dumper.py
```

## 🏗️ How to Modify
- **Custom Dump Directory**: Change `dumpfolder_dir` to store extracted text elsewhere.
- **Alternative Extraction Method**: Modify the `subprocess.run` command to use different string extraction tools.

## ⚠️ Limitations
- Only works with **Microsoft Store version of Notepad**.
- Cannot recover data if Notepad has been manually closed and cleared.
- Requires **`strings64.exe`**.

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify.

## 👤 Author
Roger

---

⚡ **Disclaimer:** This tool is for educational and recovery purposes only. Use responsibly!
