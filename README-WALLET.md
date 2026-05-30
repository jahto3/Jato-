# Jato Contract Wallet

A secure Ethereum contract wallet built with Hardhat for managing ETH and ERC-20 tokens on testnet.

## Features

- ✅ Accept ETH deposits from anyone
- ✅ Store and manage ERC-20 tokens
- ✅ Owner-only withdrawals
- ✅ Reentrancy protection
- ✅ Event logging for all transactions
- ✅ Testnet compatible (Sepolia, Goerli)

## Installation

1. Install dependencies:
```bash
npm install
```

2. Create `.env` file from `.env.example`:
```bash
cp .env.example .env
```

3. Fill in your `.env` file with:
   - Testnet RPC URL (Infura, Alchemy, etc.)
   - Private key for deployment account
   - Etherscan API key (for verification)

## Compilation

```bash
npm run compile
```

## Testing

```bash
npm test
```

## Deployment

Deploy to Sepolia testnet:
```bash
npm run deploy:sepolia
```

Deploy to Goerli testnet:
```bash
npm run deploy:goerli
```

## Contract Details

### Owner Address
```
0x5EEaFFF5ad48B2121D41F561eDf48dCD4027d387
```

### Contract Functions

#### ETH Operations
- `depositETH()` - Deposit ETH to the contract
- `withdrawETH(uint256 amount, address payable recipient)` - Owner: Withdraw ETH
- `getETHBalance()` - Get contract ETH balance

#### ERC-20 Operations
- `depositToken(address token, uint256 amount)` - Deposit ERC-20 tokens
- `withdrawToken(address token, uint256 amount, address recipient)` - Owner: Withdraw tokens
- `getTokenBalance(address token)` - Get token balance

#### Ownership
- `owner()` - Get current owner
- `transferOwnership(address newOwner)` - Transfer ownership

## Security Features

- Uses OpenZeppelin's `Ownable` for access control
- `ReentrancyGuard` protection on withdrawal functions
- Input validation on all functions
- Checks for zero addresses

## License

MIT
