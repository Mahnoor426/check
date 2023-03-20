from flask import Flask, render_template, url_for
from flask import jsonify # <- `jsonify` instead of `json`


app=Flask(__name__) #creating flask object 
# printed hello world
#@app.route('/') # route tells which url should be called
#def index():
    #return "HELLO WORLD"
    #return render_template('index.html')


#(JSON) is used to transfer data as text that can be sent over a network. it represnts objects as key value pair
#fetching JSON objects
books_db = [{"name":"secret","price":250},{"name":"secret","price":250}]

#retrieving all the books
@app.route('/books')
def get_all_book():
    return jsonify({'/books':books_db}) #convert a json output into a response object with application


if __name__ =="__main__": 
    app.run(debug=True)
