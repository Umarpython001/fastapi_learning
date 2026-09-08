from fastapi import FastAPI, Path, Query
from typing import Optional
from enum import Enum
from backend.students.routes import studentRouter
from backend.students.database_models import StudentDB, CourseDB
from database import Base, engine



app = FastAPI() 

app.include_router(studentRouter)




#Make table for students
Base.metadata.create_all(bind=engine)











# class Food(BaseModel):
#     name:str
#     classs:str
#     grams:int



# @app.get("/index")
# def home():
#     a = "kqgysj.JWIYUAGH"
#     return f"{a}, {len(a)}"


# #Path parameters
# @app.get("/food_item/{item_id}")
# def smth(item_id: int = Path(gt=0, description="The id of the food item")):


#     food_item = food[item_id]

#     return food_item


# #Query parameters
# @app.get("/items/")
# def read_items(skip: int = 0, limit: int = 10):
#     return {"skip": skip, "limit": limit}
# # GET /items/?skip=5&limit=20

# # Required + validated
# @app.get("/search/")
# def search(
#     random:int,
#     q: str = Query("Default value", min_length=5, max_length=50, description="A query to be searched for"),
# ):

#     return {"query": q,
#             "random":random}



# class sortClass(str, Enum):
#     price = "price"
#     name = "name"
#     rating = "rating"

# class categoryClass(str, Enum):
#     electronics = "electronics"
#     food = "food"
#     furniture = "furniture"
#     house_hold = "house hold"


# @app.get("/products/{category}")
# def product(

#     q:str = Query(None, min_length=3, max_length=50),

#     limit:int = Query(10, le=50, ge=1),

#     sort:sortClass = Query(None,),

#     category:categoryClass = Path(description="A category that a product must fall under"),
# ):

#     json_ans = {

#                 "category":category,
#                 "limit":limit,
#                 "query":None,
#                 "sort":None


#     }   

#     if q:
#         json_ans["query"] = q

#     if sort:
#         json_ans["sort"] = sort
#     return json_ans

    


# #Adds a new food object to the food json/database shii
# @app.post("/create_food/")
# def create_food(new_food:Food):
#     current = food["max"]
#     current += 1
#     food["max"] = current

#     food[current] = new_food
     

#     return new_food


# @app.put("/change_food/{food_id}")
# def change_food(food_id:int, new_food:Food):

#     thing = food[food_id]

#     cl = thing["classs"]
#     name = thing["name"]
#     gr = thing["grams"]

#     if new_food.name != "string":
#         thing["name"] = new_food.name

#     if new_food.classs != "string":
#         thing["classs"] = new_food.classs
        
#     if new_food.grams != 0:
#         thing["grams"] = new_food.grams

#     return thing


# @app.delete("/delete_food/{food_id}")
# def delete(food_id:int):
#     if food_id in food:
#         del food[food_id]

#         return {"Success":"Food successfully deleted"}
        
#     else:
#         return {"Error":"ID does not exist"}
#     ...


# print(food)