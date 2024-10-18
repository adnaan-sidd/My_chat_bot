import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime, timedelta

# Note: for information on how to use this example code please read https://metaapi.cloud/docs/client/usingCodeExamples

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIwZWEzYjQwMGVhNmUyMDE1YmU0MjdjZDlkZjY2YTVlOSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ODYxMTgzNjEtNmZhZi00ZDA4LWJjNGUtNDI0YzdiZjUyNjIwIl19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDo4NjExODM2MS02ZmFmLTRkMDgtYmM0ZS00MjRjN2JmNTI2MjAiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjg2MTE4MzYxLTZmYWYtNGQwOC1iYzRlLTQyNGM3YmY1MjYyMCJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjg2MTE4MzYxLTZmYWYtNGQwOC1iYzRlLTQyNGM3YmY1MjYyMCJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDo4NjExODM2MS02ZmFmLTRkMDgtYmM0ZS00MjRjN2JmNTI2MjAiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ODYxMTgzNjEtNmZhZi00ZDA4LWJjNGUtNDI0YzdiZjUyNjIwIl19LHsiaWQiOiJtZXRhYXBpLXJlYWwtdGltZS1zdHJlYW1pbmctYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ODYxMTgzNjEtNmZhZi00ZDA4LWJjNGUtNDI0YzdiZjUyNjIwIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDo4NjExODM2MS02ZmFmLTRkMDgtYmM0ZS00MjRjN2JmNTI2MjAiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiMGVhM2I0MDBlYTZlMjAxNWJlNDI3Y2Q5ZGY2NmE1ZTkiLCJpYXQiOjE3MjkxMjM4MDcsImV4cCI6MTczMTcxNTgwN30.RnOisqwfr6wD_QzEj4_Me_oTd9z8wjWs-zUxVkdO3T-wT-e29DX0_TgK8kqHJKq-HzFWBa8Rl2t9bTXXt4VfU2vlg0xsyyH09Y3qnuzINz8bkMusMl0NCIgCD2CFYD17N7ZFISyju6_4avlwXFgYQ1Y9FPEYOYkgBzDeNeERM56wMlVe4TIz1pN69pDkRZfjuEglheVebSvyV8gaNmZOzHqU_pDxRuZ_qKRV99jCYR-JuAJiZqpaZrjXFve2DkBsTW660BFQipYIWkChxoIjGA0F2NIu04rR3S9-bkllW6cPfG3-nKfAb3GG6IQg0QX7HY3eqwMMEgBkDj0cWxLf9DPKi4zmRku4hWPa1X94HkSgw5fEI6lHZb03GlUBhhZm1wyHmCNndOZ3BNzFHfo4_ZEwvh7Z5DmPeHl5uUS3tQ-R2rn_u_UYxtEN9lEhfj01mVJgqJnUO8jQ2L-BIas7eJ4XzVKlHUhcnkdblQzS3JAlq3-9cy9XNUNPeNMYWpXwjc6isEM215dAByzj8EYYhhxPfIMvQaHlFg0Hco472TmhXP3d39WcLZ5E_zlzBIhL76MO5sjJt8bNNoxo2aj1Ml6by9yKX3SZqFovoBHMYI-69Sp_5WdFW06X68SPfE4UEFljV5QMbFh6IbVlXbRGddGiu_cPHSN2KS7_RNdiDmY'
accountId = os.getenv('ACCOUNT_ID') or '86118361-6faf-4d08-bc4e-424c7bf52620'


async def test_meta_api_synchronization():
    api = MetaApi(token)
    try:
        account = await api.metatrader_account_api.get_account(accountId)
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']

        if initial_state not in deployed_states:
            #  wait until account is deployed and connected to broker
            print('Deploying account')
            await account.deploy()

        print('Waiting for API server to connect to broker (may take couple of minutes)')
        await account.wait_connected()

        # connect to MetaApi API
        connection = account.get_rpc_connection()
        await connection.connect()

        # wait until terminal state synchronized to the local state
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await connection.wait_synchronized()

        # invoke RPC API (replace ticket numbers with actual ticket numbers which exist in your MT account)
        print('Testing MetaAPI RPC API')
        print('account information:', await connection.get_account_information())
        print('positions:', await connection.get_positions())
        # print(await connection.get_position('1234567'))
        print('open orders:', await connection.get_orders())
        # print(await connection.get_order('1234567'))
        print('history orders by ticket:', await connection.get_history_orders_by_ticket('1234567'))
        print('history orders by position:', await connection.get_history_orders_by_position('1234567'))
        print(
            'history orders (~last 3 months):',
            await connection.get_history_orders_by_time_range(
                datetime.utcnow() - timedelta(days=90), datetime.utcnow()
            ),
        )
        print('history deals by ticket:', await connection.get_deals_by_ticket('1234567'))
        print('history deals by position:', await connection.get_deals_by_position('1234567'))
        print(
            'history deals (~last 3 months):',
            await connection.get_deals_by_time_range(datetime.utcnow() - timedelta(days=90), datetime.utcnow()),
        )
        print('server time', await connection.get_server_time())

        # calculate margin required for trade
        print(
            'margin required for trade',
            await connection.calculate_margin(
                {'symbol': 'GBPUSD', 'type': 'ORDER_TYPE_BUY', 'volume': 0.1, 'openPrice': 1.1}
            ),
        )

        # trade
        print('Submitting pending order')
        try:
            result = await connection.create_limit_buy_order(
                'GBPUSD', 0.07, 1.0, 0.9, 2.0, {'comment': 'comm', 'clientId': 'TE_GBPUSD_7hyINWqAlE'}
            )
            print('Trade successful, result code is ' + result['stringCode'])
        except Exception as err:
            print('Trade failed with error:')
            print(api.format_error(err))
        if initial_state not in deployed_states:
            # undeploy account if it was undeployed
            print('Undeploying account')
            await connection.close()
            await account.undeploy()

    except Exception as err:
        print(api.format_error(err))
    exit()


asyncio.run(test_meta_api_synchronization())
