class Perceptron:
    def __init__(self,pesos,bias):
        """
        Inicializa o Perceptron com pesos e bias pré-definidos
        """
        self.pesos = pesos
        self.bias = bias

    def predict(self,entradas):
        """
        Calcula e aplica a função degrau
        """
        if len(entradas) != len(self.pesos):
            raise ValueError("O número de entradas deve ser igual ao número de pesos")

        z = self.bias
        for i in range(len(entradas)):
            z += entradas[i] * self.pesos[i]

        return 1 if z >= 0 else 0