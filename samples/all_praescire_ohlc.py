import pandas as pd
from pathlib import  Path

def read_excel_file(path=Path.home().joinpath('Dropbox', 'praescire_database', 'old_databases' )):
	"""
	reading in the ohlc from excel and saving as csv
	"""

	all_data = pd.read_excel(path / "all_years.xlsx", sheet_name=1)
	all_data['Volume'] = 0
	all_data['Adj Close'] = all_data['Close']
	print(all_data)

	all_data.to_csv(Path("/home/joe/PycharmProjects/quantstats_git/quantstats/data/all_praescire.csv"), index=False)

if __name__ == "__main__":
	read_excel_file()
