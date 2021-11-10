total = 10.0;
speed = 0;
cost = 1;
function count(){
  setInterval(function() {
  total = total + speed;
                      document.getElementById('theNumber').innerHTML=addCommas(preciseRound (total,0));
                  document.getElementById('numberSpeed').innerHTML=addCommas(preciseRound((speed*10),0)) + ' number per second';
                    if (cost > total){
                          document.getElementById('goFasterButton').setAttribute('disabled','disabled');
                    }
                    else if (cost <= total){
                        document.getElementById('goFasterButton').removeAttribute('disabled');
                    }
                }, 100);
            }
            function goFaster(){
                if (cost <= total) {
                    total = total - cost;
                    cost = cost * 2.32;
                    speed = speed + 0.2;
                    document.getElementById('numberCost').innerHTML=addCommas(preciseRound(cost,0));
                }
            }
            function preciseRound(n,d){
                return Math.round(n*Math.pow(10,d)) / Math.pow(10,d);
            }
            function addCommas(nStr)
            { 
	            nStr += '';
	            x = nStr.split('.');
            	x1 = x[0];
            	x2 = x.length > 1 ? '.' + x[1] : '';
            	var rgx = /(\d+)(\d{3})/;
            	while (rgx.test(x1)) {
            		x1 = x1.replace(rgx, '$1' + ',' + '$2');
        	    }
            	return x1 + x2;
            }