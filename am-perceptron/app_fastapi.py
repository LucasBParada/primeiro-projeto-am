from fastapi import FastAPI
from pydantic import BaseModel
from perceptron_class import Perceptron


app = FastAPI(
    title="API Perceptron - Decisão de Upgrade",
    description="API para calcular upgrade com base em dois atributos"
)


class UpgradeRequest(BaseModel):
    x1: float
    x2: float


class UpgradeResponse(BaseModel):
    x1: float
    x2: float
    upgrade_concedido: bool
    mensagem: str


modelo_upgrade = Perceptron(pesos=[0.8, 0.3], bias=-7.0)


@app.post("/predict", response_model=UpgradeResponse)
def prever_upgrade(dados: UpgradeRequest):
    entradas = [dados.x1, dados.x2]
    predicao = modelo_upgrade.predict(entradas)

    status = bool(predicao)
    mensagem = (
        "Upgrade autorizado" if status else "Upgrade não concedido"
    )

    return UpgradeResponse(
        x1=dados.x1,
        x2=dados.x2,
        upgrade_concedido=status,
        mensagem=mensagem
    )