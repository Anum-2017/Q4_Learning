# 🚀 Crypto Agent – Powered by OpenAI Agent SDK

Your personal assistant for real-time cryptocurrency insights. Just ask about any major coin and get live updates!

---

# ✅ Available Tools (Functions)

### 1. detect_all_coins(user_input: str) → list[str]

**Purpose:** Parses user input and detects supported cryptocurrency symbols (e.g., BTC, ETH, DOGE).

**Input:** Natural language (e.g., "What's the price of Bitcoin and Solana?")

**Output:** List of coin symbols found in input (e.g., ["BTC", "SOL"])

---

### 2. fetch_price(symbol: str) → str

**Purpose:** Fetches current price data for a specific cryptocurrency from CoinLore API.

**Input:** A valid coin symbol (e.g., "ETH")

**Output:** A formatted string with:
Current USD price
24h change and trend 📈📉
Estimated high/low
Market cap 💼
Last updated time 🕒

---

### 3. @agent.on_chat_start

**Purpose:** Sends a warm welcome message and basic usage instructions when the chat begins.

**Triggered:** Automatically on session start

**Output:** Welcome + usage examples

---

### 4. @agent.on_message

**Purpose:** Handles incoming user messages and responds with real-time crypto data or help instructions.

**Handles:**
/help command to show supported instructions
Coin detection and price fetch
Fallback reply for unsupported coins

---

# 💡 Supported Coins

| Symbol | Name         | Emoji |
| ------ | ------------ | ----- |
| BTC    | Bitcoin      | 🟠    |
| ETH    | Ethereum     | 🟣    |
| DOGE   | Dogecoin     | 🐶    |
| SOL    | Solana       | 🌞    |
| ADA    | Cardano      | 🔷    |
| XRP    | Ripple       | 💧    |
| MATIC  | Polygon      | 🔺    |
| BNB    | Binance Coin | 🟡    |

