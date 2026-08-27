from sqlalchemy import Integer, String, Numeric
from sqlalchemy import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from database import Base


class Prodict(Base):
    __tablename__="products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    photo_path: Mapped[str] = mapped_column(String(512) , nullable=False)
    attributes: Mapped[dict] = mapped_column(JSONB, default=dict, server_default="{}")
    