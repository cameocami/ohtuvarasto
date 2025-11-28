// Main application logic

let varastot = [];
let activeBubble = null;

document.addEventListener('DOMContentLoaded', function() {
    loadVarastot();
    setupEventListeners();
});

function setupEventListeners() {
    // Open create popup
    document.getElementById('add-varasto-btn').addEventListener('click', function() {
        document.getElementById('create-popup').classList.remove('hidden');
    });

    // Close create popup
    document.getElementById('close-create-popup').addEventListener('click', function() {
        document.getElementById('create-popup').classList.add('hidden');
    });

    // Close edit popup
    document.getElementById('close-edit-popup').addEventListener('click', function() {
        document.getElementById('edit-popup').classList.add('hidden');
    });

    // Create varasto form submit
    document.getElementById('create-varasto-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const tilavuus = document.getElementById('tilavuus').value;
        const alku_saldo = document.getElementById('alku_saldo').value;

        createVarastoApi(tilavuus, alku_saldo).then(function() {
            document.getElementById('create-popup').classList.add('hidden');
            document.getElementById('create-varasto-form').reset();
            loadVarastot();
        });
    });

    // Edit varasto form submit
    document.getElementById('edit-varasto-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const varastoId = document.getElementById('edit-varasto-id').value;
        const tilavuus = document.getElementById('edit-tilavuus').value;
        const alku_saldo = document.getElementById('edit-alku_saldo').value;

        updateVarastoApi(varastoId, tilavuus, alku_saldo).then(function() {
            document.getElementById('edit-popup').classList.add('hidden');
            loadVarastot();
        });
    });

    // Delete varasto
    document.getElementById('delete-varasto-btn').addEventListener('click', function() {
        const varastoId = document.getElementById('edit-varasto-id').value;
        
        deleteVarastoApi(varastoId).then(function() {
            document.getElementById('edit-popup').classList.add('hidden');
            loadVarastot();
        });
    });

    // Close bubble when clicking outside
    document.addEventListener('click', function(e) {
        if (activeBubble && !activeBubble.contains(e.target)) {
            activeBubble.remove();
            activeBubble = null;
        }
    });
}

function loadVarastot() {
    fetchVarastot().then(function(data) {
        varastot = data;
        renderVarastot();
    });
}

function renderVarastot() {
    const container = document.getElementById('varastot-container');
    container.innerHTML = '';

    varastot.forEach(function(varasto) {
        const element = createVarastoElement(
            varasto,
            function(id, wrapper) { toggleBubble(id, wrapper); },
            function(v) { openEditPopup(v); }
        );
        container.appendChild(element);
    });
}

function toggleBubble(varastoId, wrapper) {
    // Close any existing bubble
    if (activeBubble) {
        activeBubble.remove();
        activeBubble = null;
    }

    // Create new bubble
    const bubble = createBubble(
        varastoId,
        function(maara) { lisaaVarastoon(varastoId, maara, wrapper); },
        function(maara) { otaVarastosta(varastoId, maara, wrapper); },
        function() {
            bubble.remove();
            activeBubble = null;
        }
    );

    wrapper.appendChild(bubble);
    activeBubble = bubble;
}

function lisaaVarastoon(varastoId, maara, wrapper) {
    lisaaVarastoonApi(varastoId, maara).then(function(data) {
        updateVarastoDisplay(varastoId, data);
        showFloatingNumber(wrapper, `+${data.added.toFixed(1)}`, 'green');
        updateLocalState(varastoId, data);
    });
}

function otaVarastosta(varastoId, maara, wrapper) {
    otaVarastostaApi(varastoId, maara).then(function(data) {
        updateVarastoDisplay(varastoId, data);
        showFloatingNumber(wrapper, `-${data.taken.toFixed(1)}`, 'red');
        updateLocalState(varastoId, data);
    });
}

function updateLocalState(varastoId, data) {
    const varasto = varastot.find(function(v) { return v.id === varastoId; });
    if (varasto) {
        varasto.saldo = data.saldo;
        varasto.paljonko_mahtuu = data.paljonko_mahtuu;
    }
}

function openEditPopup(varasto) {
    document.getElementById('edit-varasto-id').value = varasto.id;
    document.getElementById('edit-tilavuus').value = varasto.tilavuus;
    document.getElementById('edit-alku_saldo').value = varasto.saldo;
    document.getElementById('edit-popup').classList.remove('hidden');
}
