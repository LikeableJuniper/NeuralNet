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
    def __init__(self, layers: list[int], connections: list[Connection] | list[list[Connection]]):
        self.layers = layers
        self.connections: list[list[Connection]] = connections
        self.sortConnections()
        self.optimizeConnections()
    
    def __repr__(self):
        return "{}".format(self.connections)
    
    def __call__(self, inputs: list[int]) -> list[int]:
        values = []
        for _ in range(len(self.layers)):
            values.append([])
        for i, nodes in enumerate(self.layers):
            for _ in range(nodes):
                values[i].append([])
        intValues = [[0]*i for i in self.layers]
        if self.layers[0] != len(inputs):
            raise ValueError("Amount of inputs must be equal to number of nodes on first layer.")
        intValues[0] = inputs
        for layer in range(len(self.layers)-1):
            for connection in self.connections[layer]:
                print(values, "a")
                values[layer+1][connection.target].append(connection.weight*intValues[layer][connection.source])
                print(values, "b")

            intValues[layer+1] = [sum(i) for i in values[layer+1]]
        return intValues[-1]

    def sortConnections(self) -> list[list[Connection]]:
        sortedConnections = [[] for _ in range(len(self.layers)-1)]
        for connection in self.connections:
            sortedConnections[connection.startLayer].append(connection)
        
        self.connections = [sorted(i, key=lambda x: x.source) for i in sortedConnections]

    def optimizeConnections(self):
        optimizedConnections = self.connections
        print(self.connections)
        for i, layer in enumerate(self.connections[1:]):
            for connection in layer:
                hasSource = False
                for iConnection in self.connections[i]:
                    if iConnection.target == connection.source:
                        hasSource = True
                        break
                if not hasSource:
                    optimizedConnections[i+1].pop(optimizedConnections[i+1].index(connection))


        self.connections = optimizedConnections
        print(self.connections)


if __name__ == "__main__":
    network = Network([3, 5, 6], [Connection(1, 5, 8, 1), Connection(1, 4, 1, 0), Connection(0, 4, 1, 0), Connection(2, 4, 1, 1), Connection(2, 1, -1, 0)])
    print(network([0.1, 1, 0]))
