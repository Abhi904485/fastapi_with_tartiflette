import os.path

from fastapi import FastAPI
from tartiflette import Engine
from tartiflette_asgi import TartifletteApp

app = FastAPI()
engine = Engine(sdl=os.path.join(os.path.dirname(__file__), 'sdl'),
                modules=["resolvers.query_resolvers", "resolvers.mutation_resolvers", "resolvers.subscription_resolvers"])
graphql_app = TartifletteApp(engine=engine, subscriptions=True)

app.mount("/graphql", graphql_app)
app.add_event_handler('startup', graphql_app.startup)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API!"}
