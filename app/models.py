# # app/models.py
# from sqlmodel import SQLModel, Field
# from typing import Optional
# from datetime import datetime, timedelta

# class OAuthToken(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: str
#     access_token: str
#     refresh_token: Optional[str]
#     expires_in: Optional[int]
#     token_type: Optional[str]
#     scope: Optional[str]
#     created_at: datetime = Field(default_factory=datetime.utcnow)

#     @property
#     def is_expired(self) -> bool:
#         if self.expires_in is None:
#             return False
#         expiration_time = self.created_at + timedelta(seconds=self.expires_in)
#         return datetime.utcnow() >= expiration_time
