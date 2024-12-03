from fastapi import APIRouter
from apps.utils.database import SessionDep
from apps.quote.service import get_quote_by_id
router = APIRouter()

@router.get("/quotes/{quote_id}")
def get_quotes(quote_id: int, session: SessionDep):
    
    quote = get_quote_by_id(quote_id, session)
    context = {
        "author_id": quote.author_id,
        "content": quote.content,
    }
    
    return context