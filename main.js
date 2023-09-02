const nome_lista = 'ListaCincoPalavras.txt';
let lista = [];

(async () => {
    try {
        const response = await fetch('ListaCincoPalavras.txt'); // Substitua 'seuarquivo.txt' pelo nome do seu arquivo.
        const text = await response.text();

		lista = text.split(/[\r\n]+/);

        console.log('Arquivo lido com sucesso!');

    } catch (error) {
        console.error('Erro ao ler o arquivo:', error);
    }
})().then(() => {
    // console.log(lista); // Isso será executado após a conclusão do bloco assíncrono

	let focusedDiv = null;

	function addClickListenerToDivs(row) {
		row.forEach(div => {
			div.addEventListener('click', clickHandler);
		});
	}

	function clickHandler() {
		if (focusedDiv) {
			focusedDiv.classList.remove('edit');
		}
		focusedDiv = this;
		focusedDiv.classList.add('edit');
	}

	function removeClickListenerFromDivs(row) {
		row.forEach(div => {
			div.removeEventListener('click', clickHandler);
		});
		
	}

	const row1 = document.querySelectorAll('.letter.empty');
	addClickListenerToDivs(row1);

	document.addEventListener('keydown', (event) => {
		if (focusedDiv && event.keyCode > 64 && event.keyCode < 91 ) {
			focusedDiv.textContent = event.key;
		}
		else if(focusedDiv){
			focusedDiv.textContent = "";
		}
	});

	var n_row = 0;
	const addDivButton = document.getElementById('addDivButton');
	
	const rmvDivButton = document.getElementById('rmvDivButton');
	if(n_row === 0){
		rmvDivButton.style.pointerEvents = 'none';
		rmvDivButton.style.opacity = '0';
	}

	function moverDivParaNovoPai(divParaMover, novoPaiID) {
		const novoPai = document.getElementById(novoPaiID);
		if (novoPai) {
			const antigoPai = divParaMover.parentElement;
			antigoPai.removeChild(divParaMover);
			novoPai.appendChild(divParaMover);
		}
	}

	
	function toggleDivClasses(div){
		// Verifica a classe atual da div clicada e altera para a próxima classe
		if (div.classList.contains('wrong')) {
			div.classList.remove('wrong');
			div.classList.add('place');
		} else if (div.classList.contains('place')) {
			div.classList.remove('place');
			div.classList.add('right');
		} else if (div.classList.contains('right')) {
			div.classList.remove('right');
			div.classList.add('wrong');
		}
	}

	addDivButton.addEventListener('click', () => {
		if(n_row < 5 ){
			n_row = n_row + 1;
			moverDivParaNovoPai(document.getElementById('addDivButton'), 'r' + parseInt(n_row + 1));
			moverDivParaNovoPai(document.getElementById('rmvDivButton'), 'r' + parseInt(n_row));
			
			const pre_row =  document.querySelectorAll('#r' + parseInt(n_row - 1) +' .letter');
			removeClickListenerFromDivs(pre_row);
			pre_row.forEach(div => {
				focusedDiv = null;

				div.classList.remove('empty');
				div.classList.remove("edit");
				div.classList.add('wrong');
				div.classList.add('has');

				div.addEventListener('click', () => {
					toggleDivClasses(div);
				});
			});

			const row =  document.querySelectorAll('#r' + n_row +' .letter');
			row.forEach(div => {
				div.classList.add('empty');
			});
			addClickListenerToDivs(row);
			rmvDivButton.style.pointerEvents = 'all';
			rmvDivButton.style.opacity = '1';
		};
		if(n_row === 5){
			addDivButton.style.pointerEvents = 'none';
			addDivButton.style.opacity = '0';
		}
	});

	rmvDivButton.addEventListener('click', () => {
		if(n_row > 0 ){
			moverDivParaNovoPai(document.getElementById('addDivButton'), 'r' + parseInt(n_row));
			moverDivParaNovoPai(document.getElementById('rmvDivButton'), 'r' + parseInt(n_row - 1));
			
			const pre_row =  document.querySelectorAll('#r' + parseInt(n_row - 1) +' .letter');
			addClickListenerToDivs(pre_row);
			pre_row.forEach(div => {
				div.classList.add('empty');
				div.classList.remove('has');
				div.classList.remove('wrong');
				div.classList.remove('place');
				div.classList.remove('right');

				div.removeEventListener('click', toggleDivClasses(div));
			});

			const row =  document.querySelectorAll('#r' + n_row +' .letter');
			row.forEach(div => {
				focusedDiv = null;
				div.innerHTML = "";
				div.classList.remove('empty');
				div.classList.remove('edit');
			});
			n_row = n_row - 1;
			removeClickListenerFromDivs(row);
			addDivButton.style.pointerEvents = 'all';
			addDivButton.style.opacity = '1';
		};
		if(n_row === 0){
			rmvDivButton.style.pointerEvents = 'none';
			rmvDivButton.style.opacity = '0';
		}
	});

	const printDivsButton = document.getElementById('printDivsButton');
	printDivsButton.addEventListener('click', () => {
		const rows =  document.querySelectorAll('.row' +' .letter.has');

		for (let i = 0; i < rows.length; i += 5) {
			var palavra = ""
			palavra = rows[i].innerHTML + rows[i+1].innerHTML + rows[i+2].innerHTML + rows[i+3].innerHTML + rows[i+4].innerHTML; 	
			console.log( palavra + lista.includes(palavra));
		}
	})
});


