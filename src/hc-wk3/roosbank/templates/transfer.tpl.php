<?php include "header.tpl.php"; ?>

<?php if ($result !== false): ?>
    <div class="mt-4 p-5 bg-success text-white rounded">
        <p>Bedankt voor het overmaken van <?php echo $result['amount']; ?> aan <?php echo $result['to_client']; ?>.</p>
    </div>
<?php endif; ?>

<h4>Geld overboeken</h4>
<form method="POST">
    <div class="mb-3">
        <label for="to_client" class="form-label">Begunstigde:</label>
        <input type="text" name="to_client" class="form-control">
    </div>

    <div class="mb-3">
        <label for="amount" class="form-label">Bedrag:</label>
        <input type="number" name="amount" class="form-control">
    </div>

    <button type="submit" class="btn btn-primary">Overmaken</button>
</form>

<?php include "footer.tpl.php";