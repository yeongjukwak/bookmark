#### git 사용자 정보 설정 (초기 설정)
```bash
$ git config --global user.name <사용자 이름>
$ git config --global user.email <이메일>
```

#### github에 push
```bash
$ git clone <github repository url>
$ git status  # 파일들의 현재 상태 확인(빨간색이면 commit할 준비가 안됨)
$ git add .   # dot => ALL (모든 파일 스테이지에 올림)
$ git status  # 파일들의 현재 상태 확인(초록색이면 commit할 준비가 됨)
$ git commit -m "commit comment"
$ git pust origin <barnch>
```

#### git reset
- reset은 되돌릴 수 없으니 신중하게 한다. 되도록 revert 사용
```
$ git log                           # commit list log 
$ git reset --hard <commit log>     # 되돌아가고 싶은 commit
$ git --force push origin <branch>  # 강제 push
```
  
#### git fetch and pull
```
$ git fetch
$ git pull
```
