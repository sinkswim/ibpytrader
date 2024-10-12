from ibapi.wrapper import EWrapper

class IBWrapper(EWrapper):
    def __init__(self):
        EWrapper.__init__(self)
        self.historical_data = {}
        self.market_data = {}
        
    def historicalData(self, request_id, bar):
        bar_data = (
            bar.date,
            bar.open,
            bar.high,
            bar.low,
            bar.close,
            bar.volume,
        )
        if request_id not in self.historical_data.keys():
            self.historical_data[request_id] = []
        self.historical_data[request_id].append(bar_data)
        
    def tickPrice(self, request_id, tick_type, price, attrib):
        if request_id not in self.market_data.keys():
            self.market_data[request_id] = {}
            self.market_data[request_id][tick_type] = float(price)
