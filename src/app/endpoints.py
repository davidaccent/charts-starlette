from starlette.endpoints import HTTPEndpoint

from app.globals import templates
from app.matrix import dynamic_table


class Home(HTTPEndpoint):
    async def get(self, request):
        template = "home.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)

class Matrix(HTTPEndpoint):
    async def get(self, request):
        x = ""
        y = ""


        template = "matrix.html"
        context = {"request": request, "x": x, "y": y}
        return templates.TemplateResponse(template, context)
    
    async def post(self, request):
        x = self.request.get["x"]
        y = self.request.get["y"]

        template = "matrix.html"
        context = {"request": request, "x": x, "y": y}
        return templates.TemplateResponse(template, context)
