import json
import threading

from node import Node

with open('conf.json', 'r') as f:
    conf = json.load(f)
    nodes = {}
    
    for node in conf['nodes']:
        nodes[node[0]] = Node(uid=node[0])
    
    for i in range(len(conf['nodes'])):
        if i == len(conf['nodes']) - 1:
            nodes[conf['nodes'][i][0]].stream.add_sender(
                nodes[conf['nodes'][0][0]].address,
                conf['nodes'][i][1]    
            )        
        else:
            nodes[conf['nodes'][i][0]].stream.add_sender(
                nodes[conf['nodes'][i+1][0]].address,
                conf['nodes'][i][1])
    
    for node in nodes.values():
        threading.Thread(target=node.run).start()
  
