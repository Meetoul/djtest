function collapse(a){
	var e = document.getElementById(a);
	if(e){
		if(e.style.display == 'none'){
			e.style.display = 'block'
		} else {
			e.style.display = 'none'
		}
	}
}