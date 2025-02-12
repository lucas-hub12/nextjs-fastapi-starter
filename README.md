# 네이버 만나이 계산기 카피켓
- I created this program to adjust for the age calculation of President Yoon Suk-yeol.

### use
- https://ac.lucas12.store

### Dev
```bash
$ pyenv global
3.10.12
# $ python -m venv venv
$ source venv/bin/activate
# $pip install -r requirements.txt
$ uvicorn api.index:app --reload
```

### Contributing
- scenario #1
```bash
# setting ssh
$ git clone <URL>
$ git branch <VER>/<NAME>
$ git checkout <VER>/<NAME>
$ git push
# make PR
# doing ...
# dogng ...
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# releases & tag
```
- scenario #2
```bash
$ git branch -r
$ git checkout -t origin/<VER>/<NAME>
# doing ...
# dogng ...
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# releases & tag
```
### Ref
- https://docs.python.org/ko/3.10/library/datetime.html