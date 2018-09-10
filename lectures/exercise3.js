console.log('start new lecture');
const notes = require('./notes.js')
const fs = require('fs');
const _ = require('lodash');

// var bb = ['ahmed', 'mohamed', 'ahmed', 2, 3, 8, 10, 2, 8, 14, 15, 14, 20]

// console.log('this year is', notes.recentyear, notes.math(6,3), notes.friend1);

// console.log(_.isString('ahmed'));
// console.log(_.isString(7));
// console.log(_.union(bb));

// fs.appendFileSync('ASEEU.txt', `this our text with infromation on math and year  ${notes.recentyear} and ${notes.math(6,3)} and the friend is${notes.friend1}`);

if(process.argv[2] === 'Ahmed'){
    console.log('this is my name');
}
else if (process.argv[2] === 'Egypt'){
    console.log('this is my country');
}
else{
    console.log('wrong entry!')
}
// console.log(process.argv);

