"""
Constants list.

Robonomics node launch for dev tests:
    1st node: target/debug/robonomics --dev --tmp -l rpc=trace
    2nd node: target/debug/robonomics --dev --tmp --ws-port 9991 -l rpc=trace

"""

DAPP_NODE_REMOTE_WS = "wss://kusama.rpc.robonomics.network/"  # This if for _dapp_pubsub_simulator 23.88.52.147
AGENT_NODE_MULTIADDR = "/dns/robonomics.rpc.multi-agent.io/tcp/44440"

LAST_COMPENSATION_DATE_QUERY_TOPIC = "last_compensation_date_query"
LAST_COMPENSATION_DATE_RESPONSE_TOPIC = "last_compensation_date_response"
LIABILITY_QUERY_TOPIC = "liability_query"
LIABILITY_REPORT_TOPIC = "liability_report"

IPFS_W3GW = "/ip4/127.0.0.1/tcp/5001/http"
