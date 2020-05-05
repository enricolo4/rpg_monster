# RPG Monster

## PyCharm
* Importar a apliação
    * File -> Open
* Adicionar o interpretador
    * File -> Settings ->  Python Interpreter -> Clique na engrenagem em Add -> New Environment
* Importar libs do python
    * ```pip install -r requirements.txt``` 

## Executar a aplicação 

* No terminal execute o comando abaixo  
    * ```hupper -m waitress --port=8000 main.main:application```
 * Sua aplicação web será executada no endereço
    * ```http://localhost:8000``` 

# A aplicação
A aplicação deve criar um mostro que será utilizado no combate do jogo. 

* Deve possuir um endpoint para salvar as informações desse monstro. Esse endpoint deve ser um POST
    * Endpoint: ```/monster```
* Deve receber um playload parecido com o abaixo e salvar em um banco dados(no momento pode ser um banco de dados fake)

    ```json
    {
        "race": "Raça do monstro",
        "armor_class": ["natural armor", "shield"],
        "speed": 100,
        "life": 100,        
        "strength": 100,
        "dexterity": 100,
        "intelligence": 100,
        "charisma": 100,
        "wisdom": 100,
        "constitution": 100
    }
    ``` 
* O payload foi uma inspiração tirada do seguinte site
    * https://drive.google.com/file/d/1v_LjX-UU7bIANntPS__H28M7TFB5Ymux/view
    * https://smolderingwizard.files.wordpress.com/2013/11/dd_char_sheet_thumb.png
* Vocês podem alterar e/ou adicionar as informações, copiar do livro dos monstros de qualquer estilo de RPG
* Usem a criatividade.
  