import import_ipynb
from config import *
from bitcoin.core.script import *
from sys import exit
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from ex4a import txout_scriptPubKey


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def j_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, my_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [signature, my_public_key]


def send_from_custom_transaction(amount_to_send, txid_to_spend, utxo_index, txin_scriptPubKey, txout_scriptPubKey,
                                 network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = j_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)
    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00021  # amount of BTC in the output you're splitting minus fee

    txid_to_spend = (
        '476d697500694e504e66419b0edeb7ce6e55ac9486e13b00f6fc1905964de677')

    utxo_index = 0  # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = txout_scriptPubKey
    ######################################################################
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_custom_transaction(amount_to_send, txid_to_spend, utxo_index, txin_scriptPubKey,
                                            txout_scriptPubKey, network_type)

    print(response.status_code, response.reason)
    print(response.text)