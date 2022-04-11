developer='d1egoprog'
dateString=$(date '+%y/%m/%d')
timeString=$(date '+%H:%m:%S')
echo "-------------------------------------------"
echo "Starting push to repository"
git add *
git rm --cached commit.bat, commit.sh
git remote add text2kg https://github.com/d1egoprog/Text2KG.git
git commit -m "Update made by ${developer} on ${dateString} at ${timeString}"
git push -u text2kg master
echo "Repository upload finish"
echo "-------------------------------------------"