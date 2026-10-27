#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
from datetime import datetime

NAME = "bikash_cyber_tech_add"
SITES = {
    "1": ("YouTube", "https://youtube.com"),
    "2": ("Instagram", "https://instagram.com/bikash_cyber_tech_/"),
    "3": ("Facebook", "https://facebook.com"),
}

def banner():
    os.system("clear")
    cyan = "\033[96m"
    green = "\033[92m"
    magenta = "\033[95m"
    reset = "\033[0m"

    width = max(40, shutil.get_terminal_size((80, 24)).columns)
    inner = width - 2
    title = " BIKASH CYBER TECH "
    remaining = max(0, inner - len(title))
    left = remaining // 2
    right = remaining - left

    rows = [
        ("╔" + "═" * left + title + "═" * right + "╗", cyan),
        ("║" + " " * inner + "║", cyan),
        ("║" + "BIKASH CYBER TECH".center(inner) + "║", cyan),
        ("║" + " " * inner + "║", cyan),
        ("╠" + "═" * inner + "╣", cyan),
        ("║" + " " * inner + "║", cyan),
        ("║" + "BIKASH CYBER TECH".center(inner) + "║", green),
        ("║" + ("Author: " + NAME).center(inner) + "║", magenta),
        ("║" + " " * inner + "║", cyan),
        ("╚" + "═" * inner + "╝", cyan),
    ]

    for line, color in rows:
        print(color + line + reset)

def system_info():
    print("\n\033[92m--- SYSTEM INFORMATION ---\033[0m")
    print("User:", os.environ.get("USER", "Termux"))
    print("Date:", datetime.now().strftime("%d-%m-%Y"))
    print("Time:", datetime.now().strftime("%I:%M:%S %p"))
    total, used, free = shutil.disk_usage(os.path.expanduser("~"))
    print(f"Storage: {used // (1024**3)} GB used / {total // (1024**3)} GB total")

def launch_site(url):
    try:
        subprocess.run(["termux-open-url", url], check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Could not open the link. Check Termux:API.")

def menu():
    while True:
        banner()
        system_info()
        print("\n\033[93m--- QUICK LAUNCH ---\033[0m")
        for key, (name, _) in SITES.items():
            print(f" [{key}] {name}")
        print(" [4] Show banner only")
        print(" [0] Exit")
        choice = input("\nSelect option: ").strip()
        if choice in SITES:
            launch_site(SITES[choice][1])
            input("\nPress Enter to continue...")
        elif choice == "4":
            banner()
            input("\nPress Enter to continue...")
        elif choice == "0":
            print("Goodbye, Cyber Tech!")
            break
        else:
            print("Invalid option!")
            input("Press Enter to continue...")

def install():
    source = os.path.abspath(__file__)
    destination = os.path.expanduser("~/.local/bin/termideck")
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copy2(source, destination)
    os.chmod(destination, 0o755)
    shell_rc = os.path.expanduser("~/.bashrc")
    path_line = 'export PATH="$HOME/.local/bin:$PATH"'
    if os.path.exists(shell_rc):
        with open(shell_rc, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""
    if path_line not in content:
        with open(shell_rc, "a", encoding="utf-8") as f:
            f.write("\n" + path_line + "\n")
    print("TermiDeck installed! Restart Termux, then run: termideck")

def uninstall():
    destination = os.path.expanduser("~/.local/bin/termideck")
    if os.path.exists(destination):
        os.remove(destination)
        print("TermiDeck command removed.")
    else:
        print("TermiDeck command is not installed.")
    print("Your project files have not been deleted.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "install":
            install()
        elif command == "uninstall":
            uninstall()
        elif command == "--banner":
            banner()
        else:
            print("Usage: python termideck.py [install|uninstall|--banner]")
    else:
        menu()
