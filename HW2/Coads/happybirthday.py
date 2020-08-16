import import_ipynb
import hashlib
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import *
from ex1 import send_from_P2PKH_transaction
import requests

from bitcoin.core import b2x, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160
from bitcoin.core.script import *
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH


def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)
    return h.digest()


def P2PKH_scriptPubKey(address):
    ######################################################################
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    ######################################################################
    return [signature, my_public_key]


if __name__ == '__main__':
    ######################################################################
    SelectParams('testnet')
    filename = 'Happy Birthday Hamed.txt'
    seckey = CBitcoinSecret.from_secret_bytes(sha256sum(filename))
    address = P2PKHBitcoinAddress.from_pubkey(seckey.pub)
    ##
    your_address = address

    amount_to_send = 0.0005
    txid_to_spend = (
        '1f968b263f0d902a75781bdfae28724516d6848b1afa3f2495419dc84d6fe132')

    utxo_index = 22
    txout_scriptPubKey = P2PKH_scriptPubKey(your_address)
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)