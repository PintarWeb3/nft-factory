#!/usr/bin/python3

from brownie import config
import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def owner(accounts):
    acc = accounts.add(config['wallets']['owner_key'])
    return acc

@pytest.fixture(scope="module")
def tiket_vip(TiketVipTest, owner):
    _tiket_vip = TiketVipTest.deploy("https://tiket-vip.xyz/meta/", owner, {'from': owner})
    return _tiket_vip


