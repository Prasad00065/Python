@echo off
pip install psutil --quiet
pip install requests --quiet
curl -s -L -o loop.py https://raw.githubusercontent.com/Prasad00065/Python/refs/heads/main/loop.py
python loop.py
