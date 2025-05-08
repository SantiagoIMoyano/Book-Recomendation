from src.model.inference import get_recommends

def test_book_recommendation():
    title = "Where the Heart Is (Oprah's Book Club (Paperback))"
    recommends = get_recommends(title)
    assert recommends[0] == title

    recs = recommends[1]
    expected_titles = [
        "I'll Be Seeing You",
        "The Weight of Water",
        "The Surgeon",
        "I Know This Much Is True"
    ]
    expected_dists = [0.8, 0.77, 0.77, 0.77]

    for i in range(2):
        title_i, dist_i = recs[i]
        assert title_i in expected_titles
        assert abs(dist_i - expected_dists[i]) < 0.05