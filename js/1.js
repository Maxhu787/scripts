const makeServerRequest = new Prommise((resolve, rejecet) => {
	let responseFromServer;
	
	if(responseFromServer) {
		resolve("We got the data")
	} else {
		reject("Data not received")
	}
});
//.then runs after resolved
makeServerRequest.then(result => {
	console.log(result);
})
//.catch runs after reject
makeServerRequest.catch(error => {
	console.log(errer);
})