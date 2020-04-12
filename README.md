# blockchain

A blockchain implementation.

Only meant for educational purposes.

## Block structure:

```
{
    "header": {
        "hash_previous_block": "00004d8bfe0d30345fbe9e2ffe679b22075b9762ec25d99246b4c10d13e8c646",
        "timestamp": 1586704560293,
        "nounce": 1234
    },
    "payload": { ... }
}
```

## Proof-of-work:

For a block to be valid it must hash to a value less than the current target.
 
The default target is: `0001000000000000000000000000000000000000000000000000000000000000` (base 16), that means the 64 digits hex representation of the hash of the block should have four leading `0`.
