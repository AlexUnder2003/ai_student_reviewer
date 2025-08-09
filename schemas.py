import uuid
from pydantic import BaseModel


class Answer(BaseModel):
    question_id: int
    question_text: str
    answer: str


class AnswerReview(BaseModel):
    question_id: int
    right: bool
    text: str
    review: str


class QuizInput(BaseModel):
    answers: list[Answer]


class QuizReview(BaseModel):
    answers: list[AnswerReview]
    total: int
