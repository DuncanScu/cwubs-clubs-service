from __future__ import annotations

from typing import Optional, Protocol, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")


class Repository(Protocol[T, ID]):
    def create(self, obj: T) -> T: ...

    def get(self, obj_id: ID) -> Optional[T]: ...

    def exists(self, obj_id: ID) -> bool: ...

    def save(self, obj: T) -> T: ...

    def delete(self, obj: T) -> None: ...
