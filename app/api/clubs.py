from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.schemas import Club as ClubSchema
from app.api.schemas import ClubCreate, ClubUpdate
from app.service.clubs import get_club_service
from app.service.interfaces import ClubServiceProtocol
from models.club import Club

router = APIRouter(prefix="/clubs", tags=["clubs"])


@router.post("", response_model=ClubSchema, status_code=status.HTTP_201_CREATED)
def create_club(
    payload: ClubCreate,
    service: ClubServiceProtocol = Depends(get_club_service),
) -> Club:
    club = Club(**payload.model_dump())
    result = service.create(club)
    if not result.success or result.data is None:
        raise HTTPException(
            status_code=result.status_code or status.HTTP_400_BAD_REQUEST,
            detail=result.message or "Request failed",
        )
    return result.data


@router.get("/{club_id}", response_model=ClubSchema)
def get_club(
    club_id: UUID, service: ClubServiceProtocol = Depends(get_club_service)
) -> Club:
    result = service.get(club_id)
    if not result.success or result.data is None:
        raise HTTPException(
            status_code=result.status_code or status.HTTP_400_BAD_REQUEST,
            detail=result.message or "Request failed",
        )
    return result.data


@router.put("/{club_id}", response_model=ClubSchema)
def update_club(
    club_id: UUID,
    payload: ClubUpdate,
    service: ClubServiceProtocol = Depends(get_club_service),
) -> Club:
    result = service.update(club_id, payload.model_dump(exclude_unset=True))
    if not result.success or result.data is None:
        raise HTTPException(
            status_code=result.status_code or status.HTTP_400_BAD_REQUEST,
            detail=result.message or "Request failed",
        )
    return result.data


@router.delete("/{club_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_club(
    club_id: UUID, service: ClubServiceProtocol = Depends(get_club_service)
) -> None:
    result = service.delete(club_id)
    if not result.success:
        raise HTTPException(
            status_code=result.status_code or status.HTTP_400_BAD_REQUEST,
            detail=result.message or "Request failed",
        )
