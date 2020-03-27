import pytest
from web.dao.intellectual_property import *


def test_get_ipc_map(init_test_app):
    results = get_ipc_map(depth=0)
    assert len(results) == 8


def test_get_total_number(init_test_app):
    result = get_total_patent_number()
    assert isinstance(result, int)
    assert result > 0


def test_count_patents_with_ipc(init_test_app):
    ipc_list = ['A', 'B']
    length = 1
    results = count_patents_with_ipc(length, ipc_list, len(ipc_list))

    assert isinstance(results, list)
    assert len(results) == len(ipc_list)
    first_datum = results[0]
    assert 'code' in first_datum
    assert 'amount' in first_datum


if __name__ == '__main__':
    pytest.main([__file__, '-s'])