import import_ipynb
from config import *
from bitcoin.core.script import *
from sys import exit
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from ex1 import send_from_P2PKH_transaction


def P2PKH_scriptPubKey(address):
    ######################################################################
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0001  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '6ebf8130431fcdd42db0d491ed663ae61f47c33a144d287a414881b3ea6f0764')
    utxo_index = 0  # index of the output you are spending, indices start at 0
    ######################################################################

    timelock = 1577620800
    txout_scriptPubKey = [timelock, OP_CHECKLOCKTIMEVERIFY, OP_DROP,
                          OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG]

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)