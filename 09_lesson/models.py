from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Определяем базовый класс для моделей
Base = declarative_base()


# Определяем модель Subject
class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True, index=True)
    subject_title = Column(String, index=True)


# Настройка подключения к базе данных
DATABASE_URL = "postgresql://postgres:Skypro2024@localhost:5432/Sergei"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
