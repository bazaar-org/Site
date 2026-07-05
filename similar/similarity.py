from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from parser import App


def build_document(app: App) -> str:
    parts = [
        (app.name or "") * 3,
        (app.summary or "") * 3,
        (app.description or ""),
        " ".join(app.categories) * 2,
        " ".join(app.keywords) * 2,
        (app.developer_name or ""),
    ]
    return " ".join(parts)


def find_similar_apps(apps: list[App], top_n: int = 6) -> dict[str, list[tuple[str, float]]]:
    docs = [build_document(a) for a in apps]
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=20000,
        ngram_range=(1, 2),
        sublinear_tf=True,
    )
    matrix = vectorizer.fit_transform(docs)
    sim_matrix = cosine_similarity(matrix, dense_output=False)
    results = {}
    for i, app in enumerate(apps):
        row = sim_matrix[i].toarray().ravel()
        row[i] = -1
        for j, other in enumerate(apps):
            if other.developer_name and app.developer_name and other.developer_name == app.developer_name:
                row[j] = -1
        top_indices = np.argpartition(row, -top_n)[-top_n:]
        top_indices = top_indices[np.argsort(row[top_indices])[::-1]]
        results[app.id] = [
            (apps[j].id, float(row[j])) for j in top_indices if row[j] > 0
        ]
    return results
