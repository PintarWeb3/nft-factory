#!/usr/bin/python3

from brownie import TiketVip, accounts, config


def main():
    print("Deploying TiketVIP...")
    return TiketVip.deploy("https://tiket-vip.xyz/metadata/", {'from': accounts[0]})

