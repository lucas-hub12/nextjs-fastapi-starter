from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

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

    # 기본 나이는 올해에서 태어난 해를 뺀 값
    age = today.year - birth_date.year  
    zodiac_animals = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", "원숭이", "닭", "개", "돼지"]
    zodiac_index = (birth_date.year - 4) % 12 # 4는 기준연도(쥐 띠 시작) 보정값
    zodiac = zodiac_animals[zodiac_index]
    
    # 생일이 아직 오지 않았다면 나이를 1살 줄임
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age = age - 1
    
    return {
            "birthday": birthday,
            "age": f"{age}살 - 당신의 띠는:{zodiac}",
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }
