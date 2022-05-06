# micro-api

Rodar o comando do swarm \n
docker stack deploy -c docker-composev1.yaml stackMicroFinal

para acessar a API use
curl localhost:4000

para buscar todos os usuarios 
curl localhost:4000/usuarios

Para buscar usuario com id
curl localhost:4000/usuario/1234
