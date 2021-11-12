function tradeCommission(arg1, arg2){
let city = arg1
let numberOfSales = Number(arg2)
let commision = 0
if(city === "Sofia"){
    if(numberOfSales >= 0 && numberOfSales <= 500){
    commision = (numberOfSales * 5) * 0.01
}
else if(numberOfSales >= 500 && numberOfSales <= 1000){
commision = (numberOfSales * 7) * 0.01
}
else if(numberOfSales >= 1000 && numberOfSales <= 10000){
commision = (numberOfSales * 8) * 0.01
}
else if(numberOfSales > 10000){
commision = (numberOfSales * 12) * 0.01
}
}
else if(city === "Varna"){
if(numberOfSales >= 0 && numberOfSales <= 500){
    commision = (numberOfSales * 4.5) * 0.01
}
else if(numberOfSales >= 500 && numberOfSales <= 1000){
commision = (numberOfSales * 7.5) * 0.01
}
else if(numberOfSales >= 1000 && numberOfSales <= 10000){
commision = (numberOfSales * 10) * 0.01
}
else if(numberOfSales > 10000){
commision = (numberOfSales * 13) * 0.01
}
}
else if(city === "Plovdiv"){
if(numberOfSales >= 0 && numberOfSales <= 500){
    commision = (numberOfSales * 5.5) * 0.01
}
else if(numberOfSales >= 500 && numberOfSales <= 1000){
commision = (numberOfSales * 8) * 0.01
}
else if(numberOfSales >= 1000 && numberOfSales <= 10000){
commision = (numberOfSales * 12) * 0.01
}
else if(numberOfSales > 10000){
commision = (numberOfSales * 14.5) * 0.01
}
}
if(commision){
console.log((commision).toFixed(2))
}
else if(numberOfSales < 0 || city !== "Sofia" || city !== "Varna" || city !== "Plovdiv"){
console.log("error")
}
}
tradeCommission()