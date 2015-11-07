# 271AIgame
1. AI design

1) evaluate algorithm: how good is it? is complete? is complex? space take, time take
2) computer vs. computer, human vs. computer 
-compare to other AI to determine how good is (percentage of win, relative to speed)
-make some claims and try to back it up about our AI
3) compare with other algorithm using resources: compare with brute force and with most optimal algorithm
-how does it compare to dumb AI and how compare to AI that always makes best move (forsight)




2. Notes for teamwork:      
1) Github: command line or download a github desktop
   
  
for command:        
[Optional]download git     
[Optional]create Github folder in your computer      
config your github by     
	git config --global user.name "YOUR NAME"     
	git config --global user.email "YOUR EMAIL ADDRESS"     
clone from your github's website copy of 271AIgame, such as https://github.com/yourusername/271AIgame.git     
	git clone https:// ........git     
Start work! Remember to check for uncommited changes!     
Methods that could avoid unecessary steps:     
[Optional] Avoid merge commits for pulling     
    git config --global branch.autosetuprebase always     
   

Be Careful with the order of the commands:      
        
switch to second directory        
cd ~/repositoryfolder
   
pull in the latest changes of your remote repository        
git pull
  
make changes      
  
commit the changes   
git add .
git commit -a / git commit -m "A change"      
  
push changes to remote repository        
git push (origin)        
  
       

Other useful commands:     
$ git status     
Lists all new or modified files to be committed     
$ git diff     
Shows file differences not yet staged     
$ git add [file] / git add .  (this add all files)     
Commit change files with [descriptive message]     
$ git commit -m "[descriptive message]"     
Amend the last commit     
$ git commit --amend -m "More changes - now correct"      
Records file snapshots permanently in version history     
$ git push [target]     
Push to the main repository     
$ git log      
Show the Git log for the change     
$ git rm     
Remove file          
     
Could check:     
http://www.vogella.com/tutorials/Git/article.html#gitdefintion_localoperations     


