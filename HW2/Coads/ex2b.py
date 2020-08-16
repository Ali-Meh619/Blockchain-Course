import import_ipynb
from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from ex1 import P2PKH_scriptPubKey
from ex2a import Q2a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0005 # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
        'bed887a7178a02ab616042855b7e25f17bf581b9485dbe6b497e90a3c86cd19a')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txin_scriptSig = [5971,3639]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
