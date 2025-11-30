def test_create_project(client, token):
    res = client.post("/projects", json={"name": "My Project"}, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 201
    assert res.json()["name"] == "My Project"
