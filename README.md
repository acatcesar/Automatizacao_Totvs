<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
  <div class="container">
    <h1>Projeto de Automatização de Cadastros de Produtos no Totvs com RPA, PyAutoGUI e OpenCV</h1>
    <p>Este é um projeto de automação de processos para realizar o cadastro de produtos no sistema Totvs. A solução foi desenvolvida utilizando a linguagem de programação Python, a biblioteca PyAutoGUI e a integração com OpenCV para identificação de elementos na tela.</p>
css
Copy code
<h2>Requisitos</h2>
<ul>
  <li>Python 3.7 ou superior</li>
  <li>Biblioteca PyAutoGUI</li>
  <li>Biblioteca OpenCV</li>
  <li>Sistema Totvs</li>
</ul>

<h2>Funcionamento</h2>
<p>A automação consiste em uma sequência de passos para realizar o cadastro de um novo produto no sistema Totvs. Os passos são executados automaticamente pelo script, sem intervenção humana.</p>
<p>O script inicia com a abertura do sistema Totvs e navega até a tela de cadastro de produtos. Em seguida, utiliza a biblioteca PyAutoGUI para preencher os campos necessários, como código, descrição, unidade de medida, entre outros. A integração com OpenCV é utilizada para identificar os campos na tela e garantir que a automação seja realizada corretamente, mesmo em diferentes resoluções de tela ou configurações do sistema.</p>
<p>Ao finalizar o preenchimento dos campos, o script salva o cadastro e retorna à tela inicial do sistema.</p>

<ol>
