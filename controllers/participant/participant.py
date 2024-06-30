from controller import Robot, Motor

# Initialize the robot and get devices
robot = Robot()
leftWheel = robot.getDevice('left wheel motor')
rightWheel = robot.getDevice('right wheel motor')
rightWheelSensor = robot.getDevice('right wheel sensor')
rightWheelSensor.enable(16)

# Constants
diametro_roda = 0.195
lado_quadrado = 2
tempo_de_passo = 16

# Cálculo do ângulo a ser percorrido pela roda na linha reta
angulo_linha_reta = (lado_quadrado / (diametro_roda * 3.141592)) * 2 * 3.141592
# Cálculo do ângulo a ser percorrido pela roda na viragem
percurso_roda_viragem = (1/4) * 3.141592 * (0.33 / 2)
angulo_viragem = (percurso_roda_viragem / (diametro_roda * 3.141592)) * 2 * 3.141592

# Configuração inicial das rodas
leftWheel.setPosition(float('inf'))
rightWheel.setPosition(float('inf'))
velocidade = 2.0
leftWheel.setVelocity(velocidade)
rightWheel.setVelocity(velocidade)

robot.step(tempo_de_passo)

# Repeat the following 4 times (once for each side)
for i in range(4):
    valor_inicial_roda_direita = rightWheelSensor.getValue()
    
    # Movimentação em linha reta
    while rightWheelSensor.getValue() - valor_inicial_roda_direita < angulo_linha_reta:
        robot.step(tempo_de_passo)
    
    # Preparar para a viragem à direita
    leftWheel.setVelocity(velocidade)
    rightWheel.setVelocity(-velocidade)
    valor_inicial_roda_direita = rightWheelSensor.getValue()
    
    # Viragem em malha fechada
    while abs(rightWheelSensor.getValue() - valor_inicial_roda_direita) < angulo_viragem:
        robot.step(tempo_de_passo)
    
    # Resetar as rodas para a próxima movimentação em linha reta
    leftWheel.setVelocity(velocidade)
    rightWheel.setVelocity(velocidade)

# Parar o robô quando o caminho estiver completo
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)
