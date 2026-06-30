# Git Commands Cheat Sheet (gmail-ai-assistant)

## Daily Workflow

``` bash
git status
git add .
git commit -m "Describe your changes"
git push
```

## Initialize Repository

``` bash
git init
```

## Check Status

``` bash
git status
```

## Current Directory

``` bash
pwd
ls
ls -la
```

## Stage Files

``` bash
git add .
git add README.md
git add docs/ .github/
```

## Commit

``` bash
git commit -m "Initial commit: Gmail AI Assistant"
git commit -m "Add GitHub Actions workflow"
git commit -m "Improve README documentation"
git commit -m "Add architecture diagrams"
git commit -m "Add pytest unit tests"
```

## Push

``` bash
git push
git push -u origin main
```

## Pull

``` bash
git pull
```

## Remote

``` bash
git remote -v
git remote add origin git@github.com:<username>/gmail-ai-assistant.git
git remote set-url origin git@github.com:<username>/gmail-ai-assistant.git
```

## Branches

``` bash
git branch
git branch -M main
git checkout -b feature/my-feature
git switch main
```

## Log

``` bash
git log
git log --oneline
git log --oneline --graph --decorate
```

## Differences

``` bash
git diff
git diff --cached
```

## Restore

``` bash
git restore README.md
git restore .
```

## Tags

``` bash
git tag
git tag v1.0.0
git push origin v1.0.0
```

## Clone

``` bash
git clone git@github.com:<username>/gmail-ai-assistant.git
```

## Stash

``` bash
git stash
git stash list
git stash pop
```

## Clean

``` bash
git clean -n
git clean -fd
```

## Troubleshooting

Nothing pushed?

``` bash
git status
git add .
git commit -m "Your message"
git push
```

Check remote:

``` bash
git remote -v
```

Check commits:

``` bash
git log --oneline -5
```
