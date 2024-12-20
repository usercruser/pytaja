from datetime import datetime
from tqdm import tqdm
import random
import time
import os
import hgtk
from sys import platform
import statistics
os.getcwd()

def neofetch():
    if platform == "linux":
        os.system("fastfetch")
    elif platform == "macos":
        os.system("neofetch")
    elif platform == "win32":
        os.system("winfetch")

def clearThing():
    if platform == "linux" and "macos":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
clearThing()

def d1(filePath):
    with open(filePath,'r',encoding="UTF-8") as f:
        return f.read().split("\n")

def bubue(wordList):
    spedup = []
    corct = []
    wronG = []
    for q in tqdm(wordList, desc="완료율 "):
        time.sleep(0)
        startTime = time.time()
        userInput = input(q + '\n').strip()
        duration = time.time() - startTime

        src = hgtk.text.decompose(q).replace("ᴥ", "")
        tar = hgtk.text.decompose(userInput).replace("ᴥ", "")

        correct = 0
        for i, c in enumerate(src, start=0):
            try:
                if tar[i] == c:
                    correct += 1
            except:
                pass
        srcLen = len(src)
        c = correct / srcLen * 100
        e = (srcLen - correct) / srcLen * 100
        speed = float(correct / duration) * 60
        spedup.append(speed)
        corct.append(c)
        wronG.append(e)
        clearThing()

        spg = statistics.mean(spedup)
        cpg = statistics.mean(corct)
        wpg = statistics.mean(wronG)

        print(f"\033[31m타수: {speed:0.2f} || 정확도: {c:0.2f} % || 오타율: {e:0.2f} %\033[0m\n")
        print(f"\033[31m평균 타수: {spg:.1f} || 평균 정확도: {cpg:.1f} % || 평균 오타율: {wpg:.1f} %\033[0m\n")
    while q == 10:
        break
    print("\033[34m\n- - ~\033[36m ~ = =\033[0m 결 과\033[36m = = ~\033[34m ~ - -\n\033[0m"+f"\033[30m\033[47m평균 타수: \033[31m{spg:.1f}\033[0m \n\033[30m\033[47m평균 정확도: \033[31m{cpg:.1f}\033[0m %\n\033[30m\033[47m평균 오타율: \033[31m{wpg:.1f}\033[0m %\n")

def core(filePath):
    clearThing()
    ##기본자리
    wordList = d1(filePath)
    random.shuffle(wordList)
    bubue(wordList)
    def ask():
        dadada = input("계속 하시겠습니까? \033[90m[Y: 계속하기/N: 메뉴로] : \033[0m")
        if dadada == "y":
            core()
        elif dadada == "n":
            home()
        else:   
            print("올바른 접근이 아닙니다.")
            ask()
    ask()

def coreNonRandom(filePath):
    clearThing()
    wordList = d1(filePath)
    bubue(wordList)
    def ask():
        dadada = input("다시 하시겠습니까? \033[90m[Y: 다시하기/N: 장문연습 홈으로] : \033[0m")
        if dadada == "y":
            coreNonRandom()
        elif dadada == "n":
            novelpractice()
        else:   
            print("올바른 접근이 아닙니다.")
            ask()
    ask()

def novelpractice():
    clearThing()
    ##장문연습
    print("\033[34m\n- - ~\033[36m ~ = =\033[0m 장 문 연 습\033[36m = = ~\033[34m ~ - -\n\033[0m")
    d = input("\033[36m선택하세요\033[0m\n1. 별 헤는 밤 - 윤동주\n2. 학점 헤는 밤 - 고양아짖어봐(todayhumor.co.kr)\n3. 애국가\n4. 서시 - 윤동주\nexit. 나가기\n\n~ $ ")
    if d == "1":
        coreNonRandom('data/documents/별_헤는_밤.txt')
    elif d == "2":
        coreNonRandom('data/documents/학점_헤는_밤.txt')
    elif d == "3":
        coreNonRandom('data/documents/애국가.txt')
    elif d == "4":
        coreNonRandom('data/documents/서시.txt')
    elif d == "exit":
        home()
    else:
        print("올바른 접근이 아닙니다.")
        novelpractice()

