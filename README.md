# Inventory Report

<h3>O que foi desenvolvido</h3>
<p>
    Neste projeto, você irá desenvolver um <strong>gerador de relatórios</strong> que processa arquivos de estoque e gera relatórios abrangentes. Os dados poderão ser obtidos de duas fontes:
</p>
<ul>
    <li>Através da importação de um arquivo <code>CSV</code>;</li>
    <li>Através da importação de um arquivo <code>JSON</code>.</li>
</ul>
<p>
    O relatório final possui duas versões: <strong>simples</strong> e <strong>completa</strong>.
</p>

<h3>Arquivos com os dados de entrada</h3>
<p>
    Os arquivos de entrada estão localizados no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Eles serão gerados ao executar os testes pela primeira vez.
</p>

<h3>Exemplo de Formato dos Arquivos</h3>

<h4>Arquivos CSV</h4>
<p>
    Arquivos <strong>CSV</strong> (separados por vírgula):
</p>
<pre><code>
id,product_name,company_name,manufacturing_date,expiration_date,serial_number,storage_instructions
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
</code></pre>

<h4>Arquivos JSON</h4>
<p>
    Arquivos JSON (seguindo o modelo):
</p>
<pre><code>
[
    {
        "id": "1",
        "product_name": "Borracha",
        "company_name": "Papelaria Solar",
        "manufacturing_date": "2021-07-04",
        "expiration_date": "2029-02-09",
        "serial_number": "FR48",
        "storage_instructions": "Ao abrigo de luz solar"
    }
]
</code></pre>

<h3>Requisitos do projeto</h3>
<ul>
    <li>
        <strong>Testar o construtor do objeto <code>Product</code></strong>
        <em>Criado em:</em> <code>tests/product/test_product.py</code>
    </li>
    <li>
        <strong>Testar o relatório individual gerado por <code>Product</code></strong>
        <em>Criado em:</em> <code>tests/product_report/test_product_report.py</code>
    </li>
    <li>
        <strong>Criar a Interface <code>Importer</code></strong><br />
        Classe abstrata com o método abstrato <code>import_data</code>.<br />
        <em>Criado em:</em> <code>inventory_report/importers.py</code>
    </li>
    <li>
        <strong>Criar a classe <code>JsonImporter</code></strong><br />
        Herda de <code>Importer</code> e foi implementado <code>import_data</code> para ler JSON.<br />
        <em>Criado em:</em> <code>inventory_report/importers.py</code>
    </li>
    <li>
        <strong>Criar a classe <code>Inventory</code></strong><br />
        Foi armazenado o estoque e adicionado itens a ele.<br />
        <em>Criado em:</em> <code>inventory_report/inventory.py</code>
    </li>
    <li>
        <strong>Criar o protocolo <code>Report</code></strong><br />
        <em>Criado em:</em> <code>inventory_report/reports/report.py</code>
    </li>
    <li>
        <strong>Criar o relatório <code>SimpleReport</code></strong><br />
        Implementa os métodos <code>add_inventory</code> e <code>generate</code> do protocolo <code>Report</code>.<br />
        <em>Criado em:</em> <code>inventory_report/reports/simple_report.py</code>
    </li>
</ul>

<h3>Testes</h3>
<p>
    Para executar os testes, certifique-se de que você está com o ambiente virtual ativado.
</p>

<h3>Executar os testes</h3>
<pre><code>
python3 -m pytest
</code></pre>

<h3>Exemplos de Execução de Testes</h3>
<pre><code>
python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo especificado
python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
python3 -m pytest -k expressao  # Executa testes que contêm a expressão informada
python3 -m pytest -x  # Para na primeira falha
</code></pre>

<p>
    Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a <a href="https://docs.pytest.org/en/6.2.x/contents.html">documentação do pytest</a>.
</p>

<h3>Docker</h3>
<p>
    Se preferir executar os testes via <code>docker-compose</code>, use o comando:
</p>
<pre><code>
docker-compose run --rm inventory pytest
</code></pre>

