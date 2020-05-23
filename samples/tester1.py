"""

We modified the html tearsheet to have a distribution of daily returns

_plots.histogram(returns, resample='D', ...)

Useful as we are interested in daily returns for our yearly tearsheet

"""


import quantstats as qs

import quantstats.quantstats as qs

import pandas as pd


def get_series(filepath):
	data = pd.read_csv(filepath)
	data['Date'] = pd.to_datetime(data['Date'])
	data.set_index(['Date'], inplace=True)
	data = data[['Close']]
	data = data.pct_change()
	print(data)

	return data.iloc[:, 0]


def run(filename="PRAESCIRE19.csv", title="Praescire ytd20"):

	# extend pandas functionality with metrics, etc.
	qs.extend_pandas()

	# get praescires returns as a series
	praescire19 = get_series("/home/joe/PycharmProjects/quantstats_git/quantstats/data/" + filename)

	# fetch the daily returns for a stock
	# stock = qs.utils.download_returns('FB')

	stock = praescire19
	# show sharpe ratio
	qs.stats.sharpe(stock)

	# or using extend_pandas() :)
	stock.sharpe()

	# qs.plots.snapshot(
	# stock, title='Facebook Performance', savefig="/home/joe/PycharmProjects/quantstats/savedcharts/fb.png")

	# qs.reports.html(
	# 	stock, benchmark="SPY", output="/home/joe/PycharmProjects/quantstats_git/quantstats/savedcharts/" + filename[:-4] + ".html")

	qs.reports.html_jd(
		stock, benchmark=None, title=title + filename[-6:-4],
		output="/home/joe/PycharmProjects/quantstats_git/quantstats/savedcharts/" + filename[:-4] + ".html"
	)


if __name__ == "__main__":
	run(filename="PRAESCIRE20.csv")