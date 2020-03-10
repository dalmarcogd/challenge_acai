# Acai Api
Açai Api é um projeto que controla pedidos de açai.

### Tecnologias
Principais tecnologias utilizadas:
* [uvicorn] - Como http server para execução da api
* [alembic] - Para migração do banco de dados
* [SQLAlchemy] - ORM das entidades
* [pydantic] - Utilizado para validação dos payloads
* [fastapi] - Como web framework para construção de APIS

### Como executar

```sh
$ git clone https://github.com/dalmarcogd/challenge_acai.git
$ cd challenge_acai
$ docker-compose up
$ open http://localhost/acai-api/docs
```

### Teste
 - Utilizar o swagger para abrir pedidos no /orders
 - Utilizar o swagger para abrir pedidos no /orders

### Design
A aplicação ``integration-open-weather-background`` é responsável apenas por realizar a integração com a https://openweathermap.org/, ela é uma aplicação
que executa somente [celery] e se comunica pelo broker [redis].
Já a aplicação ``weather-forecast-api`` executa uma api rest e roda um worker do celery em background para receber atualizações das consultas de previsão do tempo. 


   [uvicorn]: <https://github.com/encode/uvicorn.git>
   [alembic]: <https://alembic.sqlalchemy.org/en/latest/>
   [SQLAlchemy]: <https://www.sqlalchemy.org/>
   [pydantic]: <https://pydantic-docs.helpmanual.io/>
   [fastapi]: <https://fastapi.tiangolo.com/>
   
   