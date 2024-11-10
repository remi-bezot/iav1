// static/js/script.js

document.getElementById("export-teams").addEventListener("click", function() {
    fetch("/export/teams")
        .then(response => response.text())
        .then(data => {
            document.getElementById("exported-data").textContent = data;
        })
        .catch(error => console.error("Erreur lors de l'export des équipes:", error));
});

document.getElementById("export-languages").addEventListener("click", function() {
    fetch("/export/languages")
        .then(response => response.text())
        .then(data => {
            document.getElementById("exported-data").textContent = data;
        })
        .catch(error => console.error("Erreur lors de l'export des langues:", error));
});
