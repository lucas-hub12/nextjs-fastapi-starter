from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random
import korean_age_calculator as kac
import sys
import subprocess

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")
command = "cat /etc/os-release"

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/{birthday}")
def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이를 포함한 JSON 응답
    """
    today = date.today()
    birth_date =datetime.strptime(birthday, "%Y-%m-%d").date()
   
    # 파이썬 버전 확인하기
    version = sys.version

    # os 정보 확인하기
    os = subprocess.run(command, shell=True, capture_output=True, text=True)

    if os.returncode == 0:
        for line in os.stdout.splitlines():
             if line.startswith("PRETTY_NAME"):
                 pretty_name = line.split("=", 1)[1].strip('"')
                 break
    # 램덤으로 이름이 나오기
    names = ["조민규","강현룡","권오준","서민혁","백지원","안재영","전희진","배형균","조성근"]
    random_name = random.choice(names)
    # 한국식 나이 계산
    kage = kac.how_korean_age(year_of_birth=birth_date.year)

    # 기본 나이는 올해에서 태어난 해를 뺀 값
    age = today.year - birth_date.year  
    zodiac_animals = [
                      "🐀 Rat", # 자 - 쥐
                      "🐂 Ox", # 축 - 소
                      "🐅 Tiger", # 인 - 호랑이
                      "🐇 Rabbit", # 묘 - 토끼
                      "🐉 Dragon", # 진 - 용
                      "🐍 Snake", # 사 - 뱀
                      "🐎 Horse", # 오 - 말
                      "🐐 Goat", # 미 - 양
                      "🐒 Monkey", # 신 - 원숭이
                      "🐓 Rooster", # 유 - 닭
                      "🐕 Dog", # 술 - 개
                      "🐖 Pig" # 해 - 돼지
                      ]
    zodiac_index = (birth_date.year - 4) % 12 # 4는 기준연도(쥐 띠 시작) 보정값
    zodiac = zodiac_animals[zodiac_index]
    
    # 생일이 아직 오지 않았다면 나이를 1살 줄임
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age = age - 1
    
    return {
            "birthday": birthday,
            "age": f"만나이는:{age}살- 한국나이는:{kage}살 - 당신의 띠는:{zodiac} - 발표자는:{random_name}!!",
            "basedate": str(today),
            "message": "Age calculated successfully!",
            "version": version,
            "os-release": pretty_name
            }
