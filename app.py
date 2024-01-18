
from flask import Flask, render_template, request, Response, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/refresh/*": {"origins": ["https://www.gvsu.edu"]}}) 

text="""
// Set this to false if you don't want the alert to show. Set it to true to have it show up.

let alertShow = {show};

// Define the Text for your alert here. No HTML needed - that is taken care of below.

let alertText = '{message}';

if(alertShow == true) {{

	// This is designed to show up in a specific spot on the GVSU Library template. 
	// If your website is different, you need to change where this places the text.
	jQuery('#cms-content').prepend('<div class="alert alert-warning"><p>' + alertText + '</p></div>');
	console.log('Adding a global alert');

}}
"""

@app.route("/refresh", methods=['POST','OPTIONS'])
def alert():
  content = request.get_json(force=True)
  try:
    alertStatus = content["alert"]
    msg = content["msg"]
  except KeyError:
    return Response("One or more json values are missing", status=400, mimetype='application/text')
  print(alertStatus)
  msg = msg.replace("\n", "")
  msg = msg.replace("-", "&#8209")
  print(msg)
  if alertStatus != "true" and alertStatus != "false":
    return Response("invalid value for 'alert', acceptable values are 'true' or false'.", status=400, mimetype='application/text')
  formatted = text.format(show=alertStatus, message=msg)
  javascriptFile = open("/var/www/html/labs/alert/alert.js", "w")
  javascriptFile.write(formatted)
  javascriptFile.close()
  returnMsg = "Alert status updated:  show alert is '{show}' and message is '{message}'.".format(show=content["alert"], message=content["msg"])
  return Response(returnMsg, status=200, mimetype='application/text')
