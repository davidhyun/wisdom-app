from apps.utils.database import SessionDep
from apps.quote.model import Quotes, Authors
from sqlmodel import select


def get_quote_by_id(quote_id: int, session: SessionDep):
    query = (
        select(Authors.author_title, Authors.author_name, Quotes.content)
        .join(Quotes, Quotes.author_id == Authors.author_id)
        .where(Quotes.quote_id == quote_id)
    )
    
    result = session.exec(query).one()._asdict()
    
    return result