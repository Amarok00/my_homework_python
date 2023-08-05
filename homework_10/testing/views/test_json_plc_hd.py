def test_get_post_json_placle(client):
    response = client.get("/placeholder/")
    assert response.status_code == 200
