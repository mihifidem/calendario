document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("filtro-eventos");

    if (!formulario) {
        return;
    }

    const selects = formulario.querySelectorAll("select");

    selects.forEach(function (select) {
        select.addEventListener("change", function () {
            formulario.submit();
        });
    });
});
