import builtins
import pytest
from ui import prompt_items

@pytest.mark.parametrize("n, weights_str, profits_str, capacity", [
    ("8", "1 2 3 4 5 6 7 8", "10 20 30 40 50 60 70 80", "50"),
])
def test_prompt_items_valid(monkeypatch, n, weights_str, profits_str, capacity):
    inputs = iter([n, weights_str, profits_str, capacity])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    weights, profits, cap = prompt_items()
    assert weights == list(map(int, weights_str.split()))
    assert profits == list(map(int, profits_str.split()))
    assert cap == int(capacity)
