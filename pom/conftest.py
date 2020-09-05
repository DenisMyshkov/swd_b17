import pytest
from pom.app.application import Application


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app
