// Set this to false if you don't want the alert to show. Set it to true to have it show up.

var alertShow = false;
var alertStyle = 'warning'; // Yellow=warning, Red=danger, Blue=info, Green=success

// Define the Text for your alert here. No HTML needed - that is taken care of below.

var alertText = '<strong>Some library online systems will be undergoing maintenance Sunday, March 22, from 9:00 am until noon.</strong> Expect some system downtime.';

if(alertShow == true) {

	jQuery('#cms-content').prepend('<div class="alert alert-' + alertStyle + '"><p>' + alertText + '</p></div>');
	console.log('Adding a global alert');

}