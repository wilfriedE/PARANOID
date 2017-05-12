from scapy.all import *
import socket
import logging
from websocket_server import WebsocketServer
import time

CONNECTIONS = 0
SERVER = WebsocketServer(13254, host='127.0.0.1')
COLLECT = True
FILTERS = [] #add your local machine's hostname as a filter

def store_packet(pck):
    time.sleep(0.1)
    if SERVER:
        try:
            if  pck['IP']:
                data = {'nodes':[], 'edges':[]}
                data['nodes'] = [{'id': str(pck['IP'].src), 'group': 2}, {'id': str(pck['IP'].dst), 'group': 3}]
                n1 = data['nodes'][0]
                n1['label'] = socket.gethostbyaddr(pck['IP'].src)[0]
                if n1['label'] in FILTERS:
                    n1['group'] = 4
                n2 = data['nodes'][1]
                n2['label'] = socket.gethostbyaddr(pck['IP'].dst)[0]
                if n2['label'] in FILTERS:
                    n2['group'] = 4
                edges = data['edges']
                edges.append({'from': str(pck['IP'].src), 'to': str(pck['IP'].dst)})
                try:
                    SERVER.send_message_to_all(str(data))
                except Exception as e:
                    pass
        except Exception as e:
            pass


def stop_collecting(pck):
    global COLLECT
    if not COLLECT:
        return True
    return False

def collect():
    sniff(iface=conf.iface, prn=store_packet, stop_filter=stop_collecting, store=0)

def new_client(client, server):
    global CONNECTIONS
    global COLLECT
    if CONNECTIONS < 1:
        CONNECTIONS += 1
        collect()

def recollect():
    collect()

def message_received(client, server, message):
    global COLLECT
    print(message)
    if message is "STOP":
        if COLLECT:
            COLLECT = False
        print("Stoping")
    if message is "RESTART":
        if not COLLECT:
            COLLECT = True
            recollect()
        print("Restarting")

if __name__ == '__main__':
    SERVER.set_fn_new_client(new_client)
    SERVER.set_fn_message_received(message_received)
    SERVER.run_forever()
