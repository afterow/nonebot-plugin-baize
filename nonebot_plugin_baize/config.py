from typing import Optional, List

import os
from pydantic import BaseModel
from pydantic import Field


class Config(BaseModel):
    baize_question_path: str = os.path.join(os.path.dirname(__file__), "questions.json")
    baize_verify_timeout: int = Field(
        default=60,
        alias="BAIZE_VERIFY_TIMEOUT",
    )
