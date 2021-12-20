import RPi.GPIO as GPIO
import time

TRIG_PIN = 10 #초음파를 보내는 핀 번호
ECHO_PIN = 8 #돌아오는 초음파를 받는 핀 번호
PEIZO_PIN = 2 #피에조 부저 핀 번호
PRI_PIN = 4 #PIR 핀 번호
SWITCH_PIN = 12 #스위치 핀 번호
a = 1 

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT) 
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(PRI_PIN, GPIO.IN)    
GPIO.setup(PEIZO_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pwm=GPIO.PWM(PEIZO_PIN, 262) #4옥타브 도음 주파수 262
try:
    while True:
         vae = GPIO.input(SWITCH_PIN)
         print(vae)
         if vae==0:
        
           GPIO.output(TRIG_PIN, True)  
           time.sleep(0.00001) #10us (microsec)
           GPIO.output(TRIG_PIN, False) 

           while GPIO.input(ECHO_PIN)==0: #펄스 발생중
             pass
           start = time.time() #ECHO PIN HIGH (시작)

           while GPIO.input(ECHO_PIN) == 1: #펄스 발생 종료
            pass
           stop = time.time() #ECHO PIN LOW (종료)
 
           duration_time = stop - start 
           distance = duration_time * 17160 #거리 계산식
        

           print('Distance: %.1fcm'% distance) #print를 통하여 거리를 보여줌
  
           if distance<= 20: 
            pwm.start(50) #거리가 20 이하일때 피에조 부저가 울린다.
            print('PIEZO on')    
            
           else:
              val = GPIO.input(PRI_PIN)
              if val == GPIO.HIGH:
               print('움직임 감지')
               print('PIEZO on')
               pwm.start(50) #움직임을 감지 했을 때 피에조 부저가 울린다.
              else:
               print('움직임 없음')
               print('PEIZO off')
               pwm.stop()  #움직임이 없을 때 피에조 부저가 울리지 않는다.
         elif vae==1: #스위치가 눌려있지 않다면 위에 있는 프로그램이 실행되지 않는다.
            pass
            
            

         time.sleep(0.5) #0.5초마다 현재 상태를 보여준다 (거리, 피에조 부저 On/Off, 움직임 감지)
         

finally:
    GPIO.cleanup()
    print('cleanup and exit')     