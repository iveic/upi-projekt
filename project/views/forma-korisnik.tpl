<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bottle web project template">
    <meta name="author" content="datamate">
     
    <title>UPI - Busevi</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">
    
    <script type="text/javascript" src="/static/jquery.js"></script>
	<script type="text/javascript" src="/static/assets/js/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script> 
</head>
<body>

	
	  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-custom static-top">
    <div class="container">
      <a class="navbar-brand" style="color:#FFEC00" href="/">Autobusne karte</a>
      <button class="navbar-toggler custom-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon custom-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" style="color:#FFEC00" href="/">Početna</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/crud-primjer">Karte</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/info">Kontakt</a>
		  </li>
	  <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/odjava">Odjava</a>
		  </li>
		  <li class="nav-item">
			<a class="nav-link" style="color:#FFEC00" href="/novi-korisnik">Novi korisnik<span class="sr-only">(current)</span></a>
		  </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
	<div class="row" style="margin-top: 50px;">
        <form style="width: 100%" action='{{form_akcija}}' method='POST'>

            <input type="hidden" class="form-control" id="kartaid" name='kartaid' value='{{data[1].id if data != None else ""}}'>
			
			<input type="hidden" class="form-control" id="imeprezime" name="imeprezime" value='{{data[0].ime_prezime if data != None else ""}}'>
			
			<div class="form-group">
                <label for="email">E-mail</label>
                <input type="text" class="form-control" id="email" name='email' value='{{data[0].email if data != None else ""}}' aria-describedby="email-help" placeholder="Unesite e-mail" required>
            </div>
			
			<label for="vrsta">Vrsta Karte</label><br>
			<select type="text" id="vrsta" name="vrsta"></select>
			<script>
				var select = document.getElementById("vrsta");
				var options = {{!podaciK}}
				
				for(var i = 0; i < options.length; i++) {
					var opt = options[i];
					var el = document.createElement("option");
					el.textContent = opt;
					el.value = opt;
					select.appendChild(el);
				}
			</script><br><br>
			
			<label for="podrucje">Vrsta podrucja</label><br>
			<select type="text" id="podrucje" name="podrucje"></select>
			<script>
				var select = document.getElementById("podrucje");
				var options = {{!podaciP}}
				
				for(var i = 0; i < options.length; i++) {
					var opt = options[i];
					var el = document.createElement("option");
					el.textContent = opt;
					el.value = opt;
					select.appendChild(el);
				}
			</script><br><br>
			
			<input type="hidden" class="form-control" id="datum" name="datum" value='{{data[1].datum if data != None else ""}}'>
			
            <button type="submit" class="btn btn-dark">Sačuvaj</button>

        </form> 
    </div>

</body>
</html>
