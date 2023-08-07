from flask import *
import json

app = Flask(__name__)
@app.route('/',methods=['GET'])
def home_page():
    data_set= {"My_City":['New York','Los Angeles','Phoenix','Chicago','Houston','Philadelphia'],"My_Gender":["Male","Female"],
               "My_Population":[4125000,4300000,1985000,2070000,99800000,1350000,1400000,1100000,1120000,800000,810000,750000,770000,
                                99125000,99800000]
}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(port=3435)