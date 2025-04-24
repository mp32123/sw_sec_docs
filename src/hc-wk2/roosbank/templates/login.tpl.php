<?php include "header.tpl.php"; ?>

<h4>Log in op uw RoosBank-account</h4>

<?php if (isset($login_failed) && $login_failed === false): ?>
    <p>Er is iets misgegaan met het inloggen...</p>
<?php endif; ?>

<form method="POST">
    <div class="mb-3">
        <label for="user" class="form-label">Gebruikersnaam:</label>
        <input type="text" name="user" class="form-control">
    </div>

    <div class="mb-3">
        <label for="pass" class="form-label">Wachtwoord:</label>
        <input type="password" name="pass" class="form-control">
    </div>

    <button type="submit" class="btn btn-primary">Inloggen</button>
</form>

<?php include "footer.tpl.php"; ?>