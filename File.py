import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

# Simulated data
np.random.seed(42)
dates = pd.date_range(start="2024-04-01", periods=100, freq='min')  # 'min' instead of 'T'
price = np.cumsum(np.random.randn(100)) + 17000
df = pd.DataFrame({'datetime': dates, 'close': price})
df.set_index('datetime', inplace=True)

# Indicators
df['ema20'] = EMAIndicator(close=df['close'], window=20).ema_indicator()
df['ema50'] = EMAIndicator(close=df['close'], window=50).ema_indicator()
df['rsi'] = RSIIndicator(close=df['close'], window=14).rsi()

# Entry/Exit logic
df['signal'] = 0
df['signal'] = np.where(
    (df['ema20'] > df['ema50']) & (df['rsi'] > 50), 1,
    np.where((df['ema20'] < df['ema50']) & (df['rsi'] < 50), -1, 0)
)
df['position'] = df['signal'].replace(to_replace=0, method='ffill')
df['returns'] = df['close'].pct_change()
df['strategy_returns'] = df['returns'] * df['position'].shift(1)

# Cumulative returns
df['cumulative_strategy'] = (1 + df['strategy_returns']).cumprod()
df['cumulative_market'] = (1 + df['returns']).cumprod()

# Plot
plt.figure(figsize=(14, 6))
plt.plot(df['cumulative_strategy'], label='Strategy Returns')
plt.plot(df['cumulative_market'], label='Market Returns', linestyle='--')
plt.title('Backtest: F&O Entry-Exit Algo (EMA + RSI)')
plt.xlabel('Time')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()