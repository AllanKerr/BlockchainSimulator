from miner import Miner
from servers import server
from servers.data_server import DataServer
from servers.request_server import RequestServer
from servers.discovery_server import DiscoveryServer
from secrets import randbits
import peer_to_peer_discovery as p2p
import logging
import random
import time
import threading

class Node:

    def __init__(self):
        """
        Initialize the servers and miner required for a peer to peer node to operate.
        """
        self.node_id = randbits(32)

        self.miner = Miner()
        self.miner.mine_event.append(self.block_mined)

        self.request_server = server.TCPServer(10000, RequestServer)
        self.request_server.miner = self.miner

        self.input_server = server.TCPServer(9999, DataServer)
        self.input_server.miner = self.miner

        self.udp_server = server.UDPServer(10029, DiscoveryServer, self.node_id)
        self.heartbeat = p2p.Heartbeat(10029, 30, self.node_id)

    def block_mined(self, block, chain_cost):
        pass

    def check_dead_nodes(self, interval, threshold):

        while True:
            time.sleep(interval)

            for node, stamp in self.udp_server.neighbour_list:
                if time.time() - stamp > threshold:
                    self.udp_server.neighbour_list.remove((node, stamp))
                    logging.debug("Node %s is dead", node)

    def run(self):
        """
        Run the servers for receiving incoming requests and start mining.
        This method never returns.
        """
        logging.debug("enable")
        logging.debug(self.node_id)
        server.start_server(self.request_server)
        server.start_server(self.input_server)
        server.start_server(self.udp_server)

        reaper = threading.Thread(target=self.check_dead_nodes, args=(30, 20,))
        reaper.daemon = True
        reaper.start()

        self.heartbeat.start()
        self.miner.mine()
