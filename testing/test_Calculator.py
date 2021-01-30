#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pytest
import yaml

sys.path.append('C:\\Users\\96918\\PycharmProjects\\Hogwarts_DZH')
print(sys.path)
from PythonModule.Calculator import Calculator


def get_add_datas():
    with open("./testdatas/datas.yml") as f:
        datas = yaml.safe_load(f)
        return (datas['add']['datas'],datas['add']['ids'])


def get_div_datas():
    with open("./testdatas/datas.yml") as f:
        datas = yaml.safe_load(f)
        return (datas['div']['datas'],datas['div']['ids'])


class TestCalc:

    datas:list=get_add_datas()
    datas1:list = get_div_datas()
    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_add(self,a, b, result):
        print(f"a={a} , b={b} , result={result}")
        assert result == self.calc.add(a,b)

    # done: 相除功能

    @pytest.mark.parametrize("a,b,result", datas1[0], ids=datas1[1])
    def test_div(self,a, b, result):
        print(f"a={a} , b={b} , result={result}")
        if b == 0:
            assert 1==0, '除数不能为0'
        else:
            assert result == self.calc.div(a,b)

