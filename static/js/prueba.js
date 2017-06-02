$().ready(function() 
	{
		$('.pasar').click(function() { return !$('#id_equiposFavoritos option:selected').remove().appendTo('#id_destino'); });  
		$('.quitar').click(function() { return !$('#id_destino option:selected').remove().appendTo('#id_equiposFavoritos'); });
		$('.pasartodos').click(function() { $('#id_equiposFavoritos option').each(function() { $(this).remove().appendTo('#id_destino'); }); });
		$('.quitartodos').click(function() { $('#id_destino option').each(function() { $(this).remove().appendTo('#id_equiposFavoritos'); }); });
		$('.submit').click(function() { $('#id_destino option').prop('selected', 'selected'); });
	});







	<div>
			<input type="button" class="pasar izq" value="Pasar »">
			<input type="button" class="quitar der" value="« Quitar">
			<br />
			<input type="button" class="pasartodos izq" value="Todos »">
			<input type="button" class="quitartodos der" value="« Todos">
			</div>
			<div class="">
			<label for="destino">aqui estan los destino</label>
			<select name="destino[]" id="destino" multiple="multiple" ></select>
			</div>