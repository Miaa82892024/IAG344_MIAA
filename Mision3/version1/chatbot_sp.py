#lo que hace esta librería es que el computador entienda el lenguaje de unir, limpiar en el vector 
#librerías exclusivas para IA también pueden ser utilizadas en JavaScript

#scikit-learn estaa libreríaa se utiliza para crear modelos de aprendizaje automático
from sklearn.feature_extraction.text import CountVectorizer 

#se encarga de encontrar conincidencias entre preguntas y respuestas
from sklearn.naive_bayes import MultinomialNB

#Función 

def build_and_train_model(train_pairs):
    #train_pairs lista de pares(pregunta, respuestas)
    #Ejemplo [("Hola""¡Hola!"),("adios","¡Hasta luego!")]
    #separamos las pereguntas y respuestas en dos listas
    
    questions = [q for q, _ in train_pairs]#lista de preguntas 
    answers = [a for _, a in train_pairs]#lista de respuestas
    # creamos el vectorizado, que traducirá el txto a números 
    vectorizer=CountVectorizer()
    #Entrenamiento
    x=vectorizer.fit_transform(questions)
    #obtenemos una lista de respuestas 
    unique_answers=sorted(set(answers))
    #crear el diccionaeio con las etiquetas 
    answers_to_label={a: i for i, a in enumerate(unique_answers)}
    #creamos una lista
    y=[answers_to_label[a] for a in answers]
    #Modelo clasificación de texto 
    model=MultinomialNB()
    #Entrenar el modelo 
    model.fit(x,y)
    return model,vectorizer,unique_answers

#funcion predict_answer

def predict_answer(model, vectorizer, unique_answers,user_text):
    #convetir la entrada del usuario en un vector
    #convertimos el texro a números
    x=vectorizer.transform([user_text])
    #el modelo predice la etiqueta de la respuesta correcta
    label=model.predict(x)[0]
    return unique_answers[label]

#programa principal

if __name__=="__main__":
    training_data= [
        ("hola","¡Hola! ¿En qué te puedo ayudar 😎?"),
        ("hola", "¡Hola! ¿En qué puedo ayudarte?"),
        ("¿cómo estás?", "Estoy bien, gracias por preguntar."),
        ("adiós", "¡Hasta luego! Que tengas un buen día."),
        ("¿qué puedes hacer?", "Puedo responder a tus preguntas y ayudarte con información."),
        ("¿cuál es tu nombre?", "Soy un chatbot creado para ayudarte."),
        ("hola", "¡Hola! ¿En qué podemos ayudarte hoy?"),
        ("buenos días", "Buenos días, gracias por contactarnos. ¿Cómo podemos asistirte?"),
        ("buenas tardes", "Buenas tardes, es un gusto atenderte. ¿Qué consulta tienes?"),
        ("buenas noches", "Buenas noches, estamos a tu disposición. ¿En qué podemos ayudarte?"),
        ("información", "Con gusto te brindamos la información que necesitas. ¿Sobre qué tema?"),
        ("soporte", "Nuestro equipo de soporte está listo para ayudarte. Cuéntanos tu inconveniente."),
        ("precio", "Con gusto te compartimos nuestros precios. ¿Qué servicio te interesa?"),
        ("gracias", "Gracias a ti por comunicarte con nosotros. ¡Que tengas un excelente día!"),
        ("chiste", "Qué le dio un árbol a otro árbol... Te dejaron plantado?")

        ]
    #Entrenae el modelo con la lista
    model, vectorizer, unique_answers = build_and_train_model(training_data)
    #Mostrar un mensaje inicial al usuario 
    print("chatbot supervisado listo, escribe salir para termina.\n")
    while True:
        #pedimos una frase al usuario
        user=input("Tú: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("Bot: ¡Hasta pronto!")
            break
        response=predict_answer(model,vectorizer, unique_answers, user)
        print("Bot: ", response)