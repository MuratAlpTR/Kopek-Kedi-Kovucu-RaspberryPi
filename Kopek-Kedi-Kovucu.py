                                                       // Proje Tarafından Yazılmıştır : MuratAlpTR // 

// Ultrasonik sensör kullanarak hayvanları uzaklaştırma


import RPi.GPIO as GPIO
import time

trigPin = 9  # Ultrasonik sensörün trig pini
echoPin = 10  # Ultrasonik sensörün echo pini
buzzerPin = 11  # Buzzer pini

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(buzzerPin, GPIO.OUT)

def measure_distance():
    GPIO.output(trigPin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)

    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()

    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Mesafe: {dist:.2f} cm")

        if dist < 50:  # Eğer hayvan 50 cm'den daha yakınsa
            GPIO.output(buzzerPin, GPIO.HIGH)  # Buzzer'ı çal
            time.sleep(1)  # 1 saniye beklet
            GPIO.output(buzzerPin, GPIO.LOW)  # Buzzer'ı kapat

except KeyboardInterrupt:
    GPIO.cleanup()


                                                       // Proje Tarafından Yazılmıştır : MuratAlpTR // 
