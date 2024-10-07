document.getElementById('scheme-search-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const query = document.getElementById('scheme_query').value;

    fetch(`/search?query=${query}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Clear previous results
            if (data.error) {
                resultsDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
            } else {
                resultsDiv.innerHTML = '<h4>Matching Schemes:</h4>';
                data.forEach(scheme => {
                    resultsDiv.innerHTML += `<p>${scheme.Scheme} (Category: ${scheme.Category})</p>`;
                });
            }
        });
});

document.getElementById('query-search-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const query = document.getElementById('query').value;

    fetch('/ml_query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        if (data.error) {
            resultsDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
        } else {
            resultsDiv.innerHTML += `<h4>Query Category:</h4><p>${data.category}</p>`;
        }
    });
});
