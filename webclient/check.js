function padZero(number) {
	return number.toString().padStart(2, "0");
}


export function extractTime2(dateString) {
	const hours = padZero(dateString.slice(9, 11))
	const minutes = padZero(dateString.slice(11, 13))
    console.log(`${hours}:${minutes}`)
	return `${hours}:${minutes}`;
}

extractTime2('05212024_010105')