from fastapi import FastAPI, Request, Depends, HTTPException, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    title = Column(String)
    body = Column(String)
  class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class PostCreate(BaseModel):
    title: str
    body: str
  Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-key-here",  
    session_cookie="blog_session"
)

templates = Jinja2Templates(directory="templates")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
      ("/", response_class=HTMLResponse)
async def list_posts(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    user = request.session.get("user")
    return templates.TemplateResponse(
        "list.html",
        {"request": request, "posts": posts, "user": user}
    )
"/signup", response_class=HTMLResponse)
async def signup_ui(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})
"/signup")
async def signup(
    username: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="使用者名稱已註冊")
    new_user = User(username=username, password=password, email=email)
    db.add(new_user)
    db.commit()
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
"/login", response_class=HTMLResponse)
async def login_ui(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
"/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="帳號或密碼錯誤")
    request.session["user"] = {"username": username}
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
"/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
"/post/new", response_class=HTMLResponse)
async def new_post(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="未登入")
    return templates.TemplateResponse("new_post.html", {"request": request})
"/post")
async def create_post(
    request: Request,
    title: str = Form(...),
    body: str = Form(...),
    db: Session = Depends(get_db)
):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="未登入")
    new_post = Post(username=user["username"], title=title, body=body)
    db.add(new_post)
    db.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
"/post/{post_id}", response_class=HTMLResponse)
async def show_post(request: Request, post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="找不到該貼文")
    return templates.TemplateResponse("show_post.html", {"request": request, "post": post})
  "/post/{post_id}/delete")
async def delete_post(request: Request, post_id: int, db: Session = Depends(get_db)):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="未登入，無法刪除文章")

    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="找不到該文章")

    if post.username != user["username"]:
        raise HTTPException(status_code=403, detail="你只能刪除自己的文章")

    db.delete(post)
    db.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
