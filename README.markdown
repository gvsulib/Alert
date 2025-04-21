# Application Name

Alert App

# Purpose

This is a small application that toggles CMS global alerts for all GVSU Library Systems. Rather than manually update every single one of our systems (14 at current count), we can send a simple post operation to this application, which toggles alert visibility and also sets the alert message.  The application outputs a javascript with the alert message that's included in all of our pages outside the CMS.

# File Structure

This is a flask app and has the standard flask directory structure (https://flask.palletsprojects.com/en/stable/)

The javascript it outputs has to be placed in the "alert" folder inside our "labs" folder on the production server.  This is where all our javascript include statements point.  The exact path is in the app file.

# Access

Setting/changing the alert message requires the URL to the POST endpoint on the server.  You can get this from the maintainer or our Head of Systems and Discovery

# usage

To set a message, send a POST request to the app URL (using something like postman).  The POST body must include properties that designate wether the alert should be shown or hidden, and the alert message that should be used.

example:

```
{
    "alert":"false",
    "msg":"test message"
}
```

Based on the previous json, the python code would write out the following to alert.js:

```

// Set this to false if you don't want the alert to show. Set it to true to have it show up.

var alertShow = false;

// Define the Text for your alert here. No HTML needed - that is taken care of below.

var alertText = 'test message';

if(alertShow == true) {

	// This is designed to show up in a specific spot on the GVSU Library template. 
	// If your website is different, you need to change where this places the text.
	jQuery('#cms-content').prepend('<div class="alert alert-warning"><p>' + alertText + '</p></div>');
	console.log('Adding a global alert');

}
```

To include the script, you need to simply load the alert.js file:

```
<script src="/PATH/TO/alert.js">
```

Some of our system back ends are inaccessible while we are off-campus. For those, we added the script loading to the existing JavaScript file:

```
var alertScript = document.createElement('script');
alertScript.src = 'PATH/TO/alert.js';
document.body.appendChild(alertScript);
```

The master branch of this repository has a generic message. To update the alert, make a new branch or use a previous non-master branch to update messaging.

# Maintainers

Matthew Reidsma [reidsmam@gvsu.edu](mailto:reidsmam@gvsu.edu)
Kyle Felker [felkerk@gvsu.edu](mailto:felkerk@gvsu.edu)
