import os
import pickle
# esta libreria convierte texto en vectores
from sklearn.feature_extraction.text import CountVectorizer
# esta libreria se encarga de buscar las relacion con las respuestas
from sklearn.naive_bayes import MultinomialNB

MODEL_DIR="models"
MODEL_PATH=os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH=os.path.join(MODEL_DIR,"vectorizer.pkl")
ANSWER_PATH=os.path.join(MODEL_DIR,"answers.pkl")

# funcion de entrenamiento preguntas y respuestas
def build_and_train_model(Train_pairs):
    # Train_pairs lista de pares (preguntas y respuestas)
    # Ejemplo [ ("hola", "¡Hola!",) , ("adios", "¡Hasta luego!") ]
    # Separar las preguntas y respuestas en dos listas
    
    questions = [q for q, _ in Train_pairs]# lista de preguntas
    answers = [a for _, a in Train_pairs]  # lista de respuestas
    # creamos el vectorizado, que traducira del texto a numeros
    vectorizer=CountVectorizer()
    #entrenamiento del modelo
    x = vectorizer.fit_transform(questions) # Convertir las preguntas en vectores
    #obtenemos una lista de respuestas unicas
    unique_answers = sorted(set(answers))
    # crear el diccionario con las etiquetas
    answer_to_label = {a: i for i, a in enumerate(unique_answers)}
    #creamos una lista
    y= [answer_to_label[a] for a in answers]
    #Modelo claseificador de texto
    model = MultinomialNB()
    #entrenamos el modelo
    model.fit(x,y)
    # Crear carpeta para guardar el modelo si no existe
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    #guardar los objetos entrenados
    with open(MODEL_DIR, "wb") as f:
        pickle.dump(model, f)
    
    #guardar los objetos entrenados
    return model, vectorizer, unique_answers
# funcion para predecir la respuesta
def predict_answer(model, vectorizer, unique_answers, user_text):
        # Convertir la entrada del usuario en un vector
        X = vectorizer.transform([user_text])
        # Predecir la etiqueta de la respuesta
        label = model.predict(X)[0]
        return unique_answers[label]
# programa principal
if __name__ == "__main__":
    # Datos de entrenamiento: pares de preguntas y respuestas
    training_data =[
    ("hola", "¡Hola! ¿En qué podemos ayudarte hoy?")
    ("buenos días", "Buenos días, gracias por contactarnos. ¿Cómo podemos asistirte?"),
    ("buenas tardes", "Buenas tardes, es un gusto atenderte. ¿Qué consulta tienes?"),
    ("buenas noches", "Buenas noches, estamos a tu disposición. ¿En qué podemos ayudarte?"),
    ("información", "Con gusto te brindamos la información que necesitas. ¿Sobre qué tema?"),
    ("soporte", "Nuestro equipo de soporte está listo para ayudarte. Cuéntanos tu inconveniente."),
    ("precio", "Con gusto te compartimos nuestros precios. ¿Qué servicio te interesa?"),
    ("gracias", "Gracias a ti por comunicarte con nosotros. ¡Que tengas un excelente día!")

    ]
    
    # Construir y entrenar el modelo
    model, vectorizer, unique_answers = build_and_train_model(training_data)
    # Bucle principal para interactuar con el usuario
    print("Chatbot: supervisado listo, escribe salir para terminar la conversación.")
    while True:
        #pedimos al usuario que ingrese un texto
        user = input("Tú:  ").strip()
        if user.lower() in ("salir","exit","quit"):
            print("Chatbot: ¡Adiós! Fue un placer ayudarte.")
            break
        response = predict_answer(model, vectorizer, unique_answers, user)
        print("hot: ", response)