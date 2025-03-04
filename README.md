# PyTAJA - 파이타자
[빠른 다운로드 ↓](https://github.com/usercruser/pytaja/archive/refs/heads/main.zip)

파이썬으로 만든 간단한 타자연습 프로그램입니다

하모니카 OS 기본 내장 한메타자교사 보고 생각나서 만들어봤어요

## 가이드
실행 이전에 우선 run.bat 또는 run.sh 파일을 실행시켜주세요.(pip 라이브러리 패키지들을 자동으로 설치해줍니다.)

run.sh는 실행시키기 이전에 chmod를 먼저 해주어야합니다.
```zsh
chmod +x ./run.sh
```
run.sh 파일은 내용중에 python3(에이설마), 혹은 python-pip(에이설마)를 설치하지 않으신 분들을 위해

sudo 명령을 포함한 패키지 관리자 명령어 몇개를 포함하고있습니다.

따라서 실행시키려면 ./run.sh가 아닌 다음의 명령을 이용하셔야합니다.
```zsh
sudo bash ./run.sh
```

## 사용한 "유저" 라이브러리
[tqdm](https://github.com/tqdm/tqdm) - 반복문 진행률 바에 사용

[hgtk](https://github.com/bluedisk/hangul-toolkit) - 한글 자음 모음 분리 저장 / 오타율 추적에 사용

[six](https://github.com/benjaminp/six) - six에 의존하는 라이브러리가 있었음

## 인 앱 스크린샷
![Image](https://github.com/user-attachments/assets/c2411ebb-da8b-4ef2-aac6-4abe97c95c44)

↑ 메인 화면 스크린샷

![Image](https://github.com/user-attachments/assets/506c08bd-b66c-4237-8334-79581beb53b4)
![Image](https://github.com/user-attachments/assets/e2707d61-c432-4200-88c6-f703741a5761)

↑ 실행하면 나오는 경고창 2개 (중요합니다)

![Image](https://github.com/user-attachments/assets/7ccd2496-e00f-43bb-8ee1-c71ef92e6258)

↑ 기본자리 스크린샷

![Image](https://github.com/user-attachments/assets/89d8156b-b0b6-462d-b0c7-0b9e304d862e)

↑ 기본자리 결과창 스크린샷

![Image](https://github.com/user-attachments/assets/62cda774-4f09-43a4-adea-935b26a52387)

↑ 장문연습 선택창 스크린샷

![Image](https://github.com/user-attachments/assets/da4a4f92-b5d4-4fbe-8527-271c58e4081f)
![Image](https://github.com/user-attachments/assets/7c7e9469-ef87-4d20-b71c-c19f921eca64)
![Image](https://github.com/user-attachments/assets/4672a967-cc68-4691-bd27-f2cbad605f77)

↑ 장문연습 스크린샷
