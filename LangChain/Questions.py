from pydantic import BaseModel, Field, validator
from typing import List

class MultipleChoice(BaseModel):
    choice_ans: str = Field(description="multiple choice answer")

class Question(BaseModel):
    question: str = Field(description="the question being asked")
    #answer: str = Field(description="answer to the question")
    MultipleChoices: List[MultipleChoice]
    correct_ans: str = Field(description="the correct answer")

    # You can add custom validation logic easily with Pydantic.
    @validator("question")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question!")
        return field


class Questions(BaseModel):
    Questions: List[Question]
