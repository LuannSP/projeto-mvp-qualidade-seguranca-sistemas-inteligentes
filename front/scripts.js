// Função para formatar valores para caixas de texto (em tempo real)
function formatCurrencyInput(value) {
    value = value.toString().replace(/\D/g, '');
    value = (value / 100).toFixed(2) + '';
    value = value.replace(".", ",");
    value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return value;
}

// Função para formatar valores para exibição na tabela
function formatCurrencyTable(value) {
    value = parseFloat(value);
    if (isNaN(value)) return '';

    value = value.toFixed(2).replace(".", ",");
    value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return value;
}

// Função para atualizar o valor da caixa de texto enquanto o usuário digita
function handleCurrencyInput(event) {
    let input = event.target;
    let unformattedValue = input.value.replace(/\./g, '').replace(',', '.');
    input.value = formatCurrencyInput(unformattedValue);
}

// Adiciona os eventos de 'input' aos campos de entrada
document.getElementById("newTV").addEventListener("input", handleCurrencyInput);
document.getElementById("newRadio").addEventListener("input", handleCurrencyInput);
document.getElementById("newNewspaper").addEventListener("input", handleCurrencyInput);

// Função para formatar o valor das caixas de texto
function formatCurrency(input) {
    input.value = formatCurrencyInput(input.value);
}

// Função para obter a lista existente do servidor via requisição GET
const getList = async () => {
    let url = 'http://127.0.0.1:5000/propagandas';
    try {
        const response = await fetch(url, { method: 'GET' });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        clearTable();
        data.advertising.forEach(item => insertList(item.id, item.tv, item.radio, item.jornal, item.resultado));
    } catch (error) {
        console.error('Error:', error);
    }
};

// Chamada da função para carregamento inicial dos dados
getList();

// Função para inserir itens na lista apresentada
const insertList = (id, tv, radio, jornal, resultado) => {
    var item = [
        formatCurrencyTable(tv), 
        formatCurrencyTable(radio), 
        formatCurrencyTable(jornal),
        resultado
    ];
    
    var table = document.getElementById('myTable');
    var row = table.insertRow();

    for (var i = 0; i < item.length - 1; i++) {
        var cell = row.insertCell(i);
        cell.textContent = item[i];
    }

    var performanceCell = row.insertCell(-1);
    var img = document.createElement('img');
    img.className = 'performance-icon';
    if (item[3] === 3) {
        img.src = 'img/green.png';
        img.alt = 'Alta Performance';
    } else if (item[3] === 2) {
        img.src = 'img/yellow.png';
        img.alt = 'Desempenho Moderado';
    } else if (item[3] === 1) {
        img.src = 'img/red.png';
        img.alt = 'Baixa Performance';
    }
    performanceCell.appendChild(img);

    var deleteCell = row.insertCell(-1);
    insertDeleteButton(deleteCell, id);
};

// Função para criar um botão de exclusão para cada item da lista
const insertDeleteButton = (parent, id) => {
    let span = document.createElement("span");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    parent.appendChild(span);

    span.onclick = function () {
        if (confirm('Você tem certeza de que deseja excluir?')) {
            deleteItem(id);
            var row = this.parentElement.parentElement;
            row.remove();
        }
    };
};

// Função para excluir um item
const deleteItem = async (id) => {
    const url = `http://127.0.0.1:5000/propaganda?id=${id}`;

    try {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error('Erro ao excluir o item');
        }
    } catch (error) {
        console.error('Erro:', error);
    }
};

// Função para validar os campos de entrada
const validateFields = () => {
    let inputTV = parseFloat(document.getElementById("newTV").value.replace(/\./g, '').replace(',', '.'));
    let inputRadio = parseFloat(document.getElementById("newRadio").value.replace(/\./g, '').replace(',', '.'));
    let inputJornal = parseFloat(document.getElementById("newNewspaper").value.replace(/\./g, '').replace(',', '.'));    

    if (isNaN(inputTV) || isNaN(inputRadio) || isNaN(inputJornal)) {
        alert("Todos os campos de investimento (TV, Rádio, Jornal) devem ser preenchidos corretamente!");
        return false;
    }

    if (inputTV <= 0 || inputRadio <= 0 || inputJornal <= 0) {
        alert("Os valores de investimento em TV, Rádio e Jornal devem ser maiores que R$ 0,00!");
        return false;
    }

    return true;
};

// Função para limpar os campos de entrada
const clearFields = () => {
    document.getElementById("newTV").value = "0,00";
    document.getElementById("newRadio").value = "0,00";
    document.getElementById("newNewspaper").value = "0,00";
};

// Função para adicionar um novo item de propaganda
const newItem = async () => {
    if (validateFields()) {
        let inputTV = parseFloat(document.getElementById("newTV").value.replace(/\./g, '').replace(',', '.'));
        let inputRadio = parseFloat(document.getElementById("newRadio").value.replace(/\./g, '').replace(',', '.'));
        let inputJornal = parseFloat(document.getElementById("newNewspaper").value.replace(/\./g, '').replace(',', '.'));

        await postItem(inputTV, inputRadio, inputJornal);
        await getList();

        setTimeout(() => {
            clearFields(); 
            document.getElementById('performanceFilter').selectedIndex = 0;
            alert("Análise de inventimento adicionada com sucesso!");
        }, 200);
    }
};

// Função para enviar os dados de propaganda ao servidor
const postItem = async (inputTV, inputRadio, inputJornal) => {
    const formData = new FormData();
    formData.append('tv', inputTV.toFixed(2));
    formData.append('radio', inputRadio.toFixed(2)); 
    formData.append('jornal', inputJornal.toFixed(2));

    let url = 'http://127.0.0.1:5000/propaganda';

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'accept': 'application/json',
            },
        });
        const data = await response.json();
    } catch (error) {
        console.error('Error:', error.message);
    }
};

// Função para limpar a tabela
const clearTable = () => {
    var table = document.getElementById('myTable');
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }
};

// Função para aplicar o filtro com base na performance
function applyFilter() {
    const filterValue = document.getElementById('performanceFilter').value;
    const rows = document.querySelectorAll('#myTable tr');

    rows.forEach(row => {
        if (row.rowIndex !== 0) {
            const performanceCell = row.cells[3];
            if (performanceCell && performanceCell.querySelector('img')) {
                const img = performanceCell.querySelector('img');
                const imgSrc = img.src.split('/').pop().split('.')[0];
                
                let isVisible = false;
                switch (filterValue) {
                    case 'geral':
                        isVisible = true;
                        break;
                    case '3':
                        isVisible = imgSrc === 'green';
                        break;
                    case '2':
                        isVisible = imgSrc === 'yellow';
                        break;
                    case '1':
                        isVisible = imgSrc === 'red';
                        break;
                }

                row.style.display = isVisible ? '' : 'none';
            }
        }
    });
}
