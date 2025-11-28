// UI functions for Varasto display and interaction

function calculateContainerSize(tilavuus) {
    // Base size + scaled size based on tilavuus
    const baseWidth = 80;
    const baseHeight = 120;
    const scaleFactor = Math.log10(tilavuus + 1) * 30;
    
    return {
        width: Math.max(baseWidth, baseWidth + scaleFactor),
        height: Math.max(baseHeight, baseHeight + scaleFactor * 1.5)
    };
}

function createVarastoElement(varasto, onClickCallback, onDblClickCallback) {
    const wrapper = document.createElement('div');
    wrapper.className = 'varasto-wrapper';
    wrapper.id = 'varasto-wrapper-' + varasto.id;

    const element = document.createElement('div');
    element.className = 'varasto-element';
    element.id = 'varasto-' + varasto.id;

    // Calculate dynamic size based on tilavuus
    const size = calculateContainerSize(varasto.tilavuus);
    element.style.width = size.width + 'px';
    element.style.height = size.height + 'px';

    const fillPercentage = (varasto.saldo / varasto.tilavuus) * 100;
    
    element.innerHTML = `
        <div class="varasto-fill" style="height: ${fillPercentage}%"></div>
        <div class="varasto-capacity">
            <span id="capacity-${varasto.id}">${varasto.paljonko_mahtuu.toFixed(1)}</span>
        </div>
    `;

    element.addEventListener('click', function(e) {
        e.stopPropagation();
        if (onClickCallback) onClickCallback(varasto.id, wrapper);
    });

    element.addEventListener('dblclick', function(e) {
        e.stopPropagation();
        if (onDblClickCallback) onDblClickCallback(varasto);
    });

    wrapper.appendChild(element);
    return wrapper;
}

function createBubble(varastoId, onLisaaClick, onOtaClick, onCloseClick) {
    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.innerHTML = `
        <button class="bubble-close">&times;</button>
        <div class="bubble-content">
            <div class="bubble-group">
                <input type="number" id="lisaa-maara-${varastoId}" step="0.1" min="0" placeholder="Määrä">
                <button class="bubble-btn lisaa-btn" data-id="${varastoId}">Lisää</button>
            </div>
            <div class="bubble-group">
                <input type="number" id="ota-maara-${varastoId}" step="0.1" min="0" placeholder="Määrä">
                <button class="bubble-btn ota-btn" data-id="${varastoId}">Ota</button>
            </div>
        </div>
        <div class="bubble-arrow"></div>
    `;

    bubble.querySelector('.bubble-close').addEventListener('click', function(e) {
        e.stopPropagation();
        if (onCloseClick) onCloseClick();
    });

    bubble.querySelector('.lisaa-btn').addEventListener('click', function(e) {
        e.stopPropagation();
        const maara = document.getElementById('lisaa-maara-' + varastoId).value;
        if (maara && onLisaaClick) {
            onLisaaClick(parseFloat(maara));
        }
    });

    bubble.querySelector('.ota-btn').addEventListener('click', function(e) {
        e.stopPropagation();
        const maara = document.getElementById('ota-maara-' + varastoId).value;
        if (maara && onOtaClick) {
            onOtaClick(parseFloat(maara));
        }
    });

    return bubble;
}

function updateVarastoDisplay(varastoId, data) {
    const capacityElement = document.getElementById('capacity-' + varastoId);
    if (capacityElement) {
        capacityElement.textContent = data.paljonko_mahtuu.toFixed(1);
    }

    const fillElement = document.querySelector('#varasto-' + varastoId + ' .varasto-fill');
    if (fillElement) {
        const fillPercentage = (data.saldo / data.tilavuus) * 100;
        fillElement.style.height = fillPercentage + '%';
    }
}

function showFloatingNumber(wrapper, text, color) {
    const floatingNum = document.createElement('div');
    floatingNum.className = 'floating-number';
    floatingNum.textContent = text;
    floatingNum.style.color = color === 'green' ? '#2e8b57' : '#dc143c';
    
    wrapper.appendChild(floatingNum);

    setTimeout(() => {
        floatingNum.classList.add('animate');
    }, 10);

    setTimeout(() => {
        floatingNum.remove();
    }, 2000);
}
