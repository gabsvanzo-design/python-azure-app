from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="App UniOpet Azure (Sem Banco)")
templates = Jinja2Templates(directory="templates")

itens_db = []
contador_id = 1

@app.get("/")
def listar_itens(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "itens": itens_db})

@app.post("/adicionar")
def adicionar_item(nome: str = Form(...), descricao: str = Form("")):
    global contador_id
    novo_item = {
        "id": contador_id,
        "nome": nome,
        "descricao": descricao
    }
    itens_db.append(novo_item)
    contador_id += 1
    return RedirectResponse(url="/", status_code=303)

@app.post("/deletar/{item_id}")
def deletar_item(item_id: int):
    global itens_db
    itens_db = [item for item in itens_db if item["id"] != item_id]
    return RedirectResponse(url="/", status_code=303)
