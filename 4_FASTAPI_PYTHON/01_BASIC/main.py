from fastapi import FastAPI, HTTPException, status, Query, Path, Header, Cookie, UploadFile, File, Form, Response, Depends, BackgroundTasks
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Dict

app = FastAPI(title="FastAPI Minimal Step-by-Step") # 웹 서버가 만들어진다

# ------------------------------------------------------
# health endpoint를 잡으면 status:ok이라는 json 이 반환
# postman : GET http://localhost:8000/health
# ------------------------------------------------------
@app.get("/health") # FastAPI 의 데코레이터 - 웹 요청(GET, POST ...) 처리하도록 핸들러 등록
def health():
    return {"status" : "HelloWorld"}

# ------------------------------------------------------
# 기본경로 설정
# postman : GET http://localhost:8000
# ------------------------------------------------------
@app.get("/") 
def root():
    return {"message" : "Fast API Main EndPoint"}


# ------------------------------------------------------
# Query 파라미터
# GET /echo?name=Alice
# Postman : GET http://localhost:8000/echo?name=Alice
# ------------------------------------------------------
@app.get("/echo") 
def echo(name: str = Query(..., min_length=1, description="이름")): # 파라미터명의 자료형지정(Query 형태로 받을 것임, ...(필수파라미터여부), description(swagger의 이름))
    return {"hello" : name}

# ------------------------------------------------------
# Path + Query 혼합
# ------------------------------------------------------
@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., ge=1), # ge : greater(1보다 커야한다는 의미)
    q: Optional[str] = Query(None, max_length=50), # Optional(null 체크를 하기위한 용도로 사용)
):
    return {"item_id" : item_id, "q":q}

# Pydantic 모델 & 기본 CRUD(in-memory)
class ItemIn(BaseModel):                    # 사용자로부터 전달받는 내용 저장하는 DTO
                                            # BaseModel : webdatabind 역할 (유효성 체크, null 체크 <- Json data를 받으면 python으로 변환하면서 )
    name : str = Field(..., min_length=1)   # 상품명
    price : float = Field(..., gt=0)        # 상품가격
    tags: List[str] = []                    # 태그
    in_stock : bool = True                  # 재고여부

class ItemOut(BaseModel):                    
    id : int
    name : str = Field(..., min_length=1)   
    price : float = Field(..., gt=0)        
    tags: List[str] = []                    
    in_stock : bool = True                  

# id 생성하는 작업
_next_id = 1
def _gen_id() -> int: # 정수형데이터로 반환자료형 명시
    global _next_id
    val = _next_id
    _next_id += 1
    return val

# ':' = type hint 문법
DB : Dict[int, ItemOut] = {} # 자료형 제안 : Dict[key는 자료형, value는 ItemOut으로] 
@app.post("/items", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemIn): # payload : request Body 부분이라고 생각
    new_id = _gen_id()
    item = ItemOut(id=new_id, name=payload.name, price=payload.price, tags=payload.tags, in_stock=payload.in_stock)
    DB[new_id] = item
    # print("ItemIn", payload)
    return item

