from datetime import date

from model.Stock import Stock
from model.StockDaySummary import StockDaySummary
from model.StockInfoReport import StockInfoReport
from model.fact_providers.StockInformationProvider import StockInformationProvider


class FakeStockInformationProvider(StockInformationProvider):
    def retrieve_historic_data(self, stock: Stock, start_date: date, end_date: date) -> list[StockDaySummary]:
        pass

    def retrieve_stock_info(self) -> list[StockInfoReport]:
        pass
