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
          <li class="nav-item active">
            <a class="nav-link" style="color:#FFEC00" href="/">Početna
              <span class="sr-only">(current)</span>
            </a>
          </li>
		  <li class="nav-item">
          <li class="nav-item">
            <a class="nav-link" style="color:#FFFFFF" href="#">Prijava
                <span class="sr-only">(current)</span>
            </a>
          </li>
            <a class="nav-link" style="color:#FFEC00" href="/crud-primjer">Karte</a>
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
    <div class="row">
        <div class="form-group">
                <label for="username">Korisničko ime</label>
                <input type="text" class="form-control" id="username" name='username' value='{{data.ime_prezime if data != None else ""}}' aria-describedby="imeprezime-help" placeholder="Unesite korisničko ime" required>
            </div>

            <div class="form-group">
                <label for="godiste">Zaporka</label>
                <input type="text" class="form-control" id="password" name='password' value='{{data.godiste if data != None else ""}}' aria-describedby="godiste-help" placeholder="Unesite zaporku" required>
            </div>
            <br>
            <button type="submit" class="btn btn-dark">Prijava</button>
    <!--./row-->
  </div>
</body>
</html>