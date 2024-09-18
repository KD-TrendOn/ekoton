from .base import Base
from .moderator import Moderator
from .flora_fauna import FloraFauna
from .submission import Submission
from .task import Task
from .report import Report

# Убедись, что все модели импортируются здесь
__all__ = [
    "Base",
    "Moderator",
    "FloraFauna",
    "Submission",
    "Task",
    "Report"
]
