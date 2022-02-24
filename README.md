# node
this a git test


#git 命令

#创建分支  

```
git branch mybranch

```

#切换分支  

	git checkout mybranch  

#创建并切换分支  

	git checkout -b mybranch

#更新master/main 主线上的东西到该分支上  

	git rebase master  

#切换到master分支  

	git checkout master  

#提交  

	git commit -m "xxx"
	git commit -a

#对最近一次的commit进行修改  

	git commit -a -amend

#commit之后,退回到上一个版本  

	git reset HEAD^  

#合并分支  

	git merge mybranch  

#删除分支  

	git branch -d mybranch  

#强制删除分支  

	git branch -D mybranch


#查看所有分支  

	git branch  

#查看各个分支最后一次提交  

	git branch -v  

#查看哪些分支合并到当前分支  

	git branch -merged  

#查看哪些分支未合并到当前分支  

	git branch -no-merged  

#更新远程库到本地  

	git fetch origin  

#推送分支  

	git push origin mybranch  

#取远程分支合并到本地  

	git merge origin/mybranch  

#取远程分支并分化一个新分支  

	git checkout -b mybranch origin/mybranch  

#删除远程分支  

	git push origin : mybranch  