def home():
    print("""\033[32m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⠀⠀⠀⠀⠀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⣿⣿⣿⡿⠿⠿⠿⠿⠏⠀⠀⠀⢀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿⠀⠀⠀⢀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⢿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠛⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⢠⣿⣿⠻⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⣸⣿⣿⣇⣀⣀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠃⠀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠃⠀⣰⣿⣿⠃⠀⢿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣧⣀⣀⣀⣀⣤⣴⣿⣿⡿⢻⣿⣿⡄⠀⠀⠀⠀⢀⣿⣿⡏⠀⠀⠀⠀⠀⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡟⠀⣼⣿⡿⠁⠀⠀⢸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠋⠀⠈⢿⣿⣷⠀⠀⠀⠀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⢠⣾⣿⡟⠁⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣧⣾⣿⡟⠁⠀⠀⠀⠸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣧⠀⠀⢰⣿⣿⠃⠀⠀⠀⠀⠀⠀⢠⣿⣿⡏⠀⠀⠀⠀⣠⣿⣿⣿⣤⣤⣤⣤⣤⣤⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡆⢀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠃⠀⠀⠀⣴⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⡀⠀⣀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⢀⣾⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣄⣀⣀⣠⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⡏⠀⢠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⢿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣴⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    print("\033[34m\n- - ~\033[36m ~ = =\033[0m U S E R C R U S E R  P Y T A J A\033[31m\033[3m  βeta\033[0m\033[36m = = ~\033[34m ~ - -\n\033[0m\n\033[1m파이타자에 오신 것을 환영합니다! \n`help`\033[0m를 입력해 \033[1m도움말\033[0m을 \033[1m열람\033[0m하실 수 있습니다.\n")
    print("\033[36m명령어 입력 \033[0m\n1 : 기본자리 || 2 : 왼손자리 || 3 : 오른손자리\n4 : 숫자자리 || 5 : 낱말연습 || 6 : 단문연습\n7 : 장문연습\n\n\033[90m(help, exit 등 기타 명령)\n\033[0m")
    def inputValue():
        iV = input(format(os.getlogin())+"@pytaja ~ $ ")
        if iV == "help":
            print("\033[34m\n- - ~\033[36m ~ = =\033[0m 도 움 말\033[36m = = ~\033[34m ~ - -\n\n\033[0m\033[1m도움말에 오신 것을 환영합니다\n\033[0m이곳에서는 \033[1m파이타자의 사용법\033[0m을\n\033[1m익힐 수 있습\033[0m니다\033[0m \n\n\033[1m기본자리 연습 - - - - \n\033[0m키보드의 기본 자판 배열을 익힙니다.\n\033[90m(KO-KR 101 Key 전체) \033[0m\033[1m\n\n왼손자리 연습 - - - - \033[0m\n키보드의 왼손 자판 배열을 익힙니다.\n\033[90m자음, 초성 (KO-KR)\033[0m\n\n\033[0m\033[1m오른손자리 연습 - - - - \033[0m\n키보드의 오른손 자판 배열을 익힙니다.\n\033[90m모음(단모음, 이중모음 포함) (KO-KR)\n\033[0m\n\033[1m명령어 도움말\nmenu : \033[0m메뉴로 돌아갑니다.\n\033[1mabout : \033[0m프로그램 정보를 확인합니다.\n\033[1mcredits : \033[0m이 프로그램을 만든 사람들을 열람합니다.\n\033[1mcopyright : \033[0m이 프로그램의 저작권을 열람합니다.\n\033[1mexit : \033[0m프로그램을 종료합니다.\n\033[1mtime : \033[0m시간을 표시합니다.\n\033[1mclear : \033[0m기록을 삭제합니다.\n")
            inputValue()
        elif iV == "about":
            print("\033[34m\n- - ~\033[36m ~ = =\033[0m 정 보\033[36m = = ~\033[34m ~ - -\n\n\033[0m\033[1mUSERCRUSER PYTAJA - 파이타자\n\033[0m\033[90m베타 릴리스 1.0\n\n\033[0mPowered by Python 3\nVersion 3.12.2[GCC 11.4.0]\n\n\033[1m사용한 라이브러리\n\033[0mtqdm - 반복분 진행률 바\nhgtk - 한글 자음 모음 분리 저장\nstatistics - 오타율, 타수, 정확도 등의 평균\n\033[90m\033[3m\n(c) Copyright 2023-2025 USERCRUSER. All Rights Reserved.\nhttps://usercruser.neocities.org/\nhttps://ishowfeed.neocities.org/\033[0m")
            inputValue()
        elif iV == "credits":
            print("\033[34m\n- - ~\033[36m ~ = =\033[0m 만 든  사 람 들\033[36m = = ~\033[34m ~ - -\n\n\033[0m\033[1mExecutive Producer\n\033[0mUSERCRUSER\n\n\033[1mUI/UX Design\n\033[0mUSERCRUSER\n\n\033[1mPrograming Manager\n\033[0mUSERCRUSER\n\n\033[1mSpecial Thanks\n\033[0mSangbeom Park\nnkj2001(블로그 글을 참고했어요)\n\n\033[3m\033[90m(c) Copyright 2023-2025 USERCRUSER. All Rights Reserved.\033[0m")
            inputValue()
        elif iV == "copyright":
            print("\033[34m\n- - ~\033[36m ~ = =\033[0m 저 작 권\033[36m = = ~\033[34m ~ - -\033[0m\n\n파이썬 저작권\n\033[90m\033[3m(c) Copyright 2001-2024 Python Software Foundation. All Rights Reserved.\n(c) Copyright 2000 BeOpen.com. All Rights Reserved.\n(c) Copyright 1995-2001 Corporation for National Research Initiatives. All Rights Reserved.\n(c) Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam. All Rights Reserved.\n\n\033[0m파이타자 저작권\033[90m\033[3m\n(c) Copyright 2023-2025 USERCRUSER. All Rights Reserved.\033[0m")
            inputValue()
        elif iV == "exit":
            exit()
        elif iV == "time":
            print("\033[34m\n- - ~\033[36m ~ = =\033[0m 시 간\033[36m = = ~\033[34m ~ - -\n\033[0m\n오늘은 . . .",datetime.today().strftime("\n\033[1m%Y년 %m월 %d일 %H시 %M분\033[0m 입니다."))
            inputValue()
        elif iV == "menu":
            home()
        elif iV == "neofetch":
            print("경고 : 이 명령을 실행시키려면 linux : fastfetch / mac : neofetch / win32 : winfetch가 깔려 있어야 합니다.\n위 프로그램을 받지 않은 경우 이 명령을 제대로 실행 시킬 수 없습니다.\n이 명령은 client.py `def clearThing()`, line 22를 테스트하는 과정에서 만들어졌습니다.")
            neofetch()
            print("멋진 하드웨어를 장착하고 계시는군요?")
            inputValue()
        elif iV == "clear":
            clearThing()
            inputValue()
        elif iV == "1":
            core('data/gibonjari.txt')
        elif iV == "2":
            core('data/leftjari.txt')
        elif iV == "3":
            core('data/rightjari.txt')
        elif iV == "4":
            core('data/numberjari.txt')
        elif iV == "5":
            core('data/letterpractice.txt')
        elif iV == "6":
            core('data/sentencepractice.txt')
        elif iV == "7":
            novelpractice()
        else:
            print(iV,"(이)는 올바른 명령이 아닙니다.")
            inputValue()
    inputValue()
home()
