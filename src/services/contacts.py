from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from datetime import date, timedelta

from repository.contacts import ContactRepository
from schemas import ContactModel


class ContactService:
    def __init__(self, db: AsyncSession):
        self.contact_repository = ContactRepository(db)

    async def create_contact(self, body: ContactModel):
        return await self.contact_repository.create_contact(body)

    async def get_contacts(self, skip: int, limit: int):
        return await self.contact_repository.get_contacts(skip, limit)

    async def get_contact(self, contact_id: int):
        return await self.contact_repository.get_contact_by_id(contact_id)

    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.contact_repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.contact_repository.remove_contact(contact_id)

    async def search_contacts(
        self,
        skip,
        limit,
        first_name: Optional[str],
        last_name: Optional[str],
        email: Optional[str],
    ) -> List[ContactModel]:
        return await self.contact_repository.search_contacts(
            skip, limit, first_name, last_name, email
        )

    async def get_upcoming_birthdays(
        self, days: int, skip: int, limit: int
    ) -> List[ContactModel]:
        today = date.today()
        next_date = today + timedelta(days=days)
        return await self.contact_repository.get_upcoming_birthdays(
            today, next_date, skip, limit
        )
