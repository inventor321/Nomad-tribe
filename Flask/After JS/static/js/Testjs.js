


var FWbutton = document.getElementById("FW")
var WWbutton = document.getElementById("WW"),
    ResW = [0,0];
    ResWNames = ["WW","FW"]




function increase(id,clr,workers,WW,FW,pop) {
    if(ResW[0]+ResW[1]>=pop){
        document.getElementById(ResWNames[id]).innerHTML = workers + " Workers " + ResW[id];// + "  | POP:" + pop + " WW:" + WW + " FW:" + FW;

    }else{
        ResW[id] += 1;
        document.getElementById(ResWNames[id]).innerHTML =  workers + " Workers " + ResW[id];// + "  | POP:" + pop + " WW:" + WW + " FW:" + FW;
        goFaster(id)
        sendUserInfo(ResWNames[id],1)
    }
    document.getElementById(ResWNames[id]).style.color = clr;

    
}


function decrease(id,clr,workers) {
    if(ResW[id]==0){
        document.getElementById(ResWNames[id]).innerHTML = workers + " Workers " + ResW[id];
    }else{
        ResW[id] -= 1;
        document.getElementById(ResWNames[id]).innerHTML =  workers + " Workers " + ResW[id];
        goSlower(id)
        sendUserInfo(ResWNames[id],-1)
    }
    document.getElementById(ResWNames[id]).style.color = clr;
}



function sendUserInfo(W, opertaion){
    let UserInfo = {
        'operation' : opertaion,
        'workers' : W,

    }
    const request = new XMLHttpRequest()
    request.open('POST',`/processUserInfo/${JSON.stringify(UserInfo)}`)
    request.onload = () => {
        const FlaskMessage = request.responseText
        console.log(FlaskMessage)
    }   
    request.send()

}


ResTotal = [0,0];
WorkingWorkers = [0,0];
Res=["W","F"]
function count(id){
    setInterval(function() {
        ResTotal[id] = ResTotal[id] + WorkingWorkers[id];
        document.getElementById(Res[id]).innerHTML=addCommas(preciseRound(ResTotal[id],0));
    }, 100);
}
function goFaster(id){
    
    WorkingWorkers[id] = WorkingWorkers[id] + 0.1;
    
}
function goSlower(id){
    
    WorkingWorkers[id] = WorkingWorkers[id] - 0.1;
    
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
        x1 = x1.replace(rgx, '$1' + "' " + '$2');
    }
    return x1 + x2;
}

function addtext(){
    const HTwoText = document.createTextNode("You find wood and some food");
    HTwoElment.appendChild(HTwoText);
    const element = document.getElementById("chat");
    element.appendChild(HTwoElment);
}

/*



// var qtyHolders = document.querySelectorAll(".qty-holder");
var qtyDecs = document.querySelectorAll(".qty-dec");
var qtyIncs = document.querySelectorAll(".qty-inc");

qtyDecs.forEach((qtyDec) => {
  qtyDec.addEventListener("click",function(e){
    if(e.target.nextElementSibling.value > 0){
      e.target.nextElementSibling.value--;
    } else {
      // delete the item, etc
    }
  })
})
qtyIncs.forEach((qtyDec) => {
  qtyDec.addEventListener("click",function(e){
    e.target.previousElementSibling.value++;
  })
})

const makeButton = (text = "", onclick = event => null) =>
{ const b = document.createElement("button")
  b.onclick = onclick
  b.appendChild(document.createTextNode(text))
  return b
}

const makeInput = (name = "", value = "") =>
{ const i = document.createElement("input")
  i.name = name
  i.value = value
  return i
}

const counter = (name = "", value = 0) =>
{ const elem = document.createElement("div")
  const input = makeInput(name, value)
  const update = f => event =>
    (value = f(value), input.value = value)
  
  input.disabled = true
  elem.appendChild(makeButton("+", update(x => x + 1)))
  elem.appendChild(makeButton("-", update(x => x - 1)))
  elem.appendChild(input)
  return elem
}

document.body.appendChild(counter("a"))      // <input name="a" value="0">
document.body.appendChild(counter("b", 3))   // <input name="b" value="3">
document.body.appendChild(counter("c", 5))   // <input name="c" value="5">





function doFunction() {
    const name = document.getElementById("name_").innerHTML

    $.ajax({
       url: '{{ url_for('
       view.path ') }}',
        type: 'POST',
       data: {
          name: name
       },
       success: function(response) {},
       error: function(response) {}
    });

 };


/*

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
            }*/
