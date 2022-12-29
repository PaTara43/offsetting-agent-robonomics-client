"""
Constants list.

Robonomics node launch for dev tests:
    1st node: target/debug/robonomics --dev --tmp -l rpc=trace
    2nd node: target/debug/robonomics --dev --tmp --ws-port 9991 -l rpc=trace

"""

ROBONOMICS_NODE = None  # None for Kusama Parachain Node. "ws://127.0.0.1:9944" for testing.
DAPP_NODE_REMOTE_WS = "ws://127.0.0.1:9991"  # This if for _dapp_pubsub_simulator 23.88.52.147
AGENT_NODE_MULTIADDR = "/ip4/127.0.0.1/tcp/44440"

LAST_BURN_DATE_QUERY_TOPIC = "last_burn_date_query"
LAST_BURN_DATE_RESPONSE_TOPIC = "last_burn_date_response"
LIABILITY_QUERY_TOPIC = "liability_query"
LIABILITY_REPORT_TOPIC = "liability_report"

UPLOAD_W3GW = "http://127.0.0.1:5001"
