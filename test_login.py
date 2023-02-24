import pytest
from signin import SignIn

@pytest.mark.login
def test_login():
    sign_in = SignIn()

    sign_in.go_to()

    sign_in.login('gis1989', 'Agent88888888!')

    sign_in.logout()

