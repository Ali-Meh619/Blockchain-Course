import import_ipynb
from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

my_private_key = CBitcoinSecret(
    'cUVvLMmSc2M5HAusXaGFGo8PGsTyw6dT1Xeu8SpQPkB6uG41YCyv')

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)


####Q.3

faraz_private_key = CBitcoinSecret(
    'cQwf8K8njiRFmkxBy7PzaLUSfcWW48h3Pn2ccBJqKng4Yvo6EZKY')

faraz_public_key = faraz_private_key.pub
faraz_address = P2PKHBitcoinAddress.from_pubkey(faraz_public_key)


sh1_private_key = CBitcoinSecret(
    'cNW5ZXHF7J3kGgqfACJrbqF4ezQE8Bsxtr1YPFevr5rYGfPXhgXT')

sh1_public_key = sh1_private_key.pub
sh1_address = P2PKHBitcoinAddress.from_pubkey(sh1_public_key)



sh2_private_key = CBitcoinSecret(
    'cV8ia5sLACeMkfVy2Ch9kVd1e73NeT8ieMqaYu27PpGikKnaTdH5')
sh2_public_key = sh2_private_key.pub
sh2_address = P2PKHBitcoinAddress.from_pubkey(sh2_public_key)



sh3_private_key = CBitcoinSecret(
    'cQGXdFzbVcjQG8RBqoPjodBFMSndhFx6zB77qEbYtZAipNUcwrna')

sh3_public_key = sh3_private_key.pub
sh3_address = P2PKHBitcoinAddress.from_pubkey(sh3_public_key)


sh4_private_key = CBitcoinSecret(
    'cNsHSWsvgFs6HbQEitZmyAVQKB6Ykn4ovT9KmhzsB5guRtKzEbxD')

sh4_public_key = sh4_private_key.pub
sh4_address = P2PKHBitcoinAddress.from_pubkey(sh4_public_key)


sh5_private_key = CBitcoinSecret(
    'cTsNkawMov2A3DaePVdCtVdpDjNBSUXk7LGkQgAhPLm6kJUnXuGA')

sh5_public_key = sh5_private_key.pub
sh5_address = P2PKHBitcoinAddress.from_pubkey(sh5_public_key)

######################################################################

######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cQqHUBEXdokiYDM5225FugFLfiWvELSdTLzYcL5YwoYfbnTYAmid')

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cSaSThGWctokgLic1ZH6jLJRmsMjqX2PL2K6Be3Coh8QpExd4MXP')

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('85d48ad4adf6ee01cb75fee5f1d61a4368ce97a721366ee85bf72e133df9c5af'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('5f8160f52df84dfca04c4f33b95f58c500101f64ff352e35fd16de5159fcbc47'))

#bob
# "private": "5f8160f52df84dfca04c4f33b95f58c500101f64ff352e35fd16de5159fcbc47",

# "public": "02458433085099ab6f0ee56d2953993f251057e52fc1742cc070e18d6e081f7c9d"

# "address": "C4u3kSirCevANYUZgM8USeGQoySwXeugah",
# "wif": "BrXgSM6hCok2DTb5ymiugQcm38497svVY1pHH5Cb3kbGme3yQwc4"
# Can be imported by alice.py or bob.py
#55fbafdd526f44c8a41dcdb9fc0962ac
##


##alice

 #"private": "85d48ad4adf6ee01cb75fee5f1d61a4368ce97a721366ee85bf72e133df9c5af",

 #"public": "02f6760a9fad1a94bab442554b84996cb04a5b6a646e5551dd7779c128359b2af1"

 #"address": "BskPeoBWwkg3aAiKRuDLQKj17DgqyeJ8rR",
 #"wif": "BspBMMQdzWSUSyrSqoSHc3ZzXNShkK5KKzuzwMxXXqT9Mn5LKa1x"


alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################

print(alice_address_BTC)