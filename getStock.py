import yfinance as yf

# def adj_close(stk, start, end):
#     data = yf.download(stk, start = start, end = end)
#     return data['Adj Close']

# stk = 'AMZN'
# start = "2020-12-31"
# end = "2020-12-31"
# ans = adj_close(stk, start, end)
# print(ans[0])

def adj_close_multi(stks, start, end):
    data = yf.download(stks, start = start, end = end)


    return data

def get_ndx(start, end):
    data = yf.download("NDX", start = start, end = end)




"""
stks = 'AMZN AAPL MSFT FB TSLA'
start = "2020-12-31"
end = "2020-12-31"
msft = adj_close_multi(stks, start, end, 'MSFT')
apl = adj_close_multi(stks, start, end, 'AAPL')
amz = adj_close_multi(stks, start, end, 'AMZN')
fb = adj_close_multi(stks, start, end, 'FB')
tsla = adj_close_multi(stks, start, end, 'TSLA')
print("MSFT: ", msft[0])
print("APL: ", apl[0])
print("AMZN: ", amz[0])
print("FB: ", fb[0])
print("TSLA: ", tsla[0])"""