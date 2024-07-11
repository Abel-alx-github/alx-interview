#!/usr/bin/node


const args = process.argv[2];

//isNaN(parseFloat(args)) ?  const id = parseFloat(args) : console.log("enter id number");
const id = isNaN(parseInt(args)) ? "Enter the correct id" : parseInt(args);
if (isNaN(parseInt(id))) {
	console.log(id)
	return	
}

const url = "https://swapi-api.alx-tools.com/api/films/" + id 


async function fetchData(url) {
	try
		{
			const respond = await fetch(url)
  		if (!respond.ok) {
				return new Error("not Ok");
			}	
			const data = await respond.json()
	
			const nextUrl = data.characters
				
			Promise.all(nextUrl.map( async (link) => {
					console.log(link)
					const res = await fetch(link)
					if (!res.ok)  {throw new Error("link is failed")}

					const dataPerson = await res.json()
					console.log(dataPerson.name)

					}))
		}
	catch(error){
		console.error(error)
		}			
}

fetchData(url)

