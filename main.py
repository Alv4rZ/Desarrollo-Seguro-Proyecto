from block import Block
from chain import Chain

chain = Chain(20)

i = 0

for i in range(5):
    chain.add_to_pool(str(i))
    chain.mine()
    


# B1 = Block("Hi")
# B1.mine(20)

# print(B1.hash.hexdigest())
# print(B1.nonce)
# print(B1.data)
