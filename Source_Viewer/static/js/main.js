var height = screen.height;
	var width = screen.width;
	var he = document.getElementById('resolutionNumber');
	
	he.innerHTML = width + " X " + height;
	
	


	var toIns = document.getElementById("visit");
	var toInsD = document.getElementById("vo");
	var value = window.localStorage.getItem("trues");
	if(value==="a"){
		var date = window.localStorage.getItem("date");
		var visits= window.localStorage.getItem("visitxs");
		var str = date;
		var totalv = visits;
		toIns.innerHTML = "You last visited this page on " + str + " .";
		toInsD.innerHTML = "You have visited this page " + totalv + " times in total.";
		var totalVisits = +visits + 1;
	}
	else if(value===null){
		toIns.innerHTML = "This is the first time you are visting us. Reload to see some magic.";
		var totalVisits = 1;
	}
	var hasVisited = "a";
	var lastDate= new Date();
	var norm = lastDate.toUTCString();

	window.localStorage.setItem("trues",hasVisited);
	window.localStorage.setItem("date",norm);
	window.localStorage.setItem("visitxs",totalVisits);


	var nVer = navigator.appVersion;
var nAgt = navigator.userAgent;
var browserName  = navigator.appName;
//var fullVersion  = ''+parseFloat(navigator.appVersion); 
var majorVersion = parseInt(navigator.appVersion);
var fullVersion , nameOffset,verOffset,ix,os;


//In stock android , the version is after Android .. It is equal to the device version as well..
 if ((verOffset=nAgt.indexOf("OPR"))!=-1) {
 browserName = "Opera Next";
 fullVersion = nAgt.substring(verOffset+4);}
 else if ((verOffset=nAgt.indexOf("Chrome"))!=-1) {
 browserName = "Google Chrome";
 fullVersion = nAgt.substring(verOffset+7);
}
else if ((verOffset=nAgt.indexOf("Firefox"))!=-1) {
 browserName = "Firefox";
 fullVersion = nAgt.substring(verOffset+8);
}
else if ((verOffset=nAgt.indexOf("Android"))!=-1) {
	browserName = "Android Browser";
	fullVersion= nAgt.substring(verOffset+8);
	
}
// In Opera, the true version is after "Opera" or after "Version"
else if ((verOffset=nAgt.indexOf("Opera"))!=-1) {
 browserName = "Opera";
 fullVersion = nAgt.substring(verOffset+6);
 if ((verOffset=nAgt.indexOf("Version"))!=-1) 
   fullVersion = nAgt.substring(verOffset+8);
}
//In Opera Next(Based on Chrome) the version is after "OPR"...


// In MSIE, the true version is after "MSIE" in userAgent
else if ((verOffset=nAgt.indexOf("MSIE"))!=-1) {
 browserName = "Microsoft Internet Explorer";
 fullVersion = nAgt.substring(verOffset+5);
}
// In Chrome, the true version is after "Chrome" 

// In Safari, the true version is after "Safari" or after "Version" 
else if ((verOffset=nAgt.indexOf("Safari"))!=-1) {
 browserName = "Safari";
 fullVersion = nAgt.substring(verOffset+7);
 if ((verOffset=nAgt.indexOf("Version"))!=-1) 
   fullVersion = nAgt.substring(verOffset+8);
}
// In Firefox, the true version is after "Firefox" 

// In most other browsers, "name/version" is at the end of userAgent 
else if ( (nameOffset=nAgt.lastIndexOf(' ')+1) < 
          (verOffset=nAgt.lastIndexOf('/')) ) 
{
 browserName = nAgt.substring(nameOffset,verOffset);
 fullVersion = nAgt.substring(verOffset+1);
 if (browserName.toLowerCase()==browserName.toUpperCase()) {
  browserName = navigator.appName;
 }
}
if ((verOffset=nAgt.indexOf("Windows NT 6.1"))!=-1) {
	os= "Windows 7";
}
else if ((verOffset=nAgt.indexOf("Windows NT 6.2"))!=-1) {
	os= "Windows 8";
}
else if ((verOffset=nAgt.indexOf("Windows NT 6.0"))!=-1) {
	os= "Windows Vista";
}
else if ((verOffset=nAgt.indexOf("Windows NT 5.0"))!=-1) {
	os= "Windows XP";
}
else if ((verOffset=nAgt.indexOf("Android"))!=-1) {
	os= "Android";

}
else if ((verOffset=nAgt.indexOf("iPad"))!=-1 || (verOffset=nAgt.indexOf("iPhone"))!=-1) {
	os= "iOS";

}
else if ((verOffset=nAgt.indexOf("Linux"))!=-1) {
	os= "Linux";

}
else if ((verOffset=nAgt.indexOf("Macintosh"))!=-1) {
	os= "Mac OS X " ;

}
// trim the fullVersion string at semicolon/space if present
if ((ix=fullVersion.indexOf(";"))!=-1)
   fullVersion=fullVersion.substring(0,ix);
if ((ix=fullVersion.indexOf(" "))!=-1)
   fullVersion=fullVersion.substring(0,ix);

majorVersion = parseFloat(''+fullVersion );
if (isNaN(majorVersion)) {
 fullVersion  = ''+parseFloat(navigator.appVersion); 
 majorVersion = parseInt(navigator.appVersion,10);
}

var browse = document.getElementById('browser');
var version = document.getElementById('version');
var agent = document.getElementById('agent');
var agent2 = document.getElementById('os');

browse.innerHTML += browserName;
version.innerHTML += majorVersion;
agent.innerHTML += navigator.userAgent;
agent2.innerHTML += os;