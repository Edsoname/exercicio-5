# crie um programa que pede ao usuário e senha e na sequencia ,
# copia e cola o usuário e senha dentro de um bloco de notas 
 
import pyautogui
email = pyautogui.prompt(text='Digite seu e-mail', title='dados de login')
print(f'voce digitou {email}')
senha = pyautogui.password(text='digite sua senha:',title='dados de login',mask='*')
print(f'voce digitou{senha}')

resposta = pyautogui.confirm(text='continuar com o login?',title='confirmação',buttons=['sim','não','cancelar'])
if resposta == 'sim':
     print('login feito com sucesso')
elif resposta =='não':
     print('encerrando seu login')
else:
     print('operação cancelada')

pyautogui.click(1159,76,duration=2)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)










