<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    body {
      font-family: Arial, sans-serif;
      color: #333;
      background-color: #f9f9f9;
      line-height: 1.5;
    }
css
Copy code
h1,
h2,
h3,
h4,
h5 {
  font-weight: bold;
  margin-top: 0;
}

p {
  margin: 0 0 1.5em 0;
}

code {
  font-family: monospace;
  background-color: #f5f5f5;
  padding: 0.25em;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2em;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.btn {
  display: inline-block;
  padding: 0.5em 1em;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #0069d9;
}
  </style>
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
