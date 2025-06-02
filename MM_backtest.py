from AlgoAPI import AlgoAPIUtil, AlgoAPI_Backtest
from datetime import datetime
from strategy import AlgoEvent  # Assuming your strategy class is saved as strategy.py

if __name__ == "__main__":
    # Initialize Algo Backtest Environment
    print("Starting Market Making Backtest...")
    bt = AlgoAPI_Backtest.AlgoBacktest()

    # Load historical market data (update the file path and format accordingly)
    bt.loadMarketDataFromFile('EURUSD_1min.csv')  # CSV or other supported format

    # Set backtest parameters
    bt.setInitialCash(100000)  # Starting capital
    bt.setCommission(0.00002)  # Optional: set transaction cost per trade
    bt.setSlippage(0.00001)    # Optional: set slippage for realism
    bt.setInstrument('EURUSD') # Symbol to backtest

    # Instantiate and run your strategy
    algo = AlgoEvent()
    algo.start(bt)

    # Run the backtest
    bt.runBacktest()

    # Print final results
    print("Backtest completed.")
    print("Final Cash:", bt.getCash())
    print("Open Positions:", bt.getOpenPositions())
    print("Total P&L:", bt.getTotalPL())

    # Optionally export results
    bt.exportPL('market_maker_results.csv')
