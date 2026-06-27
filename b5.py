from fastapi import FastAPI

app = FastAPI(
    title="Course Management API",
    description="API quản lý khóa học",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Course Management API"
    }


# 1. Xem danh sách khóa học
@app.get("/courses")
def get_courses():
    return {
        "message": "Lấy danh sách tất cả khóa học"
    }


# 2. Xem chi tiết khóa học
@app.get("/courses/detail")
def get_course_detail():
    return {
        "message": "Hiển thị chi tiết khóa học"
    }


# 3. Thêm khóa học
@app.post("/courses")
def create_course():
    return {
        "message": "Thêm khóa học thành công"
    }


# 4. Cập nhật khóa học
@app.put("/courses/update")
def update_course():
    return {
        "message": "Cập nhật khóa học thành công"
    }


# 5. Xóa khóa học
@app.delete("/courses/delete")
def delete_course():
    return {
        "message": "Xóa khóa học thành công"
    }


# 6. Thống kê khóa học
@app.get("/courses/statistics")
def course_statistics():
    return {
        "message": "Thống kê số lượng khóa học"
    }


# Endpoint mở rộng 1
@app.get("/courses/popular")
def popular_courses():
    return {
        "message": "Danh sách khóa học phổ biến"
    }


# Endpoint mở rộng 2
@app.get("/courses/newest")
def newest_courses():
    return {
        "message": "Danh sách khóa học mới nhất"
    }