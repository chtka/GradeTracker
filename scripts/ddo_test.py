from subprocess import call
print(call(["docker-compose ps | Select-String postgres"]))