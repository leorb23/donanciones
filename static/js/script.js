function start(){
	var lnkElm = document.getElementById("lnk-elm");
	if (lnkElm != null)
		lnkElm.onclick = function() { abrirEliminar() };
	var clsElm = document.getElementById("btn-cls");
	if (clsElm != null)
		clsElm.onclick = function() { cerrarEliminar() };
}

function abrirEliminar(){
	var dlgElm = document.getElementById("dlg-elm");
	dlgElm.classList.remove("none");
}

function cerrarEliminar(){
	var dlgElm = document.getElementById("dlg-elm");
	dlgElm.classList.add("none");	
}