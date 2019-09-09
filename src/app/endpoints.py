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


        template = "matrix.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    
    async def post(self, request):
        x = self.request.get["x"]
        y = self.request.get["y"]

        data = dynamic_table(x, y)

        template = "matrix.html"
        context = {"request": request, "matrix":data}
        return templates.TemplateResponse(template, context)
