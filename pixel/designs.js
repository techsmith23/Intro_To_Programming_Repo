const sizePicker = document.querySelector('#sizePicker');
const table = document.querySelector('#pixelCanvas');

makeGrid(10,10);

sizePicker.addEventListener('submit',function(event){
    event.preventDefault();
    while(table.hasChildNodes()){
        table.removeChild(table.firstChild);
    }
    
    const height = document.querySelector('#inputHeight');
    const width = document.querySelector('#inputWidth');
    makeGrid(height.value,width.value);
});

function makeGrid(height,width){
    for (let y = 0; y<height; y++){
        let row = table.insertRow(y);
        for(var x = 0; x < width; x++){
            let cell = row.insertCell(x);
            
            cell.style.backgroundColor = "white";
            cell.addEventListener('click',function(event){
                event.preventDefault();
                const color = document.querySelector('#colorPicker');
                cell.style.backgroundColor = color.value;
            });
        }
    }
}