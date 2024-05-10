from typing import List

from sqlmodel import Session

from db_models import engine, Document
from embeddings import co_embed as embed
from sqlmodel import select


def search(query, limit=10) -> List[Document]:
    res = []
    with Session(engine) as session:
        v = embed([query])[0]
        r = session.exec(
            select(Document, Document.embedding.cosine_distance(v))
            .order_by(Document.embedding.cosine_distance(v))
            .limit(limit)
        )
        for a, distance in r:
            res.append(a)
    return res


def QA(query):
    import cohere
    from settings import Settings

    co = cohere.Client(api_key=Settings().cohere_key)
    res = search(query)

    q = f"""
    {'\n'.join([a.document for a in res])}
    
    Based on the above information, answer the following:
    {query}
    """

    chat = co.chat(message=q, model="command-r-plus")
    print(chat.text)


QA("list Yitzhak family. names and relations and date of birth")
