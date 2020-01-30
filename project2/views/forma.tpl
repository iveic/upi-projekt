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
            <a class="nav-link" style="color:#FFEC00" href="/prijava">Prijava</a>
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

            <div class="form-group">
                <label for="imeprezime">Ime i prezime</label>
                <input type="text" class="form-control" id="imeprezime" name='imeprezime' value='{{data[0].ime_prezime if data != None else ""}}' aria-describedby="imeprezime-help" placeholder="Unesite ime i prezime" required>
            </div>
			
			<div class="form-group">
                <label for="email">E-mail</label>
                <input type="text" class="form-control" id="email" name='email' value='{{data[0].email if data != None else ""}}' aria-describedby="email-help" placeholder="Unesite e-mail" required>
            </div>
			
			<div class="form-group">
                <label for="vrsta">Vrsta karte</label>
                <input type="text" class="form-control" id="vrsta" name='vrsta' value='{{data[2].vrsta if data != None else ""}}' aria-describedby="podrucje-help" placeholder="Unesite vrstu karte" required>
            </div>
			
            <button type="submit" class="btn btn-dark">Sačuvaj</button>

        </form> 
    </div>
	<div id="id01" class="modal">
  <form class="modal-content animate" action="/action_page.php" method="post">
    <div class="imgcontainer">
      <span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close Modal">&times;</span>
    </div>
    <div class="container">
	<h1>Prijava</h1>
		<hr>
      <label for="login_username"><b>Korisničko ime</b></label>
      <input type="text" placeholder="Korisničko ime" name="login_username" required>

      <label for="login_password"><b>Zaporka</b></label>
      <input type="password" placeholder="Zaporka" name="login_pasword" required>
        
      <button type="submit">Prijava</button>
      <label>
        <input type="checkbox" checked="checked" name="remember"> Zapamti me
      </label>
    </div>
    <div class="container" style="background-color:#f1f1f1">
      <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Odustani</button>
      <span class="psw">Zaboravljena <a href="#">zaporka?</a></span>
    </div>
  </form>
</div>

<div id="id02" class="modal">
  <form class="modal-content animate" action="/action_page.php" method="post">
    <div class="imgcontainer">
      <span onclick="document.getElementById('id02').style.display='none'" class="close" title="Close Modal">&times;</span>
    </div>
    <div class="container">
      <h1>Registracija</h1>
		<hr>
		
		<label for="register_username"><b>Korisničko ime</b></label>
		<input type="text" placeholder="Unesite korisničko ime" name="register_username" required>

		
		<label for="register_email"><b>Email</b></label>
		<input type="text" placeholder="Unesite email" name="register_email" required>

		<label for="register_password"><b>Zaporka</b></label>
		<input type="password" placeholder="Unesite zaporku" name="register_password" required>

		<label for="register_password-repeat"><b>Ponovljena zaporka</b></label>
		<input type="password" placeholder="Ponovno unesite zaporku" name="register_password-repeat" required>
		<hr>
		<p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

		<button type="submit" class="registerbtn">Registriraj se</button>
	  </div>
  </form>
</div>

<script>
var modal = document.getElementById('id01');
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
</script>

<script>
var modal = document.getElementById('id02');
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
</script>
</body>
</html>
