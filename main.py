from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Load the similarity matrix and DataFrame
with open("similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

with open("df.pkl", "rb") as file:
    df = pickle.load(file)

# Define the request model
class RecommendRequest(BaseModel):
    name: str

# Define the recommendation model
class Recommendation(BaseModel):
    name: str
    img: str

# Define the response model
class RecommendResponse(BaseModel):
    recommend: List[Recommendation]

# Define the recommendation function
def recommend(name: str) -> List[dict]:
    index = df[df["name"] == name].index[0]
    similar = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )[1:7]
    recommend_list = []
    for s in similar:
        recommend_list.append({"name": df["name"].iloc[s[0]], "img": df["img"].iloc[s[0]]})
    return recommend_list

# Initialize FastAPI app
app = FastAPI(title="Fashion Recommender System")

# Set CORS policies
origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the endpoint for top dresses
@app.get("/top_dresses/", response_model=RecommendResponse)
def get_top_dresses():
    top_dresses = df.sample(10)[["name", "img"]]
    recommendations = [Recommendation(name=dress["name"], img=dress["img"]) for dress in top_dresses.to_dict("records")]
    return RecommendResponse(recommend=recommendations)

# Define the endpoint for recommendations
@app.post("/recommend/", response_model=RecommendResponse)
def get_recommendations(request: RecommendRequest):
    name = request.name
    if name not in df["name"].values:
        raise HTTPException(status_code=404, detail="Product not found")

    recommendations = recommend(name)
    response = [Recommendation(name=rec["name"], img=rec["img"]) for rec in recommendations]
    # print(response)
    return RecommendResponse(recommend=response)
