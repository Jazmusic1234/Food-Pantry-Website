import json

data = {}

data['item'] = []

data['item'].append({
    'name': 'Brocolli',
    'image': 'img/brocolli.jpg',
    'credit': 3
})

data['item'].append({
    'name': 'Banana',
    'image': 'img/banana.jpg',
    'credit': 4
})

data['item'].append({
    'name': 'Bread',
    'image': 'img/bread.jpg',
    'credit': 3
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
