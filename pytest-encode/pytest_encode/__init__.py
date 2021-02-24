#! /usr/bin/python
# -*- coding: utf-8 -*-
from typing import List


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: "List[Item]"
) -> None:
    # Separate parametrized setups.
    # items是所有测试用例
    print(items)
    # 改变pytest.mark默认编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
