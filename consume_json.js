
function consumirApi() {
    var endPoint = document.getElementById("api").value;
    fetch(endPoint)
.then(response => response.json())
.then(data => {
    // Extraer los datos de humedad y temperatura del JSON
    const mediciones = data.Mediciones;
    const humedad = mediciones.map(medida => medida.Humedad);
    const temperatura = mediciones.map(medida => medida.Temperatura);

    // Crear los datos para la gráfica de Plotly
    var grafica = [
    {
        x: ['Humedad', 'Temperatura'],
        y: [humedad[humedad.length - 1], temperatura[temperatura.length - 1]],
        type: 'bar'
    }
    ];

    // Definir el diseño de la gráfica
    var layout = {
    title: 'Humedad y Temperatura',
    xaxis: {
        title: 'Variable'
    },
    yaxis: {
        title: 'Valor'
    }
    };

    // Dibujar la gráfica utilizando Plotly
    Plotly.newPlot('graficaApi', grafica, layout);
})
.catch(error => console.error('Error al cargar los datos del archivo JSON:', error));
}