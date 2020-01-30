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
	<style>
		.jumbotron{
			height: 550px;
			background-image: url('https://i.postimg.cc/K8XZLLMP/upi1.jpg');
			background-size: cover;
			color: #FFF
		}
	</style>
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
            <a class="nav-link" style="color:#FFFFFF" href="/">Početna
              <span class="sr-only">(current)</span>
            </a>
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
    <div class="row">
      <div class="col-lg-12 text-center">
        <h1 class="mt-5">UPI Projekt - Busevi</h1>
        <p class="lead">Pokušaj izrade aplikacije za kupnju autobusnih karata preko interneta</p>
        <ul class="list-unstyled">
        </ul>
      </div>
    </div>
	  <div class="row">
          <div class="jumbotron">
            <h2>O projektu</h2>
            <p>Cilj projekta je napraviti potpuno funkcionalnu Python aplikaciju za evidenciju i prodaju autobusnih karata. Aplikacija preko izbornika nudi mogućnosti biranja opcija i omogućije korisniku da kreira, ažurira, briše i pregleda vrste autobusnih karata, te svih drugih entiteta potrebnih u aplikaciji. Implementirana je mogućnost evidencije i kupnje mjesečnih karata (pokaz). Omogućen je prikaz statistike prodaje za određeni vremenski interval, ispis računa i izvještaja u tekstualne datoteke. Korisnik sam bira mogućnosti sortiranja i filtere za prikaz. Aplikacija pamti podatke i podaci su dostupni i nakon isključivanja aplikacije. 
              Napraviti UML dijagrame za glavne procese u aplikaciji!
            </p>
          </div>
        </div>
        <!--./row-->
        <div class="row">
            <hr>
            <footer>
                <p>&copy; 2019 {{data["developer_organization"]}}.</p>
            </footer>           
        </div>
  </div>
</body>
</html>
