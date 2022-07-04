// way 1 to create object
const circle = {
    radius: 1,
    location: {
        x: 1,
        y: 1
    },
    draw: function(){
        console.log('muhammad has java in web');
    }
}; 

//  circle.draw();


// factory function

function createCircle(radius){
    return {
        radius,
        draw: function(){
            console.log('muhammad has 2java in web');
        }
    }
}

const circle2 = createCircle(1)
// circle2.draw() 


// constructor function

function NewCircle(radius){
    console.log('this', this)
    this.radius = radius,
    this.draw = function(){
        console.log('muhammad has 3 java in web');
    }

}

const circle3 = new NewCircle(1)