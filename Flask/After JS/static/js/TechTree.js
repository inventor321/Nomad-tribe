//                         0          ,           1            ,  2  ,  3  ,    4   ,   5  ,   6   ,  7     ,   8   
//    Techs =   [         Name        ,     button name        , Food, Wood,   Stone,  Iron,  Steel, Leather, science]
const Techs =   [["Communities",          "Communities"        , 50,   25  ,    0  ,    0  ,    0   ,  0   , 10],  //0
                ["Villagios",             "Villagios"          , 250,  225  ,   0  ,    0  ,    0   ,  0   , 210], //1
                ["Ressource Production",  "RessourceProduction", 500,  500  ,   100  ,  100  ,  100 ,  100 , 100],  //2
                ["Stone Tools",           "StoneTools"         , 50,   50  ,    0  ,    0  ,    0   ,  0   , 10],  //3
                ["Iron Tools",            "IronTools"          , 250,  250  ,   100  ,  0  ,    0   ,  0   , 50],  //4
                ["Steel Tools",           "SteelTools"         , 500,  500  ,   300  ,  100  ,  0   ,  0   , 200], //5
                ["Hunting Stratagies",    "HuntingStratagies"  , 50,   50  ,    0  ,    0  ,    0   ,  0   , 50],  //6
                ["Spears",                "Spears"             , 50,   300  ,   50  ,   0  ,    0   ,  0   , 50],  //7
                ["Atlatls",               "Atlatls"            , 50,   100  ,   100  ,  10  ,   0   ,  0   , 50],  //8

    
]
//  Researched = [    0      ,    1     ,       2             ,       3    ,    4      ,    5       ,    6              ,     7 ,     8  ]
//  Researched = [Communities, villagios, Ressource Production, Stone Tools, Iron Tools, Steel Tools, Hunting Stratagies, Spears, Atlatls]
var Researched = [ false,          false,         false       ,       false,      false,      false,        false,            false,  false]

function Redirect(link){
    SaveValues()
    window.location.href = link;
}

function UnpackValues(){

    //Res 
    ResTotal = JSON.parse(localStorage.getItem("ResTotal"));

    //ExploredArea
    ExploredArea = JSON.parse(localStorage.getItem("ExploredArea"));

    if(JSON.parse(localStorage.getItem("Researched")) === null){
        console.log("running execcpl")
        localStorage.setItem("Researched", JSON.stringify(Researched));

    }
    
    Researched = JSON.parse(localStorage.getItem("Researched"));
    console.log(Researched)

}


function SaveValues(){

    //Researched
    localStorage.setItem("Researched", JSON.stringify(Researched));

    //Res and workers
    sessionStorage.setItem("ResTotal", JSON.stringify(ResTotal));

    
}


function LoadTech(){
    UnpackValues()
    ShowTech()
}


function ShowTech(){
    console.log("showing tech")
    for(let i =0; i<Researched.length; i++){
        console.log(Researched[i], Researched.length)
        if(Researched[i]){
            document.getElementById(Techs[i][1]+"Button").disabled = true;
            document.getElementById(Techs[i+1][1]).style.display="block";
        }
        
        
    }
    console.log("finished shpwing tech")
}


function ResearchTech(TechIndex, ){
    
}


function TechCheck(TechIndex){

    let EnoughRes = true;
    for(let i =2; i<Techs[1].length-2;i++){
        if (Techs[TechIndex][i]>ResTotal[i-2]){
            console.log("not enough res", ResTotal[i-2], Techs[TechIndex][i])
            return;
        }
    }

    if (EnoughRes){

        document.getElementById(Techs[TechIndex][1]+"Button").disabled = true;
        document.getElementById(Techs[TechIndex+1][1]).style.display="block";
        for(let i =2; i<Techs[1].length-2;i++){
            ResTotal[i-2] -= Techs[TechIndex][i];
        }
        Researched[TechIndex]=true;
    }

    SaveValues()



}