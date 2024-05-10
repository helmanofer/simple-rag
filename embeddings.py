from typing import List

from settings import Settings


def co_embed(texts: List[str]):
    assert isinstance(texts, list)
    import cohere

    settings = Settings()

    co = cohere.Client(api_key=settings.cohere_key)
    res: cohere.EmbedResponse = co.embed(
        texts=texts, model="embed-multilingual-v3.0", input_type="search_document"
    )
    return res.embeddings
