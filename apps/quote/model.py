from sqlmodel import SQLModel, Field

    
class Authors(SQLModel, table=True):
    author_id: int = Field(primary_key=True)
    author_name: str
    author_title: str
    author_desc: str
    birth_year: int
    death_year: int
    
class Quotes(SQLModel, table=True):
    quote_id: int = Field(primary_key=True)
    author_id: int = Field(foreign_key="authors.author_id")
    content: str
    language: str
    translated_content: str