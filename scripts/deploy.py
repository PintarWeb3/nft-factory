#!/usr/bin/python3

from brownie import TiketVip, accounts, config


def main():
    print("Deploying TiketVIP...")
    owner = accounts.add(config['wallets']['owner_key'])
    return TiketVip.deploy("https://tiket-vip.xyz/metadata/", owner, {'from': accounts[0]})

