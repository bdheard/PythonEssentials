# Lab 10

1. Implement an async method that display the stock price given a stock ticker symbol.
1. Implement an async method that features a web api call to calculate the value of your stoke portfolio given a stock symbol and number of stocks.
1. **Bonus:** create a list of every stock in your portfolio, number of stocks. Get the latest price of the stock, the total value of the position and the total value of the portfolio.

Hint:

```python
soup = bs4.BeautifulSoup(url.text, features="html.parser")
price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
```

## References:
- https://finance.yahoo.com/quote/MSFT?p=MSFT
- https://pypi.org/project/beautifulsoup4/
