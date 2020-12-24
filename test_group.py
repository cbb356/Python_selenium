import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destructor)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(name="test_name", header="test_header", footer="test_footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(name="", header="", footer=""))
    app.logout()
