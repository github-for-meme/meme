let s = "https://www.multisoft.se/";
let a = "1112031584";
for (i = 1;  i < a.length; i++) {
    if (a[i] % 2 == a[i-1] % 2) {
        s += Math.max(a[i], a[i-1]);
    }
};
s+="/"
console.log(s);
