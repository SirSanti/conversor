# conversor

<!DOCTYPE html>
<html>
<head>
	<title>Conversor de YouTube para MP3</title>
</head>
<body>
	<h1>Conversor de YouTube para MP3</h1>
	<form id="form">
		<label for="url">URL do vídeo do YouTube:</label><br>
		<input type="text" id="url" name="url"><br>
		<button type="submit">Converter</button>
	</form>
	<p id="status"></p>
	<p id="download"></p>
	<script>
		document.getElementById('form').addEventListener('submit', function(event) {
			event.preventDefault();
			var url = document.getElementById('url').value;
			var xhr = new XMLHttpRequest();
			xhr.open('POST', '/download');
			xhr.setRequestHeader('Content-Type', 'application/json');
			xhr.onload = function() {
				if (xhr.status === 200) {
					var data = JSON.parse(xhr.responseText);
					var link = document.createElement('a');
					link.href = data.url;
					link.download = data.filename;
					link.textContent = 'Download';
					document.getElementById('download').appendChild(link);
					link.click();
				} else {
					document.getElementById('status').textContent = 'Erro ao converter o vídeo.';
				}
			};
			xhr.send(JSON.stringify({url: url}));
		});
	</script>
</body>
</html>
