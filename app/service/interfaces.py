from __future__ import annotations

from typing import Mapping, Protocol
from uuid import UUID

from app.service.result import Result
from models.club import Club


class ClubServiceProtocol(Protocol):
    def create(self, club: Club) -> Result[Club]: ...

    def get(self, club_id: UUID) -> Result[Club]: ...

    def update(self, club_id: UUID, data: Mapping[str, object]) -> Result[Club]: ...

    def delete(self, club_id: UUID) -> Result[None]: ...
