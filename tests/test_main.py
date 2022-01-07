import pytest


class TestMainAdd:

    @pytest.fixture
    def target(self):
        from src.main import add
        return add

    def test_addint(self, target):
        # call
        actual = target(1, 2)

        # verify
        expect = 3
        assert actual == expect
