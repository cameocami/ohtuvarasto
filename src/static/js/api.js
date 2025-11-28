// API functions for Varasto operations

function fetchVarastot() {
    return fetch('/api/varastot')
        .then(response => response.json());
}

function createVarastoApi(tilavuus, alku_saldo) {
    return fetch('/api/varastot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            tilavuus: parseFloat(tilavuus),
            alku_saldo: parseFloat(alku_saldo)
        })
    }).then(response => response.json());
}

function updateVarastoApi(varastoId, tilavuus, alku_saldo) {
    return fetch(`/api/varastot/${varastoId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            tilavuus: parseFloat(tilavuus),
            alku_saldo: parseFloat(alku_saldo)
        })
    }).then(response => response.json());
}

function deleteVarastoApi(varastoId) {
    return fetch(`/api/varastot/${varastoId}`, {
        method: 'DELETE'
    }).then(response => response.json());
}

function lisaaVarastoonApi(varastoId, maara) {
    return fetch(`/api/varastot/${varastoId}/lisaa`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ maara: maara })
    }).then(response => response.json());
}

function otaVarastostaApi(varastoId, maara) {
    return fetch(`/api/varastot/${varastoId}/ota`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ maara: maara })
    }).then(response => response.json());
}
