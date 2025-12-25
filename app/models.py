from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, index=True) # Для URL
    description = Column(Text, nullable=False)
    image_url = Column(String, nullable=True)      # Ссылка на скриншот
    tech_stack = Column(String)                    # "Python, FastAPI"
    github_link = Column(String, nullable=True)
    demo_link = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    order = Column(Integer, default=0)             # Чтобы менять порядок вывода
