#!/data/data/com.termux/files/usr/bin/bash
set -e
echo "⚡ TermiDeck Cyber Terminal Installer"
pkg update -y
pkg install python git -y
cd "$HOME"
if [ -d "$HOME/BH-Bikash-Ethical-GitHub_" ]; then
  cd "$HOME/BH-Bikash-Ethical-GitHub_"
  git pull --ff-only
else
  git clone https://github.com/pujamurmu49492-jpg/BH-Bikash-Ethical-GitHub_.git
  cd "$HOME/BH-Bikash-Ethical-GitHub_"
fi
python termideck.py
