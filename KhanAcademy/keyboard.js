fill(0, 0, 0);
var x = 13;
var y = 36;
var w = 25;
var h = 25;
var r = 2;
var textX = 20;
var letterKeyGap = 17;
var textY = y + letterKeyGap;
var distance = 40;

for( var i=1; i<=10; i++) {
    rect(x, y, w, h, r);     
    x = x + distance;
}
fill(255, 255, 255);
text("Q", textX + 0 * distance, textY);
text("W", textX + 1 * distance, textY);
text("E", textX + 2 * distance, textY);
text("R", textX + 3 * distance, textY);
text("T", textX + 4 * distance, textY);
text("Y", textX + 5 * distance, textY);
text("U", textX + 6 * distance, textY);
text("I", textX + 7 * distance, textY);
text("O", textX + 8 * distance, textY);
text("P", textX + 9 * distance, textY);

// Second row code starts here.
x = 20;
y = 70;
textX = 28;
textY = y + letterKeyGap;
for( var i=1; i<=9; i++) {
    fill(0, 0, 0);
    rect(x, y, w, h, r);     
    x = x + distance;
}

fill(255, 255, 255);
text("A", textX + 0 * distance, textY);
text("S", textX + 1 * distance, textY);
text("D", textX + 2 * distance, textY);
text("F", textX + 3 * distance, textY);
text("G", textX + 4 * distance, textY);
text("H", textX + 5 * distance, textY);
text("J", textX + 6 * distance, textY);
text("K", textX + 7 * distance, textY);
text("L", textX + 8 * distance, textY);

// Third row starts here.
x = 36;
y = 104;
textX = 45;
textY = y + letterKeyGap;
fill(0, 0, 0);


for( var i=1; i<=7; i++) {
    fill(0, 0, 0);
    rect(x, y, w, h, r);     
    x = x + distance;
}

fill(255, 255, 255);
text("Z", textX + 0 * distance, textY);
text("X", textX + 1 * distance, textY);
text("C", textX + 2 * distance, textY);
text("V", textX + 3 * distance, textY);
text("B", textX + 4 * distance, textY);
text("N", textX + 5 * distance, textY);
text("M", textX + 6 * distance, textY);
var spacebarX = 116;
var spacebarY = 138;
var spacebarW = 236;
fill(0, 0, 0);
rect(spacebarX, spacebarY, spacebarW, h, r);

var spacebarx = 3;
var spacebary = 5;
var spacebarw =25;
for( var i=1; i<=10; i++) {
    fill(0, 0, 0);
    rect(spacebarx, spacebary, spacebarw, h, r);     
    spacebarx = spacebarx + distance;
    
}


var textX1 = 12;
var textY1 = 22;


fill(255, 255, 255);
text("1", textX1 + 0 * distance, textY1);
text("2", textX1 + 1 * distance, textY1);
text("3", textX1 + 2 * distance, textY1);
text("4", textX1 + 3 * distance, textY1);
text("5", textX1 + 4 * distance, textY1);
text("6", textX1 + 5 * distance, textY1);
text("7", textX1 + 6 * distance, textY1);
text("8", textX1 + 7 * distance, textY1);
text("9", textX1 + 8 * distance, textY1);
text("0", textX1 + 9 * distance, textY1);

var x = 53;
var y = 137;
var w = 48;
var h = 26;
fill(0, 0, 0);
rect(x, y, w, h, r);


var x1 = 45;
var y1 = 207;
var w1 = 10;
var h1 = 10;
var r1 = -4;

fill(255, 255, 255);
rect(x1, y1, w1, h1, r1);
