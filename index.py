import logging
from hashlib import md5
from db_models import Document, engine
from embeddings import co_embed as embed

logging.basicConfig(level=logging.DEBUG)


def chuck_text(text, size=1000):
    # split text into words and split into chunks of size
    import nltk

    nltk.word_tokenize(text)
    words = text.split()
    current_chunk = []
    for word in words:
        current_chunk.append(word)
        if len(" ".join(current_chunk)) > size:
            yield " ".join(current_chunk)
            current_chunk = []


def run():
    from sqlmodel import Session

    chunks = list(chuck_text(open("rabin.txt").read()))
    vecs = embed(chunks)
    with Session(engine) as session:
        for chunk, vec in zip(chunks, vecs):
            doc = Document(
                id=md5(chunk.encode("utf-8")).hexdigest(),
                document=chunk,
                embedding=vec,
                meta={
                    "some_metadat": "metadata string",
                },
            )
            session.add(doc)
        session.commit()


run()
