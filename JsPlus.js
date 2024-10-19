// Lib for JS created by George
// BETA 1.0


function range(start=1,end=10,step=1){
    let result = []
    while (start < end){
        result.push(start)
        start += step
    }
    return result
}

function floatrange(start=1,end=10,step=1){
    let result = []
    while (start < end){
        result.push(start.toFixed(3))
        start += step
    }
    return result
}

function subrange(start=10,end=0,step=1){
    let result = []
    while (start > end){
        result.push(start)
        start -= step
    }
    return result  
}

function floatsubrange(start=10,end=0,step=1){
    let result = []
    while (start > end){
        result.push(start.toFixed(3))
        start -= step
    }
    return result  
}

function factorial(num){
    let result = num
    let a =range(2,num)
    for (i in a){
        result *= a[i]
    }
    return result
}


function chance_function(func,chance,args) {
    if ((Math.random()/0.01) <= chance){
        func(args)
    }
} 

function random_bint(){
    return Math.floor(Math.random() * 100000000000)
}
function random_sint(){
    return Math.floor(Math.random() * 100000)
}

function randelement(Listlike){
    return Listlike[random_sint() % Listlike.length]
}

function randrange(start,end,step){
    return randelement(range(start,end,step))
}

function randkey(Dict){
    let indexes = []
    for (i in Dict){
        indexes.push(i)
    }
    return randelement(indexes)
}

function randvalue(Dict){
    let indexes = []
    for (i in Dict){
        indexes.push(Dict[i])
    }
    return randelement(indexes)
}


class counter{
    constructor(){
        this.values = {}
    }
    calc(Value){
        for(let i in Value){
            if (this.values[Value[i]] == undefined){
                this.values[Value[i]] = 1
            }
            else{
            this.values[Value[i]] += 1}
            }
        }
    
    get(){
        return this.values
    }
    }


function StrInverse(str){
    let reversed = ""
    let lst = subrange(str.length-1,-1)
    for (i in lst){
        reversed += str[lst[i]]
    }
    return reversed
}

function StrIsPalindrome(str){
   return StrInverse(str) == str
}


class TranslatableStr{
    static lg = "en"
    constructor(text_dict={"en":"Hello","ru":"Привет","fr":"Bonjur","NotTranslate":"I'm don't speak your language! "}){
        this.text_dict = text_dict
    }
    get(){
        if (TranslatableStr.lg in this.text_dict){
            return this.text_dict[TranslatableStr.lg]
        }
        else{
            return this.text_dict["NotTranslate"]
        }
    }
    static change_lg(to_lg){
        TranslatableStr.lg = to_lg
    }
}




