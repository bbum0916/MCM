import pyupbit

access = "HJRJ4ngZiCJzBU50EvXh6dMDWAfGagmtrqyglpnY"          # 본인 값으로 변경
secret = "wZZThKesjMxY7uxNEEZCx32dn6otE9Z8SQrGTLGu"          # 본인 값으로 변경

upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회