from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ClubBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)


class ClubCreate(ClubBase):
    pass


class ClubUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)


class Club(ClubBase):
    id: UUID
