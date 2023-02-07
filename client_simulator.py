import ipfshttpclient2
import json
import logging
import os

from robonomicsinterface import Account, PubSub, Liability, web_3_auth
from substrateinterface import KeypairType
from threading import Thread
from time import time, sleep

from utils import (
    LAST_COMPENSATION_DATE_QUERY_TOPIC,
    LAST_COMPENSATION_DATE_RESPONSE_TOPIC,
    LIABILITY_QUERY_TOPIC,
    LIABILITY_REPORT_TOPIC,
    DAPP_NODE_REMOTE_WS,
    IPFS_W3GW,
    AGENT_NODE_MULTIADDR,
)
from utils import parse_income_message

logger = logging.getLogger(__name__)


def callback(obj, update_nr, subscription_id):
    response = parse_income_message(obj["params"]["result"]["data"])
    if response["address"] == dapp_user.get_address():
        print(response)


def subscribe(topic):
    account_ = Account(remote_ws=DAPP_NODE_REMOTE_WS)
    pubsub_ = PubSub(account_)
    pubsub_.subscribe(topic, result_handler=callback)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    # Create DAPP account
    dapp_user = Account(remote_ws=DAPP_NODE_REMOTE_WS,
                        seed=os.getenv("DAPP_SEED"),
                        crypto_type=KeypairType.ED25519)

    # Pubsub subscriber emulation
    negotiations_subscriber_thread = Thread(target=subscribe, args=(LAST_COMPENSATION_DATE_RESPONSE_TOPIC,))
    report_subscriber_thread = Thread(target=subscribe, args=(LIABILITY_REPORT_TOPIC,))
    negotiations_subscriber_thread.start()
    report_subscriber_thread.start()

    # Negotiations query emulation:
    pubsub = PubSub(dapp_user)

    while True:

        query = input("last burn date (1)/liability (2)")

        if query == "1":
            negotiations_query = dict(address=dapp_user.get_address(), kwh_current=20.0, timestamp=time())
            logger.info(pubsub.connect(AGENT_NODE_MULTIADDR))
            sleep(1)
            print(f"publish: {pubsub.publish(LAST_COMPENSATION_DATE_QUERY_TOPIC, str(negotiations_query))}")
        elif query == "2":
            logger.info(pubsub.connect(AGENT_NODE_MULTIADDR))
            sleep(1)

            content = dict(geo="59.934280, 30.335099", kwh=5.0)
            auth = web_3_auth(seed=os.getenv("DAPP_SEED"))
            client = ipfshttpclient2.connect(addr=IPFS_W3GW, auth=auth)
            technics = client.add_json(content)
            economics = 0
            promisee = dapp_user.get_address()
            liability_singer = Liability(dapp_user)
            promisee_signature = liability_singer.sign_liability(technics, economics)

            liability_query = dict(technics=technics,
                                   economics=economics,
                                   promisee=promisee,
                                   promisee_signature=dict(ED25519=promisee_signature),
                                   timestamp=time())
            print(pubsub.publish(LIABILITY_QUERY_TOPIC, str(liability_query)))
