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
	  <script type="text/javascript" src="/static/custom.js"></script>
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
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/">Početna</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/prijava">Prijava</a>
          </li>
		  <li class="nav-item active">
            <a class="nav-link" style="color:#FFFFFF" href="/crud-primjer">Karte
			<span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/info">O nama</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="#">Usluge</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="#">Kontakt</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
	<div class="row" style="margin-top: 50px;">
        <form style="width: 100%" action='{{form_akcija}}' method='POST'>

            <input type="hidden" class="form-control" id="kartaid" name='kartaid' value='{{data.id if data != None else ""}}'>

            <div class="form-group">
                <label for="imeprezime">Ime i prezime</label>
                <input type="text" class="form-control" id="imeprezime" name='imeprezime' value='{{data.ime_prezime if data != None else ""}}' aria-describedby="imeprezime-help" placeholder="Unesite ime i prezime" required>
            </div>

            <div class="form-group">
                <label for="godiste">Godište</label>
                <input type="number" class="form-control" id="godiste" name='godiste' value='{{data.godiste if data != None else ""}}' aria-describedby="godiste-help" placeholder="Unesite godište" required>
            </div>
			
			<div class="form-group">
				<label for="datumizrade">Datum izrade</label>
				<input type="date" class="form-control" id="datumizrade" name="datumizrade" value='{{data.datum_izrade if data != None else ""}}' aria-describedby="datumizrade-help" placeholder="Unesite datum izrade" required>
			</div>
			
			<div class="ui-field-contain">
				<label for="vrsta">Vrsta</label><br>
				<select name="vrsta" id="vrsta">
					<option value="{{data.vrsta if data != None else 'dnevna'}}">Dnevna</option>
					<option value="{{data.vrsta if data != None else 'mjesecna'}}">Mjesečna</option>
					<option value="{{data.vrsta if data != None else 'godisnja'}}">Godišnja</option>
				</select>
			</div>
			<br>
			
            <button type="submit" class="btn btn-dark">Sačuvaj</button>

        </form> 
    </div>
</body>
</html>
