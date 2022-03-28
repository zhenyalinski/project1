"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">Glossary</a>' in response.data
    assert b'<a class="nav-link" href="/page2">AAA</a>' in response.data
    assert b'<a class="nav-link" href="/page3">OOP</a>' in response.data
    assert b'<a class="nav-link" href="/page4">SOLID</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("page1")
    assert response.status_code == 200
    assert b"Glossary" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("page2")
    assert response.status_code == 200
    assert b"AAA" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("page3")
    assert response.status_code == 200
    assert b"OOP" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("page4")
    assert response.status_code == 200
    assert b"SOLID" in response.data
