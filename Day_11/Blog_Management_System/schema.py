from pydantic import BaseModel

# Schema for incoming requests
class BlogCreate(BaseModel):
    title:str
    content:str

# Schema for Outgoing Response
class BlogDisplay(BaseModel):
    id:int
    title:str
    content:str

    class config:                   #This class convert the pydantic object-->Dictionary-->JSON
        from_attributes=True

# AI Chat Schema
class ChatRequest(BaseModel):
    question:str

class ChatResponse(BaseModel):
    response:str

