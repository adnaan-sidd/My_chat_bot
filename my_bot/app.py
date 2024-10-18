import os
import asyncio
from src.data_collection import DataCollector
from src.data_processing import DataProcessor
from src.strategies import TradingStrategies
from src.trade_execution import execute_trade

async def main():
    token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIwZWEzYjQwMGVhNmUyMDE1YmU0MjdjZDlkZjY2YTVlOSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6ImJpbGxpbmctYXBpIiwibWV0aG9kcyI6WyJiaWxsaW5nLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19XSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6IjBlYTNiNDAwZWE2ZTIwMTViZTQyN2NkOWRmNjZhNWU5IiwiaWF0IjoxNzI5MTIzNjk4fQ.RicYdt8Sy0NOkmjyfyzd6qvKXd0vXozqTbleq5czbooISg0AEmKfAbSd60gekZ8tJCw4c4nLBs2Jv4pMiGLmy9jzzewNg54DBooJdkcDHY6oik9ZfoRKkTweQSXXOlv21w_FCwELF0LbWzrsVO2v0XsOOAd4BnzL94LJ5GW85lgz03I5nE7vFhoF1gBrRR7I_-N3sGXVhbMhxi82gdDqpnLRNwDKABdJbvHlj-sD6iDzZsBESdjIVqXLTe1v_UuOpH-41WMb3yhRbfwoox0Gcxl9KY1eShfGQbHi1rZEn5UV60H_sFeDTebPHO6W3AwFJmrxA53I9VdHq98vIqSfHCjaimicp-H7dxQyacNjSL2XrEgMm_lJYzpagBYJQB5XihIhZHSxQ9LedPmMZVdzNu5TWxEc_-JpfGF7MucRp1c4IU8ejwHZQuix7KyPegrhdDf9HqmKepeQiCFiiTI9nQGT4wWFoPuStRv6VSISzV3vlORwJ_XtjfqSeWK6TalTd6m_gsS9dTPB7vb0XKDIOevr2smv7NkqwapY0STzDRC0jNa9vtlv8iWt-jd2ZNdhKNSizYijebm6cPtfAWiGK406CMUOmKM0ddo8w84Ytww663zJG4rYzKb-HhU8dyJzK9LRVmO-OX9h9YobYwfY_0B97t8GxauxEFcIZ2LbCsY'
    account_id = os.getenv('ACCOUNT_ID') or '86118361-6faf-4d08-bc4e-424c7bf52620'
    assets = ['EURUSD', 'GBPUSD', 'JPYUSD', 'XAUUSD']

    # Step 1: Collect data
    collector = DataCollector(token, account_id)
    market_data = await collector.fetch_market_data(assets)

    # Step 2: Process data
    processor = DataProcessor()
    processed_data = processor.clean_and_normalize(market_data)

    # Step 3: Apply trading strategy
    strategy = TradingStrategies()
    signals = strategy.moving_average_strategy(processed_data)

    # Step 4: Execute trade based on signals
    if signals['positions'].iloc[-1] == 1.0:  # Buy signal
        await execute_trade(collector.metaapi, 'EURUSD', 0.1, 1.0985, 1.1050)

if __name__ == "__main__":
    asyncio.run(main())
