from apps.utils.database import SessionDep
from apps.quote.model import Quotes
from sqlmodel import select


def get_quote_by_id(quote_id: int, session: SessionDep):
    query = select(Quotes).where(Quotes.quote_id == quote_id)
    quote = session.exec(query).one()
    return quote