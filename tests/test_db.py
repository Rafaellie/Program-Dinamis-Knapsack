import pytest
from knapsack import hitung_profit_maksimal, cari_item_yang_dipilih

def test_knapsack_basic():
    weights = [2, 3, 4]
    profits = [3, 4, 5]
    capacity = 5
    memo = hitung_profit_maksimal(weights, profits, capacity)
    picked = cari_item_yang_dipilih(memo, weights, profits, capacity)
    assert sum(weights[i] for i in picked) <= capacity
    assert sum(profits[i] for i in picked) == memo[len(weights)][capacity]

def test_knapsack_all_items_fit():
    weights = [1, 2, 3]
    profits = [10, 20, 30]
    capacity = 6
    memo = hitung_profit_maksimal(weights, profits, capacity)
    picked = cari_item_yang_dipilih(memo, weights, profits, capacity)
    assert set(picked) == {0, 1, 2}

def test_knapsack_none_fit():
    weights = [10, 20, 30]
    profits = [60, 100, 120]
    capacity = 5
    memo = hitung_profit_maksimal(weights, profits, capacity)
    picked = cari_item_yang_dipilih(memo, weights, profits, capacity)
    assert picked == []
