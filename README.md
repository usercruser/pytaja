# PyTAJA - 파이타자
[빠른 다운로드 ↓](https://github.com/usercruser/pytaja/archive/refs/heads/main.zip)

파이썬으로 만든 간단한 타자연습 프로그램입니다

## 가이드
실행시키려면 먼저 pip가 있어야 하며, 아래 표기된 라이브러리를 pip를 통해 받으셔야합니다

run.sh(bash), run.ps1(powershell)파일을 실행해 앞서 설명한 라이브러리를 빠르게 설치 하실 수 있습니다.

data 파일에 크게 의존중이기에 client.py 파일만 받을 시 실행이 안되니 무조건 전체 파일을 다운로드 후 같은 디렉토리에 넣어주시기 바랍니다

git repo :
```bash
git clone https://github.com/usercruser/pytaja.git/
```

## 사용한 라이브러리
[tqdm](https://github.com/tqdm/tqdm) - 반복문 진행률 바에 사용

[hgtk](https://github.com/bluedisk/hangul-toolkit) - 한글 자음 모음 분리 저장 / 오타율 추적에 사용

[six](https://github.com/benjaminp/six) - six에 의존하는 라이브러리가 있었음

statistics - 오타율, 타수, 정확도 등의 평균을 구하는데 사용
