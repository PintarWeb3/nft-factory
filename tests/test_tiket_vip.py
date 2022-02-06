#!/usr/bin/python3
import pytest
import brownie

from consts import *

import pytest
import brownie


def test_owner_admin(tiket_vip, owner):
    assert tiket_vip.owner() == owner

def test_supports_interface(tiket_vip):
    assert tiket_vip.supportsInterface("0x01ffc9a7") == True
    assert tiket_vip.supportsInterface("0x80ac58cd") == True
    assert tiket_vip.supportsInterface("0xffffffff") == False

def test_total_supply(tiket_vip, accounts):
    assert tiket_vip.totalSupply() == 0
    tiket_vip.mint(accounts[3], {"from": accounts[3]})
    assert tiket_vip.totalSupply() == 1

@pytest.mark.parametrize("idx", range(1, 10))
def test_total_supply_increased(tiket_vip, accounts, idx):
    assert tiket_vip.totalSupply() == 0
    for i in range(idx):
        tiket_vip.mint(accounts[3], {"from": accounts[3]})
    assert tiket_vip.totalSupply() == idx

def test_base_uri(tiket_vip, owner):
    assert tiket_vip.baseTokenURI() == "https://tiket-vip.xyz/meta/"
    tiket_vip.mint(owner, {"from": owner})
    assert tiket_vip.tokenURI(1) == "https://tiket-vip.xyz/meta/1"


# @TODO(you): add tests here
