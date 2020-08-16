import import_ipynb
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)

from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 9610, OP_EQUALVERIFY, OP_SUB, 2332, OP_EQUAL]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0008 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '1f968b263f0d902a75781bdfae28724516d6848b1afa3f2495419dc84d6fe132')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
