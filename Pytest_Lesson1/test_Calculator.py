#! /usr/bin/python
# -*- coding: utf-8 -*-

# @time     : 2021/02/08
# @Author   : Zong.D
# @file     : test_Calculator.py
# @Software : PyCharm

import sys
import pytest
import yaml
import allure


sys.path.append('..')
print(sys.path)
from PythonModule.Calculator import Calculator

def get_datas(name, type):
    with open("./testdatas/datas.yml") as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name][type]['datas']
        ids = all_datas[name][type]['ids']
        return (datas,ids)

# @pytest.fixture(scope="class",autouse=True)
# def login():
#         print("\n开始计算")
#         calc = Calculator()
#         yield calc
#         print("结束计算")

@allure.feature("计算器")
class TestCalc:

    add_int_datas:list = get_datas('add','int')
    print(add_int_datas)
    add_float_datas:list = get_datas('add','float')
    div_int_datas:list = get_datas('div','int')
    # 前置条件
    def setup_class(self):
        self.calc = Calculator()

    @allure.story("相加功能")
    @pytest.mark.parametrize("a,b,result",add_int_datas[0],ids=add_int_datas[1])
    def test_add(self, calcfixture, a, b, result):
        print(f"a={a} , b={b} , result={result}")
        assert result == round(self.calc.add(a,b),2)

    # done: 相除功能
    @allure.story("相除功能")
    @pytest.mark.parametrize("a,b,result", div_int_datas[0], ids=div_int_datas[1])
    def test_div(self, calcfixture, a, b, result):
        print(f"a={a} , b={b} , result={result}")
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                assert result == self.calc.div(a,b)
        else:
            assert result == self.calc.div(a, b)


    # @pytest.mark.parametrize("a,b,expect", [
    #     [0.1,0.1,0.2],
    #     [0.1,0.2,0.3]
    # ])
    # def test_add(self, a, b, expect):
    #     assert expect == round(self.calc.add(a,b),3)
    #     print(round(self.calc.add(a,b),2))
