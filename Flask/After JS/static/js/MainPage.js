var Run = 0;

//Pop
var Population = 5;

//Ressources, Workers  and their buttons
var FWbutton = document.getElementById("FW")
var WWbutton = document.getElementById("WW"),

ResWNames = ["FW","WW","StoW","IW","SteW","LW",];
ResTotal = [0,0,0,0,0,0];
ResW = [0,0,0,0,0,0];
Res=["F","W","Sto","I", "Ste","L"];


//Explored Area
var ExploredArea = 0,
    TotalArea = '???';

//Weapons
var SwordIndex = 0;
// weapons =   [ 0 name, 1 Damage, 2 Wood Cost, 3 Stone Cost, 4 Iron Cost, 5 Steel Cost]
const Weapons = [["Fist", 1], ["Wooden", 5, 20, 0, 0, 0], ["Stone", 9, 15, 15, 0, 0], ["Iron", 13, 25, 0, 15, 0], ["Steel", 17, 30, 0, 0, 15]]


//Chat
var chat = document.getElementById("chat");
const HTwoElment = document.createElement("H2"); 
const BRElment = document.createElement("br");


function Start(){
    LoadValues();
    CheckDisplay()
    count(0);
    count(1);
}


function CheckDisplay(){
    document.getElementById(ResWNames[0]).innerHTML =  ResW[0];
    document.getElementById(ResWNames[1]).innerHTML =  ResW[1];
    document.getElementById("Population").innerHTML =  "Population : " + Population + " / 5";
    document.getElementById("WoodenSwordButton").style.visibility="hidden";
    document.getElementById(Weapons[SwordIndex+1][0]+"SwordButton").style.visibility="visible";

}


function Redirect(link){
    SaveValues()
    window.location.href = link;
}

function ClearStorage(){
    localStorage.clear();

}

function SaveValues(){

    //pop
    localStorage.setItem("Population", JSON.stringify(Population));

    //Res and workers
    localStorage.setItem("ResTotal", JSON.stringify(ResTotal));
    localStorage.setItem("ResW", JSON.stringify(ResW));

    //Weapons
    localStorage.setItem("SwordIndex", JSON.stringify(SwordIndex));

    //ExploredArea
    localStorage.setItem("ExploredArea", JSON.stringify(ExploredArea));

    //First run
    localStorage.setItem("Run", JSON.stringify(Run));



}

function LoadValues(){

    /*for (var key in localStorage){
        console.log(key)
    }

    console.log("1")

    for ( var i = 0, len = localStorage.length; i < len; ++i ) {
        console.log( localStorage.getItem( localStorage.key( i ) ) );
    }*/

    if (localStorage.getItem("Run") === null){
        SaveValues() 
        console.log("first run");
    }

    Population = JSON.parse(localStorage.getItem("Population"));

    //Res and workers
    ResTotal = JSON.parse(localStorage.getItem("ResTotal"));
    console.log("Res Total : " + ResTotal)
    ResW = JSON.parse(localStorage.getItem("ResW"));
    console.log("Res workers : " + ResW)

    //Weapons

    console.log(JSON.parse(localStorage.getItem("SwordIndex")));
    SwordIndex = JSON.parse(localStorage.getItem("SwordIndex"));

    //ExploredArea
    console.log(JSON.parse(localStorage.getItem("ExploredArea")));
    ExploredArea = JSON.parse(localStorage.getItem("ExploredArea"));

    console.log(JSON.parse(localStorage.getItem("Run")) + "run");
    Run = JSON.parse(localStorage.getItem("Run"));

}


function increase(id,clr,pop) {
    if(ResW[0]+ResW[1]<pop){
        ResW[id] += 1;
        sendUserInfo(ResWNames[id],1)
    }
    document.getElementById(ResWNames[id]).innerHTML =  ResW[id]; //workers + " Workers " + ResW[id];// + "  | POP:" + pop + " WW:" + WW + " FW:" + FW;
    document.getElementById(ResWNames[id]).style.color = clr;
    
}


function decrease(id,clr) {
    if(ResW[id]>0){
        ResW[id] -= 1;
        sendUserInfo(ResWNames[id],-1)
    }
    document.getElementById(ResWNames[id]).innerHTML =  ResW[id]; //workers + " Workers " + ResW[id];
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
    }   
    request.send()

}

function count(id){
    setInterval(function() {
        ResTotal[id] = ResTotal[id] + ResW[id]*0.05;
        document.getElementById(Res[id]).innerHTML=addCommas(preciseRound(ResTotal[id],0));
    }, 100);
}

function preciseRound(n,d){
    return Math.floor(n*Math.pow(10,d)) / Math.pow(10,d);
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
    if(ExploredArea > 5000){
        document.getElementById("CrystalLink").style.visibility="visible";
    }
}

function Randint(a, b) {
    return Math.floor(Math.random() * (1 + a - b) + b)
}

function UpgradeWeapon(){
    let EnoughRes = true;
    for (let i = 2; i < Res.length; i++) {
        if (ResTotal[i-1] < Weapons[SwordIndex+1][i]){
            EnoughRes = false;
        }
    }

    if(EnoughRes){
        
        document.getElementById(Weapons[SwordIndex+1][0]+"SwordButton").style.visibility="hidden";
        document.getElementById(Weapons[SwordIndex+1][0]+"SwordButton").style.opacity=0;
        for (let i = 2; i < Res.length;i++) {
            ResTotal[i-1] -= Weapons[SwordIndex+1][i];
        }
        SwordIndex += 1;
        document.getElementById(Weapons[SwordIndex+1][0]+"SwordButton").style.visibility="visible";
        document.getElementById("TechTreeLink").style.display="block";
        
    }


}