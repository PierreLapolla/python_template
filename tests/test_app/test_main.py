import logging

import pytest

from app.__main__ import main


def test_main_logs_greeting(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO):
        main()
    assert "Hello from python-template!" in caplog.text
