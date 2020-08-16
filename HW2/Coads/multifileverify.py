import import_ipynb
from Merkle_Tree import MerkleTreeCalculator
import hashlib
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import *
from ex1 import send_from_P2PKH_transaction


def P2PKH_scriptPubKey(address):
    ######################################################################
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    return [signature, my_public_key]
    ######################################################################


if __name__ == '__main__':
    ######################################################################

    SelectParams('testnet')
    numberoffiles = 18
    merkleroot = MerkleTreeCalculator.calculate_merkle_root(True, numberoffiles)

    seckey = CBitcoinSecret.from_secret_bytes(merkleroot)
    address = P2PKHBitcoinAddress.from_pubkey(seckey.pub)

    ##
    your_address = address
    amount_to_send = 0.0005
    txid_to_spend = (
        '1f968b263f0d902a75781bdfae28724516d6848b1afa3f2495419dc84d6fe132')
    # second tx id  'fb549c431a5d3b8fe4ef67bb21625b0c468bf55dc75305fcee7176574603962c'
    utxo_index = 28
    ######################################################################
    txout_scriptPubKey = P2PKH_scriptPubKey(your_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)    