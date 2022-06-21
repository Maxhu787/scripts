function orbitalPeriod(arr) {
    var GM = 398600.4418;
    var earthRadius = 6367.4447;

    // Loop through each item in the array arr
    arr.forEach(function (item) {
        // Calculate the Orbital period
        //Add orbitalPeriod property
        item.orbitalPeriod = Math.round(2 * Math.PI * Math.sqrt(Math.pow(earthRadius + item.avgAlt, 3) / GM));;
        //Delete the avgAlt property
        delete item.avgAlt;
    });
    return arr;
}

console.log(orbitalPeriod([{ name: "sputnik", avgAlt: 35873.5553 }]));