// [ 0 ,         1          ,    2  ,    3  ,      4      ,     5    ,      6      ]
// [name, Weight of spawning, Damage, Health, Attack Speed, Food Loot, Leather Loot]
const Enemies = [
    ["Rat", 5, 1, 3, 500, 1, 0],
    [ "Group of Rats", 4, 3, 10, 750, 3, 1], 
    ["Huge Rat", 2, 5, 15, 1000, 5, 2], 
    ["Wolf", 1, 10, 22, 1250, 7, 5],  
    ["Stag", 0, 20, 35, 1750, 20, 10]
]


var WeaponDamage = 1;
var Health = 20;
var AttackSpeed = 1000;

function LoadBattle(){
    LoadPlayer();
    LoadEnemy();
    setTimeout(Fight(), 1000);
}

function LoadPlayer(){
    document.getElementById("Health").innerHTML = "Health : 20/20";
    document.getElementById("Attack").innerHTML = "Attack : " + WeaponDamage;
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
            CurrenteHealth = CurrenteHealth - WeaponDamage;
            document.getElementById("eHealth").innerHTML = "Health : " + CurrenteHealth + "/" + ChosenEnemy[3];
        }
        if(CurrentHealth <= 0){
            clearInterval(fighting);
            population -= 1;
            WeaponDamage = 1;
        } 
        if( CurrenteHealth <= 0){
            clearInterval(fighting);
            ResW[1] += ChosenEnemy[5];
            ResW[2] += ChosenEnemy[6]
        }
        i+=1
    }, 250);
}

function LoadEnemy(){
    AssingWeights(WeaponDamage)
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

function AssingWeights(WeaponDamage){
    let RatWeight = 10;
    let GORWeight = 3;
    let GRWeight = WeaponDamage;
    let WWeight = 0;
    let SWeight = 0;

    const Weights = [RatWeight, GORWeight, GRWeight, WWeight, SWeight];

    for (let i = 0; i < Enemies.length; ++i) {
        console.log("1  :" + Weights[i]);
        Enemies[i][1] = Weights[i];
    } 

}