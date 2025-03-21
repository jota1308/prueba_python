import random, sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# El usuario deberá contestar 3 preguntas
puntos = 0 # Puntaje del usuario
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3) # Se seleccionan 3 preguntas aleatorias distintas


    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index := questions.index(questions_to_ask[0][0])]) # Se obtiene el índice de la pregunta seleccionada
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es correcta
        if not user_answer.isdigit() or int(user_answer)-1 <0 or int(user_answer)-1 >4:  # Se verifica si la respuesta es un número entre 1 y 4
            print("Respuesta invalida")
            sys.exit(1)
        user_answer = int(user_answer)-1
        if user_answer == correct_answers_index[question_index]:
            print("¡Correcto!")
            puntos += 1  # Se incrementa el puntaje del usuario
            break
        puntos -= 0.5  # Se decrementa el puntaje del usuario
        print("Incorrecto. Inténtalo de nuevo.")
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    print()
print(f"Tu puntaje final es: {puntos}")