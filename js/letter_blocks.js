function print(x) {
  process.stdout.write(x + "");
}
function println(x) {
  console.log(x);
}
var A = [
  [0,0,1,0,0],
  [0,1,0,1,0],
  [1,0,0,0,1],
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,0,0,0,1]
];
for (var i = 0; i < A.length; i++) {
  for (var j = 0; j < A[0].length; j++) {
    if (A[i][j] == 0) {
      print(" ");
    } else {
      print("1");
    }
  }
  println(" ");
}
