# Create new repo
git init

# Checkout repo
git clone path/to/repo

# Workflow of git
Working Directory -> Index -> Head

# Add (to index) & Commit (to Head)
git add *
git commit -m "committing from index to head"

# Pushing changes
git push <server> <branchname>
git remote add <server> <branchname>

# Branching
git checkout -b <branchname> 
git branch <branchname>
git checkout <branchname>
git branch -d <branchname>

# Get most recent remote updates
git pull

# Merge another branch into your active branch
git merge <branchname>
git diff

# Tagging
git tag 1.0.0 <commit id>

# Logging
git log
git log --author=bob
git log --pretty=oneline
git log --graph --oneline --decorate --all
git log --name-status

# Replace local changes
git checkout -- <filename>
This replaces the changes in your working tree with the last content in HEAD

If you want to replace all your local changes and commits,   
fetch the latest history from the server,
point your local master branch at it

git fetch origin
git reset --hard origin/master


