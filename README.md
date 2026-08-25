# DeFi TVL (DeFiLlama) API — examples

Total value locked per blockchain — DeFiLlama data, keyless.

**Live page, full schema & pricing → [quanticdata.io/collectors/defillama-api/](https://quanticdata.io/collectors/defillama-api/)**

Reads DeFiLlama's public chains endpoint and delivers one row per blockchain: current total value locked (TVL), the native token symbol and the CoinGecko/CMC ids to join against price data. Sorted by TVL, or filtered to specific chains. DeFiLlama gates history and the full protocol list behind a paid Pro key; this uses the free chains surface.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/defillama/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"max_results": 50}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `chains` (array) — Filter to specific chains (Ethereum, Solana…). Empty = all, ranked by TVL.
- `max_results` (integer) — How many chains to deliver at most (1–200). You pay only for delivered chains.

## Output — one row per chain

| field | type | description |
|---|---|---|
| `rank` | integer | TVL rank. |
| `chain` | string | Blockchain name. |
| `tvl` | integer | Total value locked, USD. |
| `token_symbol` | string | Native token symbol. |
| `chain_id` | integer | EVM chain id when applicable. |
| `gecko_id` | string | CoinGecko id (join key). |
| `cmc_id` | string | CoinMarketCap id. |

## Pricing

**$0.0003 per delivered chain** ($0.3 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 6,666 chains — no card required.

## Links

- This collector: https://quanticdata.io/collectors/defillama-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
