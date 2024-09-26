#!/bin/zsh
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
cd /Users/dewey/Desktop/alphaco2 || exit 1  # 디렉토리 이동 실패 시 종료
/usr/bin/git add .
/usr/bin/git commit -m "Auto commit at $(date +%Y-%m-%d_%H:%M)"
/usr/bin/git push
