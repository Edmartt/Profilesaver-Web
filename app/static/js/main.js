const btnDelete= document.querySelectorAll('.btn-delete')
if (btnDelete){
const btnArray=Array.from(btnDelete);
				btnArray.forEach((btn)=>{
								btn.addEventListener('click',(e)=>{
								if(!confirm('¿Seguro que deseas eliminar este registro?')){
								e.preventDefault();
								}
								});
				});
}

const btnUpdate= document.querySelectorAll('.btn-update')
if (btnUpdate){
const btnArra=Array.from(btnUpdate);
				btnArra.forEach((btn)=>{
								btn.addEventListener('click',(e)=>{
								if(!confirm('¿Deseas actualizar este registro?')){
								e.preventDefault();
								}
								});
				});
}
