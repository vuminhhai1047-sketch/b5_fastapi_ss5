




from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Course(BaseModel):
    id: int
    code: str
    name : str
    level : str
    price : int
    status : str
    teacher : str

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "Beginner",
        "price": 1500000,
        "status": "Open",
        "teacher": "Nguyen Van A"
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "Beginner",
        "price": 2000000,
        "status": "Open",
        "teacher": "Tran Thi B"
    },
    {
        "id": 3,
        "code": "DB201",
        "name": "Database Design",
        "level": "Intermediate",
        "price": 2500000,
        "status": "Closed",
        "teacher": "Le Van C"
    },
    {
        "id": 4,
        "code": "JS101",
        "name": "JavaScript Basic",
        "level": "Beginner",
        "price": 1800000,
        "status": "Open",
        "teacher": "Pham Van D"
    },
    {
        "id": 5,
        "code": "WD301",
        "name": "Web Development",
        "level": "Advanced",
        "price": 3500000,
        "status": "Coming Soon",
        "teacher": "Hoang Van E"
    }
]


@app.get("/courses")
def get_courses():
    return {
        "message" : "Danh sách khóa học",
        "data" : courese
    }


@app.get("/courses/{detail}")
def get_courses_detail(detail : int):
    if detail <= 0:
        raise HTTPException (
            status_code = 404,
            detail = "Detail phải lớn hơn 0"
        )
    
    for course in courses:
        if courses["id"] == detail:
            return course
    
    raise HTTPException(
        status_code = 404,
        detail = "Không tìm thấy id"
    )


@app.post("/courses")
def post_courses(course : Course):
    
    for cours


