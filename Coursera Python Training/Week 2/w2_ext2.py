seg=int(input("Por favor, entre com o número de segundos que deseja converter:"))
d=seg//86400
h=seg%86400//3600
m=seg%3600//60
s=seg%60
print(d,"dias,",h,"horas,",m,"minutos e",s,"segundos.")