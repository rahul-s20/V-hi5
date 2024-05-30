export function extractTime(dateString) {
	const date = new Date(dateString);
	const hours = padZero(date.getHours());
	const minutes = padZero(date.getMinutes());
	return `${hours}:${minutes}`;
}

// Helper function to pad single-digit numbers with a leading zero
function padZero(number) {
	return number.toString().padStart(2, "0");
}


export function extractTime2(dateString) {
	console.log("kkkkkkkkkkkkkkkkkk")
	console.log(dateString)
	const hours = padZero(dateString.slice(9, 11))
	const minutes = padZero(dateString.slice(11, 13))
	return `${hours}:${minutes}`;
}