from __future__ import annotations

from typing import Mapping
from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from app.repository.db import get_db
from app.repository.interfaces import Repository
from app.service.result import Result
from models.club import Club
from shared.base import BaseRepository


class ClubService:
    def __init__(self, repo: Repository[Club, UUID]) -> None:
        self._repo = repo

    def create(self, club: Club) -> Result[Club]:
        exists = self._repo.exists(club.id)
        if exists:
            return Result.fail("Club already exists", status_code=400)
        created = self._repo.create(club)
        return Result.ok(created)

    def get(self, club_id: UUID) -> Result[Club]:
        club = self._repo.get(club_id)
        if club is None:
            return Result.fail("Club not found", status_code=404)
        return Result.ok(club)

    def update(self, club_id: UUID, data: Mapping[str, object]) -> Result[Club]:
        club = self._repo.get(club_id)
        if club is None:
            return Result.fail("Club not found", status_code=404)
        for key, value in data.items():
            setattr(club, key, value)
        updated = self._repo.save(club)
        return Result.ok(updated)

    def delete(self, club_id: UUID) -> Result[None]:
        existing = self._repo.get(club_id)
        if existing is None:
            return Result.fail("Club not found", status_code=404)
        self._repo.delete(existing)
        return Result.ok(None)


def get_club_repo(db: Session = Depends(get_db)) -> Repository[Club, UUID]:
    return BaseRepository(db, Club)


def get_club_service(repo: Repository[Club, UUID] = Depends(get_club_repo)) -> ClubService:
    return ClubService(repo=repo)
