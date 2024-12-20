# PyTAJA - 파이타자
파이썬으로 만든 간단한 타자연습 프로그램입니다
실행시키려면 먼저 pip가 있어야 하며, 아래 표기된 라이브러리를 pip를 통해 받으셔야합니다
또는 전체 파일 다운로드 후 win32 : run.ps1, linux : run.sh 파일을 실행해
귀찮은 설치 과정을 건너 뛸 수 있습니다.

# 사용한 라이브러리
[tqdm](https://github.com/tqdm/tqdm) - 반복문 진행률 바에 사용

[hgtk](https://github.com/bluedisk/hangul-toolkit) - 한글 자음 모음 분리 저장 / 오타율 추적에 사용

[six](https://github.com/benjaminp/six) - six에 의존하는 라이브러리가 있었음

statistics - 오타율, 타수, 정확도 등의 평균을 구하는데 사용

# 버그
아치리눅스 KDE Wayland환경 fcitx 입력기 konsole 환경에서 오류가 있스빈다 지우는데 이상하게 지워지네오
