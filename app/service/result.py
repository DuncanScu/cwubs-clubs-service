from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Result(Generic[T]):
    success: bool
    data: Optional[T] = None
    message: Optional[str] = None
    status_code: Optional[int] = None

    @staticmethod
    def ok(data: T) -> "Result[T]":
        return Result(success=True, data=data)

    @staticmethod
    def fail(message: str, status_code: Optional[int] = None) -> "Result[T]":
        return Result(success=False, data=None, message=message, status_code=status_code)
