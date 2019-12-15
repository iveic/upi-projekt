window.onload = function()
{
	document.getElementById("kreiraj").addEventListener("click", Kreiraj)
	document.getElementById("azuriraj").addEventListener("click", Azuriraj)
	document.getElementById("izbrisi").addEventListener("click", Izbrisi)
	document.getElementById("pregled").addEventListener("click", Ispis)
}

function Kreiraj()
{
	var div = document.getElementById("ispis")
	div.innerHTML = ""
	div.innerHTML += "<br><label type = 'number'>ID: <label> <input id = 'id' type = 'number'>"
	div.innerHTML += "<br><label type = 'text'>Ime: <label> <input id = 'ime' type = 'text'>" //ime
	div.innerHTML += "<br><label type = 'text'>Prezime: <label> <input id = 'prezime' type = 'text'>" //prezime
	div.innerHTML += "<br><label type = 'text'>Vrsta: <label> <input id = 'vrsta' type = 'text'>" // vrsta karte
	div.innerHTML += "<br><button id = 'potvrda'>Potvrdi</button>" //botun za potvrdu
	document.getElementById("potvrda").addEventListener("click", Potvrda)
}

function Potvrda()
{
	if (document.getElementById("ime").value.length == 0 || document.getElementById("prezime").value.length == 0 || document.getElementById("vrsta").value.length == 0)
	{
		alert("Nepotpun unos")
	}
	else
	{
		//unit podatke u bazu
	}
}

function Azuriraj()
{
	//dodat prvo koji podatak azurirat
	//ubacit value u input boxove
	Kreiraj()
}

function Izbrisi()
{
	
}

function Ispis()
{
	document.getElementById("test").innerHTML = '{{data["developer_organization"]}}'
}