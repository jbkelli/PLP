def count_publications_by_year(data):
    """Count the number of publications per year."""
    return data['year'].value_counts().sort_index()

def top_journals(data, top_n=10):
    """Identify the top N journals by publication count."""
    return data['journal'].value_counts().head(top_n)