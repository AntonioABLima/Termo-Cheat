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
addDivButton.addEventListener('click', () => {
	if(n_row < 5 ){
		n_row = n_row + 1;
		const row =  document.querySelectorAll('#r' + n_row +' .letter');
		row.forEach(div => {
			div.classList.add('empty');
		});
		addClickListenerToDivs(row);
	};
});

const rmvDivButton = document.getElementById('rmvDivButton');
rmvDivButton.addEventListener('click', () => {
	if(n_row > 0 ){
		const row =  document.querySelectorAll('#r' + n_row +' .letter');
		row.forEach(div => {
			focusedDiv = null;
			div.innerHTML = "";
			div.classList.remove('empty');
			div.classList.remove('edit');
		});
		n_row = n_row - 1;
		removeClickListenerFromDivs(row);
	};
});

const printDivsButton = document.getElementById('printDivsButton');
printDivsButton.addEventListener('click', () => {
	const rows =  document.querySelectorAll('.row' +' .letter.empty');

	for (let i = 0; i < rows.length; i += 5) {
		var palavra = ""
		palavra = rows[i].innerHTML + rows[i+1].innerHTML + rows[i+2].innerHTML + rows[i+3].innerHTML + rows[i+4].innerHTML; 	
		console.log(palavra);
	}
	
})