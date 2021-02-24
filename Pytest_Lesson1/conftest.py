#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from typing import List
sys.path.append('../')
print(sys.path)
import pytest
from PythonModule.Calculator import Calculator



@pytest.fixture(scope="class")
def calc():
    print("计算器测试开始......")
    calc = Calculator()
    yield calc
    print("计算器测试结束......")
# @pytest.fixture(scope="function")
# def calc():
#     print("\n计算开始......")
    # calc = Calculator()
    # yield calc
@pytest.fixture(scope="function")
def calcfixture():
    print("\n计算开始...")
    yield
    #运行结束后
    print("\n计算结束...")

# 使用pytesthook函数
def pytest_collection_modifyitems(
        session: "Session",config:"Config" ,items: List["Item"]
) -> None:
    # Separate parametrized setups.
    #items是所有测试用例
    print(items)
    #改变pytest.mark默认编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
