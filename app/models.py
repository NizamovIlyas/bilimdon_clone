from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(DateTime)
    joined_at = Column(DateTime, default=datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    games = relationship("Game", back_populates="owner")
    participations = relationship("Participation", back_populates="user")

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    topic = Column(String)
    score = Column(Integer, default=0)
    start_time = Column(DateTime, default=datetime.now(timezone.utc))
    end_time = Column(DateTime)

    owner = relationship("User", back_populates="games")
    participations = relationship("Participation", back_populates="game")
    questions = relationship("GameQuestion", back_populates="game")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    topic = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    owner = relationship("User")
    options = relationship("Option", back_populates="question")

class Option(Base):
    __tablename__ = "options"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    title = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    question = relationship("Question", back_populates="options")

class Participation(Base):
    __tablename__ = "participations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    start_time = Column(DateTime, default=datetime.now(timezone.utc))
    end_time = Column(DateTime)
    gained_score = Column(Integer, default=0)
    registered_at = Column(DateTime, default=datetime.now(timezone.utc))

    user = relationship("User", back_populates="participations")
    game = relationship("Game", back_populates="participations")

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    option_id = Column(Integer, ForeignKey("options.id"))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    is_correct = Column(Boolean, default=False)
