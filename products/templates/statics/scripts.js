// Agrega el comportamiento de desplegar/subir subcategorías al hacer clic en una categoría
$(".category").click(function() {
    // Selecciona las subcategorías asociadas a la categoría clicada
    var subcategorias = $(this).next(".subcategories");
    
    // Alterna el estado de colapsado de las subcategorías
    subcategorias.collapse('toggle');
});
