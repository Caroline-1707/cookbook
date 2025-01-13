from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Recipe
from schemas import RecipeCreate, RecipeOut
from database import get_db, Base, engine

app = FastAPI(title="Cookbook API", description="API для управления рецептами", version="1.0")


@app.on_event("startup")
async def startup():
    """
    Создание всех таблиц в базе данных при старте приложения.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/recipes/",
         response_model=List[RecipeOut],
         summary="Получить все рецепты",
         description="Возвращает список всех рецептов, отсортированных по количеству просмотров и времени приготовления.")
async def get_recipes(db: AsyncSession = Depends(get_db)):
    """
    Получение списка всех рецептов.

    - **db**: Сессия базы данных.

    Возвращает список объектов `RecipeOut`.
    """
    result = await db.execute(select(Recipe).order_by(Recipe.views.desc(), Recipe.cooking_time))
    return result.scalars().all()


@app.get("/recipes/{recipe_id}",
         response_model=RecipeOut,
         summary="Получить рецепт по ID",
         description="Возвращает рецепт по указанному ID.")
async def get_recipe(recipe_id: int, db: AsyncSession = Depends(get_db)):
    """
    Получение рецепта по его ID.

    - **recipe_id**: ID рецепта.
    - **db**: Сессия базы данных.

    Возвращает объект `RecipeOut` или вызывает ошибку 404, если рецепт не найден.
    """
    recipe = await db.get(Recipe, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    recipe.views += 1
    await db.commit()

    return recipe


@app.post("/recipes/",
          response_model=RecipeOut,
          summary="Создать новый рецепт",
          description="Создает новый рецепт и возвращает его.")
async def create_recipe(recipe: RecipeCreate, db: AsyncSession = Depends(get_db)):
    """
    Создание нового рецепта.

    - **recipe**: Объект `RecipeCreate`, содержащий данные нового рецепта.
    - **db**: Сессия базы данных.

    Возвращает созданный объект `RecipeOut`.
    """
    new_recipe = Recipe(**recipe.dict())
    db.add(new_recipe)
    await db.commit()
    await db.refresh(new_recipe)

    return new_recipe
