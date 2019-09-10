from starlette.endpoints import HTTPEndpoint

from app.globals import templates
from app.matrix import dynamic_table


class Home(HTTPEndpoint):
    async def get(self, request):
        template = "home.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)


class Table(HTTPEndpoint):
    async def get(self, request):
        x = request.query_params.get("x")
        y = request.query_params.get("y")

        if x is None or y is None:
            data = ""
        else:
            x = int(x)
            y = int(y)

            data = [x, x + 1, x + 2, y, y + 1, y + 2]

        template = "table.html"
        context = {"request": request, "object": data}
        return templates.TemplateResponse(template, context)

