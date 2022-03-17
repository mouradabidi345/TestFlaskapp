
# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__)


# # @app.route('/', methods=['GET', 'POST'])
# # def home():
# #     if request.method=='POST':
# #         model = pickle.load(open('svd_algo_optimized.pkl', 'rb'))
# #         user_input1 = request.form.get('userId')
# #         user_input2 = request.form.get('itemId')
# #         print(user_input1)
# #         print(user_input2)
# #         # prediction = model.predict([user_input1],[user_input2], verbose =True)
# #         # print(prediction)
# #     return render_template('index.html')


# @app.route('')
# def my_form():
#     return render_template('index.html')

# @app.route('/', methods = ['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

# if __name__  == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template,request
import pickle
import pandas as pd
# Flask constructor
app = Flask(__name__)   


#working
# # A decorator used to tell the application
# # which URL is associated function
# @app.route('/', methods =["GET", "POST"])
# def gfg():
#     if request.method == "POST":
#        # getting input with name = fname in HTML form
#        user_id = request.form.get("userId")
#        # getting input with name = lname in HTML form 
#        item_id = request.form.get("itemid") 
#        print(user_id)
#        print(item_id)
#        model = pickle.load(open('svd_algo_optimized.pkl', 'rb'))
#        predictedrating = model.predict(user_id,item_id,r_ui=4, verbose =True)
#        print(predictedrating[3])
#        return " The Predicted rating is " + str(predictedrating(3))
#     return render_template('form.html')

@app.route('/')
def form():
   return render_template('form.html')



@app.route('/',methods = ['POST', 'GET'])
def result():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       user_id = request.form.get("userId")
       # getting input with name = lname in HTML form 
       item_id = request.form.get("itemid") 
       print(user_id)
       print(item_id)
       model = pickle.load(open('svd_algo_optimized.pkl', 'rb'))
       result = model.predict(user_id,item_id,r_ui=4, verbose =True)
     
       
       return " The Predicted rating is " + str(result[3])
    return render_template('result.html',result = result)


if __name__=='__main__':
   app.run(debug=True)