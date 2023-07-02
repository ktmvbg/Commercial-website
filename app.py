
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, product, cart, order, admin_order, news, news_comment

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(cart.router)
app.include_router(order.router)
app.include_router(admin_order.router)
app.include_router(news.router)
app.include_router(news_comment.router)
