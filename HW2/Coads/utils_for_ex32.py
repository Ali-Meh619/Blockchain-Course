import requests

from bitcoin.core import b2x, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160
from bitcoin.core.script import *
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH


def send_from_custom_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, tx_type, first_private_key, second_private_key, final_private_key,
        network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)
    txin = create_txin(txid_to_spend, utxo_index)

    txin_scriptSig = [OP_0, create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, final_private_key),
                      OP_0, create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, first_private_key),
                      create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, second_private_key),
                      ]

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)
    return broadcast_transaction(new_tx, network)


def create_txin(txid, utxo_index):
    return CMutableTxIn(COutPoint(lx(txid), utxo_index))


def create_txout(amount, scriptPubKey):
    return CMutableTxOut(amount * COIN, CScript(scriptPubKey))


def create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, seckey):
    tx = CMutableTransaction([txin], [txout])
    sighash = SignatureHash(CScript(txin_scriptPubKey), tx,
                            0, SIGHASH_ALL)
    sig = seckey.sign(sighash) + bytes([SIGHASH_ALL])
    return sig


def create_signed_transaction(txin, txout, txin_scriptPubKey,
                              txin_scriptSig):
    tx = CMutableTransaction([txin], [txout])
    txin.scriptSig = CScript(txin_scriptSig)
    VerifyScript(txin.scriptSig, CScript(txin_scriptPubKey),
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    return tx


def broadcast_transaction(tx, network):
    if network == 'btc-test3':
        url = 'https://api.blockcypher.com/v1/btc/test3/txs/push'
    elif network == 'bcy-test':
        url = 'https://api.blockcypher.com/v1/bcy/test/txs/push'
    else:
        raise InvalidArgumentException("Network must be one of either 'btc-test3', 'bcy-test'")

    raw_transaction = b2x(tx.serialize())
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    return requests.post(
        url,
        headers=headers,
        data='{"tx": "%s"}' % raw_transaction)
