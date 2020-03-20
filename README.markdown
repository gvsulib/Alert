# README

This is a quick JavaScript file that houses a global alert for all GVSU Library Systems. Rather than manually update every single one of our systems (14 at current count), we can include this JS file on each system, and simply update the alert text and whether it is on or off on a single file.

To include the script, you need to simply load the alert.js file:

```
<script src="/PATH/TO/alert.js">
```

Some of our system back ends are inaccessible while I am off-campus. For those, I added the script loading to the existing JavaScript file:

```
var alertScript = document.createElement('script');
alertScript.src = 'PATH/TO/alert.js';
document.body.appendChild(alertScript);
```

The master branch of this repository has a generic message. To update the alert, make a new branch or use a previous non-master branch to update messaging.

Questions? Email [reidsmam@gvsu.edu](mailto:reidsmam@gvsu.edu)