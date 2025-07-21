import yfinance as yf
import plotext as plt

plt.date_form('d/m/Y')

start = plt.string_to_datetime('11/04/2022')
end = plt.today_datetime()
data = yf.download('goog', start, end)

dates = plt.datetimes_to_string(data.index)
#print(data)
Open = data["Open"]; Close = data["Close"]; High = data["High"];
print(Open)
plt.candlestick(dates, data)

plt.title("Google Stock Price CandleSticks")
plt.xlabel("Date")
plt.ylabel("Stock Price $")
plt.show()