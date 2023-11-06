var total= 0;
var digits = "";
for (var i = 0, p=digits.length-1-i; i<digits.length; i++, p--) {
  total+=Number(digits[i]) * Math.pow(10, p);
}
console.log(total);