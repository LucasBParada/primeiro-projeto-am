from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="API de Aprendizado de Máquina",
    description="Interface para servir modelos preditivos e integrar IA com aplicações web e mobile",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class DadosEntrada(BaseModel):
    idade: int = Field(..., description="Idade do Cliente",examples=[35])
    renda: float = Field(...,description="Renda em reais",examples=[4500.0])
    historico_inadimplencia: bool = Field(...,description="Possui historico de inadimplencia", examples=[False])

class RespostaPredicao(BaseModel):
    limite_credito_aprovado: float
    risco_estimado: str
    status: str

@app.get('/',tags=["Geral"],summary="Endpoint Raiz")

def root():
    return{"message":"Hello from fastapi"}

@app.get("/status", tags=["Geral"],summary="Status do Servico")
def status():
    return{
        "status":"online",
        "modelo_carregado":True,
        "versao_modelo":"v1.0.0"
    }

@app.post("/predict", response_model=RespostaPredicao,
          tags=["Predicao"],
          summary="Simulação de Predição de Crédito",
          description="Recebe os atributos do cliente e simula uma predição de limite de crédito baseada em regras aprendidas.")

def realizar_predicao(dados: DadosEntrada):
    if dados.historico_inadimplencia:
        limite = 500.0
        risco = "Alto"
    else:
        limite = (dados.renda * 0.4) + (dados.idade * 10)
        risco = "Baixo" if dados.renda > 3000 else "Médio"

    return RespostaPredicao(
        limite_credito_aprovado=round(limite, 2),
        risco_estimado=risco,
        status="Aprovado")