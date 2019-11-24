const container = document.getElementById('root')
container.setAttribute('class', 'container')

let data = {
    "item": [
        {
            'name': "brocolli",
            "image": 'img/brocolli.jpg',
            'credit': 3,
        },
        {
            'name': 'Banana',
            'image': 'img/banana.jpg',
            'credit': 4
        }, {
            'name': 'Bread',
            'image': 'img/bread.jpg',
            'credit': 3
        }
    ]
}
function loadJSON(callback) {

    var xobj = new XMLHttpRequest();
        xobj.overrideMimeType("application/json");
    xobj.open('GET', 'data.json', true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
          }
    };
    xobj.send(null);
 }

var jsonData = JSON.parse(data);

jsonData.forEach(item => {
    const card = document.createElement('div')
    card.setAttribute('class', 'card')

    const h1 = document.createElement('h1')
    h1.textContent = item.name

    const pic = document.createElement('img')
    pic.src = item.image

    const credit = document.createElement('p')
    credit.textContent = item.credit

    container.appendChild(card)

    card.appendChild(h1)
    card.appendChild(pic)
    card.appendChild(credit)

    console.log(item.name)
})