from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib.ticker import MaxNLocator
from pyparsing import alphas
#check for missing values or null values.
file = pd.read_csv('SPX.csv')
nul_vals = file[['Date', 'Open', 'Close']].isnull().any()
#print(nul_vals)

'''Closing Price chart'''
dates = pd.to_datetime(file['Date']).tolist()
closing_prince_list = file['Close'].tolist()
'''
plt.plot(dates,file['Close'])
plt.ylabel('dollar value $')
plt.xlabel('Year')
plt.title('S&P 500 index Historical Chart')
start_time = datetime(1927, 12, 30)
end_time = datetime(2020, 11, 4)
plt.xlim(start_time, end_time)
#print(dates)
#plt.show()
'''




'''Plotting daily returns for last year 
data_for_daily_return = file[23069:23323]
daily_return = []
closing_price = data_for_daily_return['Close']
date = data_for_daily_return['Date'].tolist()
date.pop(0)
#need to remove date one since the formula being used compares current day's close with previous days close to calculate daily return

for i in range(23069, 23322, 1): # 0 here will be the first row that contains data 23322 last one that contains data 23324
    daily_return.append(((closing_prince_list[i+1] - closing_prince_list[i])/closing_prince_list[i])*100)


plt.plot(date,daily_return)
#plt.plot(data_for_daily_return['Date'], closing_price)
plt.xlim([date[0], date[-1]])
num_ticks = 10
tick_indices = np.linspace(0, len(date) - 1, num_ticks, dtype=int)
tick_labels = []
for i in tick_indices:
    tick_labels.append(date[i])  # Add the corresponding date at each tick index
# Set the tick positions and labels
plt.xticks(tick_indices, tick_labels, rotation=45)
plt.ylabel('% Change in Value')
plt.xlabel('Year')
plt.title('S&P 500 Daily Returns')
plt.show()  #This needs better labeling and spacing between each of the points
'''


'''Simple Moving Average'''
'''Executed on the last 20 days'''
data_for_sma = file[23223:23323]
date_for_sma = data_for_sma['Date'].tolist()
twenty_day_close = data_for_sma['Close'].tolist()
#print(twenty_day_close)

window_size = 20
sma_1 = data_for_sma['Close'].rolling(window=window_size).mean()

sma = data_for_sma['Close'].sum()/120  # adjust this depending on the window size
#print(sma_whole_set)
#plt.xlabel('Dates')
#plt.ylabel('$ price')
#plt.title('S&P 500 Simple Moving Average Oct 8 - Nov 4 2020')
#plt.plot(date_for_sma, data_for_sma['Close'])
#plt.plot(date_for_sma, [sma]*len(date_for_sma))
#plt.gcf().autofmt_xdate()
#plt.show()

'''Exponential moving average'''
data_for_ema = file[23303:23323]
#date_for_ema = data_for_sma['Date'].tolist()
ema_average = data_for_sma['Close'].sum()/120
test_ema = [3423.27]
sf = 2/(20 + 1)
for i in range(23224, 23323, 1):
    test_ema.append((file['Close'][i] * sf) + (test_ema[i-23224]*(1-sf)))

test_ema_list = [round(float(x), 2) for x in test_ema]
#plt.plot(date_for_sma,test_ema_list, label = "EMA")
#plt.show()


'''Buy Sell Signals based on SMA'''
indicator = []
for j in range(0,len(twenty_day_close),1):
    if twenty_day_close[j] > sma:
        indicator.append('buy')
    elif twenty_day_close[j] == sma:
        indicator.append('intersection')
    else:
        indicator.append('sell')
#print(f'SMA indicator: {indicator}')
marker_colors = []
for i in indicator:
    if i =="buy":
        marker_colors.append("green")
    else:
        marker_colors.append("red")




'''Buy Sell Signal based on EMA'''
indicator2 = []
for j in range(0,len(twenty_day_close),1):
    if twenty_day_close[j] > test_ema_list[j]:
        indicator2.append('buy')
    elif twenty_day_close[j] == test_ema_list[j]:
        indicator2.append('intersection')
    else:
        indicator2.append('sell')
print(f'EMA indicator: {indicator2}')

marker_colors_EMA = []
for i in indicator2:
    if i == "buy":
        marker_colors_EMA.append("green")
    else:
        marker_colors_EMA.append("red")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(date_for_sma, twenty_day_close, label="Closing Price", color="orange")
ax.plot(date_for_sma, test_ema_list, label="EMA", color="blue")
ax.plot(date_for_sma,sma_1, color="red", label="SMA")
#ax.scatter(date_for_sma, test_ema_list, c=marker_colors_EMA, marker="X", label="Buy/Sell Signal (EMA)", edgecolors="black", s=75)
ax.set_ylabel("Price", fontsize=12)
ax.set_title("Closing Price and EMA with Buy/Sell Signals", fontsize=14)
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend(loc="upper right", fontsize=10)
plt.gcf().autofmt_xdate()
plt.show()
#Include buy sell indicator on the plot
#plt.ylabel("Price ($)")
#plt.xlabel("Date")
#plt.show()



#plt.scatter(date_for_sma, data_for_sma['Close'], c=marker_colors, label="SMA signal", alpha = 0.5) # c = color of the markers, s = size of the markers defult 20



# Plot both Closing Price and EMA on the same y-axis

