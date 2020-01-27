<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bottle web project template">
    <meta name="author" content="datamate">
     
    <title>My UPI Project</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">
    
    <script type="text/javascript" src="/static/jquery.js"></script>
	  <script type="text/javascript" src="/static/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script> 
</head>
<body>

	
	  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
      <a class="navbar-brand" href="/">My UPI project</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
          </li>
		  <li class="nav-item active">
            <a class="nav-link" href="/crud-primjer">CRUD example
			<span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Services</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
	<div class="row" style="margin-top: 50px;">
        <form style="width: 100%" action='{{form_akcija}}' method='POST'>

            <input type="hidden" class="form-control" id="kartaid" name='kartaid' value='{{data[0] if data != None else ""}}'>

            <div class="form-group">
                <label for="imeprezime">Ime i prezime</label>
                <input type="text" class="form-control" id="imeprezime" name='imeprezime' value='{{data[1] if data != None else ""}}' aria-describedby="imeprezime-help" placeholder="Unesite ime i prezime" required>
            </div>

            <div class="form-group">
                <label for="godiste">Godište</label>
                <input type="number" class="form-control" id="godiste" name='godiste' value='{{data[2] if data != None else ""}}' aria-describedby="godiste-help" placeholder="Unesite godište" required>
            </div>
			
			<div class="form-group">
                <label for="mjestostanovanja">Mjesto stanovanja</label>
                <input type="text" class="form-control" id="mjestostanovanja" name='mjestostanovanja' value='{{data[3] if data != None else ""}}' aria-describedby="mjestostanovanja-help" placeholder="Unesite mjesto stanovnja" required>
            </div>
			
			<div class="form-group">
				<label for="datumizrade">Datum izrade karte</label>
				<input type="date" class="form-control" id="datumizrade" name="datumizrade" value='{{data[4] if data != None else ""}}' aria-describedby="datumizrade-help" placeholder="Unesite datum izrade" required>
			</div>
			
			<div class="form-group">
                <label for="vrsta">Vrsta karte</label>
                <input type="text" class="form-control" id="vrsta" name='vrsta' value='{{data[5] if data != None else ""}}' aria-describedby="podrucje-help" placeholder="Unesite vrstu karte" required>
            </div>
			
			<div class="form-group">
                <label for="podrucje">Područje</label>
                <input type="text" class="form-control" id="podrucje" name='podrucje' value='{{data[6] if data != None else ""}}' aria-describedby="podrucje-help" placeholder="Unesite vrstu podrucja" required>
            </div>
			
			<div class="form-group">
                <label for="zona">Zona</label>
                <input type="number" class="form-control" id="zona" name='zona' value='{{data[7] if data != None else ""}}' aria-describedby="zona-help" placeholder="Unesite zonu" required>
            </div>
			
            <button type="submit" class="btn btn-primary">Sačuvaj</button>

        </form>     
    </div>
</body>
</html>