from flask import Flask, json, request

cars = [{"Name": "Renault Alpine A110", "Personenanzahl": 2, "Stauraum": 196, "Preis": 58500, "Leistung": 258, "Umweltfreundlich": "Nein"},
 {"Name": "Corvette C8", "Personenanzahl": 2, "Stauraum": 357, "Preis": 72000, "Leistung": 495, "Umweltfreundlich": "Nein"},
  {"Name": "Jaguar  F-Type", "Personenanzahl": 2, "Stauraum": 196, "Preis": 66000, "Leistung": 300, "Umweltfreundlich": "Nein"}, 
  {"Name": "BMW 440i", "Personenanzahl": 4, "Stauraum": 480, "Preis": 58500, "Leistung": 326, "Umweltfreundlich": "Nein"}, 
  {"Name": "Toyota Supra", "Personenanzahl": 2, "Stauraum": 290, "Preis": 48000, "Leistung": 252, "Umweltfreundlich": "Nein"}, 
  {"Name": "Audi TT RS", "Personenanzahl": 4, "Stauraum": 280, "Preis": 71000, "Leistung": 400, "Umweltfreundlich": "Nein"}, 
  {"Name": "Skoda Karoq", "Personenanzahl": 5, "Stauraum": 521, "Preis": 25000, "Leistung": 110, "Umweltfreundlich": "Ja"}, 
  {"Name": "Hyundai Kona", "Personenanzahl": 5, "Stauraum": 332, "Preis": 20000, "Leistung": 120, "Umweltfreundlich": "Nein"}, 
  {"Name": "Peugeot 3008", "Personenanzahl": 5, "Stauraum": 395, "Preis": 36000, "Leistung": 131, "Umweltfreundlich": "Nein"}, 
  {"Name": "Audi Q2", "Personenanzahl": 5, "Stauraum": 355, "Preis": 26000, "Leistung": 110, "Umweltfreundlich": "Ja"}, 
  {"Name": "Cupra Formentor", "Personenanzahl": 5, "Stauraum": 420, "Preis": 35000, "Leistung": 150, "Umweltfreundlich": "Ja"}, 
  {"Name": "BMW X1", "Personenanzahl": 5, "Stauraum": 505, "Preis": 41000, "Leistung": 136, "Umweltfreundlich": "Ja"}  ]
 

api = Flask(__name__)

@api.route('/search', methods=['GET'])
def get_companies():
  args = request.args
  cars2 = []
  for i in cars :
    if i.get("Personenanzahl") >= int(args.get("sitz")):
      cars2.append(i)
    if int(args.get("sitz")) <= 2 and int(args.get("stauraum")) <= 200:
       return json.dumps(cars[0])
    
 

  return json.dumps(cars2)

  #return json.dumps(cars)

if __name__ == '__main__':
    api.run(host="0.0.0.0") 

#[{}]
