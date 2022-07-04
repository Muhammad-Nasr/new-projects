// it is a comment 
// console.log('hello world')

// declare variable
/*


var a;
console.log(a)
a = 'muhammad';
console.log(a)

var b = 5;
console.log(b)

a = b;
console.log(a)
const c = 'lamiaa';   //   can't cahnge varibable with  const
//  c = 4;    
console.log(c)

m = 'wafaa'
console.log(m)

//  a / is a escape for ""
var myfullname = "muhammad nasr \"Iam a man\" myfather is a great man"  
console.log(myfullname)

var mywork = "I am a junior programmer \n\tI love my career\n\\ I hope my career loves me"
console.log(mywork)

// concatenate
var mystring = 'this is the first sentence'
mystring += 'this is the second sentence'
console.log(mystring)


mystring = 'hello'
mystring += 'world'

myname = mystring +  ' muhammad' + ' nasr.' 
console.log(myname)



console.log(mystring[mystring.length - 1])

*////

/*

// work with arrays  [  ]    ==  list in python

myarray = ['mo', 'salah', 14]
myarray.push(['liverpool'])   // push = append
array = myarray
console.log(myarray)
console.log(array)


ourarray = [5, 6, 7]
ourarray.pop()
console.log(ourarray)

ourarray.shift()  // remove from the begining
console.log(ourarray)


ourarray.unshift(3)    // add to the begining
console.log(ourarray)

*///


// functions
/*
var number = 9

function first_function(){
    console.log('first function in java, {} = : in python')

}

first_function()


function second_function(a, b){
    console.log(number + a + b);
    new_number = 9

}
second_function(a=6, b=2)
console.log(number - new_number)



function third_function(arr, item){
    arr.push(item)
    return arr.shift()
}
var li = [1, 2, 3, 4]
console.log(li)
third_function(li, 5)
console.log(li)

function trueOrFalse(wasthattrue){
    if (wasthattrue){
       return 'yes that was true'
    }
    return 'no that was not true'

}

console.log(trueOrFalse('jfsjfsdjfs'))

// if (condition) { statement }

function cahined(num){
    if (num < 5){
        return 'Tiny'
    }else if (num < 10){
        return "small"
    }else if (num < 15){
        return "medium"
    }else if (num < 20){
        return 'large'
    }else {
        return 'x large'
    }
}

console.log(cahined(25))

if (5 == '5'){                 // java convert conditions to one type ** python don't do that
    console.log('true')         // use === to strict condition
}else {
    console.log('flase')
}

*///-------------------------------------------------

// objects
var dog={
    'name':'rex',
    'legs':4,
    'friends':[]
}
// or both true
var dog={
    name:'rex',
    legs:4,
    friends:[]
}

delete dog.legs

dog.friends = ['koko']
dog.name = 'jack'
// console.log(dog.legs)


var myarray = []
var i = 0
while (i < 5){
    myarray.push(i);
    i ++;
}
// console.log(myarray)

// anonymous function

var arrowfunction = function(){
    return ''
}
// or 
var myConcat = (arr1, arr2) => arr1.concat(arr2);

console.log(myConcat([1, 2], [1, 4, 5]))

























