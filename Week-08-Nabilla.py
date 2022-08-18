import pymongo 
from datetime import datetime
from flask import Flask,request

app = Flask(__name__)

@app.route('/nabilla',methods=['POST'])
def sensor():

    dt = datetime.now()
    client = pymongo.MongoClient("mongodb+srv://alynabilla:nabilla1@nabilla8.ivktq1x.mongodb.net/?retryWrites=true&w=majority")
    db = client['week08']
    my_collections = db['file']


    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')


    nilai_sensor = {'kecepatan':kecepatan,
                    'latitude':latitude,
                    'longitude':longitude,
                    'timestamp' : dt
                    }

    results = my_collections.insert_one(nilai_sensor)
    return ('file berhasil diupload')  



if __name__ == '__main__':
    app.run(debug=True)
