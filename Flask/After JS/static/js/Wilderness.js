// [ 0 ,         1          ,    2  ,    3  ,      4      ,     5    ,      6      ]
// [name, Weight of spawning, Damage, Health, Attack Speed, Food Loot, Leather Loot]
const Enemies = [
    ["Rat", 5, 1, 3, 500, 1, 0],
    [ "Group of Rats", 4, 3, 10, 750, 3, 1], 
    ["Huge Rat", 2, 5, 15, 1000, 5, 2], 
    ["Wolf", 1, 10, 22, 1250, 7, 5],  
    ["Stag", 0, 20, 35, 1750, 20, 10]
]

var HomeURl = window.location.protocol + '//' + window.location.host + '/menu';
console.log(HomeURl)
function GoHome(){
    window.location.replace(HomeURl);
}
var Health = 20;
var AttackSpeed = 1000;

function LoadBattle(){
    UnpackValues();

    LoadPlayer();
    LoadEnemy();
    setTimeout(function(){
        Fight()
    }, 1000);
    
    
    
    
}

function UnpackValues(){
    //pop
    //console.log(population)
    population = JSON.parse(localStorage.getItem("population"));
    //console.log(population)

    //Res and workers

    ResTotal = JSON.parse(localStorage.getItem("ResTotal"));
    ResW = JSON.parse(localStorage.getItem("ResW"));
    console.log("Res Total : " + ResTotal)
    //Weapons
    //weapons =   [ 0 name, 1 Damage, 2 Wood Cost, 3 Stone Cost, 4 Iron Cost, 5 Steel Cost]
    SwordIndex = JSON.parse(localStorage.getItem("SwordIndex"));

    //ExploredArea
    //ExploredArea = JSON.parse(localStorage.getItem("ExploredArea"));
    ExploredArea = JSON.parse(localStorage.getItem("ExploredArea"));
}


function SaveValues(){
    //pop
    sessionStorage.setItem("population", JSON.stringify(population));

    //Res and workers
    sessionStorage.setItem("ResTotal", JSON.stringify(ResTotal));
    sessionStorage.setItem("ResW", JSON.stringify(ResW));

    //Weapons
    sessionStorage.setItem("SwordIndex", JSON.stringify(SwordIndex));

    sessionStorage.setItem("Run", JSON.stringify(Run));

}

function LoadPlayer(){
    document.getElementById("Health").innerHTML = "Health : 20/20";
    document.getElementById("Attack").innerHTML = "Attack : " + Weapons[SwordIndex][1];
}

function Fight(){
    let i = 0;
    let CurrentHealth = Health;
    let CurrenteHealth = ChosenEnemy[3];
    var fighting = setInterval(function() {
        if(250*i%ChosenEnemy[4] == 0){
            CurrentHealth = CurrentHealth - ChosenEnemy[2];
            document.getElementById("Health").innerHTML = "Health : " + CurrentHealth + "/20";
        }
        if(250*i%AttackSpeed == 0){
            CurrenteHealth = CurrenteHealth - Weapons[SwordIndex][1];
            document.getElementById("eHealth").innerHTML = "Health : " + CurrenteHealth + "/" + ChosenEnemy[3];
        }
        if(CurrentHealth <= 0){
            CurrentHealth=0;
            clearInterval(fighting);
            population -= 1;
            Weapons[SwordIndex][1] = 1;
            population += 1;
            SwordIndex=0;
            console.log("Res Total : " + ResTotal)
            SaveValues();
            setTimeout(function(){
                GoHome()
            },2000);
            

        } 
        if( CurrenteHealth <= 0){
            CurrenteHealth=0;
            clearInterval(fighting);
            ResTotal[0] += ChosenEnemy[5];
            ResTotal[5] += ChosenEnemy[6];
            SaveValues();
            setTimeout(function(){
                GoHome()
            },2000);

        }
        i+=1
    }, 250);
}

function LoadEnemy(){
    AssingWeights(Weapons[SwordIndex][1])
    ChosenEnemy = ChoseEnemy();
    document.getElementById("eCharacterName").innerHTML = ChosenEnemy[0];
    document.getElementById("eHealth").innerHTML = "Health : " + ChosenEnemy[3] + "/" + ChosenEnemy[3];
    document.getElementById("eAttack").innerHTML = "Attack : " + ChosenEnemy[2];
    

}

function ChoseEnemy(){
    let weight = 0;
    for (let i = 0; i < Enemies.length; ++i) {
        weight += Enemies[i][1];
    }
    const threshold = Math.random() * weight;
    weight = 0;
    for (let i = 0; i < Enemies.length; ++i) {
        weight += Enemies[i][1];
        if (weight >= threshold) {
            return Enemies[i]
        }
    }  
}

function AssingWeights(WpnD){
    let RatWeight = 10;
    let GORWeight = 0;
    let GRWeight = 0;
    let WWeight = 0;
    let SWeight = 0;

    const Weights = [RatWeight, GORWeight, GRWeight, WWeight, SWeight];

    for (let i = 0; i < Enemies.length; ++i) {
        Enemies[i][1] = Weights[i];
    } 

}