//                         0          ,           1            ,  1  ,  2  ,    3   ,   4  ,   5   ,  6     ,   7   
//    Techs =   [         Name        ,     button name        , Food, Wood,   Stone,  Iron,  Steel, Leather, science]
const Techs =   [["Communities",          "CommunitiesButton"        , 50,   25  ,    0  ,    0  ,    0   ,  0   , 10],  //0
                ["Villagios",             "VillagiosButton"          , 250,  225  ,   0  ,    0  ,    0   ,  0   , 210], //1
                ["Ressource Production",  "RessourceProductionButton", 500,  500  ,   100  ,  100  ,  100 ,  100 , 100],  //2
                ["Stone Tools",           "StoneToolsButton"         , 50,   50  ,    0  ,    0  ,    0   ,  0   , 10],  //3
                ["Iron Tools",            "IronToolsButton"          , 250,  250  ,   100  ,  0  ,    0   ,  0   , 50],  //4
                ["Steel Tools",           "SteelToolsButton"         , 500,  500  ,   300  ,  100  ,  0   ,  0   , 200], //5
                ["Hunting Stratagies",    "HuntingStratagiesButton"  , 50,   50  ,    0  ,    0  ,    0   ,  0   , 50],  //6
                ["Spears",                "SpearsButton"             , 50,   300  ,   50  ,   0  ,    0   ,  0   , 50],  //7
                ["Atlatls",               "AtlatlsButton"            , 50,   100  ,   100  ,  10  ,   0   ,  0   , 50],  //8

    
]
//  Researched = [    0      ,    1     ,       2             ,       3    ,    4      ,    5       ,    6              ,     7 ,     8  ]
//  Researched = [Communities, villagios, Ressource Production, Stone Tools, Iron Tools, Steel Tools, Hunting Stratagies, Spears, Atlatls]
var Researched = [ false, false, false, false, false, false, false, false, false]

function Redirect(link){
    SaveValues()
    window.location.href = link;
}

function UnpackValues(){
    //Res 
    ResTotal = JSON.parse(localStorage.getItem("ResTotal"));

    //ExploredArea
    ExploredArea = JSON.parse(localStorage.getItem("ExploredArea"));
}


function SaveValues(){

    //Res and workers
    sessionStorage.setItem("ResTotal", JSON.stringify(ResTotal));
}

function ShowTech(list){
    for(let i =0; i<list.length; i++){
        document.getElementById(Techs[i][1]).style.display="block";
    }
}

function ShowBoughtTech(list){
    for(let i =0; i<list.length; i++){
        document.getElementById(list[i]).disabled = true;
    }
}

function ResearchTech(TechIndex, ){
    
}


function TechCheck(TechIndex){
    let EnoughRes = true;
    for(let i =1; i<Techs[1].length;i++){
        if (Techs[TechIndex][i]>ResTotal[i-1]){
            return;
        }
    }
    if (EnoughRes){
        for(let i =1; i<Techs[1].length;i++){
            ResTotal[i-1] -= Techs[TechIndex][i];
        }
    }
}