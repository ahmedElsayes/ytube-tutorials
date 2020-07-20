function fibonacciGenerator(n) {
    var Fabolist = [0,1];
    if (n === 1) {
        Fabolist = [0];
    } else if (n===2){
        Fabolist =[0,1];
    }
    else {
        for (var i = 1; i < n-1; i++) {
            var newvar = Fabolist[i]+Fabolist[i-1];
            Fabolist.push(newvar);
        }
    }
    return Fabolist;
}
var result = fibonacciGenerator(15);
console.log(result);