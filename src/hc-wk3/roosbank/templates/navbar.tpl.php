<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">RoosBank</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <?php if (isset($_COOKIE['ManualAuthCookie']) && $_COOKIE['ManualAuthCookie'] == 'Authenticated'): ?>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="logout.php">Log uit</a>
            </li>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="transfer.php">Maak geld over</a>
            </li>
        <?php else: ?>
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="login.php">Log in</a>
            </li>
        <?php endif; ?>
      </ul>
    </div>
  </div>
</nav>