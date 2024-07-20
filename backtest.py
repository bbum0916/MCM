import pyupbit
import numpy as np
import datetime


def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)

    # bbum: 9:00 AM -> 10:00 AM
    # start_time = df.index[0]
    start_time = df.index[0] + datetime.timedelta(hours=1)

    return start_time

df = pyupbit.get_ohlcv("KRW-BTC", count=7)

df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

print(df)


print("MDD(%): ", df['dd'].max())

now = datetime.datetime.now()
start_time = get_start_time("KRW-BTC")

# end time : 9:00 AM -> 7:00 AM
# end_time = start_time + datetime.timedelta(days=1) - datetime.timedelta(hours=2)
end_time = start_time + datetime.timedelta(hours=21)

print('now: ', now)
print('start_time: ', start_time)
print('end_time: ', end_time)


# df.to_excel("dd.xlsx")