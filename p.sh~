echo "input commit statements"
read str
git pull origin master
git add .
git commit -a -m "$str"
git push -u origin master
ssh ubuntu@115.159.217.29 "sudo su && yukunlongjiayou1 && cd blog/blog/mysite/ && git reset --hard && git pull"
