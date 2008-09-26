/*
Syncotype v1.  Created by Rob Goodlatte.
Special thanks to Emmett Nicholas for development help.
*/

var RG_Syncotype = {};

RG_Syncotype.drawControlBox = function() {
	var control = document.createElement('div');
	control.id = "syncotype_controlbox";
	control.style.position = "absolute";
	control.style.right = "5px";
	control.style.top = "0";
	control.style.width = "108px";
	control.style.color= "#fff";
	control.style.zIndex = "1000";
	control.style.backgroundImage = "url(http://s.robgoodlatte.com/i/background.png)";
	control.innerHTML = [
	'<div style="width: 50px; float: left; margin: 2px 0 0 5px;">',
	'<img src="http://s.robgoodlatte.com/i/lheight.png" alt="line height" /><br/>',
	'<input type="text" name="stype_lheight" id="stype_lheight" value="18" size="2" style="margin-left: 5px !important;" />',
	'</div>',
	'<div style="width: 50px; float: left; margin: 2px 0 0 0;">',
	'<img src="http://s.robgoodlatte.com/i/offset.png" alt="offset" style="margin-left: 4px !important;" /><br/>',
	'<input type="text" name="stype_offset" id="stype_offset" value="0" size="2" style="margin-left: 0 !important;" />',
	'</div>',
	'<input type="image" src="http://s.robgoodlatte.com/i/button.png" style="display: inline !important; border: 0 !important; margin: 4px 0 4px 4px !important; clear: left;" id="stype_button" onclick="stype_process();" value="Syncotype" />'
	].join('');
	document.body.appendChild(control);
}

RG_Syncotype.drawBaselines = function drawBaselines(lheight,offset) {
	var baseline = document.createElement('div');	
	baseline.id = "synco_baseline";
	baseline.style.backgroundImage = "url(http://s.robgoodlatte.com/i/" + lheight + ".png)";
	baseline.style.height = document.getElementsByTagName('html')[0].scrollHeight - offset + 'px';
	baseline.style.width = "100%"
	baseline.style.position = "absolute";
	baseline.style.left = "0";
	baseline.style.top = offset + "px";
	baseline.style.zIndex = "500";
	document.getElementsByTagName('body').item(0).appendChild(baseline);
 	setOpacity(baseline, 0);
	baseline.style.visibility = 'visible';
	fadeIn('synco_baseline',0);
}

function syncotype_clear() {
	document.getElementsByTagName('body').item(0).removeChild(document.getElementById('synco_baseline'));
	var st_box = document.getElementById('sType_controlbox');
	st_box.innerHTML = "<div style='width: 50px; float: left; margin: 2px 0 0 5px;'><img src='http://s.robgoodlatte.com/i/lheight.png' alt='line height' /><br/><input type='text' name='stype_lheight' id='stype_lheight' value='18' size='2' style='margin-left: 5px !important;' /></div>";
	st_box.innerHTML += "<div style='width: 50px; float: left; margin: 2px 0 0 0;'><img src='http://s.robgoodlatte.com/i/offset.png' alt='offset' style='margin-left: 4px !important;' /><br/><input type='text' name='stype_offset' id='stype_offset' value='0' size='2' style='margin-left: 0 !important;' /></div>";
	st_box.innerHTML += "<input type='image' src='http://s.robgoodlatte.com/i/button.png' style='display: inline !important; border: 0 !important; margin: 4px 0 4px 4px !important; clear: left' id='stype_button' onclick='stype_process();' value='Syncotype' />";
}

function setOpacity(obj, opacity) {
  opacity = (opacity == 100)?99.999:opacity;
  obj.style.filter = "alpha(opacity:"+opacity+")";
  obj.style.KHTMLOpacity = opacity/100;
  obj.style.MozOpacity = opacity/100;
  obj.style.opacity = opacity/100;
}

function fadeIn(objId,opacity) {
  if (document.getElementById) {
    obj = document.getElementById(objId);
    if (opacity <= 100) {
      setOpacity(obj, opacity);
      opacity += 10;
      window.setTimeout("fadeIn('"+objId+"',"+opacity+")", 100);
    }
  }
}

function synco_initialize() {
	//RG_Syncotype.drawControlBox();
	renderControlBox();
}

function renderControlBox() {
	var st_box = document.createElement('div');
	st_box.id = "sType_controlbox";
	st_box.style.position = "absolute";
	st_box.style.right = "5px";
	st_box.style.top = "0";
	st_box.style.width = "108px";
	st_box.style.color= "#fff";
	st_box.style.zIndex = "1000";
	st_box.style.backgroundImage = "url(http://s.robgoodlatte.com/i/background.png)";
	document.getElementsByTagName('body').item(0).appendChild(st_box);
	st_box.innerHTML = "<div style='width: 50px; float: left; margin: 2px 0 0 5px;'><img src='http://s.robgoodlatte.com/i/lheight.png' alt='line height' /><br/><input type='text' name='stype_lheight' id='stype_lheight' value='18' size='2' style='margin-left: 5px !important;' /></div>";
	st_box.innerHTML += "<div style='width: 50px; float: left; margin: 2px 0 0 0;'><img src='http://s.robgoodlatte.com/i/offset.png' alt='offset' style='margin-left: 4px !important;' /><br/><input type='text' name='stype_offset' id='stype_offset' value='0' size='2' style='margin-left: 0 !important;' /></div>";
	st_box.innerHTML += "<input type='image' src='http://s.robgoodlatte.com/i/button.png' style='display: inline !important; border: 0 !important; margin: 4px 0 4px 4px !important; clear: left;' id='stype_button' onclick='stype_process();' value='Syncotype' />";
	
	setOpacity(st_box, 0);
	st_box.style.visibility = 'visible';
	fadeIn('sType_controlbox',0);
}

function stype_process() {
	var lheight = document.getElementById('stype_lheight').value;
	var offset = document.getElementById('stype_offset').value;
	
	if(lheight > 0 && lheight < 37) { 
	if(offset > -999 && offset < 999) {
	if(document.getElementById('synco_baseline')) {
		setBaseline(lheight, offset);
	} else {
	document.getElementById('stype_button').setAttribute("style","display:none;");
	document.getElementById('sType_controlbox').innerHTML += "<input type='image' src='http://s.robgoodlatte.com/i/redraw.png' id='stype_redraw' style='display: inline !important; border: 0 !important; margin: 4px 0 4px 4px !important; float: none !important;' onclick='stype_process();' value='Re-draw' /><input type='image' src='http://s.robgoodlatte.com/i/clear.png' style='display: inline !important; border: 0 !important; float: none !important; margin: 4px 0 4px 2px !important;' id='stype_clear' onclick='syncotype_clear();' value='Clear' />";
	RG_Syncotype.drawBaselines(lheight,offset);
	} } else {
		alert("Offset must be a number");
	}
	} else {
		alert("Line height must be a number between 1 and 36");
	}
	

}
function setBaseline(lheight, offset) {
	setTimeout(function() {
		var baseline = document.getElementById('synco_baseline');
		baseline.style.backgroundImage = "url(http://s.robgoodlatte.com/i/" + lheight + ".png)";
		baseline.style.top = offset + "px";
		baseline.style.height = document.getElementsByTagName('html')[0].scrollHeight - offset + 'px';
		//fade
		setOpacity(baseline, 0);
		baseline.style.visibility = 'visible';
		fadeIn('synco_baseline',0);
	
	},10);
	
}

RG_Syncotype.combine = function combine(func1, func2){return function(){if (func1){func1();}if (func2){func2();}};};
window.onload = RG_Syncotype.combine(window.onload, synco_initialize);
