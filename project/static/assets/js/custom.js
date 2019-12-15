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
		alert("Nepotpun unos.")
	}
	else
	{
		var k = document.getElementById("ime").value + " " + document.getElementById("prezime").value;
		var i = document.getElementById("vrsta").value;
		localStorage.setItem(k, i); //localstorage pribacit u bazu
		document.getElementById("test").innerHTML = "Unos uspješan."
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
	if(localStorage.length==0){
			document.getElementById("test").innerHTML="Nema karata."
	}
	else{
		document.getElementById("test").innerHTML="Postojeće karte:\n"
		for(var i=0; i < localStorage.length; i++)
		{
			var kljuc = localStorage.key(i);
			document.getElementById("test").innerHTML += kljuc + " - " + localStorage.getItem(kljuc) + "\n";
		}
	}
}
