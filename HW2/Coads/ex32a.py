import import_ipynb
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import send_from_P2PKH_transaction



######################################################################
# TODO: set these parameters correctly
######################################################################

txout_scriptPubKey = [OP_DEPTH, OP_3, OP_SUB, OP_ABS,
                      sh1_public_key, sh2_public_key, sh3_public_key, OP_3, OP_CHECKMULTISIGVERIFY,
                      OP_DEPTH, OP_1SUB, my_public_key, faraz_public_key, OP_2, OP_CHECKMULTISIG
                      ]
######################################################################




if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0004 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '1f968b263f0d902a75781bdfae28724516d6848b1afa3f2495419dc84d6fe132')
    utxo_index = 15 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)