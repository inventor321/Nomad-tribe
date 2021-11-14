//Pop
var population = 5;

//Ressources, Workers  and their buttons
var FWbutton = document.getElementById("FW")
var WWbutton = document.getElementById("WW"),

ResWNames = ["FW","WW","StoW","IW","SteW","LW",],
ResTotal = [0,0,0,0,0,0],
ResW = [0,0],
Res=["F","W","Sto","I", "Ste","L"];


//Explored Area
var ExploredArea = 0,
    TotalArea = '???';

//Weapons
var SwordIndex = 0;
// weapons =   [ 0 name, 1 Damage, 2 Wood Cost, 3 Stone Cost, 4 Iron Cost, 5 Steel Cost]
const Weapons = [["Wooden", 1, 20, 0, 0, 0], ["Stone", 5, 15, 15, 0, 0], ["Iron", 9, 25, 0, 15, 0], ["Steel", 13, 30, 0, 0, 15]]


//Chat
var chat = document.getElementById("chat");
const HTwoElment = document.createElement("H2"); 
const BRElment = document.createElement("br");


function SaveValues(link){
    console.log("saving...")
    //pop
    localStorage.setItem("population", JSON.stringify(population));

    //Res and workers
    localStorage.setItem("ResWNames", JSON.stringify(ResWNames));
    localStorage.setItem("ResTotal", JSON.stringify(ResTotal));
    localStorage.setItem("ResW", JSON.stringify(ResW));
    localStorage.setItem("Res", JSON.stringify(Res));
    console.log(ResTotal)
    //Weapons
    localStorage.setItem("SwordIndex", JSON.stringify(SwordIndex));

    //ExploredArea
    localStorage.setItem("ExploredArea", JSON.stringify(ExploredArea));


    window.location.href = link;

}

function LoadValues(){

    //pop
    population = JSON.parse(localStorage.getItem("population"));

    //Res and workers
    ResWNames = JSON.parse(localStorage.getItem("ResWNames"));
    ResTotal = JSON.parse(localStorage.getItem("ResTotal"));
    ResW = JSON.parse(localStorage.getItem("ResW"));
    Res = JSON.parse(localStorage.getItem("Res"));

    //Weapons

    SwordIndex = JSON.parse(localStorage.getItem("SwordIndex"));

    //ExploredArea
    ExploredArea = JSON.parse(localStorage.getItem("ExploredArea"));

}


function increase(id,clr,workers,WW,FW,pop) {
    if(ResW[0]+ResW[1]>=pop){
        document.getElementById(ResWNames[id]).innerHTML = ResW[id]; //workers + " Workers " + ResW[id];// + "  | POP:" + pop + " WW:" + WW + " FW:" + FW;

    }else{
        ResW[id] += 1;
        document.getElementById(ResWNames[id]).innerHTML =  ResW[id]; //workers + " Workers " + ResW[id];// + "  | POP:" + pop + " WW:" + WW + " FW:" + FW;
        sendUserInfo(ResWNames[id],1)
    }
    document.getElementById(ResWNames[id]).style.color = clr;
    
}


function decrease(id,clr,workers) {
    if(ResW[id]==0){
        document.getElementById(ResWNames[id]).innerHTML = ResW[id]; //workers + " Workers " + ResW[id];
    }else{
        ResW[id] -= 1;
        document.getElementById(ResWNames[id]).innerHTML =  ResW[id]; //workers + " Workers " + ResW[id];
        sendUserInfo(ResWNames[id],-1)
    }
    document.getElementById(TotalNames[id]).style.color = clr;
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
    }   
    request.send()

}

function count(id){
    setInterval(function() {
        ResTotal[id] = ResTotal[id] + ResW[id]*0.1;
        document.getElementById(Res[id]).innerHTML=addCommas(preciseRound(ResTotal[id],0));
    }, 100);
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

function Gather(){
    Explore()
    document.getElementById("GatherButton").disabled = true;
    setTimeout(function(){document.getElementById("GatherButton").disabled = false;},11000);
    var element = document.getElementById("loading");
    element.classList.remove("progress-value");
    void element.offsetWidth;
    element.classList.add("progress-value");
    ResTotal[0] += Randint(1, 3);
    ResTotal[1] += Randint(1, 6);
    
    const BRElment = document.createElement("br");
    const HTwoElment = document.createElement("H2");
    const HTwoText = document.createTextNode("You find wood and some food");
    HTwoElment.appendChild(HTwoText);
    const child = document.querySelector(".event");
    HTwoElment.className="event";
    chat.insertBefore(HTwoElment,child);
    chat.insertBefore(BRElment,child);

    
}

function Explore()
{
    ExploredArea = ExploredArea + 5
    document.getElementById("ExploredLand").innerHTML = "World explored : " + ExploredArea + "/" + TotalArea + "m<sup>2</sup>"  + " ( " + ExploredArea/TotalArea + "% )";
     
}

function Randint(a, b) {
    return Math.floor(Math.random() * (1 + a - b) + b)
}

function UpgradeWeapon(){
    let EnoughRes = true;

    for (let i = 1; i < Res.length-1; i++) {
        if (ResTotal[i] < Weapons[SwordIndex][i]){
            EnoughRes = false;
        }
    }

    if(EnoughRes){
        
        document.getElementById(Weapons[SwordIndex][0]+"SwordButton").style.visibility="hidden";
        document.getElementById(Weapons[SwordIndex][0]+"SwordButton").style.opacity=0;
        SwordIndex += 1;
        for (let i = 1; i < Res.length-1; i++) {
            ResTotal[i] -= Weapons[SwordIndex][i];
        }
        
        document.getElementById(Weapons[SwordIndex][0]+"SwordButton").style.visibility="visible";
    }


}