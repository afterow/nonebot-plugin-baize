from typing import Optional, List

from pydantic import BaseModel
import os


class Config(BaseModel):
    baize_question_path: str = os.path.join(os.path.dirname(__file__), "questions.json")
    baize_verify_timeout: int = 60  # 验证超时时间 (秒)
    baize_on_success: Optional[str] = None  # 验证成功后执行的操作 (例如 "approve")
    baize_on_fail: Optional[str] = None  # 验证失败后执行的操作 (例如 "kick")
