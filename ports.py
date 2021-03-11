unicornGrid = [[0]*16 for i in range(16)]

ahvenanmaa = {
    "name": "Ahvenanmaa",
    "y1": 14,
    "y2": 15,
    "x1": 0,
    "x2": 1
}
turku = {
    "name": "Turku",
    "y1": 14,
    "y2": 15,
    "x1": 6,
    "x2": 7
}
helsinki = {
    "name": "Helsinki",
    "y1": 14,
    "y2": 15,
    "x1": 10,
    "x2": 11
}
hamina = {
    "name": "Hamina",
    "y1": 14,
    "y2": 15,
    "x1": 14,
    "x2": 15
}
pori = {
    "name": "Pori",
    "y1": 10,
    "y2": 11,
    "x1": 6,
    "x2": 7
}
vaasa = {
    "name": "Vaasa",
    "y1": 6,
    "y2": 7,
    "x1": 6,
    "x2": 7
}
kokkola = {
    "name": "Kokkola",
    "y1": 3,
    "y2": 4,
    "x1": 10,
    "x2": 11
}
oulu = {
    "name": "Oulu",
    "y1": 0,
    "y2": 1,
    "x1": 14,
    "x2": 15
}

def toggle_ports(port):
    if port == ahvenanmaa['name']:
        unicornGrid[ahvenanmaa['y1']][ahvenanmaa['x1']] = 1
        unicornGrid[ahvenanmaa['y1']][ahvenanmaa['x2']] = 1
        unicornGrid[ahvenanmaa['y2']][ahvenanmaa['x1']] = 1
        unicornGrid[ahvenanmaa['y2']][ahvenanmaa['x2']] = 1
    if port == turku['name']:
        unicornGrid[turku['y1']][turku['x1']] = 1
        unicornGrid[turku['y1']][turku['x2']] = 1
        unicornGrid[turku['y2']][turku['x1']] = 1
        unicornGrid[turku['y2']][turku['x2']] = 1
    if port == helsinki['name']:
        unicornGrid[helsinki['y1']][helsinki['x1']] = 1
        unicornGrid[helsinki['y1']][helsinki['x2']] = 1
        unicornGrid[helsinki['y2']][helsinki['x1']] = 1
        unicornGrid[helsinki['y2']][helsinki['x2']] = 1
    if port == hamina['name']:
        unicornGrid[hamina['y1']][hamina['x1']] = 1
        unicornGrid[hamina['y1']][hamina['x2']] = 1
        unicornGrid[hamina['y2']][hamina['x1']] = 1
        unicornGrid[hamina['y2']][hamina['x2']] = 1
    if port == pori['name']:
        unicornGrid[pori['y1']][pori['x1']] = 1
        unicornGrid[pori['y1']][pori['x2']] = 1
        unicornGrid[pori['y2']][pori['x1']] = 1
        unicornGrid[pori['y2']][pori['x2']] = 1
    if port == vaasa['name']:
        unicornGrid[vaasa['y1']][vaasa['x1']] = 1
        unicornGrid[vaasa['y1']][vaasa['x2']] = 1
        unicornGrid[vaasa['y2']][vaasa['x1']] = 1
        unicornGrid[vaasa['y2']][vaasa['x2']] = 1
    if port == kokkola['name']:
        unicornGrid[kokkola['y1']][kokkola['x1']] = 1
        unicornGrid[kokkola['y1']][kokkola['x2']] = 1
        unicornGrid[kokkola['y2']][kokkola['x1']] = 1
        unicornGrid[kokkola['y2']][kokkola['x2']] = 1
    if port == oulu['name']:
        unicornGrid[oulu['y1']][oulu['x1']] = 1
        unicornGrid[oulu['y1']][oulu['x2']] = 1
        unicornGrid[oulu['y2']][oulu['x1']] = 1
        unicornGrid[oulu['y2']][oulu['x2']] = 1
    
    print(unicornGrid)
