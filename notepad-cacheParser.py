import os
import fnmatch
import subprocess
import sys
import datetime
import colorama

# Initialize colorama
colorama.init(autoreset=True)

RED = colorama.Fore.LIGHTRED_EX
GREEN = colorama.Fore.LIGHTGREEN_EX
YELLOW = colorama.Fore.LIGHTYELLOW_EX
BLUE = colorama.Fore.LIGHTBLUE_EX
CYAN = colorama.Fore.LIGHTCYAN_EX
MAGENTA = colorama.Fore.LIGHTMAGENTA_EX
RESET = colorama.Style.RESET_ALL

#  timestamp
def timestamp():
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# Logs
def log_info(message):
    print(f"{timestamp()} {BLUE}ℹ️ [INFO]{RESET} {message}")

def log_success(message):
    print(f"{timestamp()} {GREEN}✅ [SUCCESS]{RESET} {message}")

def log_error(message):
    print(f"{timestamp()} {RED}❌ [ERROR]{RESET} {message}")

# banner
print(f"""{MAGENTA}
===============================================
 📜 Notepad Cache Dumper - By Ozz961 🔍
 Extracts strings from Notepad session files 
===============================================
{RESET}""")

# Define Paths
user_path = os.environ.get("LOCALAPPDATA")
target_path = r'Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState\TabState'
full_path = os.path.join(user_path, target_path)
script_dir = os.path.dirname(os.path.abspath(__file__))
strings_exe_path = os.path.join(script_dir, "strings64.exe")
dumpfolder_dir = os.path.join(script_dir, "Notepad Cache Dumps")

# Ensure dump folder exists
os.makedirs(dumpfolder_dir, exist_ok=True)

# Graceful Exit Function
def graceful_exit(message, exit_code=1):
    log_error(message)
    input(f"\n{YELLOW}🔸 Press Enter to exit...{RESET}")
    sys.exit(exit_code)

# Validate if source directory exists
if not os.path.exists(full_path):
    graceful_exit(f"📂 Source directory does not exist: {full_path}")

# Validate if strings64.exe exists in the dir
if not os.path.exists(strings_exe_path):
    graceful_exit(f"⚙️ strings64.exe not found at: {strings_exe_path}")

# list for storing
bin_files = []

# Search for bin files
log_info(f"📂 Scanning directory: {full_path}")
for file in os.listdir(full_path):
    if fnmatch.fnmatch(file, "*.bin") or fnmatch.fnmatch(file, "*.bin.bak"):
        bin_files.append(os.path.join(full_path, file))

# Handle files not found
if not bin_files:
    log_info("🚫 No .bin or .bin.bak files found. Exiting.")
    input(f"\n{YELLOW}🔸 Press Enter to exit...{RESET}")
    sys.exit(0)

# Processing .bin file with strings64
log_info(f"🔍 Found {len(bin_files)} file(s). Running strings64...\n")
for index, bin_file in enumerate(bin_files, start=1):
    output_file = os.path.join(dumpfolder_dir, f"cachefile{index}.txt")

    with open(output_file, "w") as out:
        subprocess.run([strings_exe_path, bin_file], stdout=out, stderr=subprocess.DEVNULL, text=True)

    log_success(f"✅ Processed: {MAGENTA}{bin_file} {YELLOW}➡️ {CYAN}{output_file}{RESET}")
    print("-" * 40)  # Separator line

log_info(f"📂 All files processed! Extracted text files are in: {dumpfolder_dir}")

# Graceful exit
input(f"\n{YELLOW}🔸 Press Enter to exit...{RESET}")
