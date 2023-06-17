from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get('/hotels')
def get_hotels(
    search_args: HotelSearchArgs = Depends(),
) -> list[SHotel]:
    hotels = [
        SHotel(
            address='ул. Гагарина, 1, Алтай',
            name='Super Hotel',
            stars=5,
        )
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
def add_booking(booking: SBooking):
    return booking
