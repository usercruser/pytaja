# PyTAJA - 파이타자
[빠른 다운로드 ↓](https://github.com/usercruser/pytaja/archive/refs/heads/main.zip)

파이썬으로 만든 간단한 타자연습 프로그램입니다

하모니카 OS 기본 내장 한메타자교사 보고 생각나서 만들어봤어요

## 가이드
실행 이전에 우선 run.bat 또는 run.sh 파일을 실행시켜주세요.

run.sh는 실행시키기 이전에 chmod를 먼저 해주어야합니다.
```zsh
chmod +x ./run.sh
```

## 사용한 "유저" 라이브러리
[tqdm](https://github.com/tqdm/tqdm) - 반복문 진행률 바에 사용

[hgtk](https://github.com/bluedisk/hangul-toolkit) - 한글 자음 모음 분리 저장 / 오타율 추적에 사용

[six](https://github.com/benjaminp/six) - six에 의존하는 라이브러리가 있었음

statistics - 오타율, 타수, 정확도 등의 평균을 구하는데 사용
