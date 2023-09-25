
// Set this to false if you don't want the alert to show. Set it to true to have it show up.

var alertShow = true;

// Define the Text for your alert here. No HTML needed - that is taken care of below.

var alertText = 'test message';

if(alertShow == true) {

	// This is designed to show up in a specific spot on the GVSU Library template. 
	// If your website is different, you need to change where this places the text.
	jQuery('#cms-content').prepend('<div class="alert alert-warning"><p>' + alertText + '</p></div>');
	console.log('Adding a global alert');

}
