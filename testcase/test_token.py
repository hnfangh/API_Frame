import pytest
import yaml

from api.get_token import GetToken


class TestToken:

    def setup(self):
        self.gt = GetToken()

    @pytest.mark.parametrize()
    def test_get_token(self):
        print(self.gt.getToken())
