@echo off
git pull
git add *.*
git rm --cached commit.bat
git remote add text2kg https://github.com/d1egoprog/Text2KG.git
git commit -m "Updating %DATE% on %TIME%"
pause
git push -u text2kg master
