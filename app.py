
from flask import Flask, render_template, request, Response, make_response
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app) 

text="""
// Set this to false if you don't want the alert to show. Set it to true to have it show up.

var alertShow = {show};

// Define the Text for your alert here. No HTML needed - that is taken care of below.

var alertText = '{message}';

if(alertShow == true) {{

	// This is designed to show up in a specific spot on the GVSU Library template. 
	// If your website is different, you need to change where this places the text.
	jQuery('#cms-content').prepend('<div class="alert alert-warning"><p>' + alertText + '</p></div>');
	console.log('Adding a global alert');

}}
"""

@app.route("/refresh", methods=['POST'])
def alert():
  if request.method == "OPTIONS": # CORS preflight
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
  content = request.get_json(force=True)
  try:
    alertStatus = content["alert"]
    msg = content["msg"]
  except KeyError:
    return Response("One or more json values are missing", status=400, mimetype='application/text')
  print(alertStatus)
  print(msg)
  if alertStatus != "true" and alertStatus != "false":
    return Response("invalid value for 'alert', acceptable values are 'true' or false'.", status=400, mimetype='application/text')
  formatted = text.format(show=alertStatus, message=msg)
  javascriptFile = open("/var/www/html/labs/alert/alert.js", "w")
  javascriptFile.write(formatted)
  javascriptFile.close()
  returnMsg = "Alert status updated:  show alert is '{show}' and message is '{message}'.".format(show=content["alert"], message=content["msg"])
  response = Response(returnMsg, status=200, mimetype='application/text')
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response
