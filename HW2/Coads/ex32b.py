import import_ipynb
from sys import exit
from bitcoin.core.script import *

from utils_for_ex32 import *
from config import *
from ex1 import P2PKH_scriptPubKey
from ex32a import txout_scriptPubKey

######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0002  # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
    '652f09e9fcc089ae31f8911f76d557550a35b1b8e0c6ae9c8d42f8b1129b602a')
utxo_index = 0  # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = txout_scriptPubKey
######################################################################
txout_scriptPubKey = [OP_DUP, OP_HASH160, faucet_address, OP_EQUALVERIFY, OP_CHECKSIG]

# tx_type==2 is when both owners are present
tx_type = 3121

if tx_type == 3121:
    first_pr_key = sh1_private_key
    second_pr_key = sh2_private_key
    third_pr_key = my_private_key

elif tx_type == 3122:
    first_pr_key = sh1_private_key
    second_pr_key = sh2_private_key
    third_pr_key = faraz_private_key

elif tx_type == 3231:
    first_pr_key = sh2_private_key
    second_pr_key = sh3_private_key
    third_pr_key = my_private_key


elif tx_type == 3232:
    first_pr_key = sh2_private_key
    second_pr_key = sh3_private_key
    third_pr_key = faraz_private_key


elif tx_type == 3132:
    first_pr_key = sh1_private_key
    second_pr_key = sh3_private_key
    third_pr_key = faraz_private_key


elif tx_type == 3131:
    first_pr_key = sh1_private_key
    second_pr_key = sh3_private_key
    third_pr_key = my_private_key

    ##############################
######################################################################


response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txout_scriptPubKey, tx_type,
    first_pr_key, second_pr_key, third_pr_key, network_type)
print(response.status_code, response.reason)
print(response.text)