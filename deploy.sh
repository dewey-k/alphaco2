#!/bin/bash
echo "Git Push Starting..."
cd /Users/dewey/Desktop/alphaco2

#check out repo
git add -A
git commit -m "Automated commit on $(date '+%Y0%m-%d %H:%M:%S')"
git push
