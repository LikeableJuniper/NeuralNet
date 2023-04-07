import math


class Connection:
    def __init__(self, source, target, weight, startLayer):
        self.startLayer = startLayer
        self.source = source
        self.target = target
        self.weight = weight
    
    def __repr__(self):
        return "Connection({}, {}, {}, {})".format(self.source, self.target, self.weight, self.startLayer)


class Network:
    def __init__(self, layers: list[int], connections: list[Connection]):
        self.layers = layers
        self.connections = connections
        self.sortConnections()
    
    def __repr__(self):
        return "{}".format(self.connections)
    
    def simulate(self, inputs) -> list[int]:
        pass

    def sortConnections(self):
        sortedConnections = [[] for _ in range(len(self.layers))]
        for connection in self.connections:
            sortedConnections[connection.startLayer].append(connection)
        
        self.connections = [sorted(i, key=lambda x: x.source) for i in sortedConnections]


if __name__ == "__main__":
    print(Network([3, 5], [Connection(1, 5, 8, 1), Connection(1, 4, 1, 0), Connection(0, 4, 1, 0)]))
