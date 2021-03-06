var Run = 0;

//Pop
var Population = 1;
var MaxPopulation = 1;



//Ressources, Workers  and their buttons
var FWbutton = document.getElementById("FW")
var WWbutton = document.getElementById("WW"),

ResWNames = ["FW","WW","StoW","IW","SteW","LW",];
ResTotal = [100,100,0,0,0,0];
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
    CheckDisplay();
    count(0);
    count(1);
}


function CheckDisplay(){
    document.getElementById(ResWNames[0]).innerHTML =  ResW[0];
    document.getElementById(ResWNames[1]).innerHTML =  ResW[1];
    console.log(Population)
    document.getElementById("Population").innerHTML =  "Population : " + Population + " / " + MaxPopulation;
    document.getElementById("WoodenSwordButton").style.visibility="hidden";
    document.getElementById(Weapons[SwordIndex+1][0]+"SwordButton").style.visibility="visible";
    document.getElementById("ExploredLand").innerHTML = "World explored : " + ExploredArea + "/" + TotalArea + "m<sup>2</sup>"  + " ( " + ExploredArea/TotalArea + "% )";
    document.getElementById("GatherButton").disabled = true;
    setTimeout(function(){document.getElementById("GatherButton").disabled = false;},11000);
    var element = document.getElementById("loading");
    element.classList.remove("progress-value");
    void element.offsetWidth;
    element.classList.add("progress-value");

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
    console.log(Population, 1)
    Population = JSON.parse(localStorage.getItem("Population"));
    console.log(Population, 1)
    //Res and workers
    ResTotal = JSON.parse(localStorage.getItem("ResTotal"));
    
    ResW = JSON.parse(localStorage.getItem("ResW"));
    

    //Weapons

    
    SwordIndex = JSON.parse(localStorage.getItem("SwordIndex"));

    //ExploredArea
    
    ExploredArea = JSON.parse(localStorage.getItem("ExploredArea"));

    
    Run = JSON.parse(localStorage.getItem("Run"));

}


function increase(id,clr) {
    if(ResW[0]+ResW[1]+1<Population){
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
        ResTotal[id] = ResTotal[id] + ResW[id]*0.01;
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
    if (Math.random()<0.6){
        Redirect('http://127.0.0.1:5000/wilderness')
    }else{
        ResTotal[0] += Randint(1, 3);
        ResTotal[1] += Randint(1, 6);
    }

    
    AddTextToChat("You find wood and some food")
    

    
}

function AddTextToChat(message){
    const BRElment = document.createElement("br");
    const HTwoElment = document.createElement("H2");
    let HTwoText = document.createTextNode(message);
    HTwoElment.appendChild(HTwoText);
    let child = document.querySelector(".event");
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
        if(Weapons[SwordIndex+1][0] == "Wooden"){

        }
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