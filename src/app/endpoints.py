from starlette.endpoints import HTTPEndpoint

from app.globals import templates


class Home(HTTPEndpoint):
    async def get(self, request):
        template = "home.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)

class Search(HTTPEndpoint):
    async def get(self, request):
        template = "search.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)