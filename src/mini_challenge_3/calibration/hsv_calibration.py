import cv2
import numpy as np

# Función para detectar círculos rojos
def detect_red_circles(frame, lower_red, upper_red):
    # Convertir el fotograma de BGR a HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear una máscara para aislar las regiones rojas
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Aplicar desenfoque gaussiano para reducir el ruido
    red_mask = cv2.GaussianBlur(red_mask, (9, 9), 2)

    # Utilizar la transformada de Hough para detectar círculos
    circles = cv2.HoughCircles(red_mask, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)

    # Si se detectan círculos, dibujarlos en el fotograma
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)

    return frame

# Función para manejar clics del ratón
def mouse_callback(event, x, y, flags, param):
    global lower_red, upper_red

    if event == cv2.EVENT_LBUTTONDOWN:
        # Obtener el color del píxel al que se hizo clic
        bgr_color = frame[y, x]

        # Convertir a HSV
        hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)[0][0]

        # Establecer el nuevo rango de colores para rojo basado en el píxel clicado
        lower_red = np.array([hsv_color[0] - 10, 100, 100])
    
        upper_red = np.array([hsv_color[0] + 10, 255, 255])
        # Print the arrays
        print("lower_red:", lower_red)
        print("upper_red:", upper_red)

# Función principal para capturar video de la cámara
def main():
    global frame, lower_red, upper_red

    # Inicializar valores HSV iniciales
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Abrir la captura de video
    cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada, cambiar si se utiliza una cámara diferente

    while True:
        # Capturar fotograma por fotograma
        ret, frame = cap.read()
        if not ret:
            break

        # Detectar círculos rojos
        frame_with_circles = detect_red_circles(frame, lower_red, upper_red)

        # Mostrar el fotograma resultante
        cv2.imshow('Red Circles Detection', frame_with_circles)

        # Llamar a la función de retorno de ratón
        cv2.setMouseCallback('Red Circles Detection', mouse_callback)

        # Romper el bucle cuando se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()